# Analisis Rasio dan Kebaruan Literatur Referensi Proposal Tugas Akhir

Dokumen ini menyajikan audit komprehensif mengenai distribusi tahun publikasi, indeks reputasi, dan rasio kebaruan literatur ilmiah yang digunakan pada draf Proposal Seminar Tugas Akhir.

---

## 📊 1. Ringkasan Eksekutif Rasio Kebaruan

Penghitungan didasarkan pada rentang waktu 5 tahun terakhir terhadap tahun berjalan (**2021–2026**):

| Kategori Literatur | Rentang Tahun | Jumlah Referensi | Persentase | Status Kelayakan Akademik |
|---|---|:---:|:---:|---|
| **Literatur Mutakhir ($\le 5$ Tahun)** | **2021–2026** | **13** | **61,90%** | Memenuhi ambang batas minimal ITS ($\ge 60\%$) |
| **Karya Induk Seminal ($> 5$ Tahun)** | **2011–2020** | **8** | **38,10%** | Pustaka rujukan penemu primer algoritma / dataset |
| **Total Referensi Aktif** | — | **21** | **100,00%** | **Sesuai Standar Format IEEE** |

---

## 🔬 2. Rincian Literatur Mutakhir ($\le 5$ Tahun / 2021–2026)

Tiga belas pustaka ini merupakan jurnal dan prosiding bereputasi tinggi (terindeks Scopus Q1/Q2, IEEE, Nature, Springer, Elsevier) serta laporan resmi otoritas siber:

| No | Kode Sitasi | Penulis & Tahun | Judul Publikasi | Venue / Penerbit | Kategori Relevansi |
|:---:|:---:|---|---|---|---|
| 1 | `[1]` | Check Point Research (2025) | *Q1 2025 Global Cyber Attack Report* | Check Point Software | Statistik Ancaman Siber Global |
| 2 | `[2]` | FBI IC3 (2024) | *2024 Internet Crime Report* | Federal Bureau of Investigation | Kerugian Finansial & Lanskap Serangan |
| 3 | `[6]` | Rosay *et al.* (2022) | *Network Intrusion Detection: A Comprehensive Analysis of CIC-IDS2017* | *Applied Sciences* (MDPI) | Audit 34 Kategori Anomali Dataset |
| 4 | `[7]` | Dube (2024) | *Faulty use of the CIC-IDS 2017 dataset in information security research* | *Int. Journal of Information Security* (Springer, Q1) | Audit Desinkronisasi Timestamp |
| 5 | `[8]` | Rinandri (2025) | *Pendekatan Semi-Supervised Learning GNN-AE untuk NIDS Real-Time* | Tugas Akhir Departemen Teknik Elektro FTEIC ITS | Benchmark Baseline Lokal FTEIC ITS |
| 6 | `[10]` | Popoola *et al.* (2021) | *Federated Deep Learning for Network Intrusion Detection in IoT* | *IEEE Trans. on Industrial Informatics* (Q1, IF ~11,7) | Arsitektur Federated Deep Learning NIDS |
| 7 | `[11]` | Ruzafa-Alcazar *et al.* (2021) | *D-FLIDS: Decentralized Federated Learning-based IDS* | *Computers & Security* (Elsevier, Q1) | Federated Learning Terdesentralisasi |
| 8 | `[13]` | Chen *et al.* (2021) | *Federated Class-Incremental Learning* | *IEEE/CVF CVPR* (Top-Tier Conf) | Formulasi Paradigma FCIL |
| 9 | `[14]` | Al-Abassi *et al.* (2023) | *Continual Learning for Cyber Threat Intelligence in Critical Networks* | *IEEE Trans. on Industrial Informatics* (Q1) | Penerapan Continual Learning NIDS |
| 10 | `[15]` | Engelen *et al.* (2021) | *Troubleshooting an Intrusion Detection Dataset: CICIDS2017 Case Study* | *IEEE Security and Privacy Workshops (SPW)* | Audit Kebocoran Port (*Port Leakage*) |
| 11 | `[16]` | Sarhan *et al.* (2022) | *Towards a Standard Feature Set of NIDS Datasets* | *Mobile Networks and Applications* (Springer, Q2) | Standarisasi Fitur Bersih NetFlow |
| 12 | `[17]` | van de Ven *et al.* (2022) | *Three types of incremental learning* | *Nature Machine Intelligence* (Q1, Top-Tier) | Landasan Skenario Task/Domain/Class-IL |
| 13 | `[18]` | Ghallab *et al.* (2025) | *Mitigating Catastrophic Forgetting in Continual Learning: A Literature Review* | *IJACSA* | Taksonomi Mitigasi Forgetting (Gbr 2.3) |

---

## 🏛️ 3. Justifikasi Ilmiah 8 Paper Induk Seminal (> 5 Tahun)

Dalam tradisi penulisan ilmiah akademik, menyitir langsung **karya penemu primer (*primary seminal discovery*)** adalah kewajiban etika riset guna menghindari misatribusi (*secondary citation distortion*). Delapan referensi berikut merupakan pilar kanonikal yang mendefinisikan konsep inti yang digunakan:

| No | Kode Sitasi | Penulis & Tahun | Peran & Justifikasi Ilmiah Wajib | Publikasi Asli |
|:---:|:---:|---|---|---|
| 1 | `[3]` | McMahan *et al.* (2017) | **Penemu Pertama Federated Averaging (FedAvg).** Fondasi algoritma agregasi bobot terdistribusi global. | *AISTATS 2017* |
| 2 | `[4]` | Zhao *et al.* (2018) | **Perumus Teoretis Divergensi Bobot Non-IID.** Bukti matematis penurunan akurasi akibat heterogenitas label. | *arXiv:1806.00582* |
| 3 | `[5]` | Kirkpatrick *et al.* (2017) | **Penemu Pertama Elastic Weight Consolidation (EWC).** Formulasi Matriks Informasi Fisher pada bobot sinaptik. | *PNAS 2017* |
| 4 | `[9]` | Sharafaldin *et al.* (2018) | **Pencipta Resmi Dataset CIC-IDS2017.** Spesifikasi teknis topologi B-Profile dan ekstraksi CICFlowMeter. | *ICISSP 2018* |
| 5 | `[12]` | Lopez-Paz & Ranzato (2017) | **Penemu Metrik Backward Transfer (BWT) & GEM.** Formulasi baku pengukuran *catastrophic forgetting*. | *NeurIPS 2017* |
| 6 | `[19]` | Beutel *et al.* (2020) | **Publikasi Resmi Framework Flower FL.** Kerangka kerja federasi berbasis gRPC yang diimplementasikan. | *arXiv:2007.14390* |
| 7 | `[20]` | Bergstra *et al.* (2011) | **Penemu Algoritma TPE (Optuna).** Formulasi matematika *Tree-structured Parzen Estimator*. | *NeurIPS 2011* |
| 8 | `[21]` | Loshchilov & Hutter (2019) | **Penemu Pengoptimal AdamW.** Formulasi matematika pemisahan (*decoupling*) *weight decay*. | *ICLR 2019* |

---

## 🚀 4. Strategi Peningkatan Rasio (Opsional Cadangan)

Jika dosen pembimbing atau dewan penguji menghendaki rasio pustaka $\le 5$ tahun meningkat menjadi **$> 75\%$**, empat paper survei mutakhir (2025–2026) yang telah terverifikasi dan tersedia fisiknya di `Literatur/PDFs/` dapat disisipkan ke dalam Bab 2:

1. **Rehman *et al.* (2026):** *Incremental Federated Learning for NIDS* (Elsevier, *Computer Networks*) $\rightarrow$ Menjadi pembanding arsitektur EWC vs Replay.
2. **Buyuktanir *et al.* (2025):** *Federated Learning for Network Intrusion Detection Systems: A Comprehensive Survey and Non-IID Analysis* $\rightarrow$ Menambah justifikasi skenario non-IID.
3. **Hernandez-Ramos *et al.* (2025):** *Federated Learning for Intrusion Detection: A Comprehensive Survey* (*ACM Computing Surveys*, Q1, IF ~16,6) $\rightarrow$ Memperkuat state-of-the-art FL-IDS.
4. **Gholizade *et al.* (2026):** *Federated Continual Learning: A Survey on Taxonomies and Future Directions* (*IEEE Access*) $\rightarrow$ Menegaskan konvergensi FL dan CL.

*Dengan penambahan 4 paper tersebut, rasio kebaruan akan meningkat dari **61,90%** menjadi **68,00%** (17 dari 25 referensi).*
