# Briefing Konsultasi Dosen Pembimbing: Audit Kritis Keputusan Ruang Lingkup & Metodologi Tugas Akhir

**Judul Penelitian:**  
Analisis Kinerja Deteksi Network Traffic Intrusion Menggunakan Metode Federated-Continual Learning pada Testbed Private Cloud Server

**Penyusun:**  
Rafli Alif Ihza Hartono (NRP 5048231003)  
Departemen Teknik Elektro, Fakultas Teknologi Elektro dan Informatika Cerdas (FTEIC)  
Institut Teknologi Sepuluh Nopember (ITS), Surabaya  

---

## 📌 Pengantar untuk Dosen Pembimbing

Dokumen ini disusun sebagai panduan diskusi terstruktur dan audit kritis menjelang seminar proposal Tugas Akhir. Seluruh keputusan desain, pemilihan parameter, dan batasan masalah yang telah dirumuskan sejauh ini diuji kembali secara transparan: membandingkan keputusan saat ini (*current decision*), bukti ilmiah pendukung, alternatif yang tersedia, serta implikasi risikonya terhadap durasi pengerjaan (target 14-16 minggu) dan kelayakan fasilitas komputasi mahasiswa sarjana.

Tujuan utama sesi diskusi ini adalah menyelaraskan ekspektasi dosen pembimbing agar ruang lingkup (*scope*) terkunci secara definitif, mencegah terjadinya *scope creep*, dan memastikan proposal siap diseminarkan tanpa cacat metodologi mendasar.

---

## 🧭 Matriks Audit Keputusan (11 Poin Kunci)

### 1. Paradigma Utama Riset: Mengapa Menggabungkan Federated Learning (FL) dan Continual Learning (CL)?

* **Keputusan Saat Ini:**  
  Mengintegrasikan **Federated Learning** (*Federated Averaging* / FedAvg) untuk privasi data terdistribusi dan **Continual Learning** (*Elastic Weight Consolidation* / EWC) untuk mitigasi kelupaan katastropik (*catastrophic forgetting*) saat serangan baru muncul bertahap.
* **Dasar Ilmiah & Bukti:**  
  Mayoritas literatur NIDS terdistribusi mengasumsikan data statis dalam satu batch waktu (Hernandez-Ramos et al., 2025). Di lapangan, serangan siber muncul secara sekuensial (misal: hari ini Brute Force SSH, bulan depan varian DoS baru). Jika model terdistribusi dilatih ulang pada data baru, pengetahuan deteksi serangan lama runtuh drastis (*catastrophic forgetting*).
* **Alternatif yang Dipertimbangkan:**  
  1. *Hanya Federated Learning murni:* Melatih semua kelas serangan sekaligus secara terdistribusi. Dieliminasi karena tidak realistis terhadap dinamika ancaman baru.  
  2. *Hanya Continual Learning terpusat:* Mengabaikan aspek privasi dan transmisi data jaringan. Dieliminasi karena melanggar regulasi kerahasiaan log trafik (UU PDP No. 27/2022).
* **Pertanyaan Kritis untuk Dosen Pembimbing:**  
  *Apakah Bapak/Ibu memandang kombinasi FL + CL ini sudah tepat dan seimbang untuk skripsi S-1 Teknik Telekomunikasi, atau apakah dosen pembimbing lebih condong menitikberatkan pada sisi efisiensi komunikasi jaringan FL dibanding continual learning-nya?*
* **Dampak Risiko:**  
  Jika CL dihilangkan, novelty metodologis berkurang karena FL-NIDS statis sudah sangat banyak diteliti. Jika scope diperlebar ke arsitektur multi-task kompleks, risiko komputasi melampaui batas waktu kelulusan.

---

### 2. Rumusan Masalah (RM) & Evaluasi Dual-Domain

* **Keputusan Saat Ini:**  
  Dibatasi tegas pada dua rumusan masalah:  
  1. **RM 1:** Bagaimana kinerja deteksi intrusi model terdistribusi (FedAvg) dibandingkan model lokal mandiri pada distribusi data non-IID?  
  2. **RM 2:** Bagaimana efektivitas regularisasi EWC dalam mempertahankan retensi deteksi serangan lama (Task 1) saat mempelajari serangan baru (Task 2)?  
  Model lokal (E1a & E1b) dievaluasi melalui protokol *Dual-Domain* (diuji pada *Local Client Test Set* dan *Global Held-Out Test Set*).
* **Dasar Ilmiah & Bukti:**  
  Membandingkan model lokal hanya pada Global Test Set tidak adil (*unfair comparison*) karena Klien A tidak pernah melihat DoS dan Klien B tidak pernah melihat SSH. Dengan Dual-Domain, terbukti bahwa model lokal hanya unggul di kandangnya sendiri, sedangkan FedAvg + EWC mampu menggeneralisasi lintas domain.
* **Alternatif yang Dipertimbangkan:**  
  Menambahkan RM 3 tentang ketahanan model terhadap serangan siber adversarial (*adversarial attack* / *poisoning attack*) pada proses federasi.
* **Pertanyaan Kritis untuk Dosen Pembimbing:**  
  *Apakah dua rumusan masalah ini dipandang cukup tajam dan tuntas, atau apakah Bapak/Ibu menyarankan penambahan atau penggantian rumusan masalah yang lebih spesifik ke arah jaringan telekomunikasi?*
* **Dampak Risiko:**  
  Menambah RM keamanan komunikasi (misal: *poisoning defense*) akan mengubah fokus riset dari adaptasi deteksi ke kriptografi/keamanan federasi, yang membutuhkan perpanjangan waktu riset 2-3 bulan.

---

### 3. Pemilihan Dataset: CIC-IDS2017 (Senin, Selasa, Rabu) & Eksklusi Kamis-Jumat

* **Keputusan Saat Ini:**  
  Hanya menggunakan berkas rekaman hari **Senin** (Normal), **Selasa** (SSH-Patator), dan **Rabu** (DoS: Hulk, GoldenEye, slowloris, slowhttptest). Berkas hari **Kamis** dan **Jumat** dieksklusi secara total. Volume bersih: 1.520.488 flow.
* **Dasar Ilmiah & Bukti:**  
  1. *Kamis (Web Attacks & Infiltration):* Menderita cacat desinkronisasi timestamp pelabelan yang parah (Rosay et al., 2022) serta kelangkaan sampel mikro ekstrem (SQL Injection hanya 21 baris, Infiltration hanya 36 baris). Tidak memenuhi syarat daya statistik untuk split multi-klien dan 5 random seeds.  
  2. *Jumat (Botnet & PortScan):* PortScan adalah aktivitas *reconnaissance*, bukan serangan penetrasi aktif; botnet mengalami bug fragmentasi alur 1-paket CICFlowMeter (Dube, 2024).  
  3. *Senin-Rabu:* Menyediakan 100% kelas target penelitian dengan volume statistik 1,53 juta baris bersih.
* **Alternatif yang Dipertimbangkan:**  
  1. *Memakai seluruh 5 hari kerja CIC-IDS2017:* Menyertakan Kamis dan Jumat.  
  2. *Mengganti ke dataset lain (UNSW-NB15, TON_IoT, atau CSE-CIC-IDS2018):*  
* **Pertanyaan Kritis untuk Dosen Pembimbing:**  
  *Apakah Bapak/Ibu menyetujui pemangkasan hari Kamis dan Jumat berdasarkan bukti empiris literatur peer-reviewed tersebut, atau Bapak/Ibu menghendaki pengujian pada dataset tolok ukur yang berbeda/lebih baru?*
* **Dampak Risiko:**  
  Jika memakai hari Kamis/Jumat, model akan terdistorsi oleh noise pelabelan dan sampel 21 baris tidak valid secara statistik. Jika mengganti dataset ke TON_IoT atau CIC-IDS2018, seluruh pipeline audit praproses 62 fitur harus diulang dari awal (membutuhkan waktu tambahan 3-4 minggu).

---

### 4. Audit Fitur: Mengapa Membuang "Destination Port" dan Menetapkan 62 Fitur?

* **Keputusan Saat Ini:**  
  Dari 79 kolom mentah CIC-IDS2017:  
  1. Membuang 10 kolom konstan (variansi nol).  
  2. Membuang 5 kolom duplikat identik ($r = 1.0$).  
  3. **Membuang kolom `Destination Port` secara sengaja.**  
  Total input akhir dikunci pada **62 fitur numerik statistik bidirectional flow**.
* **Dasar Ilmiah & Bukti:**  
  Uji empiris baseline Decision Tree (5 seed) membuktikan:  
  - Hanya dengan 1 fitur port saja: Macro-F1 mencapai **96,44%**.  
  - Tanpa port (62 fitur): Macro-F1 mencapai **98,02%**.  
  Menyertakan nomor port memicu **shortcut learning** (model menghafal Port 22 pasti SSH dan Port 80 pasti DoS). Di dunia nyata, penyerang dapat menjalankan SSH pada port non-standar (misal port 2222). Model harus dipaksa belajar dari pola dinamika paket murni (panjang paket, IAT, TCP flags, window size).
* **Alternatif yang Dipertimbangkan:**  
  1. Tetap menyertakan nomor port sebagai fitur.  
  2. Menerapkan seleksi fitur agresif (misal: hanya mengambil 15-20 fitur teratas via Random Forest Importance / PCA).  
  3. Mengadopsi standar 43/48 fitur Sarhan et al. (2022).
* **Pertanyaan Kritis untuk Dosen Pembimbing:**  
  *Apakah Bapak/Ibu sepakat dengan argumentasi pembuangan nomor port demi mencegah shortcut learning? Apakah 62 fitur hasil pembersihan matematis (variansi nol + duplikat) ini sudah optimal, atau Bapak/Ibu menyarankan reduksi fitur lebih lanjut?*
* **Dampak Risiko:**  
  Jika port disertakan, penguji sidang yang kritis dapat menjatuhkan temuan riset karena model dianggap hanya menghafal port. Jika dilakukan seleksi fitur tambahan ke 15 fitur, beban komputasi menurun namun ada risiko kehilangan sinyal statistik flow minoritas.

---

### 5. Penanganan Ketimpangan Kelas (Imbalance 414:1): Weighted Loss vs. Undersampling/SMOTE

* **Keputusan Saat Ini:**  
  Menerapkan **Pilihan C: Weighted Cross-Entropy Loss** pada seluruh 1,53 juta baris data bersih terdeduplikasi, dipadukan dengan *Gradient Clipping* (norm $\le 1.0$). Tidak melakukan undersampling dan tidak melakukan oversampling SMOTE.
* **Dasar Ilmiah & Bukti:**  
  Perbandingan data bersih: Normal (1.323.561), DoS (193.708), SSH-Patator (3.219). Rasio ketimpangan $\approx 411 : 60 : 1$.  
  - *Undersampling ke 3.200 baris:* Membuang 99,6% data normal dan 98% data DoS, merusak variabilitas trafik nyata.  
  - *SMOTE:* Menghasilkan interpolasi sintetik titik data buatan yang tidak memiliki keterkaitan fisik dengan dinamika protokol TCP nyata, serta rentan menghasilkan flow yang tidak realistis pada arsitektur terdistribusi.  
  - *Weighted Loss:* Memberikan bobot penalti gradien lebih besar untuk kelas minoritas secara proporsional ($w_c = \frac{N}{|C| \cdot N_c}$) tanpa memanipulasi data mentah.
* **Alternatif yang Dipertimbangkan:**  
  1. Menggunakan Focal Loss.  
  2. Kombinasi random undersampling data normal menjadi 100.000 sampel dipadu SMOTE pada SSH.
* **Pertanyaan Kritis untuk Dosen Pembimbing:**  
  *Apakah dosen pembimbing menyetujui pendekatan Weighted Loss dengan mempertahankan 100% data riil, atau menyarankan pemangkasan undersampling terstratifikasi demi meringankan beban waktu pelatihan?*
* **Dampak Risiko:**  
  Mempertahankan 1,53 juta flow membutuhkan waktu komputasi pelatihan $\approx 35$-45 jam CPU pada 5 seed eksperimen. Jika disetujui subsampling moderat (misal 200 ribu sampel representatif), waktu pelatihan dapat dipangkas menjadi 5-8 jam.

---

### 6. Arsitektur Model: Mengapa Multi-Layer Perceptron (MLP) Kompak 6.211 Parameter?

* **Keputusan Saat Ini:**  
  Arsitektur Feedforward MLP kompak:  
  $$\text{Input}(62) \to \text{Linear}(64) + \text{ReLU} + \text{Dropout}(0.2) \to \text{Linear}(32) + \text{ReLU} \to \text{Linear}(3) + \text{Softmax}$$  
  Total parameter: **6.211 parameter** (bobot + bias). Komunikasi Flower: **49,69 KB per ronde** (uplink + downlink).
* **Dasar Ilmiah & Bukti:**  
  1. Data CIC-IDS2017 adalah ringkasan fitur statistik tabular per-flow, bukan sekuens waktu mentah paket demi paket (LSTM/RNN tidak relevan) dan tidak memiliki korelasi spasial piksel (1D-CNN tidak alami).  
  2. Perhitungan diagonal Matriks Informasi Fisher pada EWC membutuhkan komputasi gradien analitis orde dua yang stabil. Pada MLP 6.211 parameter, Fisher dapat dihitung cepat, deterministik, dan bebas dari isu *gradient vanishing*.  
  3. Ukuran payload parameter model sangat kecil ($<50$ KB/ronde), ideal untuk kanal transmisi sensor jaringan dengan bandwidth terbatas.
* **Alternatif yang Dipertimbangkan:**  
  1. Arsitektur 1D-CNN.  
  2. Arsitektur Tabular Transformer / FT-Transformer.  
  3. MLP yang lebih dalam (misal: 4-5 layer tersembunyi, 256 neuron).
* **Pertanyaan Kritis untuk Dosen Pembimbing:**  
  *Apakah MLP kompak 6.211 parameter ini dipandang memadai sebagai representasi model deteksi intrusi edge, atau Bapak/Ibu menghendaki arsitektur deep learning yang lebih kompleks?*
* **Dampak Risiko:**  
  Menggunakan model kompleks (seperti Transformer) akan melipatgandakan parameter menjadi $>200.000$. Hal ini menyebabkan komputasi Fisher EWC menjadi sangat berat di CPU, memperlambat pelatihan, serta meningkatkan beban bandwidth transmisi federasi.

---

### 7. Metode Continual Learning: Mengapa Regularisasi EWC dan Bukan Experience Replay?

* **Keputusan Saat Ini:**  
  Menggunakan **Elastic Weight Consolidation (EWC)** berbasis regularisasi kuadratik parameter prior ($L_{\text{total}} = L_{\text{new}} + \frac{\lambda}{2} \sum F_i (\theta_i - \theta^*_{1})^2$). Metode berbasis buffer memori data (*Experience Replay* / GEM / A-GEM) ditiadakan.
* **Dasar Ilmiah & Bukti:**  
  1. *Kepatuhan Privasi Data (Privacy Compliance):* Menyimpan buffer sampel paket/flow serangan masa lalu di media penyimpanan lokal sensor melanggar prinsip kepatuhan regulasi privasi data (GDPR / UU PDP No. 27/2022). EWC hanya menyimpan vektor nilai parameter $\theta^*$ dan vektor diagonal Fisher $F$, tanpa menyimpan satu byte pun sampel data mentah masa lalu.  
  2. *Efisiensi Memori Edge:* Jejak memori EWC konstan ($<25$ KB), sedangkan Replay Buffer membutuhkan ratusan MB untuk menampung riwayat data flow.
* **Alternatif yang Dipertimbangkan:**  
  1. Menyertakan Experience Replay sebagai baseline pembanding E2/E4.  
  2. Menggunakan Synaptic Intelligence (SI) atau Learning without Forgetting (LwF).
* **Pertanyaan Kritis untuk Dosen Pembimbing:**  
  *Apakah justifikasi kepatuhan privasi (tidak menyimpan buffer data mentah) dapat diterima sebagai dasar pemilihan tunggal EWC, atau Bapak/Ibu mewajibkan adanya metode Replay sebagai pembanding di eksperimen?*
* **Dampak Risiko:**  
  Jika Replay wajib ditambahkan, kompleksitas skenario eksperimen meningkat dan klaim *strict privacy preservation* pada sensor lokal harus dinegosiasikan ulang.

---

### 8. Desain Partisi Non-IID Dua Klien & Mitigasi "EWC Dilution Effect"

* **Keputusan Saat Ini:**  
  - **Klien A (Sensor Cabang/Admin):** Memegang Normal (50%) + SSH-Patator (100%) pada Fase 1. Pada Fase 2, Klien A hanya melatih data Normal sembari menahan bobot lama menggunakan penalti EWC lokal ($F_A$).  
  - **Klien B (Sensor Web/DMZ):** Hanya memiliki data Normal (50%) pada Fase 1 (tidak melatih SSH). Pada Fase 2, Klien B melatih Normal (50%) + DoS (100%).  
  - *Mitigasi Dilution:* Telah diakui secara eksplisit bahwa karena jumlah data Klien B ($n_B \approx 860K$) lebih besar dari Klien A ($n_A \approx 670K$), agregasi rata-rata tertimbang FedAvg berpotensi mengencerkan (*dilute*) gradien penalti EWC Klien A. Fenomena ini dijadikan hipotesis investigasi pada analisis sensitivitas $\lambda$.
* **Alternatif yang Dipertimbangkan:**  
  1. Membagi kelas serangan secara parsial ke kedua klien (misal Klien A memegang 90% SSH dan 10% DoS; Klien B memegang 10% SSH dan 90% DoS).  
  2. Menambah jumlah klien menjadi 3, 5, atau 10 klien federasi.
* **Pertanyaan Kritis untuk Dosen Pembimbing:**  
  *Apakah desain 2 klien dengan partisi ekstrem non-IID (Klien A spesialis SSH, Klien B spesialis DoS) sudah representatif untuk menguji batas ketahanan EWC, atau Bapak/Ibu menyarankan penambahan jumlah klien atau distribusi label-skew berbasis Dirichlet?*
* **Dampak Risiko:**  
  Menambah jumlah klien menjadi 5-10 klien akan melipatgandakan waktu komputasi pelatihan Flower dan membutuhkan re-partisi data tabular yang belum terpetakan.

---

### 9. Infrastruktur Pengujian: Protokol Dua Tahap & Peniadaan Injeksi Lalu Lintas Aktif (*Live Traffic*)

* **Keputusan Saat Ini:**  
  1. **Tahap 1 (Lokal):** Validasi algoritma, penalaan hiperparameter Bayesian via Optuna (30 trials), dan pengujian 5 seed acak secara in-memory menggunakan Flower Virtual Client Engine pada workstation pengembang.  
  2. **Tahap 2 (Private Cloud Cluster):** Deployment 3 node pada Proxmox VE (1 Server Agregator VM/LXC, 2 Klien Node VM/LXC) untuk mengukur latensi gRPC riil, konsumsi RAM, dan throughput inferensi.  
  3. **Peniadaan Live Traffic:** Injeksi paket aktif via Scapy/Hydra/Slowloris dan live sniffing via NFStream ditiadakan secara resmi. Seluruh node membaca partisi data offline dari penyimpanan lokal.
* **Dasar Ilmiah & Bukti:**  
  Injeksi paket aktif menimbulkan variabel pengganggu (*confounding factors*) yang tidak terkendali (seperti *packet loss*, *buffer overrun*, *NIC queue drops*, dan fluktuasi latensi jaringan virtual). Hal ini mengaburkan pembuktian matematis algoritma EWC dan FedAvg. Pengujian berbasis file offline menjamin determinisme 100% dan keterulangan ilmiah (*scientific reproducibility*).
* **Alternatif yang Dipertimbangkan:**  
  Menjalankan generator trafik fisik (Hydra dan Slowloris) secara langsung ke port VM defender.
* **Pertanyaan Kritis untuk Dosen Pembimbing:**  
  *Apakah dosen pembimbing sepakat bahwa pengujian berfokus pada data tolok ukur offline deterministik tanpa live packet sniffing, ataukah Bapak/Ibu menghendaki adanya demonstrasi inferensi pasif terhadap lalu lintas jaringan aktif?*
* **Dampak Risiko:**  
  Jika live traffic diwajibkan sebagai eksperimen inti, waktu pengerjaan akan tertunda signifikan karena harus mengonfigurasi port mirroring, TAP bridging, sinkronisasi flow extractor real-time, dan penanganan ketidakstabilan generator serangan.

---

### 10. Metrik Evaluasi: Mengapa Parameter QoS Jaringan Ditiadakan dan Diganti Communication Overhead FL?

* **Keputusan Saat Ini:**  
  1. **Metrik Deteksi (Machine Learning):** *Recall per-class* (khususnya Recall SSH sebagai indikator kelupaan utama), *Macro-Averaged F1-Score*, dan *Backward Transfer* (BWT).  
  2. **Metrik Sistem Komputasi & Jaringan Terdistribusi:**  
     - *Communication Overhead:* Payload bobot model via gRPC per ronde (24,84 KB satu arah, 49,69 KB per klien/ronde, 99,38 KB total agregator/ronde).  
     - *Memory Footprint:* Pemantauan RAM fisik kontainer selama kalkulasi Fisher EWC vs pelatihan standar.  
     - *Inference Latency:* Waktu inferensi per-flow dalam mikrodetik ($\mu s$) mengadopsi standar metodologi Skripsi FTEIC ITS (Rinandri, 2024).  
  3. **Parameter QoS Fisik Ditiadakan:** Metrik fisik *jitter*, *packet loss rate*, dan *delay transmisi kabel* resmi ditiadakan.
* **Dasar Ilmiah & Bukti:**  
  Karena skenario injeksi live traffic ditiadakan, metrik QoS fisik layer 2/3 tidak merepresentasikan kinerja algoritma deteksi, melainkan hanya mengukur performa virtual switch Linux. Sebagai gantinya, efisiensi jaringan terdistribusi diukur melalui penghematan *communication payload* model federasi dibanding transmisi data mentah.
* **Alternatif yang Dipertimbangkan:**  
  Mengukur metrik QoS fisik melalui simulasi Mininet atau emulasi batasan bandwidth Linux `tc (traffic control)`.
* **Pertanyaan Kritis untuk Dosen Pembimbing:**  
  *Apakah metrik communication payload gRPC dan latensi inferensi per flow ($\mu s$) ini sudah dipandang memadai untuk memenuhi aspek keilmuan Teknik Telekomunikasi, atau ada metrik telekomunikasi lain yang ingin ditambahkan?*
* **Dampak Risiko:**  
  Jika diwajibkan mengukur QoS fisik menggunakan `tc netem` (emulasi packet loss/delay), perlu perancangan matriks eksperimen baru untuk menguji ketahanan konvergensi FedAvg terhadap lossy networks.

---

### 11. Matriks Eksperimen Baku (E0 s.d. E4)

* **Keputusan Saat Ini:**  
  Mengunci matriks pengujian ke dalam 5 kelompok eksperimen (total 7 kondisi uji) dengan 5 random seeds (42, 43, 44, 45, 46):  
  - **E0 (Upper Bound):** *Centralized Joint Training* (semua kelas dilatih simultan terpusat).  
  - **E1a & E1b (Isolasi Lokal):** Model lokal Klien A mandiri dan Klien B mandiri (menjawab RM 1).  
  - **E2a & E2b (Lokal Sekuensial):** Pelatihan lokal sekuensial Task 1 $\to$ Task 2 (E2a: Naive Fine-Tuning; E2b: EWC terpusat).  
  - **E3 (FL Naive):** Pelatihan terdistribusi 2 klien tanpa continual learning (FedAvg Naive).  
  - **E4 (Sistem Usulan FL-CL):** Pelatihan terdistribusi 2 klien dengan regularisasi EWC (FedAvg + EWC).  
  - **E5 (Live Traffic):** Resmi ditiadakan dari target kelulusan wajib.
* **Dasar Ilmiah & Bukti:**  
  Matriks ini menyediakan perbandingan *apple-to-apple* yang secara langsung menjawab RM 1 (membandingkan E1 vs E3) dan RM 2 (membandingkan E2a vs E2b untuk lokal, serta E3 vs E4 untuk federasi), dengan E0 sebagai batas atas teoretis.
* **Alternatif yang Dipertimbangkan:**  
  1. Menambahkan algoritma agregasi federasi pembanding lain (misal FedProx).  
  2. Menambahkan metode continual learning pembanding lain (misal Synaptic Intelligence atau LwF).
* **Pertanyaan Kritis untuk Dosen Pembimbing:**  
  *Apakah matriks perbandingan E0 sampai E4 ini dinilai pas dan proporsional untuk skripsi sarjana, atau apakah dosen pembimbing mewajibkan adanya satu algoritma pembanding tambahan (misal FedProx)?*
* **Dampak Risiko:**  
  Menambahkan varian algoritma baru (seperti FedProx) akan menambah 30 jam waktu komputasi pelatihan dan penalaan hiperparameter baru, yang berisiko menunda penyelesaian naskah skripsi akhir.

---

## 📋 Lembar Konfirmasi & Keputusan Cepat Dosen Pembimbing

Gunakan tabel ringkas berikut saat sesi tatap muka untuk mencatat keputusan final dari dosen pembimbing:

| No | Komponen Desain Riset | Status Saat Ini | Rekomendasi / Arahan Dosen Pembimbing | Tindak Lanjut Naskah |
|---|---|---|---|---|
| **1** | Paradigma Riset | Integrasi FedAvg + EWC (FCL) | [  ] Disetujui Penuh<br>[  ] Revisi Fokus | |
| **2** | Rumusan Masalah | 2 RM (RM 1: FedAvg vs Lokal; RM 2: Mitigasi EWC) | [  ] Disetujui Penuh<br>[  ] Tambah/Ubah RM | |
| **3** | Dataset & Hari | CIC-IDS2017 (Senin, Selasa, Rabu saja) | [  ] Setuju Eksklusi Kamis-Jumat<br>[  ] Wajib Ganti Dataset | |
| **4** | Fitur Input | 62 Fitur (Eksklusi Port Tujuan) | [  ] Setuju Buang Port<br>[  ] Port Wajib Ada / Reduksi Lagi | |
| **5** | Imbalance Data | Weighted Cross-Entropy (Semua Data Asli 1,53M) | [  ] Setuju Weighted Loss<br>[  ] Wajib Subsampling / SMOTE | |
| **6** | Arsitektur Model | Single MLP Kompak (6.211 Parameter) | [  ] Setuju MLP Kompak<br>[  ] Minta Deep Learning Lain | |
| **7** | Metode CL | EWC Murni (Tanpa Buffer Replay) | [  ] Setuju EWC (Patuh Privasi)<br>[  ] Minta Replay Pembanding | |
| **8** | Desain Klien | 2 Klien Non-IID Ekstrem (SSH vs DoS) | [  ] Setuju 2 Klien Ekstrem<br>[  ] Minta Tambah Klien / Dirichlet | |
| **9** | Testbed Lingkungan | Dua Tahap (Lokal $\to$ Proxmox VE), Tanpa Live Sniffing | [  ] Setuju Tanpa Live Traffic<br>[  ] Minta Demo Injeksi Aktif | |
| **10**| Metrik Evaluasi | Macro-F1, BWT, Payload gRPC, Latensi ($\mu s$) | [  ] Setuju Metrik Saat Ini<br>[  ] Tambah Parameter QoS Fisik | |
| **11**| Matriks Uji Coba | E0, E1a/b, E2a/b, E3, E4 (Total 7 Kondisi, 5 Seed) | [  ] Setuju Matriks E0-E4<br>[  ] Tambah Algoritma Pembanding | |

---

*Dokumen ini disiapkan untuk menjaga integritas metodologis penelitian Tugas Akhir dan menjamin kelancaran sidang seminar proposal di Departemen Teknik Elektro FTEIC ITS.*
