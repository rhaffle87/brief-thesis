---
type: literatur
title: "Troubleshooting an Intrusion Detection Dataset: The CICIDS2017 Case Study"
authors: "Gints Engelen, Vera Rimmer, Wouter Joosen"
year: 2021
venue: "2021 IEEE Security and Privacy Workshops (SPW)"
doi: "10.1109/SPW53761.2021.00009"
arxiv: "2101.06093"
pdf: "PDFs/Opsional/Engelen-2021-CICIDS2017-Troubleshooting.pdf"
dibaca_dari_pdf: ya
status: ✔ terverifikasi
tags:
  - literatur
  - dataset
  - cic-ids2017
  - data-cleaning
  - port-leakage
rm_supported: Both
relevance: ⭐⭐⭐⭐⭐
prioritas: inti-terkait
---

# Engelen et al. (2021) - Troubleshooting an Intrusion Detection Dataset: The CICIDS2017 Case Study

## Metadata

**Penulis:** Gints Engelen, Vera Rimmer, Wouter Joosen  
**Institusi:** imec-DistriNet, KU Leuven, Belgium  
**Tahun:** 2021  
**Venue:** 2021 IEEE Security and Privacy Workshops (SPW)  
**DOI:** 10.1109/SPW53761.2021.00009  
**PDF Lokal:** [Engelen-2021-CICIDS2017-Troubleshooting.pdf](PDFs/Opsional/Engelen-2021-CICIDS2017-Troubleshooting.pdf)  
**Status Verifikasi:** ✔ Terverifikasi dari Crossref REST API & IEEE Xplore  
**Relevansi Scope:** ⭐⭐⭐⭐⭐ CRITICAL - Studi forensik anomali dan cacat data pada CIC-IDS2017  

---

## 📌 3 Temuan Utama

1. **Masalah Labeling dan Sinkronisasi Jam:** Menemukan inkonsistensi waktu pada log penyerangan asli CIC-IDS2017 yang menyebabkan banyak aliran serangan terlabeli sebagai Normal, atau sebaliknya aliran normal terlabeli serangan.
2. **Kebocoran Fitur Port (Port Leakage / Shortcut Learning):** Membuktikan bahwa penggunaan `Destination Port` memungkinkan model mencapai akurasi semu 99%+ hanya dengan menghafal nomor port protokol (misal: port 22 untuk SSH, port 80 untuk Web/DoS) tanpa mempelajari karakteristik pola lalu lintas jaringan yang sebenarnya.
3. **Duplikasi Data dan Aliran Tak Berarti:** Mengidentifikasi sejumlah besar aliran jaringan duplikat dan flow tak berbobot yang mendistorsi generalisasi model evaluasi jika tidak dibersihkan dengan benar.

---

## 💡 Relevansi Terhadap Penelitian Ini

- **Dasar Penghapusan Destination Port:** Menjadi rujukan ilmiah mutlak mengapa `Destination Port` wajib dieliminasi dari daftar fitur pembelajaran (Bab 3) untuk mencegah *shortcut learning*.
- **Justifikasi Deduplikasi Aliran:** Memvalidasi prosedur pembersihan data (eliminasi duplikat flow dan normalisasi fitur ekstrem) sebelum proses training model federasi.
