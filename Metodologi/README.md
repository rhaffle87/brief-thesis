# 🔬 Direktori Metodologi

Direktori ini memuat seluruh rancangan metodologi saintifik, laporan exploratory data analysis (EDA), audit anomali dataset, serta skrip analisis eksplorasi.

## 📂 Dokumen Utama:

- **[EDA-CIC-IDS2017.md](file:///e:/Projects/thesis/Metodologi/EDA-CIC-IDS2017.md)** — Laporan komprehensif audit fitur, analisis korelasi, kebocoran port (*shortcut learning*), dan justifikasi eliminasi `Destination Port`.
- **[EDA-Verifikasi.md](file:///e:/Projects/thesis/Metodologi/EDA-Verifikasi.md)** — Hasil reproduksi empiris verifikasi 10 kolom konstan (varian nol) dan 5 pasang kolom duplikat identik.
- **[CRITICAL-CIC-IDS2017-Issues.md](file:///e:/Projects/thesis/Metodologi/CRITICAL-CIC-IDS2017-Issues.md)** — Ringkasan catatan teknis cacat dataset CIC-IDS2017 berdasarkan literatur Dube (2024) dan Engelen (2021).
- **[DATASET-UNAVAILABLE-LYCOS.md](file:///e:/Projects/thesis/Metodologi/DATASET-UNAVAILABLE-LYCOS.md)** — Dokumentasi pembuktian kegagalan akses server mirror LYCOS-IDS2017 dan justifikasi penggunaan dataset asli CIC-IDS2017 yang dikurasi secara independen.

## 🐍 Skrip Analisis:
- `eda_cicids2017.py` — Skrip bantu analisis fitur dan kalkulasi statistik awal.
- `eda_cicids2017_simple.py` — Skrip verifikasi cepat integritas kolom.
*(Skrip pipeline produksi berada di folder repositori kode `fl-cl/scripts/`).*
