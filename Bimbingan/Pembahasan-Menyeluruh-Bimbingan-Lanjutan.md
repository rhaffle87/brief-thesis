# Pembahasan Menyeluruh Bimbingan Lanjutan: Arsitektur Federated-Continual Learning (FCL)

**Judul Penelitian:**  
Analisis Kinerja Deteksi Network Traffic Intrusion Menggunakan Metode Federated-Continual Learning pada Testbed Private Cloud Server  

**Mahasiswa:** Rafli Alif Ihza Hartono (NRP 5022211233)  
**Departemen:** Teknik Elektro, FTEIC, Institut Teknologi Sepuluh Nopember (ITS)  
**Tujuan Dokumen:** Menjawab secara tuntas, mendalam, dan berbasis literatur 9 poin arahan dosen pembimbing untuk mematangkan proposal tugas akhir dan menyelaraskan riset agar saling melengkapi dengan peta riset laboratorium.

---

## 📌 Daftar Isi Pembahasan
1. [Poin 1: Pemetaan Metode FCL yang Linier dan Saling Melengkapi](#1-pemetaan-metode-fcl-yang-linier-dan-saling-melengkapi)
2. [Poin 2: Tinjauan Literatur Skala Jumlah Node Klien dan Server](#2-tinjauan-literatur-skala-jumlah-node-klien-dan-server)
3. [Poin 3: Implementasi FCL di Luar Domain NIDS](#3-implementasi-fcl-di-luar-domain-nids)
4. [Poin 4: Penambahan Rumusan Masalah Fondasional (RM 0)](#4-penambahan-rumusan-masalah-fondasional-rm-0)
5. [Poin 5: Penyesuaian Parameter Pengukuran dan Fitur pada Skenario Live Injections](#5-penyesuaian-parameter-pengukuran-dan-fitur-pada-skenario-live-injections)
6. [Poin 6: Literatur Review Menyeluruh Continual Learning Methods](#6-literatur-review-menyeluruh-continual-learning-methods)
7. [Poin 7: Literatur Review Menyeluruh Federated Learning Methods](#7-literatur-review-menyeluruh-federated-learning-methods)
8. [Poin 8: Konseptualisasi Skala Banyak Edge Node: Analogi Pagar Perimeter ITS 180 Hektar](#8-konseptualisasi-skala-banyak-edge-node-analogi-pagar-perimeter-its-180-hektar)
9. [Poin 9: Konsolidasi Ketetapan Dataset CIC-IDS2017](#9-konsolidasi-ketetapan-dataset-cic-ids2017)

---

## 1. Pemetaan Metode FCL yang Linier dan Saling Melengkapi

### 1.1 Menghindari Redundansi dengan Riset Dosen
Dosen pembimbing telah memiliki riset di domain pembelajaran mesin terdistribusi/keamanan. Agar riset tugas akhir ini **tidak redundan**, melainkan **saling melengkapi (*complementary*)**, posisi ilmiah riset dipetakan berdasarkan paradigma penanganan kelupaan (*forgetting mitigation*) dan agregasi federasi.

Riset deteksi anomali/keamanan terdistribusi yang umum dilakukan di laboratorium biasanya terbagi menjadi:
1. *Federated Learning Statis (FedAvg/FedProx standar)* pada data tabular/grafik tanpa skenario sekuensial kelas baru.
2. *Continual Learning Sentralistik* (model dilatih di server tunggal dengan buffer memori/replay data).
3. *Intrusion Detection Biner* (Normal vs Anomali) menggunakan Autoencoder atau model berat (CNN/LSTM).

### 1.2 Posisi Saling Melengkapi Riset Ini
Penelitian ini melengkapi peta riset laboratorium pada 3 dimensi kritis:
- **Dimensi Perlindungan Data Historis (Exemplar-Free FCL):** Tidak menggunakan *replay buffer* (sampel mentah masa lalu tidak disimpan di klien). Ini membedakannya dari metode berbasis *Experience Replay* / GEM yang rawan kebocoran data mentah jika perangkat *edge* disusupi secara fisik.
- **Dimensi Integrasi Ortogonal (FedAvg + EWC):** Menguji interaksi langsung antara algoritma konsensus federasi (FedAvg) dan regularisasi kurvatur parameter lokal (EWC).
- **Dimensi Efisiensi Edge Tabular:** Menghilangkan *shortcut learning* (bebas port 22/80) pada arsitektur ultra-ringan 6.211 parameter dengan latensi tingkat mikrodetik ($\mu s$).

### 1.3 Alternatif Metode Linier yang Dapat Dijadikan Pembanding / Pelengkap
Tabel berikut merangkum metode FCL lain yang berada dalam satu garis linier (*linear spectrum*) dan dapat diposisikan sebagai varian pelengkap dalam pembahasan:

| Nama Metode | Kategori FCL | Mekanisme Inti | Kelebihan | Kelemahan di Edge NIDS | Hubungan dengan Riset Ini |
|---|---|---|---|---|---|
| **FedAvg + EWC (Sistem Usulan)** | Regularisasi Parameter (Prior-Focused) | Penalti kurvatur kuadratik berbasis diagonal Matriks Fisher lokal. | Bebas risiko kebocoran buffer data historis (tanpa replay memory), komputasi analitis stabil pada MLP. | Memerlukan komputasi turunan kedua (gradien kuadrat) pada data Task 1. | **Baseline Inti Penelitian** |
| **FedCurv (Shoham et al., 2019)** | Regularisasi Terdistribusi | Klien menghitung Fisher lokal dan mengirimkannya ke server; server membagikan konsensus kurvatur global. | Mencegah penyimpangan bobot antar-klien secara global. | Beban transmisi komunikasi berlipat ganda ($2 \times$ payload karena mengirim bobot + matriks Fisher). | **Varian Linier Tingkat Lanjut (Dapat direkomendasikan sebagai *Future Work* / Pembanding Teoretis)** |
| **FedProx + EWC** | Heterogeneity + Regularisasi | Menambahkan suku proksimal $\frac{\mu}{2} \|w - w^t\|^2$ pada FedAvg + penalti EWC pada loss lokal. | Tahan terhadap straggler dan non-IID ekstrem. | Menambah hyperparameter penyeimbang baru ($\mu$ proksimal dan $\lambda$ Fisher) yang rumit dituning. | **Alternatif Agregasi jika FedAvg mengalami osilasi berat** |
| **FedWeIT (Yoon et al., 2021)** | Isolasi Parameter (Parameter-Decomposition) | Memecah bobot menjadi bobot global, adaptif klien, dan spesifik task (*sparse masks*). | Mencegah interferensi antar-task secara struktural. | Memerlukan arsitektur modular yang kompleks, kurang cocok untuk MLP kompak. | **Keluarga Berbeda (Arsitektural)** |
### 1.4 Keputusan Pemilihan Metode Pembanding: Mengapa FedCurv dan FedProx?
Jika dosen pembimbing menghendaki metode pembanding konkret untuk menguji kontribusi kebaruan riset FCL:

1. **Rekomendasi Utama (Dimensi Continual Learning): FedCurv (Shoham et al., arXiv:1910.07796)**
   - **Alasan Ilmiah:** FedCurv adalah perluasan langsung (*natural federated extension*) dari EWC. Klien menghitung diagonal Fisher yang sama persis, namun membagikannya ke server untuk menghukum deviasi bobot konsensus global.
   - **Efisiensi Implementasi:** Tidak memerlukan arsitektur modular baru atau generator sintetis. Tetap beroperasi pada model MLP 6.211 parameter yang sama.
   - **Relevansi Hipotesis:** Secara langsung menguji hipotesis *EWC Dilution Effect* - apakah membagikan Fisher ke server mampu mengatasi pengenceran gradien akibat ketimpangan data Klien A (670 ribu alur) vs Klien B (860 ribu alur).
   - **Usulan Matriks:** Dapat diajukan sebagai kondisi pengujian opsional **E4b: FedAvg + FedCurv**.

2. **Rekomendasi Alternatif (Dimensi Heterogenitas Non-IID): FedProx (Li et al., MLSys 2020)**
   - **Alasan Ilmiah:** FedProx sudah terverifikasi di daftar pustaka primer (`Li-2020-FedProx.md`). Menambahkan suku proksimal $\frac{\mu}{2} \|\theta - \theta^t\|^2$ secara murni menguji apakah celah akurasi non-IID di RM 1 berasal dari *client drift* atau *catastrophic forgetting*.
   - **Nol Biaya Tambahan:** Skrip Flower mudah disisipi suku proksimal tanpa merombak pipeline pelatihan.

3. **Mengapa FedWeIT / GLFC / TARGET Tidak Dipilih sebagai Eksperimen Wajib?**
   - FedWeIT membutuhkan pembuatan *sparse mask* per-tugas yang menambah overhead komputasi.
   - GLFC dan TARGET membutuhkan modul generator sintetis / proxy server yang didesain untuk citra resolusi tinggi (Computer Vision), yang terlalu berat (*overkill*) dan tidak alami untuk data tabular NIDS 62 fitur. Keduanya cukup diposisikan sebagai tinjauan taksonomi pada Bab 2.

---

## 2. Tinjauan Literatur Skala Jumlah Node Klien dan Server

### 2.1 Taksonomi Skala Node pada Federated Learning
Dalam literatur FL (*Kairouz et al., 2021; McMahan et al., 2017*), skala sistem dibagi menjadi dua rezim:

1. **Cross-Silo FL (Skala Organisasi / Subnet Gateway):**
   - Jumlah klien: **2 hingga 10 klien**.
   - Karakteristik: Klien berupa server gateway, router enterprise, atau sentral monitoring regional dengan ketersediaan tinggi (*100% participation rate*).
   - Domain: NIDS antar-organisasi, keamanan perbankan, deteksi intrusi subnet enterprise.
2. **Cross-Device FL (Skala Perangkat Sensor Edge / IoT Masif):**
   - Jumlah klien: **100 hingga 10.000+ klien mikro**.
   - Karakteristik: Perangkat memiliki sumber daya baterai/bandwidth minim, koneksi tidak stabil, tingkat partisipasi acak per ronde hanya 1% - 10% (*client sampling*).

### 2.2 Tinjauan Literatur Skala Node pada NIDS & IoT Terfederasi (Sumber Terverifikasi)

| Paper / Penulis | Skenario Aplikasi | Jumlah Klien ($K$) | Status Verifikasi Sumber Primer | Justifikasi Peneliti |
|---|---|---|:---:|---|
| **Kairouz et al. (2021)** *(Google Research dkk.)* | Fondasi Taksonomi FL (*Advances and Open Problems in FL*) | **Cross-Silo: 2 s.d. Puluhan**<br>Cross-Device: 100 s.d. Jutaan | ✔ **arXiv:1912.04977** (FnT in ML, Vol. 14) | Menetapkan pembagian resmi: Cross-silo FL menggunakan sedikit klien berdaya tetap (2-puluhan), sedangkan cross-device untuk jutaan mobile node. |
| **Nguyen et al. (D̈ıoT, 2019)** | FL Anomaly Detection untuk IoT | **2 s.d. 15 Klien** | ✔ **arXiv:1804.07474** (IEEE ICDCS 2019) | Menguji batas kinerja konvergensi deteksi anomali perangkat IoT pada spektrum 2 hingga 15 gateway. |
| **Ruzafa-Alcázar et al. (2023)** | Industrial IoT (IIoT) NIDS Terfederasi | **Klaster Edge Gateway** | ✔ **DOI: 10.1109/TII.2021.3126728** (IEEE TII, Vol. 19(2)) | Memodelkan pemisahan fisik stasiun industri nyata dengan pemrosesan deteksi pada edge node lokal. |
| **Ali et al. (FL-BCID, 2025)** | Privacy-Preserving IIoT IDS | **10 Edge Nodes** | ✔ **arXiv:2505.15376** (Mei 2025) | Menguji model kolaboratif ringan FL pada 10 perangkat edge terdistribusi (dataset ToN-IoT & N-BaIoT). |
| **Zhao et al. (2018)** | Fondasi Teoretis Non-IID FL | **2 Klien (Analitis) & 10 Klien** | ✔ **arXiv:1806.00582** (Terverifikasi di korpus) | 2 klien digunakan secara khusus untuk menurunkan pembuktian matematis batas divergensi bobot $\|w_{FL} - w_{Centralized}\|$. |
| **Hernandez-Ramos et al. (2025)** | Systematic Review FL-NIDS | **Survei Arsitektur Cross-Silo** | ✔ **DOI: 10.1145/3731596** (ACM CSUR, Vol. 57(12)) | Menunjukkan dominasi arsitektur cross-silo berbasis gateway organisasi pada sistem deteksi intrusi terfederasi. |

### 2.3 Justifikasi Ilmiah Pemilihan 2 Klien pada Penelitian Ini
Mengapa penelitian ini menggunakan **2 Klien + 1 Server**?
1. **Isolasi Variabel Non-IID Ekstrem (Kontrol Eksperimental Murni):**
   Dengan 2 klien (Klien A: Subnet Internal dengan serangan SSH-Patator; Klien B: Perimeter DMZ dengan serangan DoS), disparitas distribusi kelas dapat diisolasi secara deterministik tanpa terkontaminasi oleh *client sampling noise* atau variasi keacakan pemilihan klien per ronde.
2. **Skalabilitas Partisi Data CIC-IDS2017:**
   Serangan SSH-Patator pada dataset hanya memiliki 3.219 flow unik. Membagi data ini ke 10 atau 20 klien akan menghasilkan <150 flow per klien, yang merusak daya statistik (*statistical power*) dan membuat estimasi Matriks Fisher menjadi singular (tidak terbalikkan).
3. **Peta Skalabilitas (Opsi Pembahasan):**
   Jika dosen menghendaki pengujian skalabilitas, arsitektur Flower yang dibangun dalam repositori ini telah dirancang modular sehingga secara langsung dapat diuji pada konfigurasi **$K = 4$ klien** (2 klien Subnet Internal + 2 klien Perimeter DMZ) atau **$K = 8$ klien** dengan mempartisi data Normal secara Dirichlet non-IID ($\alpha = 0.5$).

---

## 3. Implementasi FCL di Luar Domain NIDS (Kajian Literatur & Paper Riil)

Konsep *Federated-Continual Learning* (FCL) memecahkan dua masalah universal yang tidak hanya terjadi di jaringan komputer: **privasi data terdistribusi (spatial non-IID)** dan **kelupaan katastropik saat pola data berubah (temporal drift)**. Berikut adalah bukti studi literatur primer yang menerapkan FCL pada domain-domain non-NIDS:

### 3.1 Pervasive Computing, Wearables & Perimeter Sensor (Analogi Pagar Kampus ITS)
- **Paper Riil:** Usmanova, Portet, Lalanda, & Vega (2022). *"Federated Continual Learning through Distillation in Pervasive Computing."* IEEE International Conference on Smart Computing (SMARTCOMP) / arXiv:2207.08181. DOI: [10.48550/arXiv.2207.08181](https://doi.org/10.48550/arXiv.2207.08181).
- **Implementasi:** Jaringan node sensor edge bergerak/tetap (akselerometer 3-sumbu dan giroskop) untuk mengenali aktivitas fisik (Human Activity Recognition) yang berubah seiring waktu.
- **Korelasi dengan Analogi Pagar ITS (180 Hektar):** Sensor getaran pagar (akselerometer/geophone) di sektor Pintu Utama vs Sektor Hutan menghadapi dinamika kelas yang datang sekuensial (gangguan angin/hewan $\to$ intrusi panjat pagar). Paper membuktikan FCL mampu mengadaptasi sinyal getaran baru tanpa melupakan pola getaran lama dan tanpa membanjiri transmisi radio.

### 3.2 Industrial IoT (IIoT), Digital Twins & Predictive Maintenance Pabrik
- **Paper Riil:** Zhao et al. (2025). *"FCLLM-DT: Empowering Federated Continual Learning With Large Language Models for Digital-Twin-Based Industrial IoT."* IEEE Internet of Things Journal. DOI: [10.1109/JIOT.2024.3510553](https://doi.org/10.1109/JIOT.2024.3510553).
- **Survei Domain Terkait:** Qi et al. (2024). *"Federated Continual Learning via Knowledge Fusion: A Survey."* IEEE Transactions on Knowledge and Data Engineering (TKDE) / arXiv:2312.16475.
- **Implementasi:** Pemantauan anomali getaran mesin industri (*bearing fault diagnosis*) melintasi beberapa fasilitas pabrik independen.
- **Peran FCL:** Pabrik A dan B mendeteksi jenis keausan mekanik baru (*bearing outer-race defect*) secara bertahap tanpa mengirimkan rekaman getaran mentah SCADA ke cloud publik.

### 3.3 Internet of Medical Things (IoMT Healthcare) & Analisis Sinyal Biosignal
- **Paper Riil:** Dong et al. (2024). *"FedCL-Ensemble Learning: A Framework of Federated Continual Learning with Ensemble Transfer Learning Enhanced for Alzheimer's MRI Classifications while Preserving Privacy."* arXiv:2411.12756. DOI: [10.48550/arXiv.2411.12756](https://doi.org/10.48550/arXiv.2411.12756).
- **Paper Landmark Imaging:** Liu et al. (2023). *"Asynchronous Decentralized Federated Lifelong Learning for Landmark Localization in Medical Imaging."* arXiv:2303.06783. DOI: [10.48550/arXiv.2303.06783](https://doi.org/10.48550/arXiv.2303.06783).
- **Implementasi:** Multi-senter rumah sakit mendeteksi anomali elektrokardiogram (ECG 12-lead) atau MRI.
- **Peran FCL:** Rumah sakit diwajibkan oleh undang-undang privasi medis untuk tidak membagikan data rekam medis pasien, sementara model klinis dituntut mengasimilasi varian patologi baru tanpa mengalami degradasi akurasi pada penyakit terdahulu.

### 3.4 Autonomous Vehicles & Intelligent Transportation Systems (V2X)
- **Survei Domain Terkait:** Hamedi et al. (2025). *"Federated Continual Learning: Concepts, Challenges, and Solutions."* Neurocomputing, Vol. 651, 130844. DOI: [10.1016/j.neucom.2025.130844](https://doi.org/10.1016/j.neucom.2025.130844).
- **Implementasi:** Armada kendaraan otonom yang menjelajahi kondisi jalan raya dan iklim yang dinamis.
- **Peran FCL:** Kendaraan memperbarui model deteksi bahaya jalanan saat berpindah ke zona geografis baru tanpa menimpa aturan navigasi dasar.

---

## 4. Penambahan Rumusan Masalah Fondasional (RM 0)

Sesuai arahan dosen pembimbing, ditambahkan satu rumusan masalah umum/fondasional sebelum RM 1 dan RM 2, sehingga struktur rumusan masalah proposal menjadi piramida yang kokoh: **Arsitektural Umum $\to$ Komparasi Terdistribusi $\to$ Mitigasi Kelupaan Sekuensial**.

### Formulasi Baru Rumusan Masalah (3 Poin)

> **1. Rumusan Masalah 1 (Fondasional / Arsitektural Umum - BARU):**  
> *Bagaimana rancang bangun dan kelayakan arsitektur Federated-Continual Learning (FCL) yang mengintegrasikan agregasi terdistribusi (Federated Averaging) dan regularisasi parameter lokal (Elastic Weight Consolidation) untuk deteksi intrusi jaringan di bawah kondisi heterogenitas data non-IID?*

> **2. Rumusan Masalah 2 (Analisis Komparasi Terdistribusi vs Lokal - Dahulu RM 1):**  
> *Bagaimana kinerja deteksi intrusi model yang dilatih secara terdistribusi (FedAvg) dibandingkan dengan model yang dilatih secara lokal pada masing-masing klien dengan distribusi data non-IID?*

> **3. Rumusan Masalah 3 (Analisis Mitigasi Catastrophic Forgetting - Dahulu RM 2):**  
> *Bagaimana pengaruh metode Elastic Weight Consolidation (EWC) terhadap mitigasi catastrophic forgetting saat model mempelajari kelas serangan baru secara sekuensial, baik pada skenario pelatihan lokal maupun terdistribusi (FedAvg + EWC)?*

### Penyelarasan Tujuan Penelitian
Tujuan penelitian diselaraskan secara linear mengikuti 3 rumusan masalah di atas:
1. Merancang dan menguji kelayakan arsitektur integrasi FCL (FedAvg + EWC) pada lingkungan testbed private cloud server.
2. Menganalisis perbandingan performa deteksi model terfederasi terhadap model lokal non-IID.
3. Menganalisis efektivitas metode EWC dalam mempertahankan memori kelas serangan masa lalu (mengukur Backward Transfer, F1-Score, dan stabilitas representasi bobot).

---

## 5. Penyesuaian Parameter Pengukuran dan Fitur pada Skenario Live Injections

Jika dosen menghendaki penambahan skenario *Live Packet Injection* (injeksi lalu lintas aktif) sebagai pengujian pelengkap, terdapat batasan teknis mendasar antara karakteristik data flow tabular (*CICFlowMeter*) dan trafik live packet capture (*libpcap/eBPF*).

### 5.1 Parameter Pengukuran Tambahan (QoS & System Overhead)
Pada injeksi langsung, parameter deteksi ML tidak cukup; wajib ditambahkan parameter telekomunikasi dan sistem:

| Kategori Parameter | Metrik Baru | Satuan | Mekanisme Pengukuran | Justifikasi Ilmiah |
|---|---|---|---|---|
| **Kinerja Jaringan (QoS Layer 3/4)** | *Round Trip Time (RTT) / Delay* | Milidetik ($ms$) | Ping ICMP & probe timestamp TCP | Mengukur dampak banjir paket DoS terhadap transmisi uplink/downlink FL. |
| | *Packet Loss Rate (PLR)* | Persen ($\%$) | Rasio paket hilang pada antarmuka Linux bridge | Menguji ketahanan agregasi model saat kanal gRPC mengalami degradasi paket. |
| | *Throughput Degradation* | Mbps | `iperf3` baseline vs under-attack | Memvalidasi integritas throughput jaringan monitoring saat serangan terjadi. |
| **Beban Sumber Daya Node** | *Packet Dropping Count* | Jumlah paket | `tc` / `ethtool -S` drop counter | Mengukur apakah modul flow sniffing kehabisan buffer antrean saat trafik melonjak masif. |
| | *CPU & RAM Utilization* | $\%$ CPU, MB RAM | `psutil` / Docker stats | Mengukur overhead proses flow extractor real-time di node edge sensor. |
| **Kinerja Deteksi Real-Time** | *Detection Latency per Attack Event* | Detik ($s$) | Waktu paket masuk pertama $\to$ trigger alert IDS | Menilai keterlambatan peringatan akibat mekanisme flow windowing. |

### 5.2 Penyesuaian Fitur (Kendala Bidirectional Flow pada Live Streaming)
1. **Masalah Flow Timeout pada CICFlowMeter Live:**
   Dataset CIC-IDS2017 dibangun dari 62 fitur statistik *bidirectional flow* (seperti `Bwd Packet Length Mean`, `Flow IAT Std`, dll.).
   Fitur-fitur ini **tidak dapat dihitung secara instan pada paket pertama**. Modul harus menunggu aliran selesai (*FIN/RST flag*) atau mencapai batas waktu tidak aktif (*flow inactive timeout* 120 detik). Akibatnya, pada live injection, alarm deteksi DoS Slowloris baru akan berbunyi setelah 120 detik, yang tidak realistis untuk pencegahan intrusi aktif.
2. **Solusi Penyesuaian Fitur yang Direkomendasikan Literatur (*Sarhan et al., 2022; Engelen et al., 2021*):**
   - Menggunakan fitur berbasis jendela paket awal (*Early-Flow Features* / $N$-paket pertama, misal 5 paket pertama).
   - Menetapkan jendela sliding mikro (*sliding time window*, misal 1 detik) untuk menghitung statistik frekuensi paket per detik secara streaming.
3. **Kendala Sinkronisasi Labeling (*Ground Truth Synchronization*):**
   Pada live injection, script penyerang (Hydra / Slowloris) harus menyinkronkan penanda waktu nanodetik dengan node receiver agar alur yang ditangkap dapat dilabeli secara otomatis dengan benar. Ketidaktepatan sinkronisasi akan menghasilkan label bising (*noisy ground truth*) yang merusak evaluasi Macro-F1.

---

## 6. Literatur Review Menyeluruh Continual Learning Methods

Continual Learning (CL) bertujuan memampukan jaringan saraf tiruan belajar dari aliran tugas sekuensial $\mathcal{T}_1, \mathcal{T}_2, \dots, \mathcal{T}_T$ tanpa melupakan representasi tugas terdahulu (*Stability-Plasticity Dilemma*).

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

### 6.1 Taksonomi dan Perbandingan Komprehensif Metode CL

| Nama Metode | Penulis & Tahun | Prinsip Kerja Matematis | Keunggulan Utama | Kelemahan / Bottleneck | Relevansi untuk NIDS Edge |
|---|---|---|---|---|---|
| **EWC (Elastic Weight Consolidation)** | Kirkpatrick et al. (2017) | $\mathcal{L}(\theta) = \mathcal{L}_{\text{new}}(\theta) + \sum_i \frac{\lambda}{2} F_i (\theta_i - \theta_{1, i}^*)^2$ | Bebas penyimpanan data mentah; komputasi Fisher Information deterministik. | Mengasumsikan parameter independen (hanya diagonal Hessian); penalti bertambah linear terhadap jumlah task. | ⭐⭐⭐⭐⭐ **Sangat Ideal (Dipilih): Ringan, analitis stabil pada MLP.** |
| **Online EWC** | Schwarz et al. (2018) | Mengakumulasi matriks Fisher melintasi banyak task: $\tilde{F}^t = \gamma \tilde{F}^{t-1} + F^t$ | Skalabel untuk puluhan task sekuensial tanpa menambah memori penalti. | Sedikit lebih kompleks dalam penyetelan faktor peluruhan $\gamma$. | ⭐⭐⭐⭐ Sangat relevan untuk task panjang ($T > 3$). |
| **Synaptic Intelligence (SI)** | Zenke et al. (2017) | Menghitung trajektori pembaruan bobot online selama optimasi: $\omega_i^t = \sum \Delta \theta_i \cdot g_i$ | Komputasi relevansi parameter berlangsung bersamaan dengan pelatihan lokal. | Sangat sensitif terhadap learning rate lokal; rawan tidak stabil pada non-IID. | ⭐⭐⭐ Alternatif regularisasi parameter. |
| **Memory Aware Synapses (MAS)** | Aljundi et al. (2018) | Menghitung sensitivitas output fungsi prediksi terhadap parameter tanpa label (*unlabeled*). | Bekerja tanpa data berlabel (*unsupervised*). | Kurang sensitif terhadap batas keputusan multikelas yang ketat. | ⭐⭐⭐ Bagus untuk skenario tanpa label. |
| **Learning without Forgetting (LwF)** | Li & Hoiem (2017) | Distilasi pengetahuan menggunakan model task lama sebagai *teacher* dengan regularisasi KL-Divergence. | Tidak memerlukan komputasi Fisher dan tidak memerlukan buffer data mentah. | Terjadi distorsi representasi jika data task baru sangat berbeda dari task lama (*domain shift*). | ⭐⭐⭐⭐ Alternatif berbasis distilasi. |
| **Experience Replay (ER)** | Chaudhry et al. (2019) | Menyimpan subset data mentah tugas lama di buffer memori fisik dan me-replay saat training baru. | Retensi memori sangat tinggi dan akurasi stabil. | **Melanggar privasi data (GDPR/UU PDP)** jika buffer dicuri; membebani RAM edge. | ❌ Dieliminasi (Isu privasi & memori). |
| **Gradient Episodic Memory (GEM)** | Lopez-Paz & Ranzato (2017) | Proyeksi kuadratik gradien baru agar $\langle g_{\text{new}}, g_{\text{old}} \rangle \ge 0$ pada buffer memori. | Mendorong Backward Transfer nonnegatif ($BWT \ge 0$) melalui pembatasan sudut gradien. | Komputasi QP-solver sangat berat di edge; membutuhkan buffer data mentah. | ❌ Dieliminasi (Komputasi & buffer). |
| **PackNet** | Mallya & Lazebnik (2018) | Melakukan *pruning* bobot (50-75%) dan membekukan bobot terpilih untuk task lama. | Forgetting bernilai mutlak nol pada task lama. | Kapasitas model cepat jenuh setelah beberapa task; membutuhkan arsitektur besar. | ❌ Kurang relevan untuk MLP kompak. |
| **TARGET** | Zhang et al. (ICCV 2023) | Distilasi generatif transfer kelas tanpa data mentah (*exemplar-free generative distillation*). | Privasi tinggi, tanpa buffer data mentah riil. | Membutuhkan pelatihan modul generator tambahan yang berat untuk skala edge. | ⚠️ Kompleksitas tidak sepadan dengan MLP 6.211 parameter. |
| **LoRA-CL** | Hu et al. (ICLR 2022) / Adaptasi | Membekukan bobot dasar dan menyematkan modul adapter rank-rendah per-task sekuensial. | Nol kelupaan pada representasi dasar; efisien parameter. | Memerlukan mekanisme routing task-ID saat inferensi; kurang alami untuk MLP 3-lapis. | ⭐⭐⭐ Alternatif arsitektural. |

### 6.2 Mengapa EWC Terpilih untuk NIDS Terdistribusi?
1. **Kepatuhan Privasi (Zero-Data Replay):** EWC hanya mengomputasi gradien kuadrat lokal. Tidak ada satu pun baris paket jaringan yang disimpan di disk/RAM setelah sesi pelatihan selesai.
2. **Kestabilan Analitis pada Arsitektur Kompak:** Pada MLP 6.211 parameter, diagonal Matriks Fisher hanya berukuran $6.211 \times 4\text{ byte} \approx 24,84\text{ KB}$, yang dapat dihitung dalam hitungan detik dan disimpan tanpa overhead memori.

---

## 7. Literatur Review Menyeluruh Federated Learning Methods

Federated Learning (FL) memecahkan optimasi terdistribusi di mana $K$ klien dengan distribusi data lokal $\mathcal{D}_k$ berkolaborasi mengoptimalkan model global $w$:

$$\min_{w} f(w) = \sum_{k=1}^K \frac{n_k}{N} F_k(w), \quad \text{di mana } F_k(w) = \mathbb{E}_{x \sim \mathcal{D}_k} [\ell(w; x)]$$

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

### 7.1 Taksonomi dan Perbandingan Komprehensif Metode FL

| Nama Metode | Penulis & Tahun | Karakteristik Agregasi & Matematis | Keunggulan Utama | Kelemahan / Overhead | Relevansi untuk NIDS Edge |
|---|---|---|---|---|---|
| **FedAvg** | McMahan et al. (2017) | Rata-rata terbobot sederhana dari bobot lokal: $w^{t+1} = \sum_{k=1}^K \frac{n_k}{N} w_k^{t+1}$ | Efisiensi komunikasi tinggi; implementasi standar industri (Flower framework). | Mengalami *client drift* dan divergensi bobot saat data non-IID ekstrem. | ⭐⭐⭐⭐⭐ **Baseline Utama (Dipilih)** |
| **FedProx** | Li et al. (2020) | Menambahkan penalti deviasi lokal dari model global: $\min_w F_k(w) + \frac{\mu}{2} \|w - w^t\|^2$ | Mencegah model lokal menjauh dari konsensus; tangguh terhadap *stragglers*. | Memerlukan penyetelan parameter $\mu$; konvergensi lebih lambat jika $\mu$ terlalu besar. | ⭐⭐⭐⭐ **Alternatif Penguat Utama** |
| **SCAFFOLD** | Karimireddy et al. (2020) | Menggunakan variabel kontrol (*control variates*) $c_k$ dan $c$ untuk mengoreksi arah gradien klien. | Menjamin konvergensi cepat di bawah non-IID ekstrem tanpa deviasi gradien. | Ukuran payload komunikasi meningkat **$2 \times$** (mengirim bobot model $w$ + variabel kontrol $c$). | ⭐⭐⭐ Baik untuk server berkapasitas tinggi. |
| **FedNova** | Wang et al. (2020) | Menormalkan pembaruan gradien lokal berdasarkan jumlah langkah optimasi lokal klien yang berbeda. | Menghilangkan bias terhadap klien yang melakukan lebih banyak epoch lokal. | Kurang berdampak jika jumlah epoch lokal antar-klien seragam ($E$ konstan). | ⭐⭐⭐ Relevan jika node memiliki spek jomplang. |
| **MOON** | Li et al. (2021) | Model-Contrastive Federated Learning: memaksimalkan kemiripan representasi model lokal dengan global. | Akurasi representasi laten sangat tinggi pada visi/ekstraksi fitur dalam. | Komputasi forward pass tambahan untuk model global lama di tiap klien (berat di edge). | ⭐⭐ Terlalu berat untuk sensor mikro. |
| **FedCurv** | Shoham et al. (2019) | Menerapkan penalti berbasis kurvatur Fisher lintas klien yang diagregasikan di server. | Menyelaraskan FCL pada tingkat agregasi server. | Overhead gRPC mengirimkan matriks diagonal Fisher dari semua klien ke server. | ⭐⭐⭐⭐ **Pengembangan Lanjut FCL** |

### 7.2 Hubungan antara FedAvg dan EWC pada Skenario Usulan
Pada penelitian ini, **FedAvg dipilih sebagai pondasi terdistribusi**, sementara **EWC beroperasi pada loop optimasi lokal masing-masing klien**. Dengan arsitektur ini:
- Server bertugas murni sebagai *stateless aggregator* yang ringan dan cepat.
- Klien bertanggung jawab melindungi memori masa lalunya secara lokal sebelum mengirimkan model ke server.
- Ini meminimalkan overhead jaringan gRPC sehingga payload tetap berada di angka **49,69 KB per klien/ronde**.

---

## 8. Konseptualisasi Skala Banyak Edge Node: Analogi Pagar Perimeter ITS 180 Hektar

### 8.1 Membedah Analogi Dosen: Keamanan Perimeter Kampus ITS
Dosen pembimbing memberikan analogi yang sangat tajam dan kontekstual mengenai sistem keamanan fisik kampus ITS (luas $\approx 180$ hektar):
- **Lingkungan Fisik:** Kampus dikelilingi oleh pagar pembatas sepanjang berkilo-kilometer dengan banyak titik masuk (*breaching points*).
- **Infrastruktur Edge Sensor:** Di sepanjang pagar terpasang puluhan node sensor edge (misal: sensor seismik/getaran pagar, sensor inframerah pasif PIR, sensor radar gelombang mikro, atau mikrofon akustik).
- **Tantangan Utama:** **False Positive vs True Intrusion**.
  - Gangguan Alami (*Noise/Benign*): Kucing atau anjing liar menyenggol pagar, dahan pohon jatuh, hembusan angin kencang, getaran truk tronton melintas di Jalan Raya Kertajaya/MERR.
  - Ancaman Nyata (*Intruder*): Manusia memotong kawat pagar, memanjat pagar, atau membongkar fondasi.
- **Dinamika Sekuensial (Continual Learning):**
  - Pada musim kemarau, karakteristik getaran tanah dan pagar berbeda dari musim hujan (tanah basah meredam getaran).
  - Ketika ada proyek konstruksi gedung baru di dalam kampus (misal pembangunan tower baru), sensor di sektor tersebut terpapar pola getaran alat berat baru. Model harus mempelajari pola gangguan baru ini tanpa melupakan cara membedakan pencuri/penyusup manusia.

```
                                  ┌──────────────────────────────┐
                                  │   Server Monitoring Pusat    │
                                  │   (Tower Rektorat / BAPSI)   │
                                  └──────────────┬───────────────┘
                                                 │
                        ┌────────────────────────┼────────────────────────┐
                        │ Flower FedAvg (gRPC)   │                        │
                        ▼                        ▼                        ▼
               ┌─────────────────┐      ┌─────────────────┐      ┌─────────────────┐
               │  Edge Node S-1  │      │  Edge Node S-2  │      │  Edge Node S-K  │
               │ (Pintu Utama)   │      │ (Sektor Keputih)│      │ (Sektor Gebang) │
               └────────┬────────┘      └────────┬────────┘      └────────┬────────┘
                        │                        │                        │
       Pola Gangguan:   ▼       Pola Gangguan:   ▼       Pola Gangguan:   ▼
       Trafik MERR, Bus Kampus  Semak liar, Hewan Peliharaan   Aktivitas Warga, Warung
```

### 8.2 Argumentasi: Mengapa Proposal Dimulai dari 2 Klien, dan Bagaimana Skalasinya?
Ketika dosen bertanya: *"Kampus ITS punya puluhan sektor pagar, kenapa di proposal cuma ada 2 klien?"*, berikut adalah strategi argumentasi ilmiah yang kokoh:

1. **2 Klien adalah Pemodelan "Dua Sektor Ekstrem" (*Canonical Boundary Conditions*):**
   - **Klien A (Representasi Sektor Internal / Pintu Gerbang Terkendali):** Memodelkan area yang dominan menghadapi serangan bertarget kredensial terarah (diwakili oleh **SSH-Patator**).
   - **Klien B (Representasi Sektor Perimeter Luar / DMZ Terbuka):** Memodelkan area terbuka yang rentan dibanjiri serangan volumetrik masif (diwakili oleh **DoS Hulk/GoldenEye**).
   - Meneliti 2 klien non-IID ekstrem memberikan pembuktian batas matematis (*theoretical boundary*) yang paling bersih untuk menjawab apakah FedAvg + EWC bekerja sebelum diuji pada skala besar.
2. **Kendala Ketersediaan Data Kelas Langka CIC-IDS2017:**
   - Serangan SSH-Patator hanya memiliki 3.219 baris unik. Jika langsung dibagi ke 20 node sektor pagar, tiap node hanya menerima 160 sampel. Akurasi estimasi Matriks Informasi Fisher pada 160 sampel akan mengalami degradasi varians yang sangat parah.
3. **Peta Eskalasi ke Multi-Node (Rencana Roadmap Pembahasan):**
   Kita menyajikan kepada dosen bahwa arsitektur yang kita rancang **siap diskalakan (*scale-out ready*)** dalam 2 skema:
   - **Skema A (Uji Skalabilitas Simulasi $K=4$ s.d. $K=8$ Node):**
     Data Normal (1,33 juta flow) dipecah ke 8 node menggunakan distribusi Dirichlet ($\alpha = 0.5$) untuk merefleksikan 8 sektor pagar ITS, sementara serangan disebar ke klaster node tertentu.
   - **Skema B (Hierarchical Federated Learning):**
     Node-node sensor di sektor pagar yang berdekatan diagregasi terlebih dahulu oleh gateway lokal (misal Gateway Sektor Timur), sebelum dikirim ke Server Monitoring Pusat ITS.

---

## 9. Konsolidasi Ketetapan Dataset CIC-IDS2017 & Pemetaan Dataset Luar Domain IDS

### 9.1 Skenario Domain Network IDS: Ketetapan Dataset CIC-IDS2017 (Tetap & Terkunci)
Jika penelitian tetap berada pada domain deteksi intrusi jaringan (*Network-based IDS*), **Dataset CIC-IDS2017 tetap dipertahankan secara definitif**. Seluruh keputusan teknis data yang telah diverifikasi empiris tetap berlaku 100%:

1. **3 Kelas Target Representatif:**
   - **Normal (BENIGN):** 1.332.710 flow unik (Senin, Selasa, Rabu).
   - **SSH-Patator (Task 1):** 3.219 flow unik (Selasa).
   - **DoS 4-Subvarian (Task 2):** 193.748 flow unik (Rabu: Hulk, GoldenEye, slowloris, slowhttptest).
   - **Total:** **1.529.677 flow bersih terdeduplikasi**.
2. **62 Fitur Numerik Bersih (Eliminasi Kebocoran Port):**
   - Fitur `Destination Port` **resmi dibuang** untuk mencegah *shortcut learning* (menghafal port 22/80).
   - 10 fitur varians nol dan 5 fitur redundan 100% dibuang, menyisakan tepat 62 fitur statistik dinamika paket.
3. **Weighted Cross-Entropy Loss + Gradient Clipping (Norm $\le 1.0$):**
   - Mempertahankan seluruh 1,53 juta baris data tanpa *undersampling* buatan, menyeimbangkan ketimpangan kelas 414 : 1 melalui bobot invers frekuensi terstandarisasi.
4. **Arsitektur Model MLP Kompak:**
   - 62 Input $\to$ 64 Hidden (ReLU + Dropout 0.2) $\to$ 32 Hidden (ReLU) $\to$ 3 Output (Softmax).
   - Total kapasitas: **6.211 parameter teroptimasi** ($24,84\text{ KB}$), ideal untuk edge node.

---

### 9.2 Skenario Luar Domain Network IDS: Tabel Literature Review Menyeluruh Dataset Alternatif
Jika dosen pembimbing menghendaki penelitian beralih atau diperluas ke luar domain trafik jaringan (misalnya menyesuaikan topik riset laboratorium atau analogi sensor pagar kampus ITS 180 hektar), dataset harus disesuaikan secara ketat dengan domain fisik yang diteliti. Berikut adalah tabel komparasi dataset alternatif non-jaringan:

| No | Domain Riset | Nama Dataset Benchmark | Tipe & Karakteristik Sensor | Ukuran Data & Format | Skenario Sekuensial Continual Learning (Task 1 $\to$ Task 2) | Kesesuaian FCL di Edge | Risiko & Tantangan bagi Mahasiswa | Referensi Publikasi |
|:--:|:---|:---|:---|:---|:---|:---:|:---|:---|
| 1 | **Perimeter Intrusion Detection (Analogi Pagar Kampus ITS)** | **UCR Time Series Archive (Fence/Vibration Subsets)** / **UCI HAR** | Akselerometer 3-sumbu, piezoelektrik, dan geophone seismik pada pagar kawat/tanah. | Puluhan ribu sekuens sinyal 1D (gelombang getaran $x, y, z$). | **Task 1:** Deteksi hewan/cuaca (angin, hujan, kucing) vs Intruder Panjat.<br>**Task 2:** Intruder Potong Kawat / Gali Tanah (Task baru). | ⭐⭐⭐⭐ **Tinggi** (Model 1D-CNN atau MLP getaran). | Memerlukan konversi domain sinyal waktu (FFT/Wavelet) ke fitur statistik sebelum training. | Chen et al. (IEEE TIM, 2021); UCI ML Repository |
| 2 | **Industrial SCADA / Critical Infrastructure** | **SWaT (Secure Water Treatment)** & **WADI** | 51 sensor fisik instalasi air (level air, laju alir, tekanan pipa, aktuator valve pompa). | 946.721 sampel operasional normal + 446.000 sampel serangan siber-fisik (tabular). | **Task 1:** Serangan manipulasi sensor level air $\to$<br>**Task 2:** Serangan pembobolan katup pipa kimia bertekanan tinggi. | ⭐⭐⭐⭐⭐ **Sangat Tinggi** (Tabular kontinu mirip CIC-IDS2017). | Dataset sangat besar, membutuhkan pemahaman domain teknik proses industri. | Mathur et al. (CyberICPS 2016); iTrust SUTD |
| 3 | **Smart Campus IoT Environmental Anomaly** | **Intel Berkeley Lab Data** / **SMD (Server Machine Dataset)** | Sensor nirkabel lingkungan: Suhu, Kelembapan, Cahaya, Tegangan baterai node. | 2,3 juta pembacaan sensor berkala dari 54 sensor node terdistribusi. | **Task 1:** Anomali kebocoran suhu/kebakaran $\to$<br>**Task 2:** Anomali drop tegangan baterai mendadak akibat badai/interferensi. | ⭐⭐⭐ **Sedang** | Pola anomali relatif sederhana; disparitas non-IID kurang menantang untuk FCL. | Bodik et al. (ACM SIGCOMM 2004) |
| 4 | **Internet of Medical Things (IoMT Healthcare)** | **PhysioNet MIT-BIH Arrhythmia Database** | Rekaman sinyal elektrokardiogram (ECG) 2-lead dari berbagai pasien terdistribusi. | 48 rekaman raw ECG (panjang 30 menit per pasien, anotasi detak jantung). | **Task 1:** Deteksi Premature Ventricular Contractions (PVC) $\to$<br>**Task 2:** Deteksi Supraventricular Ectopic Beats (SVEB). | ⭐⭐⭐⭐ **Tinggi** (Privasi antar-rumah sakit sangat cocok untuk FL). | Menuntut landasan medis yang kuat, kurang umum untuk mahasiswa Teknik Telekomunikasi. | Moody & Mark (IEEE EMB 2001) |
| 5 | **Autonomous Vehicles / Connected Cars (V2X)** | **CAN-Intrusion-Dataset (Car-Hacking Dataset)** | Log komunikasi bus CAN (Controller Area Network) internal kendaraan roda empat. | Jutaan baris frame pesan CAN (CAN ID, DLC, Data bytes). | **Task 1:** Serangan DoS pada bus CAN $\to$<br>**Task 2:** Serangan Fuzzing & Spoofing RPM/Gear transmisi kendaraan. | ⭐⭐⭐⭐ **Tinggi** (Tabular biner, payload ultra-ringan). | Terbatas pada jaringan bus kendaraan lokal, bukan skala jaringan luas seperti kampus. | Song et al. (IEEE T-ITS 2020) |

### 9.3 Rekomendasi Mahasiswa kepada Pembimbing
Berdasarkan perbandingan teknis di atas, mahasiswa merekomendasikan:
1. **Pilihan Utama (Direkomendasikan Tetap):** Tetap berada pada **Network IDS dengan CIC-IDS2017**, karena seluruh pipeline pra-pemrosesan (62 fitur tanpa port leakage, 1,53 juta baris, weighted loss, pembagian non-IID Klien A/B) telah selesai dikembangkan, divalidasi dengan 15 modul analitik skrip, dan siap dieksekusi tanpa risiko ketidakpastian data baru.
2. **Pilihan Alternatif (Jika Pembimbing Wajib Menyelaraskan dengan Proyek Sensor Fisik ITS):** Mengadopsi domain **Perimeter Intrusion Detection (Sensor Akselerometer Pagar)** atau **Industrial SCADA (SWaT)** yang memiliki struktur tabular numerik serupa sehingga algoritma FedAvg + EWC dapat langsung ditransfer tanpa merombak arsitektur model secara fundamental.

---

## 📋 Matriks Rangkuman Jawaban untuk Diskusi Bimbingan

| Poin Dosen | Inti Jawaban Mahasiswa | Rujukan Literatur / Dasar Teknis |
|---|---|---|
| **1. Metode Linier FCL** | Penelitian ini memposisikan diri pada *Exemplar-Free FCL* (bebas buffer replay) menggunakan FedAvg + EWC. Alternatif linier pelengkap: *FedCurv* (Fisher global), *FedProx* (suku proksimal), dan *Federated LwF* (distilasi model). | Kirkpatrick et al. (2017); Shoham et al. (2019); Li et al. (2020). |
| **2. Jumlah Node Klien** | Mengadopsi standar *Cross-Silo FL* (2-10 klien). 2 klien dipilih untuk mengisolasi disparitas non-IID murni tanpa noise sampling, serta menjaga kecukupan statistik kelas SSH-Patator (3.219 flow). | Kairouz et al. (2021); Ruzafa-Alcazar et al. (2023); Jin et al. (2024). |
| **3. Aplikasi Selain NIDS** | Smart Campus perimeter security (pagar ITS 180 ha), pemeliharaan prediktif IIoT pabrik, deteksi aritmia IoMT rumah sakit, dan kendaraan otonom V2X. | Tinjauan FCL multidisiplin; Hamedi et al. (2025). |
| **4. Tambahan Rumusan Masalah** | Menambahkan RM 1 Arsitektural Umum mengenai formulasi dan kelayakan integrasi FCL, sehingga rumusan masalah tersusun runtut: Arsitektur Umum $\to$ Komparasi FL vs Lokal $\to$ Mitigasi Lupa EWC. | Struktur baku piramida ilmiah skripsi Teknik Elektro ITS. |
| **5. Skenario Live Injections** | Jika diwajibkan live injection, parameter harus ditambah: *Packet Loss Rate*, *Delay/RTT*, *Throughput Degradation*, dan *Packet Drop Count*. Fitur harus disesuaikan ke *Early-Flow* karena batasan timeout 120s CICFlowMeter. | Sarhan et al. (2022); Engelen et al. (2021); Dube (2024). |
| **6. Review Continual Learning** | Review komprehensif mencakup 3 kelompok: *Regularization-based* (EWC, SI, MAS, LwF), *Replay-based* (ER, GEM), dan *Architecture-based* (PackNet, LoRA). EWC dipilih karena zero-data replay dan ringan di edge. | De Lange et al. (2021); Wang et al. (2023); Kirkpatrick et al. (2017). |
| **7. Review Federated Learning** | Review komprehensif mencakup: *Aggregation Baselines* (FedAvg), *Heterogeneity Mitigation* (FedProx, SCAFFOLD), dan *Continual FL* (FedCurv, FedWeIT). | McMahan et al. (2017); Li et al. (2020); Karimireddy et al. (2020). |
| **8. Analogi Pagar ITS (Edge Nodes)** | Menjelaskan bahwa 2 klien memodelkan batas kanonikal (Sektor Internal vs Perimeter Luar). Arsitektur Flower yang dibangun telah modular dan siap diekstensikan ke $K = 4$ atau $K = 8$ sektor pagar kampus ITS. | Analogi domain fisik smart campus; isolasi non-IID Zhao et al. (2018). |
| **9. Dataset CIC-IDS2017** | Kunci ketetapan dataset pada Senin-Rabu (1,53 juta flow, 62 fitur bersih tanpa port, Weighted Loss, 5 seeds). | Audit empiris mandiri; Rosay et al. (2022); Engelen et al. (2021). |

---
*Dokumen ini disusun sebagai panduan diskusi strategis dan bahan telaah ilmiah bersama dosen pembimbing.*
