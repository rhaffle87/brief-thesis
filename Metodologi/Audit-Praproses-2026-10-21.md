# Audit & Manifest Artefak Praproses CIC-IDS2017

**Tanggal eksekusi pipeline & audit:** 2026-10-21  
**Perintah:** `python Skrip/preprocess_cicids2017.py --input Datasets/CIC-IDS2017 --output Datasets/clean`  
**Seed partisi:** 42 · **Perilaku deduplikasi:** `keep="first"` pada ruang 78 fitur pra-seleksi (default, non-destruktif)  
**Status:** artefak DIBEKUKAN — perubahan perilaku hanya melalui flag eksplisit `--drop-conflicting-labels`

## 1. Hash SHA-256 Artefak (versi beku)

| Berkas | Ukuran (byte) | Baris | SHA-256 |
|---|---:|---:|---|
| `Datasets/interim/cic_3class_dedup.parquet` | 196,854,448 | 1,520,488 | `240806f53196484db21b018ea18c71d432f48ddd9b19ce13a2aba22527e195e8` |
| `Datasets/clean/client_a_test.parquet` | 15,059,301 | 106,400 | `d2f765836714febade9cd68f2afd45ac4546b2dc46d1279676a7dfc04391d72f` |
| `Datasets/clean/client_a_train.parquet` | 58,814,431 | 425,599 | `8a38104b03e2673a1e2e88d3fe1a1633735658521389736b1d5b747c9ed27d37` |
| `Datasets/clean/client_b_test.parquet` | 20,096,234 | 136,879 | `1047c2ae2e310a688dd9dd81ba34bf04d114324c3c1186e0396438d89c2f2e38` |
| `Datasets/clean/client_b_train.parquet` | 78,592,028 | 547,512 | `867ae339cdc97b90c4d5f6792199f15d602d44fa2d45cbe0cd4b806b583de106` |
| `Datasets/clean/global_test.parquet` | 43,625,091 | 304,098 | `59380626d94470e4beef57421ec4f90d831e48562c0a7ea5ecf48e661cc0ef0b` |
| `Datasets/clean/federated_global_stats.json` | 4,775 | - | `bebbc4ab8b43a9080d4b625e36e6087ec5b8d6a23d6aa152daeea5fca599b731` |

## 2. Distribusi Label Artefak Master (interim)

| Kelas | Jumlah Baris |
|---|---:|
| Normal | 1,323,561 |
| DoS | 193,708 |
| SSH-Patator | 3,219 |
| **Total** | **1,520,488** |

## 3. Hasil Audit Duplikat & Konflik Label (dijalankan mandiri, 2026-10-21)

| Metrik | Nilai | Ruang Fitur |
|---|---:|---|
| Baris pasca-`dropna` | 1.658.586 | 78 fitur pra-seleksi |
| Duplikat fitur (`keep=first`) | 138.098 | 78 fitur |
| Duplikat eksak (fitur+label) | 138.024 | 78 fitur |
| Selisih (baris konflik terbuang `keep=first`) | 74 | 78 fitur |
| Baris konflik lintas-label | 4.486 | 78 fitur |
| Grup vektor fitur campuran-label | 74 (ukuran min/median/maks: 2 / 8,5 / 3.361) | 78 fitur |
| Konflik kelas SSH-Patator | 0 | 78 fitur |
| Duplikat eksak sisa | 105.120 | 62 fitur final (proyeksi 78→62) |
| Konflik lintas-label sisa | 4 baris (2 grup) | 62 fitur final |
| Hasil bila `--drop-conflicting-labels` | 1.520.414 baris (diuji ke direktori sementara; artefak nyata TIDAK diubah) | 78 fitur |

## 4. Catatan Interpretasi

- **Duplikat eksak (fitur+label)** bukan kesalahan: dua aliran berbeda memang dapat menghasilkan representasi fitur identik; dipertahankan.
- **Konflik lintas-label** (vektor identik, label berbeda) adalah target audit; keputusan eliminasi hanya melalui flag eksplisit, bukan perilaku default.
- **Proyeksi 78→62** (penghapusan 16 kolom) menambah duplikat sisa di ruang final; dicatat sebagai peringatan runtime di `select_features()`, tidak dihapus otomatis.
- Sitasi Engelen et al. (2021) pada Bab 3 dibatasi pada yang memang dibahas paper (kesalahan konstruksi aliran & penempelan label), bukan konflik vektor fitur.
- Angka-angka pada dokumen lama (1.520.488 / 193.708 / 414:1) berasal dari run praproses terdahulu; artefak saat ini dan manifest ini adalah rujukan kanonik baru.
