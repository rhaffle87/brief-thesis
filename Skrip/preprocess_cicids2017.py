#!/usr/bin/env python3
"""
Pipeline Praproses Dataset CIC-IDS2017 untuk Federated-Continual Learning (FCL)
================================================================================
Penelitian Tugas Akhir:
"Analisis Kinerja Deteksi Network Traffic Intrusion Menggunakan Metode
 Federated-Continual Learning pada Testbed Private Cloud Server"
Penyusun: Rafli Alif Ihza Hartono (NRP 5048231003)
Departemen Teknik Elektro, FTEIC - ITS Surabaya

Spesifikasi Metodologis Terkunci:
- Input: Monday (Normal), Tuesday (SSH-Patator), Wednesday (DoS 4-varian)
- Filter 3 Kelas: Normal (BENIGN), SSH-Patator, DoS (Hulk, GoldenEye, slowloris, slowhttptest)
- Eksklusi: FTP-Patator (5.933 baris), Heartbleed (11 baris)
- Deduplikasi: Pembersihan 132.909 baris duplikat mentah (1.529.677 baris bersih)
- Seleksi Fitur (62 Fitur Numerik Bersih + 1 Label):
  * 10 Kolom konstan variansi nol dibuang
  * 5 Kolom duplikat identik (r=1.0) dibuang
  * 1 Kolom Destination Port dibuang (mitigasi shortcut learning)
- Partisi Federasi Non-IID:
  * Klien A: Normal (50%) + SSH-Patator (100%)
  * Klien B: Normal (50%) + DoS (100%)
  * Global Held-Out Test Set (20%) & Local Client Test Sets (20%)
- Standardisasi Skalar Global: mu_global dan sigma_global via agregasi skalar (n, sum_x, sum_x2)
- Bobot Kelas Global: w_c = N_total / (C * N_c)
"""

import sys
from pathlib import Path

if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except AttributeError:
        pass

PROJECT_ROOT = Path(__file__).resolve().parents[1]
import argparse
import json
import logging

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split

# Konfigurasi logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[logging.StreamHandler(sys.stdout)],
)
logger = logging.getLogger("preprocess_cicids2017")

# Root direktori proyek
# Daftar kolom yang wajib dieliminasi sesuai audit Bab 3
CONSTANT_COLUMNS = [
    "Bwd PSH Flags",
    "Fwd URG Flags",
    "Bwd URG Flags",
    "CWE Flag Count",
    "Fwd Avg Bytes/Bulk",
    "Fwd Avg Packets/Bulk",
    "Fwd Avg Bulk Rate",
    "Bwd Avg Bytes/Bulk",
    "Bwd Avg Packets/Bulk",
    "Bwd Avg Bulk Rate",
]

DUPLICATE_COLUMNS = [
    "Fwd Header Length.1",
    "Subflow Fwd Bytes",
    "Subflow Fwd Packets",
    "Subflow Bwd Packets",
    "SYN Flag Count",
]

SHORTCUT_COLUMNS = [
    "Destination Port",
]

TARGET_FILES = [
    ("Monday-WorkingHours.pcap_ISCX.csv", "Monday"),
    ("Tuesday-WorkingHours.pcap_ISCX.csv", "Tuesday"),
    ("Wednesday-workingHours.pcap_ISCX.csv", "Wednesday"),
]


def load_raw_csvs(input_dir: Path) -> pd.DataFrame:
    """Membaca dan menggabungkan berkas CSV mentah Senin, Selasa, dan Rabu."""
    logger.info("Langkah 1/7: Membaca berkas CSV mentah dari %s...", input_dir)
    dfs = []
    for fname, day in TARGET_FILES:
        fpath = input_dir / fname
        if not fpath.exists():
            raise FileNotFoundError(f"Berkas dataset tidak ditemukan: {fpath}")
        logger.info("  Membaca %s (%s)...", fname, day)
        df_day = pd.read_csv(fpath, skipinitialspace=True, low_memory=False)
        df_day.columns = df_day.columns.str.strip()
        df_day["Day_Source"] = day
        logger.info("    -> %s baris, %s kolom", f"{len(df_day):,}", len(df_day.columns))
        dfs.append(df_day)

    df_raw = pd.concat(dfs, ignore_index=True)
    logger.info("Total baris mentah gabungan: %s baris", f"{len(df_raw):,}")
    return df_raw


def filter_classes(df: pd.DataFrame) -> pd.DataFrame:
    """Menyaring 3 kelas target dan mengeksklusi kelas di luar batasan masalah."""
    logger.info("Langkah 2/7: Menyaring 3 kelas target (Normal, SSH-Patator, DoS)...")
    logger.info("Distribusi label mentah sebelum filtering:\n%s", df["Label"].value_counts())

    # Pemetaan varian DoS menjadi satu label agregat
    dos_variants = ["DoS Hulk", "DoS GoldenEye", "DoS slowloris", "DoS Slowhttptest"]
    mask_benign = df["Label"] == "BENIGN"
    mask_ssh = df["Label"] == "SSH-Patator"
    mask_dos = df["Label"].isin(dos_variants)

    # Catat kelas yang dieksklusi
    mask_ftp = df["Label"] == "FTP-Patator"
    mask_hb = df["Label"] == "Heartbleed"
    logger.info("Eksklusi kelas non-target: FTP-Patator (%s baris), Heartbleed (%s baris)",
                f"{mask_ftp.sum():,}", f"{mask_hb.sum():,}")

    df_filtered = df[mask_benign | mask_ssh | mask_dos].copy()
    df_filtered["Label_Clean"] = "Normal"
    df_filtered.loc[df_filtered["Label"] == "SSH-Patator", "Label_Clean"] = "SSH-Patator"
    df_filtered.loc[df_filtered["Label"].isin(dos_variants), "Label_Clean"] = "DoS"

    logger.info("Total baris setelah penyaringan 3 kelas: %s baris", f"{len(df_filtered):,}")
    logger.info("Distribusi kelas bersih:\n%s", df_filtered["Label_Clean"].value_counts())
    return df_filtered


def clean_anomalies_and_deduplicate(df: pd.DataFrame) -> pd.DataFrame:
    """Membersihkan nilai Inf/NaN dan menghapus baris duplikat identik."""
    logger.info("Langkah 3/7: Penanganan nilai anomali Inf/NaN dan deduplikasi alur...")
    
    # Deteksi dan konversi Inf ke NaN
    num_cols = df.select_dtypes(include=[np.number]).columns
    inf_count = np.isinf(df[num_cols].values).sum()
    logger.info("  Nilai Infinite ditemukan: %s sel (dikonversi ke NaN)", f"{inf_count:,}")
    df[num_cols] = df[num_cols].replace([np.inf, -np.inf], np.nan)

    # Pembersihan baris bernilai NaN
    nan_rows = df[num_cols].isnull().any(axis=1).sum()
    logger.info("  Baris memuat NaN: %s baris (dihapus)", f"{nan_rows:,}")
    df = df.dropna(subset=num_cols).copy()

    # Deduplikasi alur (menggunakan seluruh fitur asli)
    feature_cols_all = [c for c in num_cols if c not in ["Day_Source"]]
    dup_mask = df.duplicated(subset=feature_cols_all, keep="first")
    dup_count = dup_mask.sum()
    logger.info("  Baris duplikat identik ditemukan: %s baris (%0.2f%%)",
                f"{dup_count:,}", (dup_count / len(df)) * 100)
    
    df_dedup = df[~dup_mask].copy()
    logger.info("Total baris unik pasca-deduplikasi: %s baris", f"{len(df_dedup):,}")
    return df_dedup


def select_features(df: pd.DataFrame) -> tuple[pd.DataFrame, list[str]]:
    """Mengeliminasi 10 kolom konstan, 5 kolom duplikat, dan Destination Port (total 62 fitur)."""
    logger.info("Langkah 4/7: Seleksi fitur (eliminasi 10 konstan, 5 duplikat, dan nomor port)...")

    cols_to_drop = CONSTANT_COLUMNS + DUPLICATE_COLUMNS + SHORTCUT_COLUMNS
    existing_drop = [c for c in cols_to_drop if c in df.columns]
    logger.info("  Menghapus %d kolom bermasalah: %s", len(existing_drop), existing_drop)

    df_selected = df.drop(columns=existing_drop)
    
    # Ekstraksi fitur numerik murni
    feature_names = [c for c in df_selected.select_dtypes(include=[np.number]).columns 
                     if c not in ["Day_Source", "Label", "Label_Clean"]]
    
    logger.info("Jumlah fitur numerik bersih akhir: %d fitur", len(feature_names))
    if len(feature_names) != 62:
        logger.warning("PERINGATAN: Jumlah fitur numerik adalah %d, bukan 62!", len(feature_names))
    else:
        logger.info("VERIFIKASI SUKSES: Tepat 62 fitur numerik statistik flow.")

    return df_selected, feature_names


def partition_federated_data(
    df: pd.DataFrame, feature_names: list[str], test_ratio: float = 0.20, seed: int = 42
) -> dict[str, pd.DataFrame]:
    """
    Membagi dataset menjadi partisi non-IID 2 klien dan Global Test Set:
    - Global Held-Out Test Set (20% stratified)
    - Klien A: Normal (50% dari sisa train) + SSH-Patator (100% dari sisa train)
    - Klien B: Normal (50% dari sisa train) + DoS (100% dari sisa train)
    - Local Client Test Sets (20% stratified per klien)
    """
    logger.info("Langkah 5/7: Partisi dataset terdistribusi non-IID dua klien (seed=%d)...", seed)

    # 1. Pisahkan Global Held-Out Test Set (20% stratified)
    train_pool, global_test = train_test_split(
        df, test_size=test_ratio, random_state=seed, stratify=df["Label_Clean"]
    )
    logger.info("  Global Held-Out Test Set: %s sampel", f"{len(global_test):,}")

    # 2. Pisahkan data Normal, SSH, dan DoS pada train pool
    train_normal = train_pool[train_pool["Label_Clean"] == "Normal"]
    train_ssh = train_pool[train_pool["Label_Clean"] == "SSH-Patator"]
    train_dos = train_pool[train_pool["Label_Clean"] == "DoS"]

    # 3. Bagi data Normal secara acak 50:50 antar Klien A dan Klien B (mitigasi day-confound)
    normal_client_a, normal_client_b = train_test_split(
        train_normal, test_size=0.50, random_state=seed
    )

    # 4. Susun partisi Klien A (Task 1: Normal 50% + SSH-Patator 100%)
    client_a_pool = pd.concat([normal_client_a, train_ssh], ignore_index=True)
    # Split Klien A menjadi Train (80%) dan Local Test (20%)
    client_a_train, client_a_test = train_test_split(
        client_a_pool, test_size=test_ratio, random_state=seed, stratify=client_a_pool["Label_Clean"]
    )

    # 5. Susun partisi Klien B (Task 2: Normal 50% + DoS 100%)
    client_b_pool = pd.concat([normal_client_b, train_dos], ignore_index=True)
    # Split Klien B menjadi Train (80%) dan Local Test (20%)
    client_b_train, client_b_test = train_test_split(
        client_b_pool, test_size=test_ratio, random_state=seed, stratify=client_b_pool["Label_Clean"]
    )

    logger.info("  Klien A Train: %s | Local Test: %s", f"{len(client_a_train):,}", f"{len(client_a_test):,}")
    logger.info("  Klien B Train: %s | Local Test: %s", f"{len(client_b_train):,}", f"{len(client_b_test):,}")

    return {
        "global_test": global_test,
        "client_a_train": client_a_train,
        "client_a_test": client_a_test,
        "client_b_train": client_b_train,
        "client_b_test": client_b_test,
    }


def compute_federated_scaling_and_weights(
    partitions: dict[str, pd.DataFrame], feature_names: list[str]
) -> dict:
    """Menghitung standardisasi global skalar dan bobot kelas global w_c."""
    logger.info("Langkah 6/7: Menghitung statistik standardisasi global skalar dan bobot kelas...")

    df_train_a = partitions["client_a_train"]
    df_train_b = partitions["client_b_train"]

    # Statistik skalar Klien A
    n_a = len(df_train_a)
    sum_a = df_train_a[feature_names].sum(axis=0).values
    sum_sq_a = (df_train_a[feature_names] ** 2).sum(axis=0).values

    # Statistik skalar Klien B
    n_b = len(df_train_b)
    sum_b = df_train_b[feature_names].sum(axis=0).values
    sum_sq_b = (df_train_b[feature_names] ** 2).sum(axis=0).values

    # Agregasi statistik global skalar (Federated Feature Scaling)
    n_total = n_a + n_b
    sum_global = sum_a + sum_b
    sum_sq_global = sum_sq_a + sum_sq_b

    mu_global = sum_global / n_total
    var_global = (sum_sq_global / n_total) - (mu_global ** 2)
    # Proteksi pembagian nol
    var_global = np.maximum(var_global, 1e-8)
    sigma_global = np.sqrt(var_global)

    # Bobot kelas global w_c = N_total / (C * N_c)
    classes = ["Normal", "SSH-Patator", "DoS"]
    total_counts = {}
    for c in classes:
        cnt_a = (df_train_a["Label_Clean"] == c).sum()
        cnt_b = (df_train_b["Label_Clean"] == c).sum()
        total_counts[c] = int(cnt_a + cnt_b)

    c_num = len(classes)
    class_weights = {}
    for c in classes:
        nc = total_counts[c]
        class_weights[c] = float(n_total / (c_num * nc)) if nc > 0 else 1.0

    logger.info("Statistik Global Selesai: N_total=%s alur", f"{n_total:,}")
    logger.info("Bobot Kelas Global (w_c): %s", class_weights)

    return {
        "n_total": int(n_total),
        "feature_names": feature_names,
        "mu_global": mu_global.tolist(),
        "sigma_global": sigma_global.tolist(),
        "class_counts": total_counts,
        "class_weights": class_weights,
    }


def save_artifacts(
    df_master: pd.DataFrame,
    partitions: dict[str, pd.DataFrame],
    stats: dict,
    output_dir: Path,
    interim_path: Path,
):
    """Menyimpan seluruh partisi Parquet dan metadata statistik JSON."""
    logger.info("Langkah 7/7: Menyimpan berkas artefak keluaran...")
    output_dir.mkdir(parents=True, exist_ok=True)
    interim_path.parent.mkdir(parents=True, exist_ok=True)

    # Simpan dataset master bersih deduplikasi (interim)
    logger.info("  Menyimpan master parquet: %s", interim_path)
    df_master.to_parquet(interim_path, index=False)

    # Simpan partisi klien dan data uji
    for name, part_df in partitions.items():
        out_file = output_dir / f"{name}.parquet"
        logger.info("  Menyimpan partisi: %s (%s baris)", out_file.name, f"{len(part_df):,}")
        part_df.to_parquet(out_file, index=False)

    # Simpan statistik global ke JSON
    stats_file = output_dir / "federated_global_stats.json"
    logger.info("  Menyimpan statistik federasi: %s", stats_file.name)
    with open(stats_file, "w", encoding="utf-8") as fp:
        json.dump(stats, fp, indent=2)

    logger.info("Seluruh pipeline praproses berhasil diselesaikan dengan sukses!")


def main():
    parser = argparse.ArgumentParser(
        description="Pipeline Praproses CIC-IDS2017 untuk Riset FCL-NIDS (Tugas Akhir FTEIC ITS)."
    )
    parser.add_argument(
        "--input",
        type=Path,
        default=PROJECT_ROOT / "Datasets" / "CIC-IDS2017",
        help="Direktori memuat berkas CSV mentah CIC-IDS2017",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=PROJECT_ROOT / "Datasets" / "clean",
        help="Direktori tujuan penyimpanan partisi parquet bersih",
    )
    parser.add_argument(
        "--interim",
        type=Path,
        default=PROJECT_ROOT / "Datasets" / "interim" / "cic_3class_dedup.parquet",
        help="Path penyimpanan master dataset deduplikasi interim",
    )
    parser.add_argument(
        "--seed",
        type=int,
        default=42,
        help="Random seed untuk reprodusibilitas pembagian data",
    )
    args = parser.parse_args()

    logger.info("Memulai Praproses CIC-IDS2017 (Project Root: %s)", PROJECT_ROOT)
    df_raw = load_raw_csvs(args.input)
    df_filtered = filter_classes(df_raw)
    df_clean = clean_anomalies_and_deduplicate(df_filtered)
    df_selected, feature_names = select_features(df_clean)
    partitions = partition_federated_data(df_selected, feature_names, test_ratio=0.20, seed=args.seed)
    stats = compute_federated_scaling_and_weights(partitions, feature_names)
    save_artifacts(df_selected, partitions, stats, args.output, args.interim)


if __name__ == "__main__":
    main()
