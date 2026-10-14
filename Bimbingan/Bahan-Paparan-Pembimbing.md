# Bahan Paparan Bimbingan Tugas Akhir

**Judul Penelitian:**  
Analisis Kinerja Deteksi Network Traffic Intrusion Menggunakan Metode Federated-Continual Learning pada Testbed Private Cloud Server  

**Mahasiswa:** Rafli Alif Ihza Hartono (NRP 5022211233)  
**Departemen:** Teknik Elektro, FTEIC, Institut Teknologi Sepuluh Nopember (ITS)  
**Dokumen Pendukung Utama:** [Ringkasan-Untuk-Pembimbing](../Keputusan/Ringkasan-Untuk-Pembimbing.md), [Briefing-Scope-TA](../Proposal/Briefing-Scope-TA.md), [EDA-CIC-IDS2017](../Metodologi/EDA-CIC-IDS2017.md), [Crosscheck](../Literatur/Crosscheck.md)  

---

## 📌 Bagian 1: Latar Belakang & Celah Penelitian

1. **Dinamika Ancaman & Kebutuhan Model Adaptif:**  
   Serangan siber berkembang secara dinamis. Model ML deteksi intrusi yang dilatih satu kali (*static offline training*) akan mengalami penurunan performa saat menghadapi varian serangan baru di masa mendatang.
2. **Kendala Privasi Trafik Jaringan (Urgensi FL):**  
   Data log trafik memuat informasi internal yang sensitif dan terikat regulasi perlindungan data. *Federated Learning* (FedAvg) memungkinkan beberapa klien (misal: sensor subnet) melatih model bersama tanpa mengirimkan data mentah ke server pusat.
3. **Kendala Catastrophic Forgetting (Urgensi CL/EWC):**  
   Ketika model menerima data serangan baru secara sekuensial (Task 1 $\to$ Task 2), bobot jaringan tertimpa (*overwritten*), mengakibatkan lupa drastis terhadap kelas serangan terdahulu. *Elastic Weight Consolidation* (EWC) melindungi bobot-bobot krusial menggunakan penalti kuadratik berbasis matriks informasi Fisher.
4. **Celah Penelitian (*Research Gap*):**  
   Kombinasi *Federated Continual Learning* (FCL) pada data trafik jaringan dengan karakteristik distribusi non-IID antar-klien belum banyak dievaluasi secara terukur dan transparan.

---

## 🎯 Bagian 2: Rumusan Masalah & Batasan Scope

### Rumusan Masalah (2 Poin Baku Sesuai Standar Skripsi S1 Teknik Elektro ITS)
1. **RM 1:** Bagaimana kinerja deteksi intrusi model yang dilatih secara federated (FedAvg) dibandingkan dengan pelatihan lokal pada data non-IID dua klien?
2. **RM 2:** Seberapa efektif metode *Elastic Weight Consolidation* (EWC) dalam memitigasi *catastrophic forgetting* saat model mempelajari serangan baru secara sekuensial pada skenario lokal maupun federated (FedAvg + EWC)?

### 4 Titik Pembekuan Ruang Lingkup (*Anti-Scope Creep*)
- **Dataset:** Hanya **CIC-IDS2017** (Senin, Selasa, Rabu). 3 Kelas: Normal, SSH-Patator, DoS.
- **Model:** Hanya **MLP** kompak (`Input(63) → Linear(64) → Linear(32) → Linear(3)`).
- **Federated Learning:** Hanya **FedAvg** dengan **2 Client + 1 Server** (Client A: Normal+SSH; Client B: Normal+DoS).
- **Continual Learning:** Hanya **EWC** vs **Naive Fine-Tuning** (Urutan: Task 1 SSH $\to$ Task 2 DoS).

---

## 🔬 Bagian 3: Temuan Audit Empiris Dataset CIC-IDS2017

Berdasarkan pemindaian menyeluruh 1,53 juta baris data mentah:

1. **Hasil Deduplikasi Data Mentah:**
   - Total baris awal: 1.668.530 baris.
   - Duplikat identik: 132.909 baris (7,97%).
   - Baris 3-kelas bersih setelah dedup: **1.529.677 baris** (BENIGN 1.332.710; DoS 193.748; SSH-Patator 3.219).
2. **Standar Fitur Baku (62 Fitur Unik + 1 Label):**
   - Dari 78 fitur asli:
     - Dibuang **10 kolom konstan bervariansi 0** (misal: `Bwd PSH Flags`, `Fwd URG Flags`, dll.).
     - Dibuang **5 kolom duplikat 100% identik** (`Fwd Header Length.1`, `Subflow Fwd Bytes`, `Subflow Fwd Packets`, `Subflow Bwd Packets`, `SYN Flag Count`).
   - Sisa: **62 fitur unik numerik**.
3. **Uji Kebocoran Fitur Port (Port Leakage Test, 5 Seeds):**
   - Fitur `Destination Port` saja menghasilkan **Macro-F1 96,44%** (model hanya menghafal nomor port 22/80).
   - Tanpa port, Macro-F1 tetap mencapai **98,02%**, dan satu fitur `Bwd Packet Length Std` secara mandiri mencapai **Macro-F1 90,93%**.
   - **Kesimpulan:** Separabilitas tinggi dataset mencerminkan *fingerprint* alat serang, bukan kecerdasan deteksi intrusi murni. Maka Destination Port **diusulkan dibuang** agar model belajar pola statistik flow.
4. **Justifikasi Pemilihan Berkas Senin, Selasa, dan Rabu (Eliminasi Kamis & Jumat):**
   - **Senin (529K flow):** Menyediakan trafik Normal murni baseline tanpa serangan.
   - **Selasa (445K flow):** Menyediakan serangan SSH-Patator (3.219 flow bersih) untuk Task 1.
   - **Rabu (692K flow):** Menyediakan serangan DoS 4 subvarian (193.748 flow bersih) untuk Task 2.
   - **Kamis Dieliminasi:** Web Attacks & Infiltration memiliki sampel terlalu sedikit (Sql Injection 21, Infiltration 36; tidak layak secara statistik) serta mengalami desinkronisasi pelabelan pcap parah (*Rosay et al., 2022*).
   - **Jumat Dieliminasi:** PortScan adalah reconnaissance pasif, Botnet cacat fragmentasi alur, dan DDoS LOIC memicu bias confounding dengan DoS Rabu tanpa menyumbang kelas baru.

---

## 📋 Bagian 4: Tujuh Poin Konfirmasi dengan Dosen Pembimbing

| No | Poin Keputusan | Bukti / Dasar Pertimbangan | Keputusan Pembimbing | Status Konfirmasi |
|---|---|---|---|---|
| **1** | **Dataset & 62 Fitur** | Anomali 10 konstan & 5 duplikat terbukti via array hashing | Pakai solely CIC-IDS2017 resmi dengan 62 fitur unik | ✅ **DISETUJUI** |
| **2** | **Partisi Data Normal** | Klasifikasi Normal Selasa vs Rabu akurasi 62,44% (ada pola hari) | Random split 50/50 data Normal all-days (hindari bias hari) | ✅ **DISETUJUI (Opsi A)** |
| **3** | **Komposisi Kelas DoS** | Total DoS 193.748 baris; DoS Hulk mendominasi 89,2% | Pertahankan distribusi alami (volumetrik realistis) | ✅ **DISETUJUI (Opsi A)** |
| **4** | **Handling Imbalance** | Menghindari data loss 99% akibat subsampling ekstrem | Weighted Loss (Keep All Clean Data ~1.53M baris) | ✅ **DISETUJUI (Opsi C)** |
| **5** | **Perlakuan Port** | Port-only F1 = 96,44% (*shortcut learning*) | Buang Destination Port (fokus ke dinamika flow) | ✅ **DISETUJUI** |
| **6** | **Injeksi Trafik** | Terlalu banyak parameter jaringan dinamis | Dieliminasi (fokus evaluasi offline batch) | ✅ **DISETUJUI (Ditiadakan)** |
| **7** | **Staging Testbed** | Memastikan kestabilan pipeline sebelum masuk server | Local First → Simulasi Server Proxmox VE | ✅ **DISETUJUI** |
| **8** | **Keseimbangan Bobot** | Penalti EWC λ dan class weights harus seimbang | Penyeimbangan bobot metode & parameter + Gradient Clipping | ✅ **DISETUJUI** |
| **9** | **Hyperparameter Tuning**| Menjamin ketahanan dan reproduktifitas model | Grid/Random search sistematis pada 5 seed | ✅ **DISETUJUI** |

---

## 🧪 Bagian 5: Matriks Pengujian Eksperimen (E0 – E5)

```
       [ E0: Centralized Joint Baseline ] (Batas Atas Ideal)
             /                        \
    (Jalur Pelatihan Lokal)     (Jalur Pelatihan Federated)
           /                                \
  [ E1: Lokal Naive ]              [ E3: FedAvg Naive ]
          ↓ (Efek EWC)                      ↓ (Efek EWC pada FL)
  [ E2: Lokal EWC ]                [ E4: FedAvg + EWC (FL-CL) ]
                                            ↓
                                 [ E5: Live Traffic Testbed ] (Opsional)
```

- **E0 (Centralized Baseline):** MLP dilatih terpusat dengan semua kelas. Menetapkan plafon performa.
- **E1 (Lokal Naive):** Klien dilatih Task 1 (SSH), lalu Task 2 (DoS) tanpa mitigasi. Pembuktian lupa drastis.
- **E2 (Lokal EWC):** Pelatihan sekuensial lokal dengan penalti kuadratik Fisher. Mengukur pemulihan retensi.
- **E3 (FedAvg Naive):** Pelatihan terdistribusi 2 klien tanpa continual learning.
- **E4 (FedAvg + EWC):** **Metode usulan utama**. Menjawab apakah FL dan EWC saling melengkapi.
- **E5 (Live Traffic):** ❌ **Dieliminasi**. Injeksi live traffic resmi ditiadakan oleh pembimbing untuk menjaga kemurnian evaluasi algoritma FL-CL.

*Setiap eksperimen dieksekusi pada **5 seed acak terstandarisasi (42, 43, 44, 45, 46)** dan disajikan dalam format Mean ± Std.*

---

## ⚙️ Bagian 6: Parameter Evaluasi Komputasi vs QoS Jaringan (Mengacu pada Skripsi Hafizh, 2024)

1. **Parameter QoS Jaringan Mentah Ditiadakan (Out of Scope):**  
   - Metrik fisik seperti throughput, bandwidth link, packet loss, dan jitter ditiadakan selaras dengan peniadaan injeksi live traffic oleh pembimbing.  
   - *Pengganti Relevan untuk FL:* **Communication Overhead FL** (mengukur ukuran payload parameter model dalam KB per round yang ditransfer antara client dan server Flower: $2 \times \text{Size}(\theta) \times R$).
2. **Evaluasi Resource Instance Komputasi Diadopsi:**  
   - **Memory Footprint (EWC vs Replay Buffer):** Membuktikan bahwa EWC hanya membutuhkan alokasi memori bobot $\theta^*$ dan matriks Fisher diagonal $F_i$ (konstan $\approx$ beberapa puluh KB), jauh lebih efisien dibanding buffer Experience Replay yang menyimpan ribuan sampel flow mentah di RAM.  
   - **CPU Training Duration:** Mengukur overhead durasi komputasi perhitungan penalti EWC per *local epoch*.  
   - **Ukuran Model (.pt / .onnx):** Mengukur ukuran biner model MLP siap pakai di edge.
3. **Waktu Inferensi per Flow ($\mu\text{s}$):**  
   - Mengadopsi metodologi Hafizh (2024, Hal. 102) yang mengukur latensi inferensi 10,07 $\mu\text{s}$/flow. Model MLP kita (63 $\to$ 64 $\to$ 32 $\to$ 3) diukur rata-rata waktu inferensinya pada test set untuk membuktikan kesiapan *near real-time detection*.
4. **Hyperparameter Tuning Sistematis (Optuna / 5 Seeds):**  
   - Melakukan tuning parameter optimal untuk penalti EWC ($\lambda$), *learning rate* ($\eta$), dan jumlah *local epochs* ($E$) dengan evaluasi multi-seed.
5. **Confusion Matrix Komparatif Sebelum vs Sesudah Task 2:**  
   - Memvisualisasikan matriks prediksi untuk membuktikan secara empiris bahwa kelas SSH (Task 1) tidak terlupakan setelah model mempelajari serangan DoS (Task 2).

---

## 📚 Bagian 7: Landasan Pustaka 5 Tahun Terakhir (2021 – 2026)

Tugas akhir ini didukung oleh **13 artikel jurnal/prosiding internasional bereputasi dalam 5 tahun terakhir**:

1. **Liu & Chang (2026)** - *EWC Done Right*, arXiv:2603.18596 (Kritik estimasi matriks Fisher pada EWC).
2. **Rehman et al. (2026)** - *Incremental Federated Learning for IDS in IoT*, arXiv:2603.10776 (Komparasi EWC vs GEM pada FL-IDS).
3. **Gholizade et al. (2026)** - *Federated Continual Learning: A Comprehensive Survey*, arXiv:2606.11272.
4. **Buyuktanir et al. (2025)** - *Federated learning in intrusion detection: advancements, applications, and future directions*, *Cluster Computing* (Springer), DOI: 10.1007/s10586-025-05325-w.
5. **Hernandez-Ramos et al. (2025)** - *Intrusion Detection Based on Federated Learning: A Systematic Review*, *ACM Computing Surveys*, DOI: 10.1145/3731596.
6. **Hamedi et al. (2025)** - *A Survey on Federated Continual Learning*, arXiv:2502.07059.
7. **Jin et al. (2024)** - *A federated learning approach for collaborative intrusion detection against concept drift (FL-IIDS)*, *Computers & Security* (Elsevier), DOI: 10.1016/j.cose.2023.103577.
8. **Dube et al. (2024)** - *Faulty use of the CIC-IDS 2017 dataset in information security research*, *Information Systems Frontiers* (Springer), DOI: 10.1007/s11416-023-00509-7.
9. **Carta et al. (2023)** - *Avalanche: A PyTorch Library for Continual Learning*, *JMLR*, Vol. 24, No. 363.
10. **Rosay et al. (2022)** - *Network Intrusion Detection: A Comprehensive Analysis of CIC-IDS2017*, *Computers & Security*, DOI: 10.1016/j.cose.2022.102675.
11. **Talpur & Gurusamy (2022)** - *GFCL: Gradient-based Federated Continual Learning for IDS*, arXiv:2204.11010.
12. **Lomonaco et al. (2021)** - *Avalanche: an End-to-End Library for Continual Learning*, *IEEE/CVF CVPRW*, DOI: 10.1109/CVPRW53098.2021.00399.
13. **Agrawal et al. (2021)** - *Federated Learning for IDS: Concepts, Challenges, and Future Directions*, arXiv:2106.09527.

Serta didukung **3 buku teks akademik terkini**:
- **Nguyen et al. (2024)**, *Federated Learning: Theory and Practice*, Elsevier Academic Press.
- **Jung et al. (2025)**, *Federated Learning: From Theory to Practice*, Springer.
- **Gao et al. (2022)**, *Federated Learning: Fundamentals and Advances*, Springer.

---

## 🗓️ Bagian 8: Rencana Kerja & Milestone Berikutnya

- **Minggu 1–2 (Saat Ini):** Konfirmasi 7 poin ruang lingkup dan persetujuan dosen pembimbing.
- **Minggu 3–4:** Ekstraksi data 62 fitur, stratified split seimbang, pembekuan dataset (*Freeze Point 1*).
- **Minggu 5–6:** Eksekusi baseline terpusat E0 (5 seed) dan penentuan ambang batas referensi.
- **Minggu 7–12:** Implementasi eksperimen inti (E1, E2, E3, E4).
- **Minggu 13–16:** Multi-seed aggregation, penulisan buku skripsi, dan persiapan sidang.
