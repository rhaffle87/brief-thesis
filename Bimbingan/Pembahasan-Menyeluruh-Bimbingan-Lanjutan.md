# Pembahasan Menyeluruh Bimbingan Lanjutan: Arsitektur Federated-Continual Learning (FCL)

**Judul Penelitian:**  
Analisis Kinerja Deteksi Network Traffic Intrusion Menggunakan Metode Federated-Continual Learning pada Testbed Private Cloud Server  

**Mahasiswa:** Rafli Alif Ihza Hartono (NRP 5022211233)  
**Departemen:** Teknik Elektro, FTEIC, Institut Teknologi Sepuluh Nopember (ITS)  
**Tujuan Dokumen:** Menjawab secara tuntas, mendalam, empiris, dan berbasis literatur terverifikasi seluruh 9 poin arahan dosen pembimbing guna mematangkan proposal tugas akhir dan menyelaraskan peta riset laboratorium.

---

## 📌 Ringkasan 9 Poin Arahan Dosen & Solusi Mahasiswa

| No | Poin Arahan Dosen Pembimbing | Solusi & Posisi Ilmiah Mahasiswa | Bagian Dokumen |
|:--:|---|---|:---:|
| **1** | Cari metode lain yang linier/seirama FCL agar tidak redundan dan saling melengkapi dengan riset dosen. | Memetakan spektrum metode FCL (FedCurv, FedWeIT, GLFC, TARGET, Ditto) dan menegaskan posisi usulan pada *Exemplar-Free FCL* (FedAvg + Local EWC). | [Bagian 1](#1-pemetaan-metode-fcl-yang-linier-dan-saling-melengkapi) |
| **2** | Tinjau literatur mengenai jumlah node server dan klien yang diperlukan. | Menelaah standar industri *Cross-Silo FL* ($K=2\text{ s.d. }10$) vs *Cross-Device FL* ($K=20\text{ s.d. }100$) berdasarkan taksonomi Kairouz et al. (2021). | [Bagian 2](#2-tinjauan-literatur-skala-jumlah-node-klien-dan-server) |
| **3** | Cari implementasi FCL di luar domain Network Intrusion Detection Systems (NIDS). | Menyajikan paper publikasi riil terverifikasi di domain Perimeter Physical Sensing, SCADA Industrial IoT, Healthcare, dan Kendaraan Otonom V2X. | [Bagian 3](#3-implementasi-fcl-di-luar-domain-nids-kajian-literatur--paper-riil) |
| **4** | Tambahkan satu rumusan masalah umum/fondasional (RM 0) sebelum RM 1 dan RM 2. | Menyusun struktur piramida 3-tingkat: RM 0 (Kelayakan Arsitektur FCL) $\to$ RM 1 (Komparasi Spasial FL vs Lokal) $\to$ RM 2 (Mitigasi Temporal Catastrophic Forgetting via EWC). | [Bagian 4](#4-penambahan-rumusan-masalah-fondasional-rm-0) |
| **5** | Penyesuaian parameter pengukuran dan fitur jika diwajibkan penambahan skenario live injection. | Memetakan metrik QoS jaringan (Delay, Packet Loss, Throughput), beban CPU/RAM, kendala timeout 120s flow extraction, dan solusi Early-Flow Features. | [Bagian 5](#5-penyesuaian-parameter-pengukuran-dan-fitur-pada-skenario-live-injections) |
| **6** | Literature review secara menyeluruh pada metode Continual Learning (EWC dsb). | Menyusun taksonomi komparatif 10 metode CL (EWC, Online EWC, SI, MAS, LwF, ER, GEM, A-GEM, PackNet, LoRA-CL) beserta formulasi matematisnya. | [Bagian 6](#6-literatur-review-menyeluruh-continual-learning-methods) |
| **7** | Literature review secara menyeluruh pada metode Federated Learning (FedAvg dsb). | Menyusun taksonomi komparatif 9 metode FL (FedAvg, FedProx, SCAFFOLD, FedNova, MOON, FedCurv, FedWeIT, Ditto, pFedMe). | [Bagian 7](#7-literatur-review-menyeluruh-federated-learning-methods) |
| **8** | Konseptualisasi skala banyak edge node: Analogi perimeter pagar kampus ITS 180 hektar. | Merancang arsitektur hirarkis 3-tingkat (Sensor Pagar Fisik $\to$ Edge Gateway FL Clients $\to$ Server Pusat) dan fallback plan simulasi multi-node ($K=2, 5, 10$). | [Bagian 8](#8-konseptualisasi-skala-banyak-edge-node-analogi-pagar-perimeter-its-180-hektar) |
| **9** | Konsolidasi ketetapan dataset CIC-IDS2017 & pemetaan dataset alternatif non-NIDS. | Mengunci CIC-IDS2017 (62 fitur, tanpa port-leakage, Weighted Loss), melaporkan temuan 74 baris konflik label, dan memetakan 5 dataset alternatif. | [Bagian 9](#9-konsolidasi-ketetapan-dataset-cic-ids2017--pemetaan-dataset-luar-domain-ids) |

---

## 1. Pemetaan Metode FCL yang Linier dan Saling Melengkapi

### 1.1 Menghindari Redundansi dengan Peta Riset Laboratorium
Dosen pembimbing telah memiliki portofolio riset di domain pembelajaran mesin terdistribusi dan keamanan siber. Agar penelitian tugas akhir ini tidak redundan melainkan saling melengkapi (*complementary*), posisi ilmiah riset dipetakan terhadap spektrum riset eksisting:

```
[ Peta Riset Eksisting Laboratorium ]
  ├─ FL Statis: FedAvg/FedProx pada data tabular tanpa skenario sekuensial kelas baru (Batch Learning).
  ├─ CL Sentralistik: EWC / Replay pada server tunggal tanpa desentralisasi privasi.
  └─ Deteksi Anomali Biner: Normal vs Anomali menggunakan Autoencoder / CNN berat.

[ Posisi Saling Melengkapi Riset Ini (Novelty Space) ]
  ├─ Dimensi Privasi: Exemplar-Free FCL (Zero-buffer; tidak menyimpan sampel mentah di edge client).
  ├─ Dimensi Sinergi: Menguji interaksi langsung antara agregasi spasial (FedAvg) dan penalti temporal lokal (EWC).
  └─ Dimensi Efisiensi Edge: Model MLP ultra-ringan 6.211 parameter (~24,84 KB) dengan latensi inferensi mikrodetik (μs).
```

### 1.2 Pemisahan Eksplisit: Dimensi Spasial vs Dimensi Temporal
Salah satu aspek terpenting yang harus dijelaskan secara transparan kepada pembimbing adalah pemisahan dua dimensi persoalan dalam FCL:

1. **Dimensi Spasial (Non-IID Label Skew antar-Klien):**
   - Klien A memegang data lalu lintas Subnet Internal (dominan serangan kredensial: **Normal + SSH-Patator**).
   - Klien B memegang data lalu lintas Perimeter DMZ (dominan serangan volumetrik: **Normal + DoS**).
   - Kelas Normal hadir pada kedua klien sebagai baseline trafik operasional (bukan *zero class overlap* murni, melainkan *attack-label skew*).
   - Ditangani oleh algoritma agregasi terpusat **FedAvg** di Server Flower.

2. **Dimensi Temporal (Aliran Tugas Sekuensial Task 1 $\to$ Task 2 di Klien):**
   - **Fase 1 (Task 1: SSH-Patator, Ronde $1 \dots R_1$):**
     * Klien A melatih data Normal + SSH-Patator.
     * Klien B melatih data Normal.
     * Server mengagregasi bobot global via FedAvg.
     * Di akhir ronde $R_1$, Klien A menghitung diagonal Matriks Informasi Fisher ($F_A$) dan mengunci bobot acuan $\theta_1^*$. Nilai $F_A$ dan $\theta_1^*$ disimpan secara privat di lokal Klien A (tidak diunggah ke server).
   - **Fase 2 (Task 2: DoS, Ronde $R_1+1 \dots R_1+R_2$):**
     * Klien A menerima tugas baru (atau data background Normal) dan melatih model dengan fungsi loss total berpenalti EWC:
       $$\mathcal{L}_{\text{total}}(\theta) = \mathcal{L}_{\text{Task2}}(\theta) + \frac{\lambda}{2} \sum_{i} F_{A,i} (\theta_i - \theta_{1,i}^*)^2$$
     * Klien B melatih data Normal + DoS menggunakan Cross-Entropy biasa.
     * Server FedAvg merata-ratakan bobot pembaruan dari kedua klien.
   - **Inti Hipotesis Ilmiah yang Diuji (*EWC Dilution Effect*):**
     Apakah rata-rata bobot di server FedAvg akan melunturkan (*dilute*) proteksi penalti Fisher yang dipasang secara lokal oleh Klien A saat Klien B memperbarui bobot ke arah kelas DoS? Jika terjadi pelunturan, seberapa besar nilai degradasi *Backward Transfer* (BWT)?

### 1.3 Tabel Komparasi Menyeluruh Metode Seirama FCL
Tabel berikut memetakan metode-metode pembelajaran terfederasi berkelanjutan (*Federated Continual Learning*) yang linier di literatur:

| Nama Metode & Rujukan | Paradigma FCL | Dimensi Fokus | Fungsi Objektif / Mekanisme Inti | Overhead Komunikasi per Ronde | Kebutuhan Memori Lokal | Posisi Komplementer terhadap Riset Dosen |
|---|---|---|---|---|---|---|
| **FedAvg + Local EWC**<br>*(Sistem Usulan)* | Regularisasi Parameter Lokal (*Exemplar-Free*) | **Temporal & Spasial Ortogonal** (EWC di lokal, FedAvg di server) | $\min_w \mathcal{L}_{\text{local}}(w) + \frac{\lambda}{2} \sum_i F_i (w_i - w_{1,i}^*)^2$<br>Agregasi: $w^{t+1} = \sum \frac{n_k}{N} w_k^{t+1}$ | **Sangat Rendah**<br>($1\times$ payload bobot model, estimasi teoretis $\approx 24,84\text{ KB}$) | **Sangat Ringan**<br>(Hanya vektor diagonal Fisher $F_i$ dan bobot $\theta^*$) | **Inti Usulan Skripsi:** Menguji ketahanan proteksi EWC lokal terhadap agregasi FedAvg di edge NIDS. |
| **FedCurv**<br>*(Shoham et al., arXiv:1910.07796)* | Regularisasi Kurvatur Terdistribusi | **Spasial Non-IID Drift** (Meredam divergensi bobot antar-klien) | $\mathcal{L}_k(w) + \sum_{j \neq k} \frac{\lambda}{2} (w - w_j^*)^T F_j (w - w_j^*)$ | **Tinggi ($2\times$ lipat)**<br>Klien mengirim bobot $w$ DAN diagonal Fisher $F$ ke server | Sedang<br>(Menyimpan Fisher dan bobot seluruh klien lain) | **Pembanding Teoretis Bab 2:** Regularisasi Fisher tingkat server; payload komunikasi berlipat ganda. |
| **FedWeIT**<br>*(Yoon et al., ICML 2021)* | Isolasi Parameter Modular | **Temporal & Spasial Terpadu** (Mencegah interferensi task) | Dekomposisi bobot jaringan:<br>$W_k^{(t)} = B \odot M_k^{(t)} + A_k^{(t)}$ | **Tinggi**<br>(Transmisi sparse mask $M$ dan modul adaptif $A$) | Tinggi<br>(Alokasi parameter membengkak seiring jumlah task) | **Varian Arsitektural:** Terlalu kompleks (*overkill*) untuk MLP tabular 6.211 parameter. |
| **GLFC**<br>*(Dong et al., CVPR 2022)* | Replay Terdistribusi + Distilasi | **Class-Incremental Learning** (Visi Komputer) | Replay buffer lokal + generator prototipe sintetis + loss distilasi kelas lama | Sedang-Tinggi<br>(Pertukaran prototipe fitur kelas antar-klien) | Sangat Tinggi<br>(Menyimpan buffer gambar & modul generator) | **Domain Visual:** Membutuhkan representasi fitur kontinu; tidak alami untuk tabular flow. |
| **TARGET**<br>*(Zhang et al., IEEE ICCV 2023)* | Distilasi Generatif Bebas-Sampel | **Exemplar-Free FCL** | Melatih generator lokal untuk mentransfer distribusi data lama tanpa buffer | Sangat Tinggi<br>(Pelatihan GAN/generator lokal di edge) | Tinggi<br>(Modul generator tambahan membebani edge) | **Domain Visual Kompleks:** Beban komputasi generator melampaui kapasitas prosesor edge NIDS. |
| **Ditto**<br>*(Li et al., ICML 2021)* | Personalized Federated Learning (pFL) | **Spasial Personalisasi** (Client-Specific Model) | $\min_{v_k} h_k(v_k) = F_k(v_k) + \frac{\lambda}{2} \|v_k - w^*\|^2$<br>Menjaga model personal dekat dengan global | Rendah<br>(Hanya bertukar bobot model global $w^*$) | Sedang<br>(Menyimpan model personal $v_k$ dan model global $w^*$) | **Alternatif Personalisasi:** Menghasilkan model yang berbeda di tiap klien; tidak menguji retensi memori temporal. |

### 1.4 Penajaman Matriks Komplementer dengan Payung Riset Dosen Pembimbing
Untuk memastikan kontribusi skripsi ini berada dalam posisi saling menguatkan (*complementary synergy*) dan bukan duplikasi terhadap publikasi laboratorium pembimbing, berikut adalah pemetaan komplementer eksplisit antara payung riset dosen dan fokus tugas akhir mahasiswa:

| Dimensi Komparasi | Payung Riset Dosen Pembimbing (Eksisting / Baseline Lab) | Riset Tugas Akhir Mahasiswa (FCL Usulan) | Sinergi & Nilai Tambah bagi Laboratorium |
|---|---|---|---|
| **Paradigma Pelatihan** | Pembelajaran Terfederasi Statis (Batch FL) atau Deteksi Anomali Tersentralisasi. | *Federated Continual Learning* (FCL) yang menggabungkan pembelajaran spasial dan temporal sekuensial. | Memperluas kapabilitas arsitektur FL laboratorium dari model batch statis menjadi model adaptif yang tahan terhadap serangan baru. |
| **Penanganan Dinamika Serangan** | Asumsi kelas serangan tersedia serentak pada fase inisialisasi pelatihan model. | Skenario *Class-Incremental Learning* (Class-IL) di mana kelas serangan muncul secara sekuensial (Task 1 $\to$ Task 2). | Menyediakan bukti empiris mengenai fenomena *catastrophic forgetting* pada trafik jaringan terdistribusi di bawah fluktuasi ancaman temporal. |
| **Kepatuhan Privasi Data Historis** | Menggunakan data terpusat atau *Experience Replay buffer* pada node lokal untuk menjaga akurasi. | *Exemplar-Free FCL* (Zero-buffer) berbasis regularisasi kelengkungan parameter (*Elastic Weight Consolidation*). | Mengeliminasi risiko pelanggaran regulasi privasi (UU PDP / GDPR) karena node edge sama sekali tidak menyimpan rekaman paket mentah historis. |
| **Distribusi Data Klien** | Umumnya dievaluasi pada data berdistribusi identik (IID) atau variasi kuantitas alur sederhana. | *Non-IID Label Skew* terpolarisasi (Klien A: Subnet Internal, Klien B: Perimeter DMZ) dengan data latar belakang Normal beririsan. | Menguji batas ketahanan (*boundary condition*) algoritma konsensus saat tiap gateway menghadapi karakteristik serangan yang berbeda. |
| **Integritas Fitur Dataset** | Seringkali menggunakan set fitur default CIC-IDS2017 tanpa audit kebocoran fitur. | Pembersihan ketat 62 fitur numerik dengan **eliminasi atribut `Destination Port`** dan 74 baris *ambiguous contradictory flows*. | Memperkuat standar metodologi laboratorium dalam mencegah bias *shortcut learning* pada evaluasi performa model keamanan. |
| **Target Luaran & Manfaat Ilmiah** | Publikasi kerangka kerja deteksi anomali skala makro enterprise. | Analisis kinerja mendalam, evaluasi stabilitas multi-seed (5 seed), profiling latensi mikrodetik ($\mu$s), dan payload komunikasi. | Memberikan modul pengujian empiris siap pakai di testbed Proxmox VE yang dapat dijadikan baseline bagi riset mahasiswa berikutnya. |

---

## 2. Tinjauan Literatur Skala Jumlah Node Klien dan Server

### 2.1 Taksonomi Standar Skala Node FL (Kairouz et al., 2021)
Rujukan otoritatif dunia dalam pembelajaran terfederasi (*Advances and Open Problems in Federated Learning*, Foundations and Trends in Machine Learning, 2021, arXiv:1912.04977) membagi arsitektur FL ke dalam dua rezim fundamental:

```
                    ┌─────────────────────────────────────────────────────┐
                    │            Taksonomi Skala Node FL                  │
                    │           (Ref: Kairouz et al., 2021)               │
                    └──────────────────────────┬──────────────────────────┘
                                               │
               ┌───────────────────────────────┴───────────────────────────────┐
               ▼                                                               ▼
┌───────────────────────────────┐                               ┌───────────────────────────────┐
│        Cross-Silo FL          │                               │        Cross-Device FL        │
├───────────────────────────────┤                               ├───────────────────────────────┤
│ • Jumlah Klien: 2 s.d. 10     │                               │ • Jumlah Klien: 100 s.d. 10^6 │
│ • Sifat Node: Gateway / Server│                               │ • Sifat Node: HP / Sensor IoT │
│ • Partisipasi: 100% per ronde │                               │ • Partisipasi: 1-10% sampling │
│ • Keandalan: Koneksi stabil   │                               │ • Keandalan: Rawan putus      │
│ • Domain: NIDS Subnet Kampus  │                               │ • Domain: Keyboard Gboard     │
└───────────────────────────────┘                               └───────────────────────────────┘
```

### 2.2 Tabel Literatur Skala Node Klien ($K$) pada Penelitian Terverifikasi

| Paper / Rujukan | Domain Aplikasi | Jumlah Klien ($K$) | Rezim FL | Dasar Ilmiah & Justifikasi Peneliti |
|---|---|:---:|:---:|---|
| **Zhao et al. (2018)**<br>*(arXiv:1806.00582)* | Fondasi Analitis Non-IID | **$K = 2$ dan $K = 10$** | Cross-Silo | Menggunakan $K=2$ untuk menurunkan pembuktian analitis batas atas divergensi bobot $\|w_{\text{FL}} - w_{\text{Centralized}}\|$ sebelum validasi numerik. |
| **Kairouz et al. (2021)**<br>*(Foundations and Trends in ML)* | Survei Standar Industri FL | **$K = 2$ s.d. puluhan** | Cross-Silo | Menetapkan definisi baku bahwa cross-silo beroperasi pada sedikit klien yang andal (organisasi, subnet, sentral data regional). |
| **Ruzafa-Alcázar et al. (2023)**<br>*(IEEE Trans. Ind. Informatics)* | Industrial IoT NIDS | **Klaster Gateway Industri** | Cross-Silo | Memodelkan pemisahan fisik stasiun industri nyata dengan pemrosesan deteksi pada edge node lokal. |
| **Ali et al. (2025)**<br>*(arXiv:2505.15376)* | Privacy-Preserving IIoT IDS | **$K = 10$** | Cross-Silo | Menguji kolaborasi 10 edge gateway pada dataset ToN-IoT dan N-BaIoT. |
| **Nguyen et al. (DïoT, 2019)**<br>*(IEEE ICDCS 2019)* | IoT Anomaly Detection | **$K = 2$ s.d. $15$** | Cross-Silo | Menguji deteksi anomali pada spektrum 2 hingga 15 gateway terdistribusi. |
| **Popoola et al. (2022)**<br>*(IEEE Internet of Things Journal)* | Zero-Day Botnet Detection | **$K = 4$ s.d. $8$** | Cross-Silo | Membagi lalu lintas botnet ke 4-8 edge router subnet IoT. |

---

## 3. Implementasi FCL di Luar Domain NIDS (Kajian Literatur & Paper Riil)

Konsep *Federated-Continual Learning* (FCL) memecahkan dua masalah universal: **privasi data terdistribusi (spatial non-IID)** dan **kelupaan katastropik saat pola data berubah (temporal drift)**. Berikut adalah studi literatur primer yang menerapkan FCL pada domain-domain non-NIDS:

| No | Domain Riset Non-NIDS | Paper Riil Terverifikasi | Tipe Sinyal & Karakteristik Fitur | Skenario Sekuensial (Task 1 $	o$ Task 2) | Peran & Keunggulan FCL |
|:--:|---|---|---|---|---|
| **1** | **Perimeter Physical Intrusion Sensing (Analogi Pagar ITS)** | **Usmanova et al. (2022)**<br>*(IEEE SMARTCOMP / arXiv:2207.08181)* | Sinyal deret waktu akselerometer 3-sumbu ($x, y, z$) dan sensor geophone getaran tanah. | **Task 1:** Deteksi getaran lingkungan (angin, hujan, hewan) vs Intruder Panjat.<br>**Task 2:** Intruder Potong Kawat / Gali Tanah (kelas baru). | Mengadaptasi sinyal intrusi baru tanpa melupakan pola gangguan lama dan tanpa mentransfer data mentah sensor ke cloud. |
| **2** | **Industrial IoT (IIoT) & Predictive Maintenance SCADA** | **Zhao et al. (2025)**<br>*(IEEE Internet of Things Journal, DOI: 10.1109/JIOT.2024.3510553)* | Pembacaan getaran mekanis sensor getaran mesin industri (*bearing vibration*). | **Task 1:** Deteksi keausan inner-race mesin $\to$<br>**Task 2:** Deteksi kerusakan gear outer-race yang muncul belakangan. | Pabrik-pabrik independen berkolaborasi meningkatkan akurasi deteksi anomali mesin tanpa membagikan data internal SCADA. |
| **3** | **Internet of Medical Things (IoMT Healthcare)** | **Dong et al. (2024)**<br>*(arXiv:2411.12756)* & **Liu et al. (2023)**<br>*(arXiv:2303.06783)* | Citra medis MRI resolusi tinggi atau rekaman biosignal elektrokardiogram (ECG 12-lead). | **Task 1:** Deteksi patologi dasar (Ventricular Anomaly) $\to$<br>**Task 2:** Deteksi patologi baru (Atrial Fibrillation). | Multi-senter rumah sakit mematuhi regulasi privasi data medis (HIPAA/GDPR), menjaga retensi memori terhadap penyakit lama. |
| **4** | **Autonomous Vehicles & Intelligent Transportation (V2X)** | **Hamedi et al. (2025)**<br>*(Neurocomputing, Vol. 629, 130844)* | Log telemetri kendaraan, lidar point cloud, dan bus CAN (*Controller Area Network*). | **Task 1:** Pola navigasi jalan raya normal $\to$<br>**Task 2:** Kondisi bahaya cuaca ekstrem / salju / konstruksi baru. | Armada kendaraan memperbarui model deteksi bahaya secara sekuensial tanpa menimpa parameter navigasi dasar. |

---

## 4. Penambahan Rumusan Masalah Fondasional (RM 0)

Sesuai arahan dosen pembimbing, ditambahkan satu rumusan masalah umum/fondasional (RM 0) sebelum RM 1 dan RM 2, sehingga struktur rumusan masalah tersusun dalam piramida hierarkis yang kokoh:

```
                  ┌──────────────────────────────────────────────┐
                  │   RM 0: Rancang Bangun & Kelayakan FCL       │
                  │   (Integrasi FedAvg + EWC di Private Cloud)  │
                  └──────────────────────┬───────────────────────┘
                                         │
                 ┌───────────────────────┴───────────────────────┐
                 ▼                                               ▼
  ┌──────────────────────────────┐                ┌──────────────────────────────┐
  │ RM 1: Dimensi Spasial        │                │ RM 2: Dimensi Temporal       │
  │ Komparasi Kinerja Deteksi    │                │ Mitigasi Catastrophic        │
  │ Terdistribusi vs Lokal Non-IID│               │ Forgetting via Penalti EWC   │
  └──────────────────────────────┘                └──────────────────────────────┘
```

### Formulasi Naskah Rumusan Masalah (Diselaraskan ke Bab 1)
1. **Rumusan Masalah 1 (Fondasional / Arsitektural Umum - BARU):**  
   *Bagaimana rancang bangun dan kelayakan kerangka kerja Federated-Continual Learning (FCL) yang mengintegrasikan algoritma agregasi Federated Averaging (FedAvg) dan regularisasi parameter lokal Elastic Weight Consolidation (EWC) dalam mendeteksi network traffic intrusion secara adaptif dan terdistribusi?*
2. **Rumusan Masalah 2 (Analisis Dimensi Spasial Non-IID - Dahulu RM 1):**  
   *Bagaimana kinerja deteksi intrusi model yang dilatih secara terdistribusi (Federated Averaging / FedAvg) dibandingkan dengan model yang dilatih secara lokal pada masing-masing klien dengan distribusi data non-IID?*
3. **Rumusan Masalah 3 (Analisis Dimensi Temporal Catastrophic Forgetting - Dahulu RM 2):**  
   *Bagaimana pengaruh metode Elastic Weight Consolidation (EWC) terhadap mitigasi catastrophic forgetting saat model mempelajari kelas serangan baru secara sekuensial, baik pada skenario pelatihan lokal maupun terdistribusi (FedAvg + EWC)?*

### Penyelarasan Tujuan Penelitian
1. Merancang dan menguji kelayakan kerangka kerja *Federated-Continual Learning* (FCL) yang mengintegrasikan algoritma *Federated Averaging* (FedAvg) dan regularisasi *Elastic Weight Consolidation* (EWC) untuk mendeteksi *network traffic intrusion* pada lingkungan *testbed private cloud server*.
2. Menganalisis kinerja deteksi intrusi model yang dilatih secara terdistribusi (*Federated Averaging* / FedAvg) dibandingkan dengan model yang dilatih secara lokal pada masing-masing klien dengan distribusi data non-IID.
3. Menganalisis pengaruh metode *Elastic Weight Consolidation* (EWC) terhadap mitigasi *catastrophic forgetting* saat mempelajari kelas serangan baru secara sekuensial, baik pada skenario pelatihan lokal maupun terdistribusi (FedAvg + EWC), serta mengevaluasi efisiensi komputasi model (latensi inferensi per aliran data dalam mikrodetik, alokasi memori RAM *footprint*, dan *communication payload*) sebagai analisis pendukung penerapan pada *testbed private cloud server*.

---

## 5. Penyesuaian Parameter Pengukuran dan Fitur pada Skenario Live Injections

Jika dosen menghendaki analisis penambahan skenario *Live Packet Injection* (injeksi lalu lintas aktif), berikut adalah tabel komparasi teknis yang membedakan evaluasi flow offline (*CIC-IDS2017*) vs injeksi live streaming:

| Parameter Komparasi | Skenario Aliran Offline (CIC-IDS2017) | Skenario Live Packet Injection (Trafik Aktif) |
|---|---|---|
| **Pipeline Ekstraksi Fitur** | File CSV statis hasil kalkulasi *CICFlowMeter* pcap penuh (62 fitur statistik alur). | Modul ekstraksi real-time berbasis *libpcap* / *Zeek* / *eBPF*. Menghadapi batas waktu alur (*flow timeout* 120 detik) sebelum fitur statistik lengkap dapat dikalkulasi. |
| **Karakteristik Fitur** | Statistik alur dua arah penuh (*Full Bidirectional Flow Statistics*): durasi, rata-rata IAT, total panjang paket arah bolak-balik. | Wajib menggunakan *Early-Flow Features* ($N$-paket pertama, misal 5 paket awal) atau jendela geser (*sliding time window* 1 detik) agar sistem mampu merespons serangan sebelum koneksi TCP berakhir. |
| **Sinkronisasi Ground Truth** | Label telah dianotasi pasti di dataset (*BENIGN*, *SSH-Patator*, *DoS*). Bebas dari ketidakpastian sinkronisasi waktu saat pelatihan. | Memerlukan sinkronisasi penanda waktu (*timestamp*) presisi tingkat mikrodetik antara mesin penyerang (*Hydra / Slowloris*) dan sensor edge. Rentan menghasilkan *noisy ground truth*. |
| **Potensi Feature Drift** | Bebas dari pergeseran format fitur karena data telah melalui kurasi standarisasi dan normalisasi *Min-Max / Z-Score*. | Sangat rentan terhadap *feature drift* akibat fluktuasi latensi jaringan fisik, perubahan konfigurasi MTU switch, dan variasi beban sistem. |
| **Metrik Evaluasi Sistem** | Metrik Machine Learning murni: *Macro-F1*, *Precision*, *Recall*, *Backward Transfer* (BWT), dan ukuran payload parameter model (KB). | Tambahan Metrik QoS Jaringan & Sistem Telekomunikasi:<br>1. *End-to-End Alert Latency* (detik/milidetik dari paket pertama $\to$ alert).<br>2. *Packet Loss Rate (PLR)* pada antarmuka bridge Linux.<br>3. *Throughput Degradation* (Mbps) saat banjir paket DoS berlangsung.<br>4. *CPU & Memory Overhead* dari modul flow sniffer kontinu di edge node. |

---

## 6. Literatur Review Menyeluruh Continual Learning Methods

Continual Learning (CL) bertujuan memampukan jaringan saraf tiruan belajar dari aliran tugas sekuensial $\mathcal{T}_1, \mathcal{T}_2, \dots, \mathcal{T}_T$ tanpa melupakan representasi tugas terdahulu (*Stability-Plasticity Dilemma*)[23], [24].

```
                            ┌─────────────────────────────────────────┐
                            │       Continual Learning Methods        │
                            └────────────────────┬────────────────────┘
                                                 │
         ┌───────────────────────────────────────┼──────────────────────────────────────┐
         ▼                                       ▼                                      ▼
┌──────────────────┐                   ┌──────────────────┐                   ┌──────────────────┐
│  Regularization  │                   │   Replay-based   │                   │ Architecture-    │
│  (Prior-Focused) │                   │  (Memory Buffer) │                   │ based (Dynamic)  │
└────────┬─────────┘                   └────────┬─────────┘                   └────────┬─────────┘
         │                                      │                                      │
         ├─ EWC (Kirkpatrick, 2017)             ├─ Experience Replay (Chaudhry, 2019)  ├─ Progressive Nets (Rusu, 2016)
         ├─ Online EWC (Schwarz, 2018)          ├─ GEM (Lopez-Paz, 2017)               ├─ PackNet (Mallya, 2018)
         ├─ Synaptic Intel. (Zenke, 2017)       ├─ A-GEM (Chaudhry, 2018)              ├─ Dynamic Expandable (Yoon, 2018)
         ├─ MAS (Aljundi, 2018)                 └─ Generative Replay (Shin, 2017)      └─ LoRA/Adapter Modules
         └─ LwF (Li & Hoiem, 2017)
```

### 6.1 Tabel Komparasi 10 Metode Continual Learning

| Nama Metode | Penulis & Tahun | Formulasi Matematis / Mekanisme | Keunggulan Utama | Kelemahan / Bottleneck | Relevansi untuk NIDS Edge |
|---|---|---|---|---|:---:|
| **EWC** | Kirkpatrick et al. (2017)[5] | $\mathcal{L}(\theta) = \mathcal{L}_{\text{new}}(\theta) + \sum_i \frac{\lambda}{2} F_i (\theta_i - \theta_{1, i}^*)^2$ | Bebas buffer data mentah (*zero-buffer*); estimasi kurvatur Fisher stabil dan deterministik pada MLP. | Mengasumsikan parameter independen (diagonal Hessian); kapasitas proteksi terbatas jika task sangat banyak. | ⭐⭐⭐⭐⭐<br>**Metode Terpilih** |
| **Online EWC** | Schwarz et al. (2018) | $\tilde{F}^t = \gamma \tilde{F}^{t-1} + F^t$ (Akumulasi Fisher berbobot waktu) | Skalabel untuk puluhan task sekuensial tanpa menambah memori penalti kuadratik. | Memerlukan kalibrasi teliti faktor peluruhan $\gamma$. | ⭐⭐⭐⭐<br>Ekstensi $T > 3$ |
| **Synaptic Intelligence (SI)** | Zenke et al. (2017) | $\omega_i^t = \sum \Delta \theta_i \cdot g_i$ (Akumulasi lintasan bobot online) | Komputasi relevansi parameter menyatu dengan fase pelatihan lokal. | Sensitif terhadap ukuran *learning rate*; rentan instabilitas pada data non-IID. | ⭐⭐⭐<br>Alternatif |
| **Memory Aware Synapses (MAS)** | Aljundi et al. (2018) | $\Omega_i = \frac{1}{N} \sum \| \nabla_{\theta_i} f(x) \|$ (Sensitivitas output fungsi) | Beroperasi tanpa label data (*unsupervised*). | Kurang sensitif terhadap batas keputusan multikelas yang ketat. | ⭐⭐⭐<br>Alternatif |
| **Learning without Forgetting (LwF)** | Li & Hoiem (2017) | Distilasi pengetahuan model lama (KL-Divergence) saat melatih data baru | Tanpa komputasi Fisher dan tanpa buffer sampel mentah. | Distorsi representasi terjadi jika domain tugas baru sangat berbeda (*domain shift*). | ⭐⭐⭐⭐<br>Alternatif Distilasi |
| **Experience Replay (ER)** | Chaudhry et al. (2019) | Menyimpan sebagian data mentah tugas lama di buffer memori fisik dan me-replay | Retensi memori sangat kuat dan mudah diimplementasikan. | **Melanggar privasi data (GDPR/UU PDP)** jika buffer dicuri; membebani RAM edge. | ❌ Dieliminasi<br>*(Isu Privasi)* |
| **Gradient Episodic Memory (GEM)** | Lopez-Paz & Ranzato (2017)[10] | Proyeksi kuadratik gradien agar $\langle g_{\text{new}}, g_{\text{mem}} \rangle \ge 0$ | Mendorong Backward Transfer nonnegatif ($BWT \ge 0$). | Komputasi QP-solver sangat berat untuk prosesor edge; memerlukan buffer sampel mentah. | ❌ Dieliminasi<br>*(Komputasi Berat)* |
| **A-GEM** | Chaudhry et al. (2018) | Penyederhanaan proyeksi gradien GEM pada batch acak | Komputasi jauh lebih cepat daripada GEM reguler. | Tetap memerlukan buffer memori fisik data mentah. | ❌ Dieliminasi<br>*(Isu Buffer)* |
| **PackNet** | Mallya & Lazebnik (2018) | Pruning terstruktur (50-75%) dan pembekuan bobot tugas lama | Forgetting bernilai mutlak nol pada tugas yang telah dibekukan. | Kapasitas model cepat jenuh; membutuhkan arsitektur jaringan saraf berskala besar. | ❌ Kurang Sesuai<br>*(Overkill MLP)* |
| **LoRA-CL** | Hu et al. (2022) / Adaptasi | Membekukan bobot dasar dan menyematkan adapter rank-rendah per-task | Nol kelupaan pada representasi dasar; efisien parameter. | Memerlukan mekanisme routing task-ID saat inferensi; kurang alami untuk MLP 3-lapis. | ⭐⭐⭐<br>Alternatif Modular |

---

## 7. Literatur Review Menyeluruh Federated Learning Methods

Federated Learning (FL) memecahkan optimasi terdistribusi di mana $K$ klien dengan distribusi data lokal $\mathcal{D}_k$ berkolaborasi mengoptimalkan model global $w$:

$$\min_{w} f(w) = \sum_{k=1}^K \frac{n_k}{N} F_k(w), \quad \text{di mana } F_k(w) = \mathbb{E}_{(x, y) \sim \mathcal{D}_k} [\ell(w; x, y)]$$

```
                            ┌─────────────────────────────────────────┐
                            │        Federated Learning Methods       │
                            └────────────────────┬────────────────────┘
                                                 │
         ┌───────────────────────────────────────┼──────────────────────────────────────┐
         ▼                                       ▼                                      ▼
┌──────────────────┐                   ┌──────────────────┐                   ┌──────────────────┐
│    Baselines     │                   │  Heterogeneity   │                   │  Personalized &  │
│   Aggregation    │                   │   (Non-IID Drift)│                   │  Continual FL    │
└────────┬─────────┘                   └────────┬─────────┘                   └────────┬─────────┘
         │                                      │                                      │
         ├─ FedAvg (McMahan, 2017)              ├─ FedProx (Li, 2020)                  ├─ Per-FedAvg (Fallah, 2020)
         ├─ FedSGD (McMahan, 2017)              ├─ SCAFFOLD (Karimireddy, 2020)        ├─ pFedMe (Dinh, 2020)
         └─ FedNova (Wang, 2020)                ├─ MOON (Li, 2021)                     ├─ FedCurv (Shoham, 2019)
                                                └─ FedDyn (Acar, 2021)                 └─ FedWeIT (Yoon, 2021)
```

### 7.1 Tabel Komparasi 9 Metode Federated Learning

| Nama Metode | Penulis & Tahun | Karakteristik Agregasi & Matematis | Keunggulan Utama | Kelemahan / Overhead Jaringan | Relevansi untuk NIDS Edge |
|---|---|---|---|---|:---:|
| **FedAvg** | McMahan et al. (2017)[3] | Rata-rata terbobot sederhana:<br>$w^{t+1} = \sum_{k=1}^K \frac{n_k}{N} w_k^{t+1}$ | Efisiensi komunikasi tinggi; standar *de facto* industri (Flower framework). | Mengalami *client drift* dan divergensi bobot saat data non-IID ekstrem. | ⭐⭐⭐⭐⭐<br>**Baseline Utama FL** |
| **FedProx** | Li et al. (2020)[22] | Penambahan suku deviasi proksimal lokal:<br>$\min_w F_k(w) + \frac{\mu}{2} \|w - w^t\|^2$ | Meredam penyimpangan bobot lokal; tangguh terhadap *stragglers* dan heterogenitas sistem. | Memerlukan tuning hyperparameter $\mu$; konvergensi lambat jika $\mu$ terlalu dominan. | ⭐⭐⭐⭐<br>**Alternatif Penguat** |
| **SCAFFOLD** | Karimireddy et al. (2020) | Koreksi arah gradien menggunakan *control variates* $c_k$ dan $c$ | Menjamin laju konvergensi stabil di bawah non-IID ekstrem tanpa deviasi gradien. | Ukuran payload transmisi komunikasi melonjak **$2\times$** (mengirim bobot $w$ + variabel kontrol $c$). | ⭐⭐⭐<br>Beban Jaringan |
| **FedNova** | Wang et al. (2020) | Normalisasi gradien lokal berdasarkan variasi langkah pembaruan klien | Menghilangkan bias konvergensi akibat variasi epoch komputasi lokal antar-klien. | Kurang berdampak jika jumlah epoch lokal antar-klien telah seragam ($E$ konstan). | ⭐⭐⭐<br>Alternatif Heterogen |
| **MOON** | Li et al. (2021) | *Model-Contrastive Learning*: memaksimalkan kemiripan representasi lokal dengan global | Akurasi representasi laten sangat tinggi pada ekstraksi fitur dalam (deep features). | Komputasi forward pass tambahan untuk model global lama di tiap klien (berat di edge). | ⭐⭐<br>Overkill Sensor Edge |
| **FedCurv** | Shoham et al. (2019) | Penalti berbasis kurvatur Fisher lintas klien yang diagregasikan di server | Meredam divergensi bobot antar-klien dengan menjaga kurvatur solusi bersama. | Overhead transmisi gRPC melonjak **$2\times$ lipat** (mengirim bobot $w$ dan matriks diagonal Fisher $F$). | ⭐⭐⭐⭐<br>**Pembanding Teoretis** |
| **FedWeIT** | Yoon et al. (2021) | Dekomposisi bobot menjadi parameter global, klien, dan *task mask* | Mencegah interferensi antar-tugas secara struktural melalui dekomposisi parameter. | Memerlukan arsitektur modular yang rumit; tidak cocok untuk MLP kompak. | ⭐⭐<br>Arsitektur Berbeda |
| **pFedMe** | Dinh et al. (NeurIPS 2020) | Personalisasi FL menggunakan *Moreau Envelopes* | Memberikan model yang disesuaikan untuk karakteristik data lokal masing-masing klien. | Mengoptimalkan objektif bi-level yang memerlukan komputasi gradien berlapis di edge. | ⭐⭐⭐<br>Alternatif pFL |
| **Per-FedAvg** | Fallah et al. (NeurIPS 2020) | Personalisasi FL berbasis kerangka kerja *Model-Agnostic Meta-Learning* (MAML) | Model global dapat diadaptasi dengan cepat ke data klien baru melalui *one-step gradient update*. | Memerlukan kalkulasi produk Hessian-vektor pada turunan kedua yang membebani edge. | ⭐⭐⭐<br>Alternatif Meta-FL |

---

## 8. Konseptualisasi Skala Banyak Edge Node: Analogi Pagar Perimeter ITS 180 Hektar

### 8.1 Membedah Analogi Dosen Pembimbing: Keamanan Pagar Perimeter Kampus ITS
Dosen pembimbing memberikan analogi sistem keamanan fisik kampus ITS (luas $\approx 180$ hektar):
- **Kondisi Fisik Lapangan:** Kampus dikelilingi oleh pagar pembatas sepanjang berkilo-kilometer dengan banyak titik masuk (*breaching points*).
- **Infrastruktur Edge Sensor:** Di sepanjang pagar terpasang puluhan hingga ratusan node sensor fisik (sensor getaran pagar piezoelektrik/akselerometer, sensor inframerah pasif PIR, mikrofon akustik).
- **Tantangan Utama:** **False Positive vs True Intrusion**.
  * Gangguan Alami (*Noise/Benign*): Kucing atau anjing liar menyenggol pagar, dahan pohon jatuh, hembusan angin kencang, getaran truk tronton melintas di Jalan Raya Kertajaya / MERR.
  * Ancaman Nyata (*Intruder*): Manusia memotong kawat pagar, memanjat pagar, atau membongkar fondasi pembatas.
- **Dinamika Sekuensial (Continual Learning):**
  * Pola getaran tanah pada musim kemarau berbeda dari musim hujan (tanah basah meredam getaran).
  * Saat ada proyek konstruksi gedung baru di dalam kampus, sensor di sektor tersebut terpapar pola getaran alat berat baru. Model harus mempelajari pola gangguan baru ini secara lokal tanpa melupakan cara mendeteksi intrusi manusia dan tanpa membanjiri transmisi radio kampus.

### 8.2 Arsitektur Hirarkis 3-Tingkat (Tiered Edge-Fog Architecture)
Untuk menjembatani analogi ratusan sensor pagar dengan pemodelan 2 node klien di proposal, dirumuskan arsitektur hirarkis 3-tingkat:

```
[ Tier 3: Central Cloud Server ]
         Server Agregator Flower (Data Center Gedung Rektorat / DPTSI ITS)
                                ▲
                                │  gRPC FL Payload (Weights Only, Est. ~24.84 KB)
                                ▼
[ Tier 2: Edge Aggregator / Gateway Nodes = FL Clients ]
   Gateway Sektor Barat (Klien A)           Gateway Sektor Timur (Klien B)
   (Pos Menwa / Subnet Internal)            (Perimeter Asrama / DMZ Luar)
   • Ekstraksi 62 Fitur Alur / Sinyal       • Ekstraksi 62 Fitur Alur / Sinyal
   • Pelatihan Lokal FedAvg + EWC           • Pelatihan Lokal FedAvg + EWC
   • Menyimpan Fisher FA & Bobot θ*A         • Menyimpan Fisher FB & Bobot θ*B
                ▲                                        ▲
                │ Kabel RS-485 / LoRa Mesh               │ Kabel RS-485 / LoRa Mesh
                ▼                                        ▼
[ Tier 1: Field / Leaf Sensors ]
   Sensor Pagar P-01 ... P-50               Sensor Pagar P-51 ... P-100
   (Piezo, Akselerometer, PIR, Geophone)    (Piezo, Akselerometer, PIR, Geophone)
   * Hanya bertugas membaca sinyal fisik mentah (Microcontroller ESP32/STM32)
   * TIDAK menjalankan training FL/CL karena keterbatasan RAM/prosesor
```

**Penjelasan Alur Hirarkis:**
1. **Tier 1 (Leaf Sensors):** Ratusan sensor fisik di pagar bukan merupakan FL client langsung. Mikrokontroler mikro (ESP32/STM32) tidak memiliki kapasitas memori dan komputasi untuk menjalankan backpropagation PyTorch. Tugasnya murni mentransmisikan sinyal mentah ke gateway sektor terdekat via kanal lokal (RS-485 atau LoRa).
2. **Tier 2 (Edge Gateway = FL Clients):** Unit komputer mini (Industrial Edge PC / Raspberry Pi 4 / VM Proxmox) bertindak sebagai agregator sektor. Di sinilah proses kalkulasi 62 fitur statistik berlangsung dan eksekusi pelatihan lokal FedAvg + EWC dijalankan. Inilah yang dimodelkan sebagai **Klien A dan Klien B**.
3. **Tier 3 (Central Server):** Server di data center kampus menerima bobot dari gateway sektor, merata-ratakannya via FedAvg, dan mendistribusikan model global kembali ke seluruh gateway.

### 8.3 Opsi Kompromi Eksperimen (Fallback Plan untuk Dosen)
Saat bimbingan nanti, mahasiswa tidak bersikap kaku mempertahankan $K=2$, melainkan menawarkan opsi terstruktur:

1. **Rencana Utama (Eksperimen Inti $K=2$ Gateway pada VM Terpisah):**
   - Menjelaskan bahwa $K=2$ adalah representasi **dua sektor ekstrem (*canonical worst-case boundary condition*)**: Sektor Internal yang dominan serangan kredensial (SSH-Patator) vs Sektor Perimeter Luar yang dominan serangan volumetrik (DoS).
   - Menjaga integritas data kelas langka SSH-Patator (3.219 flow) agar tidak terpecah menjadi sampel mikro yang merusak kalkulasi Matriks Fisher.
2. **Rencana Cadangan / Fallback Plan (Eksperimen Sensitivitas Skalabilitas Node):**
   - Sampaikan kepada pembimbing:  
     *"Jika Bapak menghendaki evaluasi skalabilitas jumlah node sesuai analogi sektor area kampus ITS, saya siap menambahkan pengujian variasi jumlah klien ($K \in \{2, 5, 10\}$ node) menggunakan simulasi multi-proses di Flower. Dengan demikian, kita dapat membuktikan secara empiris apakah penambahan jumlah gateway sektor memperparah atau justru meredam fenomena catastrophic forgetting (BWT)."*

---

## 9. Konsolidasi Ketetapan Dataset CIC-IDS2017 & Pemetaan Dataset Luar Domain IDS

### 9.1 Skenario Domain Network IDS: Ketetapan Dataset CIC-IDS2017 (Terkunci & Tervalidasi)
Jika penelitian tetap berfokus pada Network IDS, dataset **CIC-IDS2017 tetap dipertahankan secara definitif** dengan keputusan metodologi yang telah tervalidasi:

1. **3 Kelas Target Representatif:**
   - **Normal (BENIGN):** 1.323.561 flow unik.
   - **SSH-Patator (Task 1):** 3.219 flow unik.
   - **DoS 4-Subvarian (Task 2):** 193.708 flow unik (Hulk, GoldenEye, slowloris, slowhttptest).
2. **Temuan Empiris Audit Data Cleaning (74 Baris Konflik Label):**
   - Audit pada dataset mentah menemukan tepat **74 baris (37 pasang flow)** yang memiliki 78 fitur numerik identik persis namun berlabel kontradiktif (satu flow berlabel Normal dan satu flow berlabel DoS).
   - Tidak ada konflik label yang melibatkan SSH-Patator.
   - **Kebijakan Saintifik:** Mengeliminasi ke-74 baris ambigu tersebut (*drop contradictory flows*) saat membekukan dataset akhir, menyisakan tepat **1.520.451 flow bersih**, agar gradien fungsi loss tidak menerima target yang bertentangan pada titik fitur yang sama.
3. **62 Fitur Statistik Bersih:**
   - Mengeliminasi `Destination Port` untuk mencegah *shortcut learning* (akurasi semu 96,44% dari port semata).
   - Mengeliminasi 10 kolom konstan dan 5 kolom duplikat identik.
4. **Weighted Cross-Entropy Loss + Gradient Clipping (Norm $\le 1.0$):**
   - Menyeimbangkan rasio ketimpangan kelas 414 : 60 : 1 tanpa membuang 99% data Normal.

### 9.2 Skenario Luar Domain Network IDS: Tabel Literature Review Menyeluruh Dataset Alternatif

| No | Domain Riset | Nama Dataset Benchmark | Tipe Sensor & Karakteristik Fitur | Ukuran Data & Format | Skenario Sekuensial (Task 1 $	o$ Task 2) | Kesesuaian FCL di Edge | Risiko bagi Mahasiswa | Referensi Publikasi |
|:--:|---|---|---|---|---|:---:|---|---|
| **1** | **Perimeter Intrusion Detection (Analogi Pagar ITS)** | **UCR Fence/Vibration Subsets** / **UCI HAR** | Akselerometer 3-sumbu, piezoelektrik, dan geophone seismik pada pagar kawat. | Puluhan ribu sekuens sinyal deret waktu 1D ($x, y, z$). | **Task 1:** Deteksi hewan/cuaca vs Intruder Panjat.<br>**Task 2:** Intruder Potong Kawat / Gali Fondasi. | ⭐⭐⭐⭐<br>**Tinggi** (1D-CNN atau MLP getaran) | Memerlukan transformasi sinyal waktu (FFT/Wavelet) ke statistik fitur sebelum training. | Chen et al. (IEEE TIM, 2021); UCI ML Repository |
| **2** | **Industrial SCADA / Critical Infrastructure** | **SWaT (Secure Water Treatment)** & **WADI** | 51 sensor fisik instalasi air (level air, laju alir, tekanan pipa, aktuator valve). | 946.721 sampel operasional normal + 446.000 sampel serangan siber-fisik (tabular). | **Task 1:** Manipulasi sensor level air $	o$<br>**Task 2:** Pembobolan katup pipa kimia bertekanan tinggi. | ⭐⭐⭐⭐⭐<br>**Sangat Tinggi** (Tabular kontinu mirip CIC-IDS2017) | Dataset sangat besar; membutuhkan pemahaman proses kimiawi pengolahan air. | Mathur et al. (CyberICPS 2016); iTrust SUTD |
| **3** | **Smart Campus IoT Environmental Anomaly** | **Intel Berkeley Lab Data** / **SMD** | Sensor nirkabel lingkungan: Suhu, Kelembapan, Cahaya, Tegangan baterai node. | 2,3 juta pembacaan sensor berkala dari 54 node sensor terdistribusi. | **Task 1:** Anomali suhu/kebakaran $	o$<br>**Task 2:** Anomali drop tegangan baterai mendadak akibat badai. | ⭐⭐⭐<br>**Sedang** | Pola anomali relatif sederhana; heterogenitas non-IID kurang menantang untuk FCL. | Bodik et al. (ACM SIGCOMM 2004) |
| **4** | **Internet of Medical Things (IoMT Healthcare)** | **PhysioNet MIT-BIH Arrhythmia Database** | Rekaman sinyal elektrokardiogram (ECG 2-lead) dari pasien rawat terdistribusi. | 48 rekaman raw ECG (panjang 30 menit per pasien, anotasi detak jantung). | **Task 1:** Deteksi Premature Ventricular Contractions $	o$<br>**Task 2:** Deteksi Supraventricular Ectopic Beats. | ⭐⭐⭐⭐<br>**Tinggi** (Privasi antar-RS sangat cocok untuk FL) | Menuntut justifikasi medis kardiologi yang berada di luar lingkup Teknik Telekomunikasi. | Moody & Mark (IEEE EMB 2001) |
| **5** | **Autonomous Vehicles / Connected Cars (V2X)** | **CAN-Intrusion-Dataset (Car-Hacking)** | Log komunikasi bus CAN (*Controller Area Network*) internal mobil. | Jutaan baris frame pesan CAN (CAN ID, DLC, Data bytes). | **Task 1:** Serangan DoS pada bus CAN $	o$<br>**Task 2:** Serangan Fuzzing & Spoofing RPM/Gear transmisi. | ⭐⭐⭐⭐<br>**Tinggi** (Tabular biner, payload ringan) | Terbatas pada jaringan bus kendaraan lokal, bukan skala jaringan luas seperti kampus. | Song et al. (IEEE T-ITS 2020) |

### 9.3 Rekomendasi Mahasiswa kepada Pembimbing
1. **Pilihan Utama (Sangat Direkomendasikan Tetap):** Tetap berada pada **Network IDS dengan CIC-IDS2017**, karena seluruh pipeline pembersihan fitur (62 fitur tanpa port leakage, 1,52 juta baris bersih, Weighted Loss, isolasi non-IID Klien A/B) telah selesai diaudit secara empiris, bebas dari spekulasi data baru, dan siap dieksekusi pada matriks E0-E4.
2. **Pilihan Alternatif (Jika Pembimbing Mengharuskan Selaras Fisik Pagar ITS):** Mengadopsi domain **Perimeter Intrusion Detection (Akselerometer Pagar)** atau **Industrial SCADA (SWaT)** yang memiliki karakteristik data tabular numerik kontinu serupa sehingga algoritma FedAvg + EWC dapat langsung ditransfer tanpa merombak arsitektur model secara fundamental.

---
*Dokumen ini disusun sebagai panduan diskusi strategis dan bahan telaah ilmiah bersama dosen pembimbing.*
