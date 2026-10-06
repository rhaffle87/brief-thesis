# Ringkasan Eksekutif & Poin Diskusi Pembimbing

**Topik Tugas Akhir:**  
Analisis Kinerja Deteksi Network Traffic Intrusion Menggunakan Metode Federated-Continual Learning pada Testbed Private Cloud Server  

**Mahasiswa:** Rafli Alif Ihza Hartono (NRP 5022211233)  
**Departemen:** Teknik Elektro, FTEIC, Institut Teknologi Sepuluh Nopember (ITS)  
**Tanggal Update:** 2026-10-04  
**Status Dokumen:** Siap Dipaparkan untuk Konfirmasi & Persetujuan Pembimbing  

---

## 🎯 7 Poin Keputusan Kritis & Bukti Empiris

### 1. Versi Dataset & Standar 63 Fitur (Paling Mendasar)
- **Keputusan:** Menggunakan dataset resmi **CIC-IDS2017** (berkas CSV dari UNB untuk Senin, Selasa, Rabu).
- **Justifikasi Ilmiah:** Sumber benchmark standar internasional. Anomali dan bug dataset telah terdokumentasi secara transparan di literatur (*Rosay et al., 2022; Dube et al., 2024*).
- **Bukti Reduksi Fitur Empiris:**
  - Total kolom mentah: 79 kolom (78 fitur numerik + 1 kolom Label).
  - **10 Kolom Konstan Dibuang (Variansi = 0,000000):**  
    `Bwd PSH Flags`, `Fwd URG Flags`, `Bwd URG Flags`, `CWE Flag Count`, `Fwd Avg Bytes/Bulk`, `Fwd Avg Packets/Bulk`, `Fwd Avg Bulk Rate`, `Bwd Avg Bytes/Bulk`, `Bwd Avg Packets/Bulk`, `Bwd Avg Bulk Rate`.
  - **5 Kolom Duplikat Dibuang (100% Identik via Hash):**  
    `Fwd Header Length.1`, `Subflow Fwd Bytes`, `Subflow Fwd Packets`, `Subflow Bwd Packets`, `SYN Flag Count`.
  - **Hasil:** **63 Fitur Unik + 1 Kolom Label** (Total 64 kolom).
  - *Opsi Lanjutan:* Terdapat 3 kolom nyaris identik (99,99% kesamaan: `Avg Fwd Segment Size`, `Avg Bwd Segment Size`, `Subflow Bwd Bytes`). Jika dibuang, fitur menjadi 60.
- **Konfirmasi Pembimbing:** *Apakah Bapak/Ibu menyetujui penggunaan 63 fitur unik ini sebagai baseline data skripsi?*

---

### 2. Eliminasi Fitur "Destination Port" (Pencegahan Shortcut Learning)
- **Temuan Uji Empiris (Decision Tree Baseline, 5 Seeds, 3.219 flow/kelas):**

| Kondisi Masukan Fitur | Macro-F1 ($Mean \pm Std$) | Keterangan |
|---|---|---|
| **Port Saja (1 Fitur)** | **96,44% ± 0,16%** | Model hanya menghafal nomor port (SSH=22, HTTP=80) |
| **Tanpa Port (62 Fitur)** | **98,02% ± 0,34%** | Klasifikasi mengandalkan statistik flow trafik |
| **Semua Fitur (63 Fitur)** | **99,35% ± 0,17%** | Separabilitas mendekati sempurna |

- **Temuan Dominasi Fitur Tunggal:**  
  Fitur `Bwd Packet Length Std` secara mandiri mampu menghasilkan **Macro-F1 90,93% ± 0,28%**. Hal ini menunjukkan tingginya separabilitas bawaan dataset akibat *fingerprint* alat serang (Hulk, Patator).
- **Usulan Mahasiswa:** **Membuang fitur Destination Port sebagai konfigurasi default**. Tujuannya agar model tidak sekadar menghafal nomor port layanan, melainkan belajar dari dinamika statistik flow.
- **Konfirmasi Pembimbing:** *Apakah Destination Port disetujui untuk dieksklusi dari masukan model?*

---

### 3. Pemilihan Data Normal Antar-Tugas (*Temporal Confound Mitigation*)
- **Temuan Empiris:**  
  Pengujian klasifikasi Normal Selasa vs Normal Rabu (tanpa port) menghasilkan akurasi **62,44% ± 0,34%** (di atas peluang acak 50%). Ini membuktikan adanya pola harian (*day-pattern confound*).
- **Pilihan:**
  - **Opsi A (Diusulkan):** Pembagian acak (*Random Split*) data Normal dari Senin, Selasa, dan Rabu ke dalam Task 1 dan Task 2. Menghindari model mempelajari pergeseran hari alih-alih pola serangan.
  - **Opsi B:** Normal Selasa untuk Task 1, Normal Rabu untuk Task 2 (Realistis secara kronologis, tetapi berisiko bias hari).
- **Konfirmasi Pembimbing:** *Apakah Opsi A disetujui untuk partisi data Normal?*

---

### 4. Komposisi Kelas Serangan DoS
- **Data Riil Setelah Deduplikasi:**  
  Total flow DoS = 193.748 baris. Terdiri atas: DoS Hulk (172.849; 89,2%), DoS GoldenEye (10.286), DoS slowloris (5.385), dan DoS Slowhttptest (5.228).
- **Usulan Mahasiswa:** Mempertahankan distribusi alami (didominasi Hulk 89%) karena mencerminkan volume volumetrik serangan di dunia nyata, dengan tetap menyertakan seluruh 4 varian serangan DoS.
- **Konfirmasi Pembimbing:** *Apakah komposisi DoS alami (Hulk-dominated) disetujui?*

---

### 5. Plafon Subsampling Seimbang (*Balanced Sampling Limit*)
- **Fakta Data Riil:**  
  Setelah deduplikasi 79 kolom, kelas minoritas **SSH-Patator hanya memiliki 3.219 flow unik** (dibandingkan Normal 1.332.710 flow dan DoS 193.748 flow).
- **Usulan Mahasiswa:**  
  Mengunci plafon evaluasi seimbang pada **~3.200 sampel per kelas** (~2.250 data latih per kelas setelah stratified split 70/15/15). Ini mencegah bias mayoritas ekstrem tanpa perlu melakukan oversampling sintetis (SMOTE) yang berisiko mengubah distribusi flow.
- **Konfirmasi Pembimbing:** *Apakah plafon seimbang ~3.200 sampel per kelas ini disepakati?*

---

### 6. Fokus Metrik Evaluasi Forgetting
- **Analisis Kritis:**  
  Karena separabilitas global sangat tinggi (~98%), rata-rata akurasi atau Macro-F1 global tidak sensitif terhadap terjadinya *catastrophic forgetting*.
- **Usulan Mahasiswa:**  
  Evaluasi pembuktian EWC difokuskan pada:
  1. **Recall Kelas SSH-Patator (Task 1)** sebelum vs sesudah model mempelajari DoS (Task 2).
  2. **Nilai Backward Transfer (BWT):** $BWT = R_{2,1} - R_{1,1}$.
- **Konfirmasi Pembimbing:** *Apakah pelaporan hasil memprioritaskan metrik Recall SSH dan BWT?*

---

### 7. Desain Partisi Non-IID Dua Client
- **Rancangan Partisi:**
  - **Client A:** Normal + SSH-Patator (Simulasi sensor cabang kantor/server SSH).
  - **Client B:** Normal + DoS (Simulasi sensor web-server/DMZ).
  - **Alur Sekuensial:** Task 1 (SSH) $\to$ Task 2 (DoS).
- **Konfirmasi Pembimbing:** *Apakah skenario partisi 2 client non-IID ini disepakati?*

---

## 📊 Matriks Eksperimen yang Siap Dieksekusi

| Kode | FL Mode | CL Mode | Peran dalam Tugas Akhir | Target Bukti Ilmiah |
|---|---|---|---|---|
| **E0** | – | – | *Centralized Joint Baseline* | Batas atas performa ideal |
| **E1** | Lokal | *Naive* | Pelatihan lokal sekuensial tanpa CL | Membuktikan terjadinya catastrophic forgetting |
| **E2** | Lokal | **EWC** | Pelatihan lokal sekuensial dengan penalti Fisher | Mengukur pemulihan retensi (efek EWC lokal) |
| **E3** | **FedAvg** | *Naive* | Pelatihan federated terdistribusi tanpa CL | Mengukur dampak kolaborasi FL pada data non-IID |
| **E4** | **FedAvg** | **EWC** | **Metode Usulan (FL-CL)** | Membuktikan integrasi FL + EWC meredam forgetting |
| **E5** | – | – | *(Opsional)* Inferensi live traffic lab Proxmox | Uji inferensi pasif bila diminta penguji |

*Semua eksperimen (E0–E4) dijalankan 5 seed acak (42, 43, 44, 45, 46) dan dilaporkan $Mean \pm Std$.*

---

## 📚 Tinjauan Literatur 5 Tahun Terakhir (13 Paper Utama: 2021–2026)

1. **Liu & Chang (2026)** - *EWC Done Right*, arXiv:2603.18596.
2. **Rehman et al. (2026)** - *Incremental FL for IDS*, arXiv:2603.10776.
3. **Gholizade et al. (2026)** - *Federated Continual Learning Survey*, arXiv:2606.11272.
4. **Buyuktanir et al. (2025)** - *FL in Intrusion Detection (non-IID)*, Cluster Computing, DOI: 10.1007/s10586-025-05325-w.
5. **Hernandez-Ramos et al. (2025)** - *Intrusion Detection Based on FL Survey*, ACM CSUR, DOI: 10.1145/3731596.
6. **Hamedi et al. (2025)** - *Federated Continual Learning Survey*, arXiv:2502.07059.
7. **Jin et al. (2024)** - *FL-IIDS Concept Drift*, Computers & Security, DOI: 10.1016/j.cose.2023.103577.
8. **Dube et al. (2024)** - *Faulty Use of CIC-IDS2017*, Information Systems Frontiers, DOI: 10.1007/s11416-023-00509-7.
9. **Carta et al. (2023)** - *Avalanche: A PyTorch Library for CL*, JMLR 24(363).
10. **Rosay et al. (2022)** - *NID Analysis of CIC-IDS2017 (LycoSTand)*, Computers & Security, DOI: 10.1016/j.cose.2022.102675.
11. **Talpur & Gurusamy (2022)** - *GFCL: Gradient-based FCL for IDS*, arXiv:2204.11010.
12. **Lomonaco et al. (2021)** - *Avalanche Library*, IEEE/CVF CVPRW, DOI: 10.1109/CVPRW53098.2021.00399.
13. **Agrawal et al. (2021)** - *FL for IDS: Concepts & Challenges*, arXiv:2106.09527.

*(Didukung 3 buku teks FL terkini: Nguyen 2024, Jung 2025, Gao 2022; serta 5 seminal paper klasik: McMahan 2017, Kirkpatrick 2017, Lopez-Paz 2017, Sharafaldin 2018, Beutel 2020).*

---

## 📌 Dokumen Rujukan Terkait di Vault
- Dokumen Proposal Lengkap: [[Briefing Scope TA_ Federated-Continual Learning untuk Deteksi Intrusi]]
- Laporan Lengkap EDA: [[EDA-CIC-IDS2017]]
- Rekapitulasi Verifikasi Metadata: [[Crosscheck]]
- Bukti Audit Terminal: [[Audit-Bukti-2026-10-03]]
