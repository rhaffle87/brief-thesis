# Ringkasan Eksekutif & Keputusan Hasil Bimbingan

**Topik Tugas Akhir:**  
Analisis Kinerja Deteksi Network Traffic Intrusion Menggunakan Metode Federated-Continual Learning pada Testbed Private Cloud Server  

**Mahasiswa:** Rafli Alif Ihza Hartono (NRP 5022211233)  
**Departemen:** Teknik Elektro, FTEIC, Institut Teknologi Sepuluh Nopember (ITS)  
**Tanggal Briefing:** 2026-10-06  
**Status Dokumen:** **TELAH DISETUJUI PEMBIMBING — KEPUTUSAN TERKUNCI (READY FOR PREPROCESSING)**  

---

## 🎯 8 Keputusan Metodologis Hasil Diskusi Pembimbing

Berdasarkan hasil tatap muka bimbingan bersama dosen pembimbing, seluruh poin kritis metodologi telah disepakati dan dibekukan sebagai acuan mutlak penulisan Tugas Akhir:

### 1. Injeksi Trafik Riil Ditiadakan
- **Status:** **DISETUJUI / ELIMINASI**
- **Justifikasi Pembimbing:** Injeksi trafik live (menggunakan VM 400 Hydra/Slowloris) melibatkan terlalu banyak variabel jaringan eksternal (packet loss, delay jitter, saturasi bridge interface Proxmox, dropped frames) yang tidak relevan dengan esensi pengujian algoritma. Eksperimen E0 s.d. E4 dijalankan murni berbasis offline tabular batch flow CIC-IDS2017.

### 2. Protokol Staging Testbed: Local First $\to$ Simulasi Server
- **Status:** **DISETUJUI (Two-Stage Execution)**
- **Justifikasi Pembimbing:** Seluruh arsitektur kode (pipeline praproses, arsitektur MLP, loss weighting, ekstraksi Fisher EWC, dan agregasi FedAvg Flower) direalisasikan dan divalidasi hingga stabil di workstation lokal (Docker Compose / isolated Python environment). Setelah terbukti konvergen pada 5 random seeds, konfigurasi tersebut dilanjutkan ke simulasi server pada klaster Proxmox VE.

### 3. Keseimbangan Bobot Metode dan Parameter
- **Status:** **DISETUJUI (Balanced Weighting Policy)**
- **Justifikasi Pembimbing:** Bobot regularisasi EWC ($\lambda$) harus proporsional terhadap loss tugas baru ($\mathcal{L}_{\text{task2}}$) agar tidak terjadi *plasticity freeze* (terlalu kaku) maupun *catastrophic forgetting* (terlalu bebas). Bobot kelas pada Weighted Loss juga dikalibrasi terstandarisasi serta diproteksi dengan *gradient clipping* (norm $\le 1.0$) agar gradien kelas minoritas stabil.

### 4. Hyperparameter Tuning Terstruktur
- **Status:** **DISETUJUI (Systematic Search)**
- **Justifikasi Pembimbing:** Melakukan pencarian parameter optimal secara sistematis untuk learning rate, batch size, penalti $\lambda$ EWC, communication rounds, dan local epochs dengan evaluasi rata-rata performa pada validation set 5 random seeds.

### 5. Dataset Solely CIC-IDS2017 Bersih (63 Fitur Unik)
- **Status:** **DISETUJUI (Pilihan A)**
- **Justifikasi Pembimbing:** Menggunakan secara eksklusif berkas resmi UNB CIC-IDS2017 (**Senin, Selasa, Rabu**):
  - **Senin:** Normal murni baseline (529K flow).
  - **Selasa:** SSH-Patator (3.219 flow bersih) untuk Task 1 / Client A.
  - **Rabu:** DoS 4 subvarian (193.748 flow bersih) untuk Task 2 / Client B.
  - **Kamis Dieliminasi:** Web Attacks & Infiltration memiliki sampel terlalu sedikit (Sql Injection 21, Infiltration 36; tidak layak statistik) serta cacat pelabelan pcap parah (*Rosay et al., 2022*).
  - **Jumat Dieliminasi:** PortScan adalah reconnaissance pasif, Botnet menderita bug fragmentasi flow, dan DDoS LOIC memicu bias confounding dengan DoS Rabu.
  - Dibuang 10 kolom konstan, 5 kolom duplikat identik, dan `Destination Port` (mencegah shortcut learning). Total fitur bersih: **63 fitur numerik unik + 1 Label**.

### 6. Partisi Data Normal: Random Split 50/50 All Days
- **Status:** **DISETUJUI (Pilihan A)**
- **Justifikasi Pembimbing:** Seluruh data Normal dari 3 hari digabung, lalu dibagi acak 50% untuk Task 1 dan 50% untuk Task 2 guna mengeliminasi bias pola harian (*day-pattern confound*).

### 7. Komposisi Kelas Serangan DoS Alami (Keep As-Is)
- **Status:** **DISETUJUI (Pilihan A)**
- **Justifikasi Pembimbing:** Mempertahankan komposisi alami subtipe DoS (Hulk ~89,2%, GoldenEye ~5,3%, slowloris ~2,8%, Slowhttptest ~2,7%) yang digabung menjadi satu kelas volumetrik `DoS` (total 193.748 flow).

### 8. Penanganan Class Imbalance: Weighted Loss (Keep All Clean Data)
- **Status:** **DISETUJUI (Pilihan C)**
- **Justifikasi Pembimbing:** Mempertahankan seluruh 1.529.677 baris data bersih tanpa pemangkasan massal. Menggunakan fungsi Weighted Cross-Entropy Loss dengan bobot invers frekuensi terkalibrasi untuk melindungi kelas minoritas (SSH-Patator).

---

## 📊 Matriks Eksperimen yang Dibekukan

| Kode | FL Mode | CL Mode | Peran dalam Tugas Akhir | Target Bukti Ilmiah |
|---|---|---|---|---|
| **E0** | – | – | *Centralized Joint Baseline* | Batas atas performa ideal (*Upper Bound*) |
| **E1** | Lokal | *Naive* | Pelatihan lokal sekuensial tanpa CL | Membuktikan terjadinya *catastrophic forgetting* lokal |
| **E2** | Lokal | **EWC** | Pelatihan lokal sekuensial dengan penalti Fisher | Mengukur pemulihan retensi (efek EWC lokal) |
| **E3** | **FedAvg** | *Naive* | Pelatihan federated terdistribusi tanpa CL | Mengukur dampak kolaborasi FL pada data non-IID |
| **E4** | **FedAvg** | **EWC** | **Metode Usulan Utama (FL-CL)** | Membuktikan integrasi FL + EWC meredam forgetting lintas klien |

*Seluruh pengujian (E0–E4) dieksekusi dengan 5 seed acak baku: **42, 43, 44, 45, 46** dan dilaporkan dalam format $Mean \pm Std$.*

---

## 🚀 Kesiapan Langkah Berikutnya (Next Steps)

1. **Preprocessing Dataset:** Menjalankan modul ekstraksi `scripts/preprocess_cicids2017.py` menghasilkan berkas partisi tabular Parquet bersih.
2. **Local Baseline (E0):** Melatih model MLP terpusat sebagai patokan skor atas.
3. **Local Continual Learning (E1 & E2):** Mengukur degradasi naive vs pemulihan EWC pada Task 1 (SSH) $\to$ Task 2 (DoS).
4. **Federated Execution (E3 & E4):** Menjalankan simulasi client Flower secara lokal, dilanjutkan evaluasi klaster Proxmox VE.

---

## 📌 Dokumen Rujukan Terkait di Vault
- Dokumen Keputusan Lengkap: [[Keputusan-Untuk-Pembimbing]]
- Dokumen Proposal Lengkap: [[Briefing Scope TA]]
- Laporan Lengkap EDA: [[EDA-CIC-IDS2017]]
- Rekapitulasi Verifikasi Metadata: [[Crosscheck]]
