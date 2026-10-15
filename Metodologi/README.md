# 🔬 Direktori Metodologi

Direktori ini memuat seluruh rancangan metodologi saintifik, laporan exploratory data analysis (EDA), audit anomali dataset, serta skrip analisis eksplorasi.

## 📂 Dokumen Utama:

- **[EDA-CIC-IDS2017.md](EDA-CIC-IDS2017.md)**: Laporan komprehensif audit fitur, analisis korelasi, kebocoran port (*shortcut learning*), dan justifikasi eliminasi `Destination Port`.
- **[EDA-Verifikasi.md](EDA-Verifikasi.md)**: Hasil reproduksi empiris verifikasi 10 kolom konstan (varian nol) dan 5 pasang kolom duplikat identik.
- **[CRITICAL-CIC-IDS2017-Issues.md](CRITICAL-CIC-IDS2017-Issues.md)**: Ringkasan catatan teknis cacat dataset CIC-IDS2017 berdasarkan literatur Dube (2024) dan Engelen (2021).
- **[DATASET-UNAVAILABLE-LYCOS.md](DATASET-UNAVAILABLE-LYCOS.md)**: Dokumentasi pembuktian kegagalan akses server mirror LYCOS-IDS2017 dan justifikasi penggunaan dataset asli CIC-IDS2017 yang dikurasi secara independen.

## 🐍 Skrip Analisis & Verifikasi:
Seluruh skrip audit empiris dan validasi fitur telah dipindahkan secara permanen ke direktori internal repositori:
- **[Direktori Skrip Utama](../Skrip/README.md)** (`Skrip/`): Memuat skrip praproses dan modul EDA.
- `Skrip/EDA/` (15 skrip): Skrip audit kolom konstan, pasangan hash duplikat, uji baseline Decision Tree 5-seed, dan pemindai tautan Markdown.
- Skrip lokal tambahan: `eda_cicids2017.py` dan `eda_cicids2017_simple.py`.
