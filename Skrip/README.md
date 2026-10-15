# 🛠️ Direktori Skrip Repositori Tugas Akhir (`Skrip/`)

Direktori ini memuat seluruh modul kode sumber untuk praproses dataset, exploratory data analysis (EDA), audit integritas fitur, dan validasi reprodusibilitas eksperimen Tugas Akhir:
> **Judul:** *Analisis Kinerja Deteksi Network Traffic Intrusion Menggunakan Metode Federated-Continual Learning pada Testbed Private Cloud Server*  
> **Penyusun:** Rafli Alif Ihza Hartono (NRP 5048231003)  
> **Departemen:** Teknik Elektro, FTEIC - ITS Surabaya

---

## 📂 Struktur Direktori & Berkas

```
Skrip/
├── README.md                      # Dokumentasi katalog dan panduan eksekusi skrip (berkas ini)
├── preprocess_cicids2017.py       # Pipeline produksi praproses CIC-IDS2017 (62 fitur, 3 kelas, partisi FL)
├── preprocess_lycos.py            # Modul praproses legacy format LYCOS-IDS2017
└── EDA/                           # Modul analisis eksplorasi data dan audit empiris fitur
    ├── column_pairs_check.py      # Pengecekan multikolinearitas dan korelasi pasangan kolom
    ├── constant_columns_check.py  # Deteksi 10 kolom konstan (variansi tepat 0)
    ├── day_artifact_test.py       # Uji day-confound perbedaan latar belakang trafik antar-hari
    ├── eda_full_pandas.py         # Audit penuh 79 kolom CIC-IDS2017 berbasis pandas
    ├── eda_full_stdlib.py         # Audit dataset berbasis standard library (efisiensi RAM)
    ├── feature_importance_analysis.py # Analisis daya pisah dan dominasi fitur tunggal
    ├── port_leakage_fast.py       # Uji cepat kebocoran label pada Destination Port
    ├── port_leakage_targeted.py   # Uji terarah kebocoran port SSH dan DoS
    ├── port_leakage_test.py       # Eksperimen komparatif klasifikasi dengan vs tanpa port
    ├── port_test_classification.py # Uji baseline Decision Tree 5-seed (bukti F1 96,44%)
    ├── port_test_full.py          # Uji skala penuh kebocoran port pada seluruh data bersih
    ├── rosay_column_check.py      # Verifikasi duplikasi kolom sesuai temuan Rosay et al. (2022)
    ├── scan_vault_links.py        # Pemindaian integritas tautan internal dokumen Markdown
    └── verify_column_hashes.py    # Deteksi 5 pasang kolom duplikat identik via hashing SHA-256
```

---

## 🔬 Spesifikasi Modul Utama

### 1. Pipeline Praproses Produksi (`preprocess_cicids2017.py`)
* **Masukan:** Tiga berkas CSV mentah CIC-IDS2017 (`Monday`, `Tuesday`, `Wednesday`) di `Datasets/CIC-IDS2017/`.
* **Proses:**
  1. *Penyaringan 3 Kelas Target:* Normal (BENIGN), SSH-Patator, dan DoS (gabungan Hulk, GoldenEye, slowloris, slowhttptest).
  2. *Eksklusi:* FTP-Patator (5.933 alur) dan Heartbleed (11 alur).
  3. *Pembersihan Nilai Ekstrem:* Konversi Inf ke NaN dan eliminasi baris bernilai NaN.
  4. *Deduplikasi:* Eliminasi 132.909 baris duplikat mentah (menyisakan 1.529.677 baris bersih).
  5. *Seleksi Fitur Terkunci (62 Fitur):* Eliminasi 10 kolom konstan variansi nol, 5 kolom duplikat identik ($r=1.0$), dan kolom `Destination Port` (anti-*shortcut learning*).
  6. *Partisi Terdistribusi Non-IID:*
     - Klien A: Normal (50%) + SSH-Patator (100%)
     - Klien B: Normal (50%) + DoS (100%)
     - Global Held-Out Test Set (20% terstratifikasi)
     - Local Client Test Sets (20% terstratifikasi per klien)
  7. *Kalkulasi Skalar Global (Federated Global Scaling):* Menghitung $\mu_{\text{global}}$ dan $\sigma_{\text{global}}$ via agregasi skalar ($n_k, \sum x, \sum x^2$), serta bobot kelas global $w_c = \frac{N_{\text{total}}}{C \cdot N_c}$ ke berkas `federated_global_stats.json`.
* **Keluaran:** Berkas master `Datasets/interim/cic_3class_dedup.parquet` dan partisi siap latih di `Datasets/clean/`.

### 2. Uji Kebocoran Port (`EDA/port_test_classification.py`)
* **Fungsi:** Membuktikan secara empiris bahwa nomor port menjadi jalan pintas (*shortcut learning*).
* **Metode:** Pengujian baseline Decision Tree pada 5 random seeds (42, 43, 44, 45, 46) dengan 3.219 sampel seimbang per kelas.
* **Hasil Empiris:**
  - Port Only (1 fitur): Macro-F1 **96,44% +/- 0,16%**
  - Tanpa Port (62 fitur): Macro-F1 **98,02% +/- 0,34%**
  - Semua Fitur (termasuk port): Macro-F1 **99,35% +/- 0,17%**
* **Signifikansi:** Menjadi bukti ilmiah mandiri untuk mengeksklusi `Destination Port` dari naskah proposal.

### 3. Verifikasi Kolom Konstan (`EDA/constant_columns_check.py`)
* **Fungsi:** Memindai kolom bervariansi nol pada seluruh 1.529.677 baris data bersih.
* **Hasil:** 10 kolom bervariansi tepat 0,000000 (`Bwd PSH Flags`, `Fwd URG Flags`, `Bwd URG Flags`, `CWE Flag Count`, `Fwd Avg Bytes/Bulk`, `Fwd Avg Packets/Bulk`, `Fwd Avg Bulk Rate`, `Bwd Avg Bytes/Bulk`, `Bwd Avg Packets/Bulk`, `Bwd Avg Bulk Rate`).

### 4. Verifikasi Kolom Duplikat (`EDA/verify_column_hashes.py`)
* **Fungsi:** Menguji korelasi dan kesamaan nilai array kolom menggunakan SHA-256 hash.
* **Hasil:** Mengonfirmasi 5 pasang kolom dengan korelasi Pearson $r = 1.0$ yang menyebabkan multikolinearitas sempurna (`Fwd Header Length.1`, `Subflow Fwd Bytes`, `Subflow Fwd Packets`, `Subflow Bwd Packets`, `SYN Flag Count`).

---

## 🚀 Panduan Eksekusi Terminal

Seluruh skrip dirancang mandiri (*portable*) menggunakan `pathlib.Path` dinamis sehingga dapat dijalankan langsung dari akar repositori:

```powershell
# 1. Menjalankan pipeline praproses lengkap (menghasilkan partisi 62 fitur):
python Skrip/preprocess_cicids2017.py --input Datasets/CIC-IDS2017 --output Datasets/clean

# 2. Verifikasi 10 kolom konstan (variansi nol):
python Skrip/EDA/constant_columns_check.py

# 3. Uji empiris kebocoran port (Decision Tree 5-seed):
python Skrip/EDA/port_test_classification.py

# 4. Verifikasi duplikasi kolom identik:
python Skrip/EDA/verify_column_hashes.py

# 5. Pemindaian integritas tautan internal dokumen Markdown:
python Skrip/EDA/scan_vault_links.py
```
