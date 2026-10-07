# Keputusan Metodologi Awal (ARSIP TERTUTUP & TERREKONSILIASI)

**Tanggal Draf Awal:** 2026-10-02 14:05 UTC+7  
**Tanggal Rekonsiliasi & Penutupan:** 2026-10-06 19:15 UTC+7  
**Status Dokumen:** ✅ **SELESAI / ARSIP TERTUTUP (SELURUH POIN TELAH DISETUJUI & DIKUNCI OLEH DOSEN PEMBIMBING)**  
**Rujukan Resmi Terkunci:** [Keputusan-Untuk-Pembimbing](../Keputusan/Keputusan-Untuk-Pembimbing.md) dan [Ringkasan-Untuk-Pembimbing](../Keputusan/Ringkasan-Untuk-Pembimbing.md)  

---

## 📌 Pengantar Status Dokumen
Dokumen ini merupakan catatan historis opsi-opsi metodologi yang semula berstatus *pending* pada awal inisiasi proyek (2 Oktober 2026). Melalui sesi tatap muka bimbingan bersama dosen pembimbing pada **6 Oktober 2026**, seluruh opsi implementasi telah dievaluasi, disepakati, dan dikunci secara definitif. Dokumen ini diarsipkan sebagai bukti rekam jejak evolusi desain penelitian (*audit trail*).

---

## 📋 Rekonsiliasi 4 Keputusan Metodologis Awal

### 1. Pemilihan Dataset: CIC-IDS2017 Original vs. LYCOS
* **Konteks Draf Awal (2 Okt 2026):**
  * Tautan repositori dataset bersih LYCOS-IDS2017 (Universitas Le Mans) mengalami galat *404 Not Found*.
  * Terdapat wacana menunggu mirror LYCOS atau beralih ke dataset alternatif (UNSW-NB15, CICIoMT2024).
* **Fakta Aktual Codebase & Keputusan Final (6 Okt 2026):**
  * **Status:** ✅ **DISETUJUI / TERKUNCI (Opsi CIC-IDS2017 Original)**.
  * **Keputusan Pembimbing:** Menggunakan secara eksklusif berkas resmi UNB **CIC-IDS2017 (Senin, Selasa, Rabu)**.
  * **Strategi Pembersihan:** Transparansi penuh mengutip kritik Rosay et al. (2022) [Rosay-2022-LycoSTand](../Literatur/Rosay-2022-LycoSTand.md) dan Dube et al. (2024) [Dube-2024-Faulty-CIC-IDS2017](../Literatur/Dube-2024-Faulty-CIC-IDS2017.md).
  * Menghapus 10 kolom konstan bervariansi 0, 5 kolom duplikat identik, serta `Destination Port` (mencegah *shortcut learning*). Menyisakan **63 fitur unik numerik + 1 Label**.

---

### 2. Strategi Pembagian Data (Train/Val/Test Split) & Partisi Normal
* **Konteks Draf Awal (2 Okt 2026):**
  * Mempertanyakan apakah pembagian data sebaiknya menggunakan *temporal split* (Senin train, Selasa val, Rabu test) atau *random stratified split*.
* **Fakta Aktual Codebase & Keputusan Final (6 Okt 2026):**
  * **Status:** ✅ **DISETUJUI / TERKUNCI (Random Stratified 70/15/15 + Opsi A)**.
  * **Keputusan Pembimbing:**
    1. **Split Rasio:** 70% Train, 15% Validation, 15% Test secara terstratifikasi per kelas.
    2. **Partisi Normal Task 1 & Task 2:** **Opsi A (Random Split 50/50 All Days)**. Seluruh data Normal dari Senin, Selasa, dan Rabu digabung lalu dibagi acak 50% untuk Task 1 dan 50% untuk Task 2.
    3. **Justifikasi Empiris:** Uji Decision Tree membuktikan klasifikasi Normal Selasa vs Normal Rabu menghasilkan akurasi 62,44% ± 0,34% (ada pola harian). Pembagian 50/50 meratakan variasi tersebut dan mencegah *day-pattern confound*.

---

### 3. Penanganan Class Imbalance: Undersampling vs. Weighted Loss
* **Konteks Draf Awal (2 Okt 2026):**
  * Mengasumsikan perkiraan distribusi kotor: Normal ~1,4M, SSH ~5,9K, DoS ~170K.
  * Mengusulkan opsi pemangkasan (*undersampling*) ekstrem mayoritas Normal hingga batas ~3.200 atau ~6.000 sampel per kelas (total hanya ~18K flow).
* **Fakta Aktual Codebase & Keputusan Final (6 Okt 2026):**
  * **Distribusi Terukur Riil (Pasca-Deduplikasi 79 Kolom):**
    * **Normal (BENIGN):** 1.332.710 flow (87,1%)
    * **DoS (4 Subvarian):** 193.748 flow (12,7%)
    * **SSH-Patator:** **3.219 flow bersih** (0,2%)
    * **Total Bersih 3 Kelas:** **1.529.677 flow unik** (rasio ketimpangan ~ 414 : 60 : 1).
  * **Status:** ✅ **DISETUJUI / TERKUNCI (Opsi C: Weighted Loss, Keep All Data)**.
  * **Keputusan Pembimbing:** Menolak keras opsi undersampling ekstrem karena akan membuang 99,6% data Normal dan 98% data DoS yang berharga. Seluruh 1,53 juta flow bersih dipertahankan (*keep all clean data*).
  * Ketimpangan kelas diatasi secara analitis menggunakan **Weighted Cross-Entropy Loss** dengan bobot invers frekuensi terstandarisasi:
    $$w_c = \frac{N}{|C| \times N_c}$$
    Serta diproteksi dengan *gradient clipping* (`clip_grad_norm_ <= 1.0`) untuk menjaga stabilitas gradien batch minoritas.

---

### 4. Seleksi Fitur & Perlakuan Kolom Shortcut Port
* **Konteks Draf Awal (2 Okt 2026):**
  * Mengasumsikan dataset memiliki 82 fitur mentah dan berencana memangkas menjadi 15–30 fitur menggunakan analisis korelasi atau XGBoost feature importance.
* **Fakta Aktual Codebase & Keputusan Final (6 Okt 2026):**
  * **Format Kolom Baku:** CSV asli memiliki tepat 79 kolom (78 fitur numerik + 1 kolom `Label`).
  * **Eliminasi Berbasis Bukti Empiris:**
    1. **10 Kolom Konstan (Zero Variance):** `Bwd PSH Flags`, `Fwd URG Flags`, `Bwd URG Flags`, `CWE Flag Count`, `Fwd Avg Bytes/Bulk`, `Fwd Avg Packets/Bulk`, `Fwd Avg Bulk Rate`, `Bwd Avg Bytes/Bulk`, `Bwd Avg Packets/Bulk`, `Bwd Avg Bulk Rate`.
    2. **5 Kolom Duplikat Identik (Hash Match 100%):** `Fwd Header Length.1`, `Subflow Fwd Bytes`, `Subflow Fwd Packets`, `Subflow Bwd Packets`, `SYN Flag Count`.
    3. **1 Kolom Shortcut Leakage:** `Destination Port`. Uji empiris 5-seed membuktikan port saja mencapai Macro-F1 96,44% (*shortcut learning* menghafal port 22/80).
  * **Status:** ✅ **DISETUJUI / TERKUNCI**.
  * **Hasil Akhir:** Tepat **63 fitur unik numerik + 1 Label** (total 64 kolom dataset bersih; 66 kolom pada dataframe interim dengan kolom metadata `Day` & `Label_Original`). Tidak dipangkas ke 15–30 fitur arbitrer agar seluruh profil statistik flow tetap utuh.

---

## 🔒 Ringkasan Seluruh Batasan Scope Terkunci (Scope Freeze)

Berikut adalah daftar batasan ruang lingkup yang telah dikunci secara permanen:

1. ✅ **Dataset:** Solely CIC-IDS2017 (Senin, Selasa, Rabu; 63 fitur unik numerik + 1 Label).
2. ✅ **Kelas Deteksi:** Tepat 3 kelas (Normal, SSH-Patator, DoS gabungan 4 subvarian).
3. ✅ **Model:** Single Multilayer Perceptron (MLP) kompak (Input: 63 $\to$ Dense: 64 $\to$ Dense: 32 $\to$ Output: 3) dengan Hyperparameter Tuning sistematis. Tidak menggunakan CNN, LSTM, maupun Transformer.
4. ✅ **Algoritma FL:** Federated Averaging (FedAvg) murni dengan topologi 2 Klien + 1 Server Agregator (Flower framework).
5. ✅ **Algoritma CL:** Elastic Weight Consolidation (EWC) dengan penalti kuadratik Fisher vs. Naive Fine-Tuning. Memory replay (GEM, A-GEM) ditiadakan demi privasi.
6. ✅ **Partisi Klien (Non-IID):** Client A = Normal (50%) + SSH-Patator; Client B = Normal (50%) + DoS.
7. ✅ **Skenario Tugas Sekuensial:** Task 1 = Normal + SSH-Patator $\to$ Task 2 = Normal + DoS.
8. ✅ **Penanganan Imbalance:** Weighted Cross-Entropy Loss pada seluruh 1,53 juta baris data bersih (Keep All Data).
9. ✅ **Staging Testbed:** Local First (workstation lokal) $\to$ Simulasi Server (Proxmox VE cluster).
10. ✅ **Injeksi Trafik Riil:** ❌ **DIELIMINASI RESMI** (Eksperimen E5 ditiadakan pembimbing).
11. ✅ **Matriks Eksperimen:** E0 (Centralized Upper Bound), E1 (Lokal Naive), E2 (Lokal EWC), E3 (FedAvg Naive), E4 (FedAvg + EWC). Masing-masing dieksekusi pada 5 random seeds (42, 43, 44, 45, 46).
12. ✅ **Metrik Utama:** Macro-F1, per-class Recall/F1, dan Backward Transfer (BWT).

---

## 📝 Catatan Audit Arsip

- **Status Riwayat:** Dokumen ini resmi ditutup sebagai draf pending. Tidak ada lagi keputusan metodologis yang berstatus *pending* atau menunggu persetujuan pembimbing.
- **Transisi:** Tahapan proyek beralih dari fase formulasi metodologi ke fase **implementasi praproses dataset** (`cic_3class_dedup.parquet` $\to$ 63 fitur, stratified split, weighted loss).
