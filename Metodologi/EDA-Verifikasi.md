# Verifikasi Ulang Hasil EDA CIC-IDS2017

**Tanggal Eksekusi:** 2026-10-03  
**Lingkungan:** `E:/Projects/fl-cl/.venv/Scripts/python.exe`  
**Dataset Mentah:** `E:/Projects/thesis/Datasets/CIC-IDS2017/` (Monday, Tuesday, Wednesday CSV)  
**Dataset Cache:** `E:/Projects/thesis/Datasets/interim/cic_3class_dedup.parquet` (1.529.677 baris)

---

## 1. Jumlah Baris dan Distribusi Label per File Mentah

Skrip eksekusi: `E:/Projects/fl-cl/scripts/eda/eda_full_pandas.py`

### Monday-WorkingHours.pcap_ISCX.csv
- Total baris: 529.918 (79 kolom)
- BENIGN: 529.918 (100.00%)
- Baris duplikat (semua 79 kolom): 26.935 (5,08%)
- Baris unik setelah dedup: 502.983

### Tuesday-WorkingHours.pcap_ISCX.csv
- Total baris: 445.909 (79 kolom)
- BENIGN: 432.074 (96,90%)
- FTP-Patator: 7.938 (1,78%) [di luar scope 3-kelas]
- SSH-Patator: 5.897 (1,32%) [target kelas 1]
- Baris duplikat (semua 79 kolom): 24.065 (5,40%)
- Setelah dedup: 421.844 baris
  - BENIGN: 412.692 (97,83%)
  - FTP-Patator: 5.933 (1,41%)
  - SSH-Patator: 3.219 (0,76%)

### Wednesday-workingHours.pcap_ISCX.csv
- Total baris: 692.703 (79 kolom)
- BENIGN: 440.031 (63,52%)
- DoS Hulk: 231.073 (33,36%)
- DoS GoldenEye: 10.293 (1,49%)
- DoS slowloris: 5.796 (0,84%)
- DoS Slowhttptest: 5.499 (0,79%)
- Heartbleed: 11 (0,00%) [di luar scope]
- Baris duplikat (semua 79 kolom): 81.909 (11,82%)
- Setelah dedup: 610.794 baris
  - BENIGN: 417.035 (68,28%)
  - DoS Hulk: 172.849 (28,30%)
  - DoS GoldenEye: 10.286 (1,68%)
  - DoS slowloris: 5.385 (0,88%)
  - DoS Slowhttptest: 5.228 (0,86%)
  - Heartbleed: 11 (0,00%)
- DoS Total (setelah dedup, 4 varian digabung): 193.748 baris (Hulk mendominasi 89,21%)

### Rekapitulasi Data Mentah
- Total baris sebelum dedup: 1.668.530
- Total duplikat (semua kolom): 132.909 (7,97%)
- Total baris setelah dedup: 1.535.621
- Total data 3 kelas (BENIGN + SSH-Patator + DoS, tanpa FTP-Patator dan Heartbleed): 1.529.677 baris

---

## 2. Analisis Kolom Konstan (Zero Variance)

Skrip eksekusi: `E:/Projects/fl-cl/scripts/eda/constant_columns_check.py`  
Dataset: 1.529.677 baris (data 3 kelas setelah dedup)

Daftar 10 kolom dengan variansi tepat 0 (semua baris bernilai identik):
1. `Bwd PSH Flags` (variance = 0,000000, 1 nilai unik)
2. `Fwd URG Flags` (variance = 0,000000, 1 nilai unik)
3. `Bwd URG Flags` (variance = 0,000000, 1 nilai unik)
4. `CWE Flag Count` (variance = 0,000000, 1 nilai unik)
5. `Fwd Avg Bytes/Bulk` (variance = 0,000000, 1 nilai unik)
6. `Fwd Avg Packets/Bulk` (variance = 0,000000, 1 nilai unik)
7. `Fwd Avg Bulk Rate` (variance = 0,000000, 1 nilai unik)
8. `Bwd Avg Bytes/Bulk` (variance = 0,000000, 1 nilai unik)
9. `Bwd Avg Packets/Bulk` (variance = 0,000000, 1 nilai unik)
10. `Bwd Avg Bulk Rate` (variance = 0,000000, 1 nilai unik)

---

## 3. Analisis Pasangan Kolom Identik (Hashing Seluruh Kolom)

Metode: Hashing nilai array per kolom pada 1.529.677 baris.

### Grup Kolom Identik Tepat (100% Identik):
1. `Fwd Header Length` == `Fwd Header Length.1` (100,0000%, corr = 1,000000)
2. `Total Length of Fwd Packets` == `Subflow Fwd Bytes` (100,0000%, corr = 1,000000)
3. `Total Fwd Packets` == `Subflow Fwd Packets` (100,0000%, corr = 1,000000)
4. `Total Backward Packets` == `Subflow Bwd Packets` (100,0000%, corr = 1,000000)
5. `Fwd PSH Flags` == `SYN Flag Count` (100,0000%, corr = 1,000000)
6. `Fwd Packet Length Mean` == `Avg Fwd Segment Size` (99,9999% identik karena floating-point, corr = 1,000000)
7. `Bwd Packet Length Mean` == `Avg Bwd Segment Size` (99,9968% identik karena floating-point, corr = 1,000000)
8. `Total Length of Bwd Packets` == `Subflow Bwd Bytes` (99,9946% identik, 82 baris selisih numerik mikro, corr = 1,000000)

### Pasangan Serupa tetapi Tidak Identik:
- `Average Packet Size` vs `Packet Length Mean`:
  - Identik: 13,69% (209.425 / 1.529.677 baris)
  - Korelasi Pearson: 0,997691
  - Kesimpulan: Bukan kolom identik, tetapi fitur turunan dengan korelasi sangat tinggi.

---

## 4. Perhitungan Jumlah Fitur Akhir yang Sah

- Total kolom CSV asli: 79 kolom
- Komposisi CSV asli: 78 kolom fitur + 1 kolom `Label`
- Dikurangi kolom konstan (zero variance): 10 kolom
- Sisa fitur setelah eliminasi konstan: 78 - 10 = 68 fitur

### Opsi A (Standar Baku yang Disepakati & Disetujui Pembimbing):
- Kolom duplikat yang dibuang (5 kolom 100% identik):
  1. `Fwd Header Length.1` (duplikat persis `Fwd Header Length`)
  2. `Subflow Fwd Bytes` (duplikat persis `Total Length of Fwd Packets`)
  3. `Subflow Fwd Packets` (duplikat persis `Total Fwd Packets`)
  4. `Subflow Bwd Packets` (duplikat persis `Total Backward Packets`)
  5. `SYN Flag Count` (duplikat persis `Fwd PSH Flags`)
- Perhitungan: 78 fitur - 10 konstan - 5 duplikat = **63 fitur unik numerik** (+ 1 kolom `Label` = **64 kolom dataset bersih**, atau 66 kolom jika menyertakan kolom pembantu `Day` dan `Label_Original` di dataframe interim).

### Opsi B (Pembersihan Lengkap Termasuk Pasangan Floating-Point Rosay 2022):
- Menghapus 8 kolom redundan (`Fwd Header Length.1`, `Subflow Fwd Bytes`, `Subflow Bwd Bytes`, `Subflow Fwd Packets`, `Subflow Bwd Packets`, `Avg Fwd Segment Size`, `Avg Bwd Segment Size`, `SYN Flag Count`):
- Perhitungan: 78 fitur - 10 konstan - 8 duplikat = **60 fitur unik** (+ 1 kolom `Label` = 61 kolom total).

*Catatan penting: Cache parquet interim memiliki 66 kolom karena menyertakan kolom metadata `Day` dan `Label_Original`. Kedua kolom pembantu ini dikeluarkan sebelum pelatihan sehingga menyisakan 63 input fitur + 1 label target.*

---

## 5. Uji Destination Port dan Tiga Kondisi Pohon Keputusan (5 Seed)

Skrip eksekusi: `E:/Projects/fl-cl/scripts/eda/port_test_classification.py`  
Sampel: 3.219 per kelas (seimbang, dibatasi jumlah minimum SSH-Patator), 5 seed (42-46).

### Hasil Per-Seed (Macro-F1):
| Seed | Port Only | No Port | All Features |
|---|---|---|---|
| 42 | 0,9626 | 0,9739 | 0,9914 |
| 43 | 0,9640 | 0,9807 | 0,9914 |
| 44 | 0,9664 | 0,9804 | 0,9948 |
| 45 | 0,9660 | 0,9831 | 0,9952 |
| 46 | 0,9629 | 0,9831 | 0,9948 |
| **Rerata ± Std** | **0,9644 ± 0,0016** | **0,9802 ± 0,0034** | **0,9935 ± 0,0017** |

### Perbandingan dengan Laporan Terdahulu:
- Angka yang dilaporkan sebelumnya: 96,44 / 98,02 / 99,35 macro-F1.
- Angka hasil uji ulang hari ini: 96,44 / 98,02 / 99,35 macro-F1.
- Selisih: **0,0000** (terverifikasi 100% konsisten dan deterministik).

### Analisis Fitur Dominan (Keterbatasan Dataset):
- Skrip: `feature_importance_analysis.py`
- Fitur tunggal `Bwd Packet Length Std`: menghasilkan macro-F1 **90,93% ± 0,28%** tanpa fitur lain.
- Fitur tunggal `Bwd Header Length`: menghasilkan macro-F1 **88,37% ± 0,36%**.
- **Keterbatasan Kritis:** Separabilitas tinggi (98% macro-F1 tanpa port) bukan berarti sistem IDS sudah sempurna, melainkan menunjukkan bahwa dataset CIC-IDS2017 memiliki pintasan (shortcut features) dan artefak perangkat penyerang. Oleh karena itu, evaluasi forgetting pada FedAvg+EWC harus dinilai dari **Recall SSH-Patator dan BWT (Backward Transfer)**, bukan dari Macro-F1 agregat.
