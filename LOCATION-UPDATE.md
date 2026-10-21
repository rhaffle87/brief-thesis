# Status Lokasi & Organisasi Proyek (Thesis & FL-CL)

**Terakhir Diperbarui:** 2026-10-06 19:10 UTC+7  
**Status Sistem:** ✅ Terorganisasi, Bersih, & Siap Eksekusi  

---

## 📁 1. Lokasi Proyek Aktual

### A. Repositori Dokumentasi & Obsidian Vault (Thesis)
- **Path Utama:** `E:\Projects\thesis\`
- **Struktur:** 14 direktori bersih tanpa prefiks angka (nama folder: `Dashboard`, `Proposal`, `Literatur`, `Metodologi`, `Eksperimen`, `Hasil`, `Penulisan`, `Bimbingan`, `Keputusan`, `Aset`, `Laporan`, `Arsip`, `Templates`, `Datasets`).
- **Cadangan Riil (Snapshot):** `E:\Projects\thesis_backup_20261002\` (snapshot sebelum restrukturisasi massal tanggal 2–3 Oktober 2026).
- **Integritas Tautan:** 190 tautan internal aktif tervalidasi (0 broken links).

### B. Skrip EDA & Verifikasi Internal Repositori (Thesis)
- **Path Skrip Utama:** `E:\Projects\thesis\Skrip\`
- **Modul EDA & Audit Fitur:** `E:\Projects\thesis\Skrip\EDA\` (15 skrip tervalidasi)
  - `scan_vault_links.py` (Pemindaian tautan internal Markdown)
  - `verify_column_hashes.py` & `rosay_column_check.py` (Verifikasi kolom konstan & duplikat via hash array)
  - `port_test_classification.py` (Uji kebocoran fitur port 5-seed: Macro-F1 96,44%)
  - `feature_importance_analysis.py` (Analisis dominasi fitur tunggal)
  - `preprocess_lycos.py` (Skrip standardisasi format dataset)
- **Repositori Implementasi Eksternal (FL-CL):** `E:\Projects\fl-cl\` (Lingkungan Virtual `.venv` dan modul runtime FL)

---

## 📊 2. Status Dataset & Aturan Fitur

### A. Dataset Terkunci: CIC-IDS2017
- **Lokasi Mentah:** `E:\Projects\thesis\Datasets\CIC-IDS2017\`
  - `Monday-WorkingHours.pcap_ISCX.csv` (100% BENIGN)
  - `Tuesday-WorkingHours.pcap_ISCX.csv` (BENIGN + SSH-Patator + FTP-Patator)
  - `Wednesday-workingHours.pcap_ISCX.csv` (BENIGN + 4 varian DoS: Hulk, GoldenEye, slowloris, Slowhttptest)
- **Lokasi Cache Dedup:** `E:\Projects\thesis\Datasets\interim\cic_3class_dedup.parquet` (1.520.488 baris, 3 kelas).
- **Catatan LYCOS-IDS2017:** Tautan unduh resmi server Universitas Le Mans berstatus *404 Not Found*. Diputuskan secara formal menggunakan CIC-IDS2017 resmi dengan batasan terdokumentasi (lihat [DATASET-UNAVAILABLE-LYCOS.md](Metodologi/DATASET-UNAVAILABLE-LYCOS.md)).

### B. Aturan Seleksi Fitur (62 Fitur Unik + 1 Label)
- **Total Kolom Awal:** 79 kolom (78 fitur + 1 Label).
- **10 Kolom Konstan Dibuang (Variansi = 0):**  
  `Bwd PSH Flags`, `Fwd URG Flags`, `Bwd URG Flags`, `CWE Flag Count`, `Fwd Avg Bytes/Bulk`, `Fwd Avg Packets/Bulk`, `Fwd Avg Bulk Rate`, `Bwd Avg Bytes/Bulk`, `Bwd Avg Packets/Bulk`, `Bwd Avg Bulk Rate`.
- **5 Kolom Duplikat Dibuang (100% Identik):**  
  `Fwd Header Length.1`, `Subflow Fwd Bytes`, `Subflow Fwd Packets`, `Subflow Bwd Packets`, `SYN Flag Count`.
- **Fitur Tersisa:** **62 fitur unik numerik + 1 Label** (total 64 kolom).
- **3 Kolom Nyaris Identik (99,99%) Dicatat untuk Opsi Pembimbing:**  
  `Avg Fwd Segment Size`, `Avg Bwd Segment Size`, `Subflow Bwd Bytes`.

---

## 📚 3. Status Literatur & Pembekuan Algoritma

1. **Literatur:**
   - 25 paper inti dan pendukung tersedia lengkap dalam bentuk PDF di [Literatur/PDFs/](Literatur/PDFs) (13 paper) dan [Literatur/PDFs/Opsional/](Literatur/PDFs/Opsional) (12 paper).
   - Seluruh metadata diverifikasi pada [Literatur/Crosscheck.md](Literatur/Crosscheck.md).
2. **Algoritma Terkunci:**
   - **FL:** Hanya FedAvg dengan topologi 2 client + 1 server aggregator ([Keputusan-Pembekuan-FL.md](Keputusan/Keputusan-Pembekuan-FL.md)).
   - **CL:** Hanya EWC vs Naive Fine-Tuning sekuensial ([Keputusan-Pembekuan-CL.md](Keputusan/Keputusan-Pembekuan-CL.md)).
   - **Arsitektur Model:** Single MLP (Input: 62 → Dense: 64 (ReLU) → Dense: 32 (ReLU) → Output: 3 (Softmax)).

---

## 🎯 4. Dokumen Kunci untuk Tahap Sekarang

1. **Briefing Pembimbing:** [Keputusan/Ringkasan-Untuk-Pembimbing.md](Keputusan/Ringkasan-Untuk-Pembimbing.md) (memuat 7 pertanyaan konfirmasi scope, dataset, dan evaluasi).
2. **Dashboard Proyek:** [Dashboard/Dashboard.md](Dashboard/Dashboard.md) (monitoring mingguan dan matriks E0-E5).
3. **Hasil Verifikasi EDA:** [Metodologi/EDA-CIC-IDS2017.md](Metodologi/EDA-CIC-IDS2017.md) dan [Metodologi/EDA-Verifikasi.md](Metodologi/EDA-Verifikasi.md).
4. **Struktur Lengkap Vault:** [README-Structure.md](README-Structure.md).

---

## 🚀 5. Rencana Langkah Kerja Berikutnya

1. **Konsultasi Pembimbing:** Membawa dokumen `Ringkasan-Untuk-Pembimbing.md` untuk mengunci kesepakatan final 7 pertanyaan.
2. **Pipeline Praproses CIC-IDS2017:**
   - Ekstrak subset data 3 kelas dari CSV/parquet.
   - Buang 10 kolom konstan dan 5 kolom identik (menghasilkan 62 fitur).
   - Normalisasi (StandardScaler fit hanya pada train set).
   - Pembagian stratified train/val/test (60/20/20) dengan 5 seed (42 s.d. 46).
3. **Pipeline Metrik & Verifikasi BWT:**
   - Implementasi perhitungan Macro-F1, per-class recall/F1, Accuracy.
   - Implementasi rumus Backward Transfer (BWT) dan pengujian pada matriks sintetis.
4. **Eksekusi Eksperimen E0 (Centralized Baseline):**
   - Melatih MLP terpusat pada 5 seed untuk menetapkan *upper bound* performa klasifikasi.
