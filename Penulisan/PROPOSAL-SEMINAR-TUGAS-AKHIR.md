<!--
================================================================================
PROPOSAL TUGAS AKHIR MAHASISWA PROGRAM STUDI S-1 TEKNIK TELEKOMUNIKASI
DEPARTEMEN TEKNIK ELEKTRO
FAKULTAS TEKNOLOGI ELEKTRO DAN INFORMATIKA CERDAS (FTEIC)
INSTITUT TEKNOLOGI SEPULUH NOPEMBER (ITS) SURABAYA

STANDAR FORMAT: SK REKTOR ITS NO. 280/IT2/T/HK.00.01/2022
Ukuran Kertas: A4 HVS 80g | Spasi: 1 (Single)
Margin: Atas 3.0 cm, Bawah 2.5 cm, Kiri 3.0 cm, Kanan 2.0 cm
Font: Times New Roman 12 pt (Judul 14-18 pt Bold)
Sistem Penomoran Halaman:
- Halaman Awal: Romawi kecil (i, ii, iii, dst.) di kanan bawah
- Halaman Isi s.d. Daftar Pustaka: Angka Arab (1, 2, 3, dst.) di kanan bawah
================================================================================
-->


<!--
FORMAT SAMPUL PROPOSAL TUGAS AKHIR ITS (SK Rektor No. 280/IT2/T/HK.00.01/2022 - Lampiran 1)
Kertas: A4 HVS 80g | Spasi: 1 | Margin: Atas 3 cm, Bawah 2.5 cm, Kiri 3 cm, Kanan 2 cm
Tipografi: Trebuchet MS / Times New Roman, Bold, Center
-->

<div align="center">

<img src="../Aset/logo_its.png" alt="Logo ITS" width="120" onerror="this.src='https://www.its.ac.id/wp-content/uploads/2020/07/Lambang-ITS-2-300x300.png'"/>

<br><br>

### **PROPOSAL TUGAS AKHIR - EC234701**

<br>

## **ANALISIS KINERJA DETEKSI NETWORK TRAFFIC INTRUSION MENGGUNAKAN METODE FEDERATED-CONTINUAL LEARNING PADA TESTBED PRIVATE CLOUD SERVER**
### *Studi Pengaruh Elastic Weight Consolidation dan Federated Averaging pada Distribusi Data Non-IID Dua Client*

<br><br>

**RAFLI ALIF IHZA HARTONO**  
**NRP 5048231003**  

<br><br>

**Dosen Pembimbing:**  
**Dr. Ir. Achmad Affandi, DEA.**  
**NIP 196510141990021001**  

<br><br><br>

**Program Studi S-1 Teknik Telekomunikasi**  
**Departemen Teknik Elektro**  
**Fakultas Teknologi Elektro dan Informatika Cerdas**  
**INSTITUT TEKNOLOGI SEPULUH NOPEMBER**  
**SURABAYA**  
**2026**  

</div>

\newpage

<!--
FORMAT LEMBAR PENGESAHAN PROPOSAL TUGAS AKHIR ITS (SK Rektor No. 280/IT2/T/HK.00.01/2022 - Lampiran 2)
-->

<div align="center">

## **LEMBAR PENGESAHAN**

<br>

### **ANALISIS KINERJA DETEKSI NETWORK TRAFFIC INTRUSION MENGGUNAKAN METODE FEDERATED-CONTINUAL LEARNING PADA TESTBED PRIVATE CLOUD SERVER**
#### *Studi Pengaruh Elastic Weight Consolidation dan Federated Averaging pada Distribusi Data Non-IID Dua Client*

<br>

**PROPOSAL TUGAS AKHIR**  
Diajukan untuk memenuhi salah satu syarat  
memperoleh gelar Sarjana Teknik (S.T.) pada  
Program Studi S-1 Teknik Telekomunikasi  
Departemen Teknik Elektro  
Fakultas Teknologi Elektro dan Informatika Cerdas  
Institut Teknologi Sepuluh Nopember  

<br>

Oleh:  
**RAFLI ALIF IHZA HARTONO**  
NRP. 5048231003  

<br>

Disetujui oleh Tim Penguji Proposal Tugas Akhir:

</div>

<br>

1. **Dr. Ir. Achmad Affandi, DEA.**  
   NIP. 196510141990021001  
   *(Pembimbing)* : ............................................................

<br>

2. **Dosen Penguji 1**  
   NIP. ............................................................  
   *(Penguji)* : ............................................................

<br>

3. **Dosen Penguji 2**  
   NIP. ............................................................  
   *(Penguji)* : ............................................................

<br>

4. **Dosen Penguji 3**  
   NIP. ............................................................  
   *(Penguji)* : ............................................................

<br><br>

<div align="center">

**SURABAYA**  
**Oktober, 2026**

</div>

\newpage

# ABSTRAK

**ANALISIS KINERJA DETEKSI NETWORK TRAFFIC INTRUSION MENGGUNAKAN METODE FEDERATED-CONTINUAL LEARNING PADA TESTBED PRIVATE CLOUD SERVER**  
*(Studi Pengaruh Elastic Weight Consolidation dan Federated Averaging pada Distribusi Data Non-IID Dua Client)*

**Nama Mahasiswa / NRP** : Rafli Alif Ihza Hartono / 5048231003  
**Departemen** : Teknik Elektro (Program Studi S-1 Teknik Telekomunikasi) FTEIC - ITS  
**Dosen Pembimbing** : Dr. Ir. Achmad Affandi, DEA.  

#### Abstrak
Eskalasi serangan siber menuntut *Network Intrusion Detection System* (NIDS) mampu mendeteksi variasi ancaman baru tanpa mengorbankan privasi data pengguna. Namun, sentralisasi trafik melanggar regulasi privasi, sedangkan model terdistribusi sekuensial rentan mengalami *catastrophic forgetting* terhadap ancaman terdahulu. Penelitian ini bertujuan menganalisis kinerja deteksi intrusi berbasis *Federated Continual Learning* yang mengintegrasikan *Federated Averaging* (FedAvg) dan *Elastic Weight Consolidation* (EWC) pada data non-IID. Pengujian menggunakan dataset CIC-IDS2017 bersih (Senin-Rabu) dengan mengeksklusi *Destination Port* guna mencegah *shortcut learning* dan menghasilkan 62 fitur statistik numerik. Seluruh 1.529.677 aliran dipertahankan menggunakan *Weighted Cross-Entropy Loss* dan *gradient clipping* untuk memitigasi ketimpangan kelas ekstrem antara Normal, SSH-Patator, dan DoS. Skenario *Class-Incremental Learning* disimulasikan pada dua klien dengan partisi kelas Normal 50/50. Model klasifikasi menggunakan *Multilayer Perceptron* (MLP) kompak tiga lapis berkapasitas 6.211 parameter guna efisiensi komputasi *edge*. Klien lokal menghitung Matriks Informasi Fisher diagonal untuk memproteksi bobot kritis tugas terdahulu sebelum agregasi global Flower. Penerapan EWC diharapkan mampu menekan *catastrophic forgetting* dengan mempertahankan skor Macro-F1 dan *Backward Transfer* yang stabil mendekati nol. Penelitian ini berkontribusi menyediakan arsitektur NIDS adaptif yang aman privasi dan hemat bandwidth untuk gerbang jaringan enterprise.

**Kata kunci:** *Catastrophic Forgetting*, *Continual Learning*, *Elastic Weight Consolidation*, *Federated Learning*, *Network Intrusion Detection System*, *Non-IID*.

---

# ABSTRACT

**PERFORMANCE ANALYSIS OF NETWORK TRAFFIC INTRUSION DETECTION USING FEDERATED-CONTINUAL LEARNING ON A PRIVATE CLOUD SERVER TESTBED**  
*(Study on the Effects of Elastic Weight Consolidation and Federated Averaging under Two-Client Non-IID Data Distribution)*

**Student Name / NRP** : Rafli Alif Ihza Hartono / 5048231003  
**Department** : Electrical Engineering (Telecommunication Engineering Study Program) FTEIC - ITS  
**Advisor** : Dr. Ir. Achmad Affandi, DEA.  

#### Abstract
Escalating cyber threats require Network Intrusion Detection Systems (NIDS) to detect emerging attack variations without compromising user data privacy. However, centralizing raw traffic violates privacy regulations, while sequentially trained distributed models are prone to catastrophic forgetting regarding prior threats. This research aims to analyze intrusion detection performance using Federated Continual Learning integrating Federated Averaging (FedAvg) and Elastic Weight Consolidation (EWC) under non-IID data. Testing utilizes clean CIC-IDS2017 datasets (Monday-Wednesday) excluding Destination Port to prevent shortcut learning, yielding 62 clean numerical features. All 1,529,677 flows are preserved using Weighted Cross-Entropy Loss and gradient clipping to handle extreme class imbalance between Normal, SSH-Patator, and DoS. The Class-Incremental Learning scenario is simulated across two clients with a 50/50 Normal partition. The classification model adopts a compact three-layer Multilayer Perceptron (MLP) with 6,211 parameters for edge computational efficiency. Local clients compute diagonal Fisher Information Matrices to protect critical parameters of prior tasks before global Flower aggregation. Applying EWC is expected to mitigate catastrophic forgetting by sustaining stable Macro-F1 scores and near-zero Backward Transfer. This research contributes an adaptive, privacy-preserving, and bandwidth-efficient NIDS architecture for enterprise network security gateways.

**Keywords:** *Catastrophic Forgetting*, *Continual Learning*, *Elastic Weight Consolidation*, *Federated Learning*, *Network Intrusion Detection System*, *Non-IID*.

\newpage

# DAFTAR ISI

<br>

**LEMBAR PENGESAHAN** ............................................................................................................ ii  
**ABSTRAK** ................................................................................................................................... iii  
**ABSTRACT** ................................................................................................................................. iv  
**DAFTAR ISI** ................................................................................................................................. v  
**DAFTAR GAMBAR** ................................................................................................................... vii  
**DAFTAR TABEL** ....................................................................................................................... viii  
**DAFTAR SINGKATAN** .............................................................................................................. ix  

<br>

**BAB 1 PENDAHULUAN** ............................................................................................................... 1  
1.1 Latar Belakang .......................................................................................................................... 1  
1.2 Rumusan Masalah ...................................................................................................................... 3  
1.3 Batasan Masalah ....................................................................................................................... 3  
1.4 Tujuan ...................................................................................................................................... 4  
1.5 Manfaat .................................................................................................................................... 5  

**BAB 2 TINJAUAN PUSTAKA** ....................................................................................................... 6  
2.1 Keamanan Jaringan ................................................................................................................. 6  
2.2 Serangan Siber ................................................................................................................... 7  
2.3 Penelitian Terdahulu ............................................................................................................ 8  
2.4 Kerangka Teoretis Continual Learning ................................................................................. 10  
2.5 Kerangka Teoretis Federated Learning ................................................................................. 12  
2.6 Posisi Sintesis: Integrasi FedAvg dan EWC Lokal ................................................................. 13  
2.7 Deteksi Intrusi ................................................................................................................. 14  
2.8 PyTorch ......................................................................................................................... 15  
2.9 Flower .......................................................................................................................... 15  
2.10 Multilayer Perceptron .......................................................................................................... 16  
2.11 Regularisasi EWC ............................................................................................................... 17  
2.12 Dataset .......................................................................................................................... 18  
2.13 Evaluasi Metrik ................................................................................................................. 20  
2.14 Hyperparameter Tuning ...................................................................................................... 21  
2.15 Optimizer .......................................................................................................................... 22  
2.16 Fungsi Aktivasi ................................................................................................................. 23  
**BAB 3 METODOLOGI** ................................................................................................................ 23  
3.1 Metode yang Digunakan .......................................................................................................... 23  
3.2 Bahan dan Peralatan yang Digunakan ....................................................................................... 25  
3.2.1 Bahan Penelitian .................................................................................................................... 25  
3.2.2 Peralatan Penelitian ............................................................................................................... 25  
3.3 Urutan Pelaksanaan Penelitian ................................................................................................. 26  
3.3.1 Praproses Data dan Ekstraksi 62 Fitur Numerik .................................................................... 26  
3.3.2 Pengembangan Model Dasar MLP Kompak .......................................................................... 29  
3.3.3 Integrasi Sistem Usulan: FedAvg dan EWC pada Lingkungan Terdistribusi ......................... 30  
3.3.4 Penyetelan Hiperparameter Bayesian (Optuna TPE) ............................................................. 31  
3.3.5 Matriks Skenario Pengujian Komparatif E0-E4 .................................................................... 32  
3.3.6 Mekanisme Evaluasi Multi-Seed dan Profiling Komputasi ................................................... 33  
3.4 Jadwal Pelaksanaan Penelitian ................................................................................................ 34  

**DAFTAR PUSTAKA** ................................................................................................................... 35  

---

# DAFTAR GAMBAR

<br>

Gambar 2.1 Model CIA Triad Keamanan Informasi ............................................................................ 6  
Gambar 2.2 Taksonomi Pendekatan Mitigasi Catastrophic Forgetting pada Continual Learning ...... 10  
Gambar 2.3 Siklus Pelatihan dan Agregasi Bobot pada Federated Learning (FedAvg) .................... 12  
Gambar 2.4 Perbandingan Topologi Arsitektur Penempatan NIDS dan HIDS ................................ 14  
Gambar 2.5 Struktur Arsitektur Jaringan Multilayer Perceptron (MLP) ............................................ 16  
Gambar 2.6 Mekanisme Regularisasi EWC Membatasi Pergeseran Bobot Kritis pada Kontur Kerugian 17  
Gambar 2.7 Struktur Dasar Confusion Matrix untuk Evaluasi Deteksi Biner dan Multi-kelas .......... 20  
Gambar 2.8 Pemodelan Distribusi Ketidakpastian pada Optimasi Bayesian ..................................... 21  
Gambar 3.1 Arsitektur Penempatan Sensor NIDS Terdistribusi dalam Jaringan Enterprise ............. 23  
Gambar 3.2 Fishbone Diagram Identifikasi Tantangan NIDS Terdistribusi ..................................... 24  
Gambar 3.3 Diagram Alir Urutan Pelaksanaan Penelitian .............................................................. 26  
Gambar 3.4 Diagram Alur Global Data Preprocessing ................................................................... 27  
Gambar 3.5 Arsitektur Sistem Federated Continual Learning yang Diimplementasikan ................. 30  
Gambar 3.6 Diagram Alir Skenario Pengujian Sekuensial Non-IID ................................................. 32  

---

# DAFTAR TABEL

<br>

Tabel 2.1 Perbandingan Penelitian Terdahulu dalam Domain FL, Continual Learning, dan NIDS ..... 8  
Tabel 2.2 Taksonomi dan Perbandingan Menyeluruh Metode Continual Learning (CL) .............. 11  
Tabel 2.3 Taksonomi dan Perbandingan Menyeluruh Metode Federated Learning (FL) ............... 13  
Tabel 3.1 Spesifikasi Lingkungan Perangkat Keras dan Perangkat Lunak ...................................... 25  
Tabel 3.2 Ringkasan 62 Fitur Statistik Numerik Aliran Bersih CIC-IDS2017 ................................. 28  
Tabel 3.3 Alokasi Partisi Data Non-IID dan Peran Klien pada Setiap Fase Pembelajaran ............ 29  
Tabel 3.4 Konfigurasi Parameter Pelatihan Baseline dan Ruang Pencarian Hiperparameter ..... 31  
Tabel 3.5 Matriks Skenario Pengujian Eksperimen E0-E4 .............................................................. 32  
Tabel 3.6 Jadwal Pelaksanaan Penelitian Tugas Akhir ................................................................... 34  

---

# DAFTAR SINGKATAN

<br>

| Singkatan | Kepanjangan / Definisi |
|---|---|
| **ABDS** | *Anomaly-Based Detection System* |
| **AdamW** | *Adam with Decoupled Weight Decay* |
| **AUC** | *Area Under the Curve* |
| **BWT** | *Backward Transfer* |
| **CIA** | *Confidentiality, Integrity, and Availability* |
| **CIC** | *Canadian Institute for Cybersecurity* |
| **CL** | *Continual Learning* |
| **CPU** | *Central Processing Unit* |
| **DMZ** | *Demilitarized Zone* |
| **DoS** | *Denial of Service* |
| **EWC** | *Elastic Weight Consolidation* |
| **FCL** | *Federated Continual Learning* |
| **FedAvg** | *Federated Averaging* |
| **FIM** | *Fisher Information Matrix* |
| **FL** | *Federated Learning* |
| **FN** | *False Negative* |
| **FP** | *False Positive* |
| **FNR** | *False Negative Rate* |
| **FPR** | *False Positive Rate* |
| **GDPR** | *General Data Protection Regulation* |
| **GPU** | *Graphics Processing Unit* |
| **gRPC** | *Google Remote Procedure Call* |
| **HIDS** | *Host-Based Intrusion Detection System* |
| **IAT** | *Inter-Arrival Time* |
| **IID** | *Independent and Identically Distributed* |
| **IP** | *Internet Protocol* |
| **ITS** | Institut Teknologi Sepuluh Nopember |
| **MLP** | *Multilayer Perceptron* |
| **NIC** | *Network Interface Card* |
| **NIDS** | *Network Intrusion Detection System* |
| **Non-IID** | *Non-Independent and Identically Distributed* |
| **ONNX** | *Open Neural Network Exchange* |
| **PR-AUC** | *Precision-Recall Area Under Curve* |
| **PVE** | *Proxmox Virtual Environment* |
| **RAM** | *Random Access Memory* |
| **ReLU** | *Rectified Linear Unit* |
| **ROC-AUC** | *Receiver Operating Characteristic - Area Under Curve* |
| **SGD** | *Stochastic Gradient Descent* |
| **SIDS** | *Signature-Based Intrusion Detection System* |
| **SIEM** | *Security Information and Event Management* |
| **SMOTE** | *Synthetic Minority Over-sampling Technique* |
| **SSH** | *Secure Shell* |
| **TAP** | *Test Access Point* |
| **TCP** | *Transmission Control Protocol* |
| **TN** | *True Negative* |
| **TP** | *True Positive* |
| **TPE** | *Tree-structured Parzen Estimator* |
| **UDP** | *User Datagram Protocol* |
| **UU PDP** | Undang-Undang Pelindungan Data Pribadi |

\newpage

# BAB 1 PENDAHULUAN

## 1.1 Latar Belakang

Perkembangan teknologi informasi dan transformasi digital yang kian pesat telah meningkatkan ketergantungan infrastruktur enterprise, institusi publik, dan layanan perbankan terhadap integritas jaringan komputer. Namun, eskalasi keterhubungan ini diiringi oleh lonjakan volume dan kompleksitas ancaman siber (*cyber threats*). Menurut laporan global *Check Point Research*, terjadi kenaikan serangan siber mingguan sebesar 47% secara tahun-ke-tahun (*year-over-year*) per organisasi di seluruh dunia, dengan sektor telekomunikasi, pendidikan, dan infrastruktur kritis menjadi sasaran eksploitasi utama[1]. Selain itu, laporan *FBI Internet Crime Complaint Center* (IC3) mencatat total kerugian ekonomi akibat pengaduan kejahatan siber di Amerika Serikat telah melampaui 12,5 miliar dolar pada laporan tahunan IC3, dengan vektor serangan intrusi jaringan seperti eksploitasi *brute-force* autentikasi (SSH) dan serangan penolakan layanan (*Denial of Service* / DoS) tetap mendominasi spektrum insiden keamanan operasional[2]. Peningkatan baik dari sisi jumlah maupun kompleksitas teknik serangan ini menuntut sistem pertahanan yang adaptif dan mampu mengamankan jaringan secara berkesinambungan.

Dalam menjaga integritas, kerahasiaan (*confidentiality*), dan ketersediaan (*availability*) aset jaringan, *Network Intrusion Detection System* (NIDS) bertindak sebagai garda pertahanan utama untuk memantau, mendeteksi, dan mengklasifikasikan anomali lalu lintas data secara *near real-time*. Pendekatan NIDS konvensional berbasis *signature* (*Signature-Based Intrusion Detection System* / SIDS) bekerja dengan mencocokkan pola aktivitas terhadap basis data tanda tangan serangan yang telah diketahui, namun rentan mengalami kegagalan deteksi terhadap varian serangan baru (*zero-day attacks*). Sebaliknya, sistem deteksi berbasis anomali menggunakan *Machine Learning* (ML) dan *Deep Learning* (DL) memiliki keunggulan adaptif dalam mengekstraksi representasi statistik aliran data (*bidirectional network flows*) guna mengenali anomali lalu lintas secara otomatis.

Meskipun model pembelajaran mesin terpusat (*centralized learning*) menunjukkan akurasi deteksi yang tinggi, paradigma pengumpulan data secara sentral menghadapi dua tantangan fundamental di dunia nyata, yaitu regulasi privasi data dan keterbatasan lebar pita (*bandwidth*). Lalu lintas jaringan memuat data internal yang sangat sensitif, seperti kredensial, identitas pengguna, dan struktur topologi intranet. Memusatkan rekaman paket mentah (*raw pcap* atau *flow logs*) dari berbagai cabang subnet ke satu server sentral berpotensi melanggar regulasi kepatuhan privasi data, seperti Undang-Undang Pelindungan Data Pribadi (UU PDP No. 27/2022) di Indonesia dan GDPR di tingkat global, serta menimbulkan risiko kerentanan titik kegagalan tunggal (*single point of failure*) terhadap insiden kebocoran data. Di samping itu, mentransfer jutaan aliran paket jaringan berskala gigabita secara berkesinambungan ke server analitik sentral menimbulkan *bandwidth bottleneck* yang membebani kapasitas jaringan operasional enterprise.

Untuk mengatasi batasan privasi dan transmisi data tersebut, paradigma *Federated Learning* (FL), khususnya algoritma *Federated Averaging* (FedAvg), muncul sebagai arsitektur pelatihan terdistribusi yang menjanjikan[3]. Melalui FL, setiap node sensor (klien) melatih model deteksi intrusi secara lokal menggunakan data lalu lintas di perimeter jaringannya sendiri. Node klien kemudian hanya mengirimkan pembaruan parameter bobot model (*gradient/weight updates*) ke server agregator terpusat, tanpa pernah membagikan data lalu lintas mentah.

Kendati demikian, implementasi FL pada domain deteksi intrusi jaringan memicu tantangan baru yang signifikan. Pada kondisi operasional nyata, distribusi data lalu lintas antar-node sensor bersifat sangat heterogen atau *non-Identical and Independently Distributed* (non-IID). Sebagai contoh, node sensor di perimeter subnet server autentikasi internal dominan menghadapi serangan *brute-force* SSH, sedangkan node sensor di zona publik (*Demilitarized Zone* / DMZ) dominan menghadapi serangan volumetrik web DoS (*label skew*). Zhao dkk. menunjukkan secara analitis dan empiris bahwa heterogenitas non-IID memicu divergensi bobot lokal (*weight divergence*) yang drastis, sehingga agregasi rata-rata konvensional pada FedAvg rentan mengalami degradasi akurasi yang signifikan[4].

Tantangan ini diperparah oleh dinamika temporal dari serangan jaringan. Serangan siber tidak terjadi secara serentak, melainkan muncul secara berkala dan berurutan dari waktu ke waktu (*continuous streaming data*). Ketika model deteksi intrusi dilatih menggunakan kelas serangan baru (seperti DoS pada Task 2) setelah sebelumnya mempelajari kelas serangan terdahulu (seperti SSH-Patator pada Task 1), pembaruan bobot jaringan saraf tiruan cenderung menimpa representasi laten yang telah dipelajari sebelumnya. Fenomena ini dikenal dalam literatur *Continual Learning* (CL) sebagai **catastrophic forgetting**[5]. Akibatnya, sistem IDS mengalami penurunan drastis pada kemampuan mengenali kembali serangan lawas yang sewaktu-waktu dapat dilancarkan kembali oleh penyerang.

Untuk menanggulangi *catastrophic forgetting*, salah satu pendekatan yang paling elegan dan ramah privasi adalah metode berbasis regularisasi parameter, yaitu **Elastic Weight Consolidation (EWC)**. EWC mengkalkulasi signifikansi parameter bobot terhadap tugas masa lalu menggunakan Matriks Informasi Fisher diagonal (*Fisher Information Matrix*). Saat model mempelajari tugas baru, EWC menambahkan fungsi penalti kuadratik yang mengekang perubahan bobot-bobot krusial tersebut. Berbeda dari metode *Experience Replay* yang mengharuskan penyimpanan *buffer* sampel data mentah di memori lokal (yang berpotensi melanggar privasi dan membebani kapasitas RAM perangkat sensor *edge*), EWC bekerja murni pada ruang parameter model, menjadikannya solusi ideal untuk integrasi *Federated Continual Learning* (FCL)[5].

Penelitian mengenai integrasi FL dan CL pada NIDS di bawah distribusi non-IID saat ini masih berada pada tahap eksplorasi awal dan menghadapi tantangan metodologis yang krusial. Sebagaimana diidentifikasi dalam survei literatur mutakhir oleh Hernandez-Ramos dkk.[31] serta Buyuktanir dkk.[32], sebagian studi FL-NIDS mengasumsikan data terdistribusi secara identik (IID), mengabaikan fenomena kebocoran fitur (*shortcut learning*) akibat penggunaan nomor port layanan, atau menerapkan pemangkasan data (*undersampling*) buatan yang mengaburkan realitas operasional ketimpangan kelas (*class imbalance*). 

Oleh karena itu, penelitian tugas akhir ini berfokus pada **analisis kinerja deteksi *network traffic intrusion* menggunakan metode *Federated-Continual Learning* pada *testbed private cloud server*, dengan studi pengaruh *Elastic Weight Consolidation* (EWC) dan *Federated Averaging* (FedAvg) pada distribusi data non-IID dua *client* guna memitigasi *catastrophic forgetting***. Penelitian ini menggunakan dataset tolok ukur resmi CIC-IDS2017 yang dikurasi secara ketat bebas dari kebocoran fitur *Destination Port*, mempertahankan representasi sebaran data bersih melalui fungsi *Weighted Cross-Entropy Loss*, serta dievaluasi melintasi lima *random seed* independen untuk memperkirakan variabilitas performa dan stabilitas model secara empiris.

---

## 1.2 Rumusan Masalah

Berdasarkan latar belakang yang telah diuraikan, maka rumusan masalah dalam penelitian tugas akhir ini dirumuskan dalam tiga tingkatan hierarkis sebagai berikut:
1. Bagaimana rancang bangun dan kelayakan kerangka kerja *Federated-Continual Learning* (FCL) yang mengintegrasikan algoritma agregasi *Federated Averaging* (FedAvg) dan regularisasi parameter lokal *Elastic Weight Consolidation* (EWC) dalam mendeteksi *network traffic intrusion* secara adaptif dan terdistribusi?
2. Bagaimana kinerja deteksi intrusi model yang dilatih secara terdistribusi (*Federated Averaging* / FedAvg) dibandingkan dengan model yang dilatih secara lokal pada masing-masing klien dengan distribusi data non-IID?
3. Bagaimana pengaruh metode *Elastic Weight Consolidation* (EWC) terhadap mitigasi *catastrophic forgetting* saat model mempelajari kelas serangan baru secara sekuensial, baik pada skenario pelatihan lokal maupun terdistribusi (FedAvg + EWC)?

---

## 1.3 Batasan Masalah

Dalam merampungkan tugas akhir ini, penulis mengonsep batasan ruang lingkup masalah untuk memberikan arah yang lebih terfokus. Berikut merupakan batasan-batasan masalah yang diberikan:

1. Metrik evaluasi yang digunakan meliputi *Macro-averaged F1-Score*, *Precision*, *Recall*, *Accuracy*, *Backward Transfer* (BWT), waktu inferensi per aliran data, alokasi memori RAM *footprint*, dan *communication payload*.
2. Model deteksi intrusi yang dikembangkan berbasis arsitektur *Multilayer Perceptron* (MLP) kompak tiga lapis dengan masukan 62 fitur statistik numerik bersih.
3. Penelitian hanya menggunakan dataset publik *offline tabular flow* CIC-IDS2017 pada rekaman hari Senin (Normal murni), Selasa (SSH-Patator), dan Rabu (DoS GoldenEye, Hulk, slowloris, Slowhttptest). Berkas rekaman hari Kamis dan Jumat dieksklusi secara sengaja karena kelas serangan target (SSH-Patator dan DoS) hanya terdapat pada hari Selasa dan Rabu. Alur serangan FTP-Patator (Selasa) dan Heartbleed (Rabu) juga dieksklusi guna memfokuskan investigasi pada tiga kelas representatif (Normal, SSH-Patator, dan DoS) dengan eliminasi atribut `Destination Port` serta fitur bervariansi nol untuk mencegah bias *shortcut learning*.
4. Pendekatan pembelajaran berkelanjutan (*Continual Learning*) dibatasi pada skenario *Class-Incremental Learning* (Class-IL) tanpa penyediaan Task-ID saat inferensi, dengan metode mitigasi lupa berbasis *Elastic Weight Consolidation* (EWC).
5. Topologi pembelajaran terdistribusi menggunakan algoritma *Federated Averaging* (FedAvg) dengan kerangka kerja Flower, yang memodelkan 2 *node* klien terisolasi non-IID (Klien A: sensor subnet internal dengan serangan SSH-Patator, dan Klien B: sensor DMZ dengan serangan DoS) serta 1 server agregator global yang dilatih melintasi dua fase sekuensial.
6. Implementasi eksperimen dievaluasi melintasi 5 *random seed* independen (42, 43, 44, 45, dan 46) untuk mengukur variabilitas dan dispersi performa konvergensi model terhadap inisialisasi bobot dan partisi data.
7. Profil efisiensi komputasi model (latensi inferensi per alur menggunakan penanda waktu beresolusi nanodetik, jejak alokasi memori RAM instans klien, dan payload komunikasi jaringan) dievaluasi pada lingkungan komputasi prosesor serta testbed *private cloud server* berbasis klaster Proxmox VE sebagai analisis kelayakan operasional.
8. Penelitian ini tidak mencakup penangkapan paket langsung (*live packet capture*), injeksi lalu lintas aktif, maupun pengujian langsung di jaringan produksi enterprise.

---

## 1.4 Tujuan

Penelitian ini bertujuan untuk:
1. Merancang dan menguji kelayakan kerangka kerja *Federated-Continual Learning* (FCL) yang mengintegrasikan algoritma *Federated Averaging* (FedAvg) dan regularisasi *Elastic Weight Consolidation* (EWC) untuk mendeteksi *network traffic intrusion* pada lingkungan *testbed private cloud server*.
2. Menganalisis kinerja deteksi intrusi model yang dilatih secara terdistribusi (*Federated Averaging* / FedAvg) dibandingkan dengan model yang dilatih secara lokal pada masing-masing klien dengan distribusi data non-IID.
3. Menganalisis pengaruh metode *Elastic Weight Consolidation* (EWC) terhadap mitigasi *catastrophic forgetting* saat mempelajari kelas serangan baru secara sekuensial, baik pada skenario pelatihan lokal maupun terdistribusi (FedAvg + EWC), serta mengevaluasi efisiensi komputasi model (latensi inferensi per aliran data dalam mikrodetik, alokasi memori RAM *footprint*, dan *communication payload*) sebagai analisis pendukung penerapan pada *testbed private cloud server*.

---

## 1.5 Manfaat

Pelaksanaan penelitian ini diharapkan dapat memberikan kontribusi dan manfaat teoretis maupun praktis sebagai berikut:
1. **Manfaat Teoretis (Akademik):**
   - Memberikan kontribusi empiris dan analitis mengenai perilaku interaksi antara algoritma agregasi Federated Learning (FedAvg) dan regularisasi Continual Learning (EWC) pada domain keamanan siber di bawah kondisi heterogenitas data non-IID.
   - Memperkaya literatur NIDS mengenai metodologi evaluasi bebas bias *shortcut learning* melalui eliminasi fitur nomor port dan pengujian berbasis multi-seed.
2. **Manfaat Praktis (Teknologi & Industri):**
   - Menyediakan kerangka arsitektur deteksi intrusi adaptif yang aman privasi dan hemat *bandwidth* untuk diaplikasikan pada sensor *node* jaringan enterprise atau *smart campus*.
   - Membuktikan bahwa pembaruan model keamanan dapat dilakukan secara berkala dan berkesinambungan tanpa perlu mengirimkan log rekaman data mentah pengguna ke server eksternal dan tanpa kehilangan kapabilitas mendeteksi ancaman masa lalu.

\newpage

# BAB 2 TINJAUAN PUSTAKA

## 2.1 Keamanan Jaringan

Keamanan jaringan merupakan pilar fundamental dalam disiplin ilmu teknik komputer dan telekomunikasi yang berfokus pada perlindungan infrastruktur jaringan, kanal komunikasi, dan perangkat komputasi dari akses tidak sah (*unauthorized access*), modifikasi data ilegal, eksploitasi kerentanan, serta gangguan ketersediaan layanan[6]. Di era komputasi awan dan transformasi digital saat ini, keterhubungan antar-sistem semakin terbuka, yang secara bersamaan memperluas permukaan serangan (*attack surface*) dari pihak penyerang siber.

Dalam kerangka kerja keamanan jaringan, salah satu pilar konseptual paling fundamental yang dijadikan acuan perancangan sistem pertahanan adalah CIA Triad, yang mengintegrasikan tiga prinsip inti: kerahasiaan (*Confidentiality*), integritas (*Integrity*), dan ketersediaan [*Availability*](6). Prinsip kerahasiaan (*Confidentiality*) berfokus pada jaminan bahwa transmisi informasi serta rekaman data sensitif yang melintasi infrastruktur jaringan hanya dapat diakses dan diinterpretasikan oleh entitas yang memiliki hak akses (*authorization*). Perlindungan kerahasiaan ini umumnya ditegakkan melalui enkripsi protokol komunikasi *end-to-end* seperti TLS, IPsec, dan SSH, serta penerapan kebijakan kontrol akses berbasis identitas yang ketat, guna mencegah potensi intersepsi data ilegal seperti *packet sniffing* dan *eavesdropping*.

Selanjutnya, prinsip integritas (*Integrity*) menekankan pada keharusan menjaga keaslian dan konsistensi paket data agar tidak mengalami modifikasi, penyisipan muatan berbahaya, pemotongan, maupun manipulasi di tengah jalur transmisi (*man-in-the-middle tampering*). Integritas dipertahankan melalui mekanisme fungsi *hash* kriptografis, kode autentikasi pesan (*Message Authentication Code* / MAC), serta tanda tangan digital yang mampu memverifikasi keabsahan data secara presisi. Sementara itu, prinsip ketersediaan (*Availability*) menjamin bahwa seluruh sumber daya komputasi, kapasitas *bandwidth*, dan layanan aplikasi jaringan senantiasa siap sedia serta dapat diakses oleh pengguna yang berhak tanpa mengalami gangguan layanan (*downtime*). Aspek ketersediaan ini terancam secara langsung oleh serangan siber volumetrik seperti *Denial of Service* (DoS) yang berupaya menguras antrean soket dan kapasitas komputasi server.

Ketiga elemen dalam CIA Triad saling terikat secara sinergis dan tidak dapat dipisahkan satu sama lain. Untuk menegakkan prinsip tersebut secara holistik, infrastruktur jaringan enterprise mengadopsi model pertahanan berlapis (*Defense-in-Depth*). Dalam kerangka ini, sistem pertahanan tidak hanya mengandalkan perimeter luar (*firewall*), melainkan menyematkan kontrol keamanan pada setiap lapisan jaringan, mulai dari penyaringan paket, segmentasi jaringan (*Virtual LAN* / VLAN), hingga inspeksi aktif terhadap aliran lalu lintas data oleh sistem deteksi intrusi jaringan [*Network Intrusion Detection System*](6).

![Gambar 2.1 Model CIA Triad Keamanan Informasi](../Aset/cia_triad_stationx.png)  
*Gambar 2.1 Model CIA Triad Keamanan Informasi.*

---

## 2.2 Serangan Siber

Serangan siber terhadap jaringan komputer memiliki taksonomi yang luas berdasarkan tujuan penyerang, protokol yang dieksploitasi, dan mekanisme gangguan yang ditimbulkan. Dalam penelitian ini, analisis difokuskan pada tiga kategori utama perilaku lalu lintas data yang bersumber dari dataset tolok ukur CIC-IDS2017[7]:

### 2.2.1 Trafik Normal

Trafik normal merepresentasikan seluruh aliran komunikasi data sah yang dihasilkan oleh pengguna dan aplikasi resmi di dalam jaringan[7]. Aliran ini mencakup protokol web (HTTP/HTTPS), kueri *Domain Name System* (DNS), pertukaran surat elektronik (SMTP, IMAP), sinkronisasi waktu jaringan (NTP), serta lalu lintas manajemen internal. Karakteristik statistik dari trafik normal ditandai oleh distribusi panjang paket (*packet length*) yang heterogen, interval waktu kedatangan antar-paket (*inter-arrival time* / IAT) yang bervariasi sesuai interaksi manusia, serta rasio dua arah (*forward/backward packets*) yang proporsional sesuai standar protokol TCP/IP.

### 2.2.2 SSH-Patator

Protokol *Secure Shell* (SSH) yang beroperasi pada port standar 22 merupakan protokol *de facto* untuk administrasi jarak jauh pada server Linux dan perangkat jaringan enterprise. Dalam lanskap ancaman siber, serangan **SSH-Patator** merupakan bentuk serangan audit penetrasi otomatis multi-utas (*multi-threaded brute force tool*) yang mengeksekusi ribuan kombinasi *username* dan *password* dari basis data kamus (*dictionary attack*) secara masif guna membobol akun administrator sistem[7].

Dari sudut pandang analisis statistik aliran lalu lintas (*flow statistics*), serangan SSH-Patator meninggalkan karakteristik pola yang sangat distingtif dibandingkan dengan sesi interaktif normal. Serangan ini ditandai oleh lonjakan frekuensi inisiasi koneksi TCP menuju nomor port layanan autentikasi dalam jendela waktu yang sangat sempit. Sebagian besar aliran memiliki durasi yang sangat singkat (*short flow duration*), mengingat server target segera memutus sesi koneksi melalui transmisi *flag* TCP RST atau FIN sesaat setelah pertukaran *handshake* kredensial dinyatakan gagal. Di samping itu, ukuran paket data arah maju (*forward*) dan arah mundur (*backward*) menunjukkan konsistensi volume muatan yang seragam pada fase negosiasi kunci kriptografi awal sebelum pemutusan sesi berlangsung, membedakannya secara tajam dari dinamika aliran sesi interaktif pengguna yang sah[7].

### 2.2.3 Serangan DoS

Serangan **Denial of Service (DoS)** bertujuan melumpuhkan pilar ketersediaan (*availability*) sistem target dengan membanjiri sumber daya komputasi seperti CPU, memori, *bandwidth*, atau batas antrean soket koneksi server web, sehingga server target gagal melayani permintaan pengguna yang sah[7]. Dalam penelitian ini, analisis difokuskan pada empat subvarian serangan DoS lapisan aplikasi (*application-layer DoS*) yang merepresentasikan spektrum ancaman volumetrik agresif dan ancaman berkecepatan lambat (*low-and-slow attacks*).

Pada kelompok serangan volumetrik agresif, subvarian pertama adalah **DoS Hulk**, yang melancarkan pembanjiran permintaan HTTP GET bervolume masif dengan memanipulasi *header User-Agent* serta menyisipkan parameter unik acak pada URL guna menggagalkan sistem *caching* server web, memaksa server mengalokasikan siklus komputasi CPU dan memori secara berulang. Subvarian kedua adalah **DoS GoldenEye**, yang mengeksploitasi mekanisme koneksi persisten HTTP (*keep-alive*) dan perintah *Cache-Control: no-cache* secara simultan dalam jumlah besar untuk menahan *worker process* server web tetap terkunci hingga kapasitas *thread pool* server habis terpakai.

Sebaliknya, pada kelompok serangan berkecepatan lambat (*low-and-slow*), subvarian **DoS Slowloris** beroperasi secara *stealthy* dengan mengirimkan fragmen *header* HTTP parsial secara berkala dengan interval lambat. Server target dipaksa menahan soket koneksi tetap terbuka sambil menunggu *header* selesai, menghabiskan batas konkurensi koneksi server tanpa menimbulkan lonjakan volume trafik yang mencurigakan. Serupa dengan Slowloris, subvarian **DoS Slowhttptest** mengeksploitasi spesifikasi protokol HTTP dengan mengirimkan muatan badan (*body*) permintaan POST secara sangat lambat (misalnya 1 bita per interval waktu tertentu), mengunci sumber daya penerimaan data server web secara berkepanjangan dan mencegah pengguna lain untuk menjalin komunikasi[7].

---

## 2.3 Penelitian Terdahulu

Penelitian terkait penerapan kecerdasan buatan untuk deteksi intrusi jaringan terdistribusi dan adaptif telah berkembang pesat dalam beberapa tahun terakhir. Tinjauan kritis terhadap literatur ilmiah berfokus pada tiga kelompok kajian utama:

Pertama, pada domain pembelajaran terdistribusi, *Federated Learning* (FL) yang diperkenalkan oleh McMahan *et al.*[3] melalui algoritma *Federated Averaging* (FedAvg) telah menjadi fondasi utama pelatihan kolaboratif lintas node tanpa transmisi data mentah. Penerapan FedAvg pada NIDS telah diteliti oleh Popoola *et al.*[8] untuk mendeteksi serangan *zero-day botnet* pada perangkat *edge* IoT dan Ruzafa-Alcázar *et al.*[9] pada lingkungan *Industrial IoT* (IIoT) dengan mekanisme privasi diferensial. Selain itu, survei komprehensif oleh Hernandez-Ramos *et al.*[31] dan Buyuktanir *et al.*[32] menegaskan potensi besar FL dalam mengamankan lalu lintas jaringan heterogen. Namun, mayoritas studi FL-NIDS beroperasi dalam paradigma pelatihan batch/statis, mengasumsikan distribusi data IID atau hanya menguji variasi non-IID kuantitas sederhana, serta mengabaikan fenomena pergeseran konsep (*concept drift*) saat varian serangan baru muncul di jaringan secara sekuensial. Pada kondisi nyata, data lalu lintas jaringan bersifat *non-Identical and Independently Distributed* (non-IID), yang secara teoretis dan empiris dibuktikan oleh Zhao *et al.*[4] dapat memicu divergensi bobot (*weight divergence*) dan menurunkan akurasi model global.

Kedua, pada domain pembelajaran berkelanjutan (*Continual Learning* / CL), adaptasi model NIDS terhadap kelas serangan baru secara sekuensial menghadapi kendala berat berupa *catastrophic forgetting*[5]. Ketika model dilatih pada serangan baru, representasi bobot lama tertimpa sehingga kemampuan mendeteksi serangan terdahulu merosot drastis. Tinjauan sistematis oleh Hamedi *et al.*[34] memetakan tantangan mendasar pada *Federated Continual Learning* (FCL), di mana kelupaan katastropik teramplifikasi oleh heterogenitas data antar-klien. Berbagai metode mitigasi telah diajukan, seperti *Experience Replay* dan *Gradient Episodic Memory* (GEM) oleh Lopez-Paz dan Ranzato[10], serta integrasi *Federated Class-Incremental Learning* (FCIL) oleh Dong *et al.*[11] pada domain visi komputer. Dalam domain keamanan jaringan, pendekatan *incremental learning* terfederasi seperti FL-IIDS oleh Jin *et al.*[12] dan deteksi anomali bertahap IoT oleh Rehman *et al.*[33] mulai mengeksplorasi adaptasi ancaman sekuensial. Namun, pendekatan seperti FL-IIDS masih mengandalkan mekanisme penyimpanan sampel data historis (*replay memory buffer*) pada memori lokal klien yang memicu potensi risiko kebocoran privasi jika data tersimpan berhasil diekstraksi penyerang. Sebaliknya, metode regularisasi parameter *Elastic Weight Consolidation* (EWC) yang dirumuskan oleh Kirkpatrick *et al.*[5] menawarkan keunggulan proteksi memori murni pada ruang bobot melalui penalti kelengkungan Matriks Informasi Fisher diagonal tanpa memerlukan penyimpanan sampel lalu lintas masa lalu.

Ketiga, pada domain evaluasi dan integritas dataset tolok ukur CIC-IDS2017, studi audit mutakhir oleh Rosay *et al.*[13] mengungkap keberadaan *bug* logika ekstraksi fitur pada perangkat CICFlowMeter, terminasi alur TCP prematur, dan kesalahan pelabelan alur serangan. Selain itu, investigasi oleh Dube[14] membuktikan bahwa data ringkasan alur CSV dari CIC-IDS2017 terlalu kasar dan rentan menghasilkan model deteksi yang tidak memadai untuk implementasi jaringan produksi nyata. Di samping itu, investigasi kritis oleh Engelen *et al.*[15] mengungkap kelemahan mendasar konstruksi alur trafik pada CICFlowMeter serta memperingatkan potensi terjadinya *shortcut learning* pada atribut metadata alur. Berdasarkan fenomena tersebut, penelitian ini melakukan evaluasi empiris mandiri yang mengonfirmasi bahwa penggunaan fitur nomor port tujuan (`Destination Port`) menghasilkan akurasi semu akibat kebocoran port layanan (Macro-F1 port-only mencapai 96,44%), sehingga fitur tersebut dieksklusi secara ketat. Dalam konteks latensi operasional, penelitian tugas akhir terdahulu oleh Rinandri[16] menegaskan pentingnya pengukuran efisiensi inferensi tingkat mikrodetik per aliran data pada arsitektur pendeteksi anomali.

Berdasarkan kajian kritis terhadap literatur di atas, perbandingan 15 penelitian terdahulu yang relevan dalam domain Federated Learning, Continual Learning, dan Network Intrusion Detection System disajikan dalam Tabel 2.1.

*Tabel 2.1 Perbandingan Penelitian Terdahulu dalam Domain FL, Continual Learning, dan NIDS.*

| No | Penulis & Tahun | Judul Penelitian | Metode / Algoritma | Dataset | Kontribusi Utama | Keterbatasan / Research Gap |
| :---: | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | Rosay *et al.* [2022](13) | *Network Intrusion Detection: A Comprehensive Analysis of CIC-IDS2017* | Audit & ML Analysis | CIC-IDS2017 | Mengidentifikasi *bug* logika penanganan *flag* TCP pada CICFlowMeter, durasi flow anomali, dan kesalahan pelabelan | Hanya mengevaluasi kelemahan dataset mentah, tidak merancang arsitektur model deteksi atau mitigasi kelupaan. |
| 2 | Engelen *et al.* [2021](15) | *Troubleshooting an Intrusion Detection Dataset: the CICIDS2017 Case Study* | Flow Construction & Feature Audit | CIC-IDS2017 | Mengidentifikasi kelemahan konstruksi alur TCP (FIN prematur, timeout 120s) dan memperingatkan bahaya *shortcut learning* | Hanya fokus pada analisis integritas flow, tidak menguji skenario terdistribusi atau pembelajaran kelas inkremental. |
| 3 | Dube [2024](14) | *Faulty use of the CIC-IDS 2017 dataset in information security research* | Audit Kritis & Analisis Fitur | CIC-IDS2017 | Membuktikan bahwa fitur ringkasan CSV CIC-IDS2017 terlalu kasar (*too coarse*) dan tidak memadai untuk deteksi produksi | Evaluasi bersifat kritis analitis dataset, belum mengusulkan arsitektur model pertahanan terdistribusi terfederasi. |
| 4 | Kirkpatrick *et al.* [2017](5) | *Overcoming catastrophic forgetting in neural networks* | EWC & Fisher Information | Permuted MNIST | Merumuskan fondasi matematis penalti kelengkungan kuadratik berbasis diagonal Matriks Informasi Fisher | Diuji terbatas pada domain visi komputer sederhana, belum diuji pada lalu lintas jaringan terdistribusi. |
| 5 | McMahan *et al.* [2017](3) | *Communication-Efficient Learning of Deep Networks from Decentralized Data* | Federated Averaging (FedAvg) | MNIST, CIFAR-10 | Menetapkan standar arsitektur Federated Learning terdistribusi dan menganalisis konvergensi pada partisi non-IID | Dirancang untuk skenario batch/statis, tanpa proteksi *catastrophic forgetting* saat kelas baru muncul secara sekuensial. |
| 6 | Zhao *et al.* [2018](4) | *Federated Learning with Non-IID Data* | Analisis Divergensi Bobot | CIFAR-10 | Membuktikan secara analitis dan empiris degradasi akurasi FedAvg akibat pergeseran distribusi data non-IID | Memerlukan penyebaran sebagian data publik ke seluruh klien untuk memitigasi divergensi bobot lokal. |
| 7 | Lopez-Paz & Ranzato [2017](10) | *Gradient Episodic Memory for Continual Learning* | GEM / BWT Metric | CIFAR-100 | Merumuskan metrik evaluasi *Backward Transfer* (BWT) untuk mengukur retensi memori terhadap tugas terdahulu | Mengandalkan *episodic replay buffer* penyimpanan data mentah yang rentan terhadap pelanggaran privasi data. |
| 8 | Dong *et al.* [2022](11) | *Federated Class-Incremental Learning* | FCIL & Model Consolidation | Visi Komputer | Mengintegrasikan federasi dan penambahan kelas inkremental tanpa akses terpusat pada data historis | Memerlukan pertukaran prototipe representasi data atau modul generator sintetis antar-klien dengan komputasi tinggi. |
| 9 | Ruzafa-Alcázar *et al.* [2023](9) | *Intrusion Detection Based on Privacy-Preserving Federated Learning for the Industrial IoT* | FedAvg & Differential Privacy | ToN_IoT | Mengimplementasikan FL dengan mekanisme *Differential Privacy* pada lingkungan Industrial IoT di bawah non-IID | Model dievaluasi pada tugas klasifikasi statis, tidak menangani *catastrophic forgetting* pada skenario alur sekuensial. |
| 10 | Popoola *et al.* [2022](8) | *Federated Deep Learning for Zero-Day Botnet Attack Detection in IoT-Edge Devices* | FedAvg DNN | BoT-IoT | Mendeteksi serangan *zero-day botnet* pada arsitektur terdistribusi perangkat *edge* tanpa agregasi trafik mentah | Tidak menyertakan mekanisme *continual learning*, sehingga performa rentan terdegradasi saat dilatih pada varian baru. |
| 11 | Jin *et al.* [2024](12) | *FL-IIDS: A novel federated learning-based incremental intrusion detection system* | FL + Replay-based Incremental Learning | CSE-CIC-IDS2018 | Mengusulkan sistem deteksi intrusi inkremental terfederasi untuk mengadaptasi serangan baru secara berkala | Mengandalkan *memory buffer* untuk *replay* data historis yang memicu risiko kebocoran privasi lokal. |
| 12 | Rehman *et al.* [2026](33) | *Incremental Federated Learning for Intrusion Detection in IoT Networks* | Incremental FL (IoV/IoT) | Edge-IIoTset | Mengembangkan pembelajaran terfederasi inkremental adaptif terhadap lanskap ancaman IoT yang berevolusi | Terbatas pada klasifikasi anomali biner perangkat bersumber daya mikro, belum mengkaji multi-kelas Class-IL komprehensif. |
| 13 | Hernandez-Ramos *et al.* [2025](31) | *Intrusion Detection Based on Federated Learning: A Systematic Review* | Systematic Review & Taxonomy | Ragam Dataset NIDS | Menyusun taksonomi komprehensif tantangan arsitektur, privasi, dan heterogenitas data pada FL-NIDS | Merupakan studi survei literatur, tidak mengusulkan implementasi empiris algoritma mitigasi kelupaan katastropik. |
| 14 | Hamedi *et al.* [2025](34) | *Federated Continual Learning: Concepts, Challenges, and Solutions* | Comprehensive Survey | Ragam Benchmark CL | Memetakan metodologi FCL dan membuktikan bahwa non-IID mengamplifikasi kelupaan katastropik terdistribusi | Merupakan tinjauan konseptual sistematis, belum menyajikan benchmark empiris NIDS pada trafik jaringan enterprise. |
| 15 | Sarhan *et al.* [2022](17) | *Towards a Standard Feature Set for Network Intrusion Detection System Datasets* | NetFlow Feature Engineering | NetFlow-V2 | Menstandardisasi ekstraksi representasi fitur aliran berbasis alur NetFlow standar industri | Menggunakan format representasi tergeneralisasi yang mengabaikan investigasi mendalam terhadap artefak raw flow. |

Investigasi ilmiah mutakhir mengidentifikasi kelemahan mendasar dalam dataset mentah CIC-IDS2017 yang berpotensi menghasilkan evaluasi model yang bias apabila digunakan tanpa kurasi yang ketat[13], [14], [15]. Audit komprehensif oleh Rosay *et al.*[13] mengungkap bahwa perangkat ekstraksi fitur CICFlowMeter mengandung *bug* logika penanganan *flag* TCP (mengakhiri rekaman alur secara prematur pada deteksi *flag* FIN/RST pertama tanpa memperhatikan *handshake* penutupan dua arah) yang memecah koneksi normal sah menjadi beberapa fragmen alur tak lengkap, serta menghasilkan anomali perhitungan durasi alur dan fitur inter-arrival time. Selain itu, investigasi kritis oleh Dube[14] membuktikan bahwa sebagian besar riset NIDS menggunakan CIC-IDS2017 secara keliru (*faulty use*) karena fitur-fitur ringkasan CSV CIC-IDS2017 terlalu kasar (*too coarse*) dan tidak memadai untuk deteksi intrusi di lingkungan produksi (Dube, 2024, hlm. 203, 210), serta mengevaluasi model pada CSV ringkasan tanpa verifikasi pada trafik paket PCAP mentah atau komparasi dengan performa sistem deteksi/pencegahan intrusi (IDS/IPS) produksi nyata (hlm. 204). Di samping itu, kelangkaan sampel mikro ekstrem pada kelas Infiltration (hanya 36 alur dari total 2,8 juta) dan Sql Injection (hanya 21 alur) secara statistik tidak memadai untuk melatih representasi *deep learning* maupun menghitung Matriks Informasi Fisher yang stabil. Atas dasar pertimbangan integritas ilmiah tersebut, rekaman hari Kamis dan Jumat dieksklusi secara sengaja dari penelitian ini guna menjamin validitas eksperimental.

Lebih lanjut, studi audit oleh Engelen *et al.*[15] membuktikan adanya kelemahan mendasar konstruksi alur trafik pada CICFlowMeter (seperti terminasi alur prematur dan batas waktu alur 120 detik yang memotong koneksi normal secara artifisial, hlm. 3-4) serta memberikan peringatan terhadap potensi terjadinya *shortcut learning* pada fitur metadata alur. Berdasarkan peringatan tersebut, penelitian tugas akhir ini melakukan pengujian empiris mandiri yang mengonfirmasi bahwa model pembelajaran mesin yang hanya dilatih menggunakan fitur nomor port tujuan (`Destination Port`) mampu mencapai Macro-F1 sebesar 96,44%, membuktikan secara nyata terjadinya kebocoran jalan pintas port layanan (*port leakage*) pada dataset. Apabila fitur ini dipertahankan, model NIDS akan runtuh (*fail completely*) di lingkungan produksi nyata saat penyerang mengubah port target layanan ke port non-standar. Oleh karena itu, penelitian ini secara tegas mengeksklusi fitur `Destination Port` dari seluruh proses pelatihan dan inferensi, menyisakan tepat 62 fitur statistik alur numerik bersih.

---

## 2.4 Kerangka Teoretis Continual Learning (Pembelajaran Berkelanjutan)

Continual Learning (CL) atau pembelajaran mesin berkelanjutan bertujuan mengatasi dilema stabilitas-plastisitas (*Stability-Plasticity Dilemma*), di mana model pembelajaran mesin dituntut memiliki plastisitas untuk mengasimilasi informasi dari aliran tugas (*task*) baru $\mathcal{T}_1, \mathcal{T}_2, \dots, \mathcal{T}_T$ tanpa mengorbankan stabilitas representasi yang telah terbentuk pada tugas-tugas sebelumnya[23], [24]. Dalam skenario *Class-Incremental Learning* (Class-IL) yang diadopsi pada penelitian ini, model dievaluasi pada seluruh kelas yang telah dipelajari tanpa bantuan identitas tugas (*Task-ID*) saat inferensi.

Secara taksonomi, pendekatan mitigasi *catastrophic forgetting* dalam literatur Continual Learning terbagi menjadi tiga keluarga utama: metode berbasis regularisasi parameter (*prior-focused regularization*), metode berbasis pemutaran ulang (*replay/rehearsal-based*), dan metode berbasis alokasi arsitektur [*parameter allocation*](23), [25]. Taksonomi pendekatan mitigasi kelupaan ini diilustrasikan pada Gambar 2.2, sedangkan perbandingan menyeluruh dari metode-metode tersebut disajikan dalam Tabel 2.2.

![Gambar 2.2 Taksonomi Pendekatan Mitigasi Catastrophic Forgetting pada Continual Learning](../Aset/continual_learning_taxonomy_taxonomy_fig2.png)  
*Gambar 2.2 Taksonomi Pendekatan Mitigasi Catastrophic Forgetting pada Continual Learning[19].*


*Tabel 2.2 Taksonomi dan Perbandingan Menyeluruh Metode Continual Learning (CL).*

| Keluarga Metode | Nama Algoritma & Rujukan | Mekanisme Inti & Formulasi Matematis | Keunggulan Utama | Keterbatasan di Lingkungan Edge NIDS | Kesesuaian Riset Ini |
| --- | --- | --- | --- | --- | :---: |
| **Regularisasi Parameter (Prior-Focused)** | **Elastic Weight Consolidation (EWC)**<br>*(Kirkpatrick et al., 2017)*[5] | Penalti kuadratik berbasis diagonal Matriks Informasi Fisher:<br>$\mathcal{L}(\theta) = \mathcal{L}_{\text{new}}(\theta) + \sum_i \frac{\lambda}{2} F_i (\theta_i - \theta_{1,i}^*)^2$ | Bebas penyimpanan sampel mentah (*zero-buffer*); komputasi Fisher deterministik dan stabil pada MLP. | Mengabaikan korelasi off-diagonal Hessian; kapasitas proteksi terbatas jika jumlah task sangat panjang. | ⭐⭐⭐⭐⭐<br>**Metode Terpilih** |
| | **Online EWC**<br>*(Schwarz et al., 2018)* | Akumulasi Fisher melintasi banyak task dengan faktor peluruhan:<br>$\tilde{F}^t = \gamma \tilde{F}^{t-1} + F^t$ | Skalabel untuk rangkaian task kontinu tanpa pembengkakan suku penalti. | Memerlukan penyetelan teliti pada faktor peluruhan $\gamma$. | ⭐⭐⭐⭐<br>Ekstensi $T > 3$ |
| | **Synaptic Intelligence (SI)**<br>*(Zenke et al., 2017)* | Akumulasi kontribusi lintasan parameter selama proses optimasi online. | Komputasi relevansi parameter menyatu dengan fase pelatihan lokal. | Sensitif terhadap ukuran *learning rate*; rentan instabilitas gradien pada data tabular non-IID. | ⭐⭐⭐<br>Alternatif |
| | **Memory Aware Synapses (MAS)**<br>*(Aljundi et al., 2018)* | Menghitung sensitivitas magnitudo output fungsi prediksi tanpa memerlukan label data. | Beroperasi tanpa label data (*unsupervised importance estimation*). | Batas keputusan kelas serangan NIDS yang rapat kurang terproteksi optimal. | ⭐⭐⭐<br>Alternatif |
| **Regularisasi Data (Distillation)** | **Learning without Forgetting (LwF)**<br>*(Li & Hoiem, 2017)* | Distilasi pengetahuan menggunakan keluaran model lama sebagai sinyal regulasi (KL-Divergence). | Tidak memerlukan estimasi Fisher maupun buffer data historis. | Terjadi distorsi representasi jika fitur serangan baru memiliki disparitas statistik ekstrem dari serangan lama. | ⭐⭐⭐⭐<br>Alternatif |
| **Replay / Rehearsal (Memory Buffer)** | **Experience Replay (ER)**<br>*(Chaudhry et al., 2019)* | Menyimpan cuplikan paket/flow mentah tugas lama dalam buffer fisik memori lokal untuk dilatih ulang bersama data baru. | Retensi memori sangat kuat dan mudah diimplementasikan. | **Melanggar prinsip privasi data** (buffer data mentah rentan terekstraksi jika node edge disusupi); membebani kapasitas RAM. | ❌ Dieliminasi<br>*(Isu Privasi & RAM)* |
| | **Gradient Episodic Memory (GEM)**<br>*(Lopez-Paz & Ranzato, 2017)*[10] | Pembatasan proyeksi gradien baru agar sudut terhadap gradien memori non-negatif:<br>$\langle g_{\text{new}}, g_{\text{mem}} \rangle \ge 0$ | Mendorong transfer ke belakang non-negatif (*Backward Transfer* / BWT $\ge 0$). | Komputasi *Quadratic Programming* (QP-solver) sangat berat untuk prosesor edge; memerlukan buffer sampel mentah. | ❌ Dieliminasi<br>*(Overhead Komputasi)* |
| **Alokasi Arsitektur (Modular)** | **PackNet**<br>*(Mallya & Lazebnik, 2018)* | Melakukan *network pruning* terstruktur dan membekukan subset parameter penting untuk tugas lama. | Kelupaan katastropik bernilai nol secara teoritis pada tugas yang telah dibekukan. | Membutuhkan arsitektur jaringan saraf berkapasitas sangat besar; tidak sepadan untuk MLP kompak 6.211 parameter. | ❌ Kurang Sesuai<br>*(Overkill MLP)* |

Berdasarkan perbandingan di atas, **EWC dipilih sebagai metode inti** dalam penelitian ini karena memenuhi kriteria *zero-data replay* (kepatuhan privasi penuh tanpa buffer flow mentah) dan memiliki profil komputasi yang sangat efisien untuk arsitektur MLP kompak di node edge.

---

## 2.5 Kerangka Teoretis Federated Learning (Pembelajaran Terfederasi)

Federated Learning (FL) merupakan paradigma pembelajaran mesin terdistribusi di mana $K$ node klien berkolaborasi melatih model konsensus global tanpa memindahkan data lokal mentah $\mathcal{D}_k$ ke server sentral[3]. Formulasi optimasi FL dirumuskan sebagai:

$$\min_{w} f(w) = \sum_{k=1}^K \frac{n_k}{N} F_k(w), \quad \text{dengan } F_k(w) = \mathbb{E}_{(x, y) \sim \mathcal{D}_k} [\ell(w; x, y)]$$

Tantangan utama FL pada deteksi intrusi jaringan adalah fenomena *client drift* akibat heterogenitas data [*non-IID label skew*](4), [31]. Berbagai algoritma agregasi dan optimasi terfederasi telah diusulkan dalam literatur untuk menangani masalah heterogenitas spasial maupun kontinuitas sekuensial. Alur siklus pelatihan dan agregasi bobot pada Federated Learning (FedAvg) diilustrasikan pada Gambar 2.3, sedangkan taksonomi metode FL disajikan dalam Tabel 2.3.

![Gambar 2.3 Siklus Pelatihan dan Agregasi Bobot pada Federated Learning (FedAvg)](../Aset/fedavg_flowchart_researchgate.png)  
*Gambar 2.3 Siklus Pelatihan dan Agregasi Bobot pada Federated Learning (FedAvg)[3].*


*Tabel 2.3 Taksonomi dan Perbandingan Menyeluruh Metode Federated Learning (FL).*

| Kategori Metode | Algoritma & Rujukan | Mekanisme Agregasi / Formulasi Matematis | Keunggulan Utama | Keterbatasan & Beban Komunikasi | Kesesuaian Riset Ini |
| --- | --- | --- | --- | --- | :---: |
| **Agregasi Baseline** | **Federated Averaging (FedAvg)**<br>*(McMahan et al., 2017)*[3] | Rata-rata terbobot proporsional dari parameter lokal klien:<br>$w^{t+1} = \sum_{k=1}^K \frac{n_k}{N} w_k^{t+1}$ | Efisiensi komunikasi tinggi; overhead minimal (hanya payload bobot); standar *de facto* industri (Flower framework). | Mengalami *client drift* dan divergensi bobot saat data non-IID ekstrem. | ⭐⭐⭐⭐⭐<br>**Baseline Utama FL** |
| | **FedNova**<br>*(Wang et al., 2020)* | Normalisasi pembaruan gradien lokal berbasis variasi jumlah langkah iterasi lokal klien. | Menghilangkan bias konvergensi akibat heterogenitas komputasi lokal antar-klien. | Dampak minimal jika jumlah epoch lokal antar-klien ditetapkan seragam ($E$ konstan). | ⭐⭐⭐<br>Alternatif Heterogen |
| **Mitigasi Heterogenitas (Non-IID Drift)** | **FedProx**<br>*(Li et al., 2020)*[22] | Penambahan penalti deviasi proksimal terhadap model global:<br>$\min_w F_k(w) + \frac{\mu}{2} \|w - w^t\|^2$ | Meredam divergensi bobot lokal dari konsensus global; stabil menghadapi *stragglers*. | Memerlukan penyetelan cermat hyperparameter $\mu$; konvergensi lebih lambat jika $\mu$ terlalu dominan. | ⭐⭐⭐⭐<br>**Alternatif Pembanding Spasial** |
| | **SCAFFOLD**<br>*(Karimireddy et al., 2020)* | Menggunakan variabel kontrol (*control variates*) untuk mengoreksi arah gradien lokal klien. | Menjamin laju konvergensi stabil di bawah non-IID ekstrem tanpa deviasi gradien. | Ukuran payload transmisi komunikasi berlipat ganda **$2\times$** (mengirim bobot $w$ + variabel kontrol $c$). | ⭐⭐⭐<br>Beban Jaringan Tinggi |
| **Personalized & Continual FL** | **FedCurv**<br>*(Shoham et al., 2019)* | Penalti kurvatur Fisher lintas klien terdistribusi:<br>$\mathcal{L}_k(w) = \mathcal{L}_{\text{local}}(w) + \sum_{j \neq k} \frac{\lambda}{2} (w - w_j^*)^T F_j (w - w_j^*)$ | Meredam penyimpangan bobot antar-klien dengan menjaga kurvatur solusi bersama. | Beban transmisi komunikasi melonjak **$2\times$ lipat** (mengirim bobot $w$ dan diagonal Fisher $F$); belum terintegrasi native di Flower. | ⭐⭐⭐⭐<br>**Pembanding Teoretis Bab 2** |
| | **FedWeIT**<br>*(Yoon et al., 2021)* | Dekomposisi bobot jaringan menjadi parameter global, parameter klien, dan *task-specific sparse masks*. | Mencegah interferensi antar-tugas secara struktural melalui dekomposisi parameter. | Memerlukan perancangan arsitektur modular yang kompleks; tidak efisien untuk model MLP kompak. | ⭐⭐<br>Arsitektur Berbeda |

---

## 2.6 Posisi Sintesis: Integrasi FedAvg dan EWC Lokal

Berdasarkan tinjauan kritis pada Tabel 2.1, 2.2, dan 2.3, penelitian tugas akhir ini memadukan **FedAvg sebagai algoritma konsensus federasi terpusat yang ringan** dengan **EWC sebagai mekanisme regularisasi kelupaan temporal pada loop pelatihan lokal klien**.

Kombinasi ortogonal ini memisahkan secara tegas dua domain persoalan:

1. **Dimensi Spasial (Non-IID Antar-Klien):** Ditangani oleh agregasi FedAvg di server sentral, di mana model global menyerap representasi serangan yang berbeda dari masing-masing sektor klien tanpa pertukaran data mentah.
2. **Dimensi Temporal (Mitigasi Forgetting Lintas Waktu):** Ditangani oleh penalti kuadratik Fisher EWC di masing-masing klien, di mana parameter sensitif terhadap serangan terdahulu (Task 1: SSH-Patator) diproteksi secara lokal saat model mengasimilasi serangan baru (Task 2: DoS).

Dengan konfigurasi ini, server Flower tetap beroperasi secara *stateless* dan efisien tanpa memerlukan transmisi matriks Fisher melalui jaringan, dengan estimasi teoretis ukuran pembaruan bobot model MLP 6.211 parameter (tipe float32) sebesar ~24,84 KB per transmisi yang akan diverifikasi secara empiris pada tahap pengujian sistem, sekaligus meniadakan risiko kebocoran data mentah akibat ketiadaan penyimpanan buffer rekaman trafik historis (*exemplar-free*).

---

## 2.7 Deteksi Intrusi

*Network Intrusion Detection System* (NIDS) merupakan mekanisme pertahanan siber yang ditempatkan pada infrastruktur jaringan untuk menginspeksi lalu lintas data dan mendeteksi aktivitas mencurigakan yang mengindikasikan adanya intrusi, eksploitasi kerentanan, atau pelanggaran kebijakan keamanan[20].

### 2.7.1 Arsitektur Penempatan
Berdasarkan arsitektur penempatan dan cakupan monitoringnya, sistem deteksi intrusi secara mendasar terbagi menjadi dua kategori utama, yaitu *Host-Based IDS* (HIDS) dan *Network-Based IDS* (NIDS)[20]. HIDS beroperasi secara langsung pada tingkat sistem operasi dari perangkat *endpoint* atau server individual untuk mengawasi integritas berkas sistem (*file integrity*), log autentikasi, serta pemanggilan instruksi sistem (*system calls*). Karakteristik HIDS sangat efektif untuk mengidentifikasi ancaman internal atau eksploitasi hak akses di tingkat lokal, namun memerlukan instalasi agen pada setiap mesin dan mengonsumsi sumber daya komputasi dari server aplikasi target. Sebaliknya, NIDS ditempatkan secara strategis pada tautan jaringan (*network links*), seperti *switch*, *gateway*, atau port agregasi, guna memantau seluruh paket dan aliran data yang melintasi segmen jaringan secara non-invasif. Keunggulan utama NIDS terletak pada kemampuannya mengawasi puluhan hingga ratusan perangkat sekaligus secara simultan tanpa membebani performa komputasi server aplikasi serta mampu mendeteksi pola serangan yang bergerak lintas subnet jaringan[20], sebagaimana diilustrasikan pada Gambar 2.4.

![Gambar 2.4 Perbandingan Topologi Arsitektur Penempatan NIDS dan HIDS pada Infrastruktur Jaringan](../Aset/nids_vs_hids_architecture.png)  
*Gambar 2.4 Perbandingan Topologi Arsitektur Penempatan NIDS dan HIDS pada Infrastruktur Jaringan (Sumber: Stephen, 2023).*

### 2.7.2 Metode Deteksi
Ditinjau dari metodologi deteksi yang diimplementasikan, NIDS terbagi menjadi pendekatan berbasis tanda tangan (*Signature-Based IDS* / SIDS) dan pendekatan berbasis anomali (*Anomaly-Based IDS* / ABDS)[20]. SIDS beroperasi dengan mencocokkan setiap muatan paket atau pola lalu lintas terhadap basis data tanda tangan serangan (*attack signatures*) yang telah didefinisikan sebelumnya oleh analis keamanan. Pendekatan SIDS memiliki keunggulan dalam kecepatan komputasi dan menghasilkan tingkat alarm palsu (*false positive*) yang sangat rendah untuk ancaman lama yang telah terdaftar, namun mengalami kegagalan mutlak ketika berhadapan dengan serangan baru (*zero-day attacks*) atau varian serangan yang telah dimodifikasi polanya. Sebaliknya, ABDS memodelkan perilaku lalu lintas normal sebagai profil tolok ukur (*baseline*), sehingga setiap penyimpangan statistik yang signifikan akan ditandai sebagai indikasi anomali intrusi. ABDS modern mengandalkan model pembelajaran mesin dan jaringan saraf tiruan untuk mengevaluasi fitur statistik aliran dua arah (*bidirectional flow features*), memberikan kemampuan generalisasi yang tangguh dalam mengidentifikasi pola ancaman baru yang belum pernah terpetakan sebelumnya[8], [20].

---

## 2.8 PyTorch

PyTorch merupakan pustaka komputasi ilmiah dan *deep learning* sumber terbuka berbasis Python yang dikembangkan oleh Meta AI, yang telah menjadi standar *de facto* dalam riset kecerdasan buatan modern[21]. Keunggulan fundamental PyTorch bersumber dari mekanisme graf komputasi dinamis (*Dynamic Computational Graph* berbasis paradigma *Define-by-Run* melalui mesin diferensiasi otomatis Autograd), yang memungkinkan struktur jaringan saraf tiruan dieksekusi dan dimodifikasi secara interaktif selama waktu eksekusi (*runtime*) tanpa memerlukan kompilasi graf statis terlebih dahulu[21]. Pendekatan dinamis ini mempermudah pelacakan alur gradien (*backpropagation*) dan proses *debugging* tensor secara langsung menggunakan pustaka bawaan Python.

Di samping itu, PyTorch menyediakan antarmuka tensor multi-dimensi berperforma tinggi yang terintegrasi secara mulus dengan akselerasi perangkat keras GPU melalui pustaka *NVIDIA CUDA* dan *cuDNN*, serta optimasi aljabar linear pada prosesor CPU[21]. Arsitektur modular PyTorch, khususnya abstraksi `torch.nn` dan `torch.optim`, memberikan keleluasaan penuh dalam menyusun fungsi kerugian kustom (*custom loss function*)[21]. Fleksibilitas manipulasi gradien ini sangat krusial dalam penelitian ini untuk merekayasa fungsi objektif lokal yang menggabungkan *Weighted Cross-Entropy Loss* dengan suku penalti kuadratik EWC berbasis perkalian tensor elemen-per-elemen secara langsung pada ruang bobot parameter tanpa menimbulkan *overhead* komputasi graf statis yang kaku[5], [21].

---

## 2.9 Flower

Dalam mengimplementasikan paradigma pembelajaran terdistribusi, penelitian ini memanfaatkan Flower (`flwr`), yaitu kerangka kerja *Federated Learning* sumber terbuka yang dirancang modular, terukur, dan agnostik terhadap berbagai pustaka *machine learning*[22]. Arsitektur komunikasi Flower memisahkan tanggung jawab sistem secara tegas antara modul koordinator terpusat (`Server`) dan simpul komputasi lokal (`Client`), yang berinteraksi melalui protokol komunikasi berkecepatan tinggi *Google Remote Procedure Call* (gRPC) di atas lapisan transport HTTP/2 pada port standar TCP 8080[22]. Protokol ini menjamin pertukaran pesan asinkron yang andal, efisien, dan memiliki latensi minimal pada kanal jaringan terdistribusi.

Dalam setiap siklus federasi, Flower mengorkestrasi pertukaran parameter model secara efisien tanpa mentransmisikan data mentah milik klien[22]. Parameter bobot model PyTorch pada setiap simpul klien diekstraksi ke dalam larik terindeks NumPy berpresisi 32-bit (*float32*), kemudian diserialisasi ke dalam format biner terkompresi *Protocol Buffers* (`Parameters` proto) sebelum dikirimkan ke server melalui instruksi `fit_res`[22]. Server agregator kemudian menerapkan strategi federasi seperti *Federated Averaging* (FedAvg) untuk menggabungkan parameter lokal menjadi model global baru[3], [22]. Penggunaan arsitektur model MLP kompak dalam penelitian ini (memuat 6.211 parameter *float32*) menghasilkan estimasi teoretis ukuran muatan biner parameter sebesar $pprox 24,84$ KB ($24.844$ bita) per transmisi klien. Dengan estimasi total pertukaran parameter untuk dua klien sebesar $pprox 99,38$ KB per ronde komunikasi (yang akan diverifikasi pengukurannya pada tahap pengujian eksperimental), Flower menghasilkan penghematan lebar pita jaringan sebesar lebih dari $99,4\%$ dibandingkan skenario sentralisasi yang mentransmisikan data mentah berukuran gigabita, seraya mendukung emulasi klien virtual maupun penerapan nyata pada simpul *edge* fisik (*cross-silo deployment*)[22].

---

## 2.10 Multilayer Perceptron

*Multilayer Perceptron* (MLP) merupakan arsitektur dasar jaringan saraf tiruan umpan-maju (*feedforward neural network*) yang terdiri dari sekurang-kurangnya tiga lapisan neuron komputasi terstruktur: satu lapisan masukan (*input layer*), satu atau lebih lapisan tersembunyi (*hidden layers*), dan satu lapisan keluaran (*output layer*)[23]. Pada arsitektur MLP terhubung penuh (*fully connected layers*), setiap neuron pada suatu lapisan menerima kombinasi linear terbobot dari seluruh neuron pada lapisan sebelumnya, menambahkan skalar bias, dan memetakan hasilnya melalui fungsi aktivasi non-linear guna membentuk batas keputusan (*decision boundaries*) yang mampu memisahkan kelas-kelas data yang tidak dapat dipisahkan secara linear (*linearly non-separable*)[23].

Untuk memenuhi batasan komputasi perangkat gerbang jaringan (*edge gateway*) dan menghindari latensi komputasi yang tinggi pada sistem deteksi intrusi waktu nyata, arsitektur model klasifikasi dalam penelitian ini dirancang menggunakan konfigurasi MLP kompak 62-64-32-3[23]. Model menerima vektor fitur masukan $x \in \mathbb{R}^{62}$ yang merepresentasikan statistik aliran paket jaringan, dan memprosesnya secara matematis melalui tahapan propagasi maju (*forward pass*)[23]:

$$
\begin{aligned}
h_1 &= f_1(W_1 x + b_1), \quad W_1 \in \mathbb{R}^{64 \times 62}, \ b_1 \in \mathbb{R}^{64} \\
h_2 &= f_2(W_2 h_1 + b_2), \quad W_2 \in \mathbb{R}^{32 \times 64}, \ b_2 \in \mathbb{R}^{32} \\
z &= W_3 h_2 + b_3, \quad W_3 \in \mathbb{R}^{3 \times 32}, \ b_3 \in \mathbb{R}^{3} \\
\hat{y} &= \text{Softmax}(z)
\end{aligned}
$$

di mana $f_1$ dan $f_2$ merupakan fungsi aktivasi non-linear *Rectified Linear Unit* (ReLU), $z$ adalah vektor logit klasifikasi, dan $\hat{y}$ merepresentasikan estimasi probabilitas posterior kelas aliran lalu lintas jaringan (BENIGN, SSH-Patator, atau DoS)[23].

Pemilihan topologi MLP kompak ini didasarkan pada pertimbangan kritis terhadap keterbatasan sumber daya komputasi simpul sensor jaringan (*edge gateways*) dan tuntutan latensi inspeksi paket berkecepatan tinggi[23]. Dengan 62 fitur masukan, 64 neuron pada lapisan tersembunyi pertama, 32 neuron pada lapisan tersembunyi kedua, dan 3 neuron keluaran, total parameter teroptimasi model dihitung secara eksak sebagai[23]:

$$
|\theta| = (62 \times 64 + 64) + (64 \times 32 + 32) + (32 \times 3 + 3) = 4.032 + 2.080 + 99 = 6.211 \text{ parameter}
$$

Dengan representasi bilangan mengambang 32-bit (*single precision float32* berukuran 4 bita), estimasi teoretis ukuran biner parameter model mencapai sekitar **24,84 KB** ($6.211 	imes 4$ bita = $24.844$ bita). Jejak memori (*memory footprint*) yang sangat ringkas ini memberikan dua keuntungan operasional yang krusial. Pertama, proses serialisasi dan transmisi bobot melalui protokol gRPC Flower pada setiap ronde federasi dapat diselesaikan dalam orde milidetik tanpa membebani kapasitas lebar pita jaringan terdistribusi. Kedua, model mampu mengeksekusi inferensi klasifikasi aliran data secara lokal dalam skala mikrodetik per sampel aliran ($\mu\text{s/flow}$), memastikan sistem mampu mengimbangi laju paket pada tautan jaringan berkecepatan tinggi tanpa memicu penumpukan antrean (*buffer bloat*) yang berisiko menyebabkan hilangnya paket data (*packet drop*)[22], [23]. Struktur arsitektur jaringan MLP yang dirancang diilustrasikan pada Gambar 2.5.

![Gambar 2.5 Struktur Arsitektur Jaringan Multilayer Perceptron (MLP)](../Aset/mlp_nn_hidden_layer_researchgate.png)  
*Gambar 2.5 Struktur Arsitektur Jaringan Multilayer Perceptron (MLP) dengan Lapisan Tersembunyi.*

---

## 2.11 Regularisasi EWC

*Elastic Weight Consolidation* (EWC) merupakan metode mitigasi *catastrophic forgetting* berbasis regularisasi parameter yang diperkenalkan oleh Kirkpatrick *et al.*[5], yang terinspirasi oleh fenomena konsolidasi memori sinaptik pada otak biologis mamalia di mana plastisitas sinapsis ditekan secara selektif untuk mempertahankan keterampilan yang telah dipelajari sebelumnya. Dari perspektif inferensi Bayesian, proses pembelajaran tugas kedua $\mathcal{D}_2$ setelah menyelesaikan pelatihan tugas pertama $\mathcal{D}_1$ dirumuskan melalui distribusi probabilitas posterior parameter $\theta$[5]:

$$
\log p(\theta \mid \mathcal{D}_1, \mathcal{D}_2) = \log p(\mathcal{D}_2 \mid \theta) + \log p(\theta \mid \mathcal{D}_1) - \log p(\mathcal{D}_2)
$$

Distribusi prior $p(\theta \mid \mathcal{D}_1)$ memuat seluruh akumulasi pengetahuan mengenai tugas pertama. Karena bentuk eksak distribusi posterior pada jaringan saraf tiruan non-linear bersifat rumit dan tidak dapat dihitung secara analitis, EWC mengaproksimasi $\log p(\theta \mid \mathcal{D}_1)$ menggunakan ekspansi deret Taylor orde kedua di sekitar titik parameter optimal tugas pertama $\theta_1^{\ast}$ sebagai distribusi Gaussian multivariat, dengan presisi kelengkungan yang ditentukan oleh **Matriks Informasi Fisher (Fisher Information Matrix / FIM)**[5]:

$$
F = \mathbb{E}_{x \sim \mathcal{D}_1, y \sim p(y \mid x, \theta_1^{\ast})} \left[ \nabla_\theta \log p(y \mid x, \theta_1^{\ast}) \nabla_\theta \log p(y \mid x, \theta_1^{\ast})^T \right]
$$

Guna menghindari kompleksitas komputasi inversi matriks kovariansi penuh yang berukuran $|\theta| \times |\theta|$, EWC mengasumsikan independensi kuasi antar-parameter dan hanya mengevaluasi elemen-elemen diagonal matriks Fisher ($F_i$)[5]. Dalam penerapan praktis *machine learning*, ekspektasi analitis tersebut didekati melalui **Empirical Fisher Information Matrix**, di mana gradien kuadratik dihitung terhadap label kebenaran dasar (*ground truth*) dari $N$ sampel data tugas pertama[5]:

$$
F_i = \frac{1}{N} \sum_{n=1}^N \left( \left. \frac{\partial \mathcal{L}_{\text{CE}}(f(x_n; \theta), y_n)}{\partial \theta_i} \right|_{\theta = \theta_1^{\ast}} \right)^2
$$

Saat model melanjutkan pembelajaran pada alur data tugas kedua, fungsi kerugian total lokal diintegrasikan dengan penalti kuadratik terbobot Fisher terhadap deviasi parameter optimal lama[5]:

$$
\mathcal{L}_{\text{total}}(\theta) = \mathcal{L}_2(\theta) + \sum_{i} \frac{\lambda}{2} F_i (\theta_i - \theta_{1, i}^{\ast})^2
$$

di mana $\lambda$ merupakan koefisien hiperparameter penalti EWC yang mengontrol keseimbangan (*trade-off*) antara plastisitas terhadap tugas baru dan stabilitas retensi memori terhadap tugas lama, $\theta_{1, i}^{\ast}$ adalah nilai parameter optimal tugas pertama yang dibekukan, dan $F_i$ mengukur seberapa sensitif kinerja tugas pertama terhadap pergeseran parameter ke-$i$[5]. Parameter dengan nilai $F_i$ besar dilindungi dari pembaruan gradien besar, sedangkan parameter dengan $F_i$ mendekati nol leluasa dimodifikasi oleh data baru, sebagaimana diilustrasikan pada Gambar 2.6.

![Gambar 2.6 Mekanisme Regularisasi EWC Membatasi Pergeseran Bobot Kritis pada Kontur Kerugian](../Aset/ewc_parameter_space_kirkpatrick2017.png)  
*Gambar 2.6 Mekanisme Regularisasi EWC Membatasi Pergeseran Bobot Kritis pada Kontur Kerugian[5].*

Dalam mengoperasikan model pada kondisi lalu lintas jaringan dengan ketimpangan kelas yang parah, fungsi kerugian dasar $\mathcal{L}_2(\theta)$ distabilkan menggunakan pembobotan invers frekuensi kelas (*Weighted Cross-Entropy Loss*)[5]:

$$
\mathcal{L}_{\text{CE}}(y, \hat{y}) = - \sum_{c=1}^{C} w_c \cdot y_c \log(\hat{y}_c), \quad \text{dengan } w_c = \frac{N_{\text{total}}}{C \cdot N_c}
$$

Selain itu, guna mencegah ledakan magnitudo gradien (*exploding gradients*) yang dipicu oleh akumulasi penalti EWC berbobot besar dan ketimpangan bobot kelas minoritas, mekanisme pemotongan gradien (*Gradient Clipping*) berbasis norma L2 diterapkan sebelum langkah pembaruan bobot dijalankan[5]:

$$
\text{jika } \|\mathbf{g}\|_2 > \gamma, \quad \text{maka } \mathbf{g} \leftarrow \frac{\gamma}{\|\mathbf{g}\|_2} \mathbf{g}, \quad \text{dengan } \gamma = 1.0
$$

---

## 2.12 Dataset

Dataset tolok ukur yang digunakan dalam penelitian ini adalah **CIC-IDS2017** (*Canadian Institute for Cybersecurity Intrusion Detection System 2017*). Dataset ini dibangun menggunakan topologi jaringan korban (*Victim Network*) dan jaringan penyerang (*Attack Network*) yang merekam lalu lintas paket nyata selama lima hari kerja (Senin s.d. Jumat)[7].

### 2.12.1 Karakteristik Aliran
Seluruh lalu lintas jaringan mentah dalam format *packet capture* (pcap) diekstraksi menggunakan perangkat lunak *CICFlowMeter* menjadi rekaman statistik aliran dua arah (*bidirectional flow features*). Berkas lalu lintas yang dianalisis dalam penelitian ini mencakup berkas hari Senin (*Monday*) yang merepresentasikan lalu lintas operasional normal (BENIGN) secara eksklusif, berkas hari Selasa (*Tuesday*) yang memuat aktivitas normal dan serangan penetrasi autentikasi SSH (*SSH-Patator*), serta berkas hari Rabu (*Wednesday*) yang memuat lalu lintas normal dan varian serangan *Denial of Service* (DoS Slowloris, Slowhttptest, Hulk, dan GoldenEye)[7].

### 2.12.2 Kurasi Fitur
Meskipun CIC-IDS2017 merupakan tolok ukur standar dalam riset NIDS, sejumlah studi audit saintifik mutakhir mengidentifikasi kelemahan mendasar dalam dataset mentah yang berpotensi menghasilkan evaluasi model yang bias[13], [14], [15]. Audit oleh Rosay *et al.*[13] dan Dube[14] membuktikan bahwa berkas hari Kamis menderita desinkronisasi penanda waktu (*timestamp labeling error*) yang parah antara file rekaman pcap dan file CSV, serta memiliki kelangkaan sampel kelas ekstrem (seperti serangan Infiltration yang hanya terdiri dari 36 baris dan Sql Injection sebanyak 21 baris). Kondisi ini menyebabkan berkas hari Kamis dan Jumat dieksklusi secara sengaja dari penelitian ini guna menjamin validitas dan reliabilitas eksperimen.

Lebih lanjut, studi audit oleh Engelen *et al.*[15] membuktikan adanya fenomena *shortcut learning* atau kebocoran fitur (*feature leakage*) akibat keberadaan atribut nomor port tujuan (`Destination Port`). Ketika fitur nomor port diikutsertakan, algoritma pembelajaran mesin cenderung mengambil jalan pintas dengan menghafal nomor port layanan standar (misalnya port 22 untuk SSH dan port 80 untuk DoS), sehingga menghasilkan akurasi klasifikasi yang tinggi semu tanpa pernah mempelajari pola statistik lalu lintas paket yang sebenarnya. Menjawab tantangan tersebut, penelitian ini menerapkan protokol kurasi yang ketat dengan membuang fitur `Destination Port` secara definitif guna mengeliminasi celah *feature leakage*, mengeliminasi baris data duplikat identik, membuang fitur konstan bervariansi nol, serta mengeliminasi pasangan fitur duplikat mutlak. Melalui prosedur praproses ini, diperoleh tepat **62 fitur statistik numerik bersih** yang memastikan model dievaluasi secara otentik atas dinamika perilaku aliran jaringan[15], [17].

---

## 2.13 Evaluasi Metrik

Evaluasi sistem dilakukan secara komprehensif mencakup metrik kinerja deteksi kecerdasan buatan, metrik retensi continual learning, dan metrik profil komputasi perangkat.

### 2.13.1 Kinerja Klasifikasi
Kinerja deteksi model dievaluasi secara menyeluruh menggunakan matriks konfusi (*Confusion Matrix*) yang mengelompokkan prediksi model ke dalam empat kuadran hasil: *True Positive* (TP), *True Negative* (TN), *False Positive* (FP), dan *False Negative* (FN) sebagaimana diilustrasikan pada Gambar 2.7[24].

![Gambar 2.7 Struktur Dasar Confusion Matrix untuk Evaluasi Deteksi Biner dan Multi-kelas](../Aset/confusion_matrix_accessibleai.png)  
*Gambar 2.7 Struktur Dasar Confusion Matrix untuk Evaluasi Deteksi Biner dan Multi-kelas.*

Metrik pertama adalah **Akurasi (*Accuracy*)**, yang mengukur proporsi keseluruhan prediksi yang benar terhadap total sampel data yang dievaluasi:

$$
\text{Accuracy} = \frac{TP + TN}{TP + TN + FP + FN}
$$

Meskipun akurasi memberikan gambaran umum efektivitas model, metrik ini rentan menghasilkan interpretasi yang menyesatkan pada dataset deteksi intrusi yang memiliki ketimpangan kelas ekstrem di mana kelas normal mendominasi secara absolut. Oleh karena itu, metrik **Presisi (*Precision*)** digunakan untuk mengukur ketepatan deteksi positif dari seluruh peringatan yang dibunyikan oleh model, yang dirumuskan sebagai:

$$
\text{Precision} = \frac{TP}{TP + FP}
$$

Presisi yang tinggi menjamin bahwa sistem meminimalkan frekuensi alarm palsu (*false alarm rate*), sehingga tidak membebani operator keamanan jaringan dengan peringatan keliru. Selanjutnya, metrik **Recall (*Sensitivity*)** mengevaluasi kemampuan sistem dalam menjaring seluruh insiden serangan yang sebenarnya terjadi di dalam jaringan:

$$
\text{Recall} = \frac{TP}{TP + FN}
$$

Nilai *Recall* yang tinggi memastikan sistem memiliki tingkat deteksi lolos (*false negative*) yang rendah, sehingga serangan berbahaya tidak menyusup tanpa terdeteksi. Sebagai penyeimbang trade-off antara Presisi dan Recall, evaluasi utama dalam penelitian ini mengadopsi metrik **Macro-Averaged F1 (Macro-F1)**, yang menghitung rata-rata harmonik F1-score secara mandiri pada setiap kelas tanpa dipengaruhi oleh bobot proporsi jumlah sampel:

$$
\text{Macro-F1} = \frac{1}{C} \sum_{c=1}^C \frac{2 \cdot \text{Precision}_c \cdot \text{Recall}_c}{\text{Precision}_c + \text{Recall}_c}
$$

Dengan menghitung rata-rata secara unweighted antar-kelas, Macro-F1 memberikan bobot evaluasi yang setara pada kelas minoritas (seperti SSH-Patator) maupun kelas mayoritas (BENIGN), menjadikannya metrik objektif paling andal untuk mengukur performa NIDS pada kondisi distribusi data yang timpang[24].

### 2.13.2 Retensi Memori
Dalam skenario pembelajaran berkelanjutan (*Continual Learning*), retensi pengetahuan model terhadap tugas lampau setelah mempelajari tugas baru diukur secara matematis menggunakan metrik **Backward Transfer (BWT)**[10]:

$$
\text{BWT} = R_{2, 1} - R_{1, 1}
$$

di mana $R_{1, 1}$ menyatakan skor Macro-F1 pada tugas pertama sesaat setelah fase pelatihan pertama selesai, sedangkan $R_{2, 1}$ merepresentasikan skor Macro-F1 pada tugas pertama setelah model menyelesaikan pelatihan pada tugas kedua. Nilai $\text{BWT} < 0$ mengindikasikan terjadinya degradasi representasi memori atau *catastrophic forgetting*, di mana semakin negatif nilai BWT maka semakin parah derajat kepunahan memori model terhadap ancaman lampau. Sebaliknya, nilai $\text{BWT} \ge 0$ membuktikan bahwa model mampu mempertahankan representasi tugas lama secara stabil atau bahkan mengalami transfer pengetahuan positif (*positive backward transfer*)[10].

### 2.13.3 Efisiensi Sumberdaya
Di samping evaluasi kinerja klasifikasi, pengukuran efisiensi komputasi menjadi parameter penentu kelayakan sistem NIDS saat dioperasikan secara nyata pada perangkat jaringan, mengadopsi standar profiling yang dirumuskan pada penelitian teknik elektro terdahulu[16]. Profiling ini mencakup tiga parameter utama. Parameter pertama adalah **Waktu Inferensi per Aliran (*Inference Time*)**, yang mengukur rata-rata durasi eksekusi algoritma dalam memproses dan mengklasifikasikan satu sampel aliran data jaringan:

$$
\text{Inference Time} = \frac{T_{\text{total}}}{N_{\text{flows}}} \quad (\mu\text{s/flow})
$$

Pengukuran waktu inferensi dilakukan dengan menerapkan fase pemanasan (*warm-up phase*) untuk menstabilkan alokasi memori *cache*, kemudian waktu diukur secara presisi menggunakan pewaktu resolusi nanodetik (`time.perf_counter_ns()`) melintasi 10.000 aliran data uji independen. Parameter kedua adalah **Konsumsi Memori RAM (*Memory Footprint*)**, yang mengukur alokasi memori fisik puncak selama fase pelatihan lokal dan penyimpanan bobot, membuktikan efisiensi memori EWC (hanya menyimpan vektor diagonal Fisher $\approx 24,84$ KB) dibandingkan metode *Experience Replay* yang membutuhkan *buffer* data mentah puluhan megabita. Parameter ketiga adalah **Beban Komunikasi Jaringan (*Communication Overhead*)**, yang menghitung total volume biner parameter model yang ditransmisikan antara node klien dan server agregator per putaran federasi:

$$
\text{Payload} = 2 \times |\theta| \times \text{sizeof}(\text{float32}) \quad (\text{KB})
$$

Parameter ini menunjukkan efisiensi protokol gRPC Flower dalam meminimalkan beban lebar pita jaringan selama kolaborasi terdistribusi berlangsung, di mana estimasi teoretis ukuran bobot float32 $\approx 24,84$ KB per transmisi akan diverifikasi pengukurannya pada tahap pengujian eksperimental sistem[16], [22].

---

## 2.14 Hyperparameter Tuning

Penyetelan hiperparameter (*hyperparameter tuning*) merupakan tahapan metodologis yang sangat kritis dalam menentukan stabilitas konvergensi, kapasitas generalisasi, dan efektivitas retensi memori model deteksi intrusi[25], [26]. Berbeda dengan bobot parameter internal yang dioptimasi secara otomatis melalui propagasi balik gradien, hiperparameter (seperti koefisien penalti regularisasi EWC $\lambda$, laju pembelajaran $\eta$, ukuran *batch*, dan *weight decay*) berada di luar jangkauan gradien langsung dan harus dikonfigurasi sebelum proses pelatihan dimulai[25]. Metode pencarian konvensional seperti *Grid Search* menderita kutukan dimensi (*curse of dimensionality*) karena jumlah evaluasi meningkat secara eksponensial terhadap jumlah variabel, sedangkan *Random Search* tidak memanfaatkan riwayat evaluasi masa lalu untuk memandu penelusuran ruang parameter berikutnya[25], [26].

Untuk mengatasi keterbatasan tersebut, penelitian ini mengadopsi metode **Bayesian Optimization** terotomatisasi menggunakan kerangka kerja **Optuna** berbasis algoritma *Tree-structured Parzen Estimator* (TPE)[25], [26]. Berbeda dengan optimasi Bayesian berbasis Proses Gaussian (*Gaussian Process*) yang memodelkan fungsi objektif $p(y \mid x)$ secara langsung dengan kompleksitas kubik $\mathcal{O}(n^3)$, algoritma TPE memodelkan probabilitas kondisional konfigurasi parameter $x$ terhadap metrik performa validasi $y$ secara non-parametrik dengan membagi riwayat observasi menjadi dua fungsi densitas terpisah[25]:

$$
p(x \mid y) = \begin{cases} \ell(x), & \text{jika } y < y^{\ast} \\ g(x), & \text{jika } y \ge y^{\ast} \end{cases}
$$

di mana $y^{\ast}$ merepresentasikan nilai ambang kuantil performa objektif (misalnya persentil ke-15 terbaik), $\ell(x)$ adalah densitas probabilitas konfigurasi hiperparameter yang menghasilkan performa superior, dan $g(x)$ adalah densitas probabilitas konfigurasi yang menghasilkan performa inferior[25], [26]. Algoritma TPE kemudian memaksimalkan fungsi perolehan harapan (*Expected Improvement* / EI) dengan memilih kandidat konfigurasi $x$ yang memaksimumkan rasio perbandingan[25]:

$$
\text{EI}_{y^{\ast}}(x) = \frac{\gamma y^{\ast} \ell(x) - \ell(x) \int_{-\infty}^{y^{\ast}} p(y) dy}{\gamma \ell(x) + (1-\gamma) g(x)} \propto \left( \gamma + \frac{g(x)}{\ell(x)}(1-\gamma) \right)^{-1}
$$

Dengan memaksimalkan rasio $\frac{\ell(x)}{g(x)}$, TPE secara cerdas mengarahkan penelusuran ke wilayah ruang pencarian yang berpeluang tinggi menghasilkan skor Macro-F1 tertinggi pada subset validasi, menyeimbangkan secara presisi nilai koefisien penalti EWC $\lambda$ dan laju pembelajaran federasi dalam jumlah iterasi percobaan (*trials*) yang minimal[25], [26], sebagaimana diilustrasikan pada Gambar 2.8.

![Gambar 2.8 Pemodelan Distribusi Ketidakpastian pada Optimasi Bayesian Berbasis Estimator Parzen (TPE)](../Aset/bayesian_optimization_gp_optuna.png)  
*Gambar 2.8 Pemodelan Distribusi Ketidakpastian pada Optimasi Bayesian Berbasis Estimator Parzen (TPE)[25].*

---

## 2.15 Optimizer

Algoritma pengoptimalan (*optimizer*) bertugas memperbarui bobot parameter dan bias jaringan saraf tiruan $\theta$ di sepanjang permukaan fungsi kerugian empiris guna meminimalkan nilai galat prediksi selama proses perambatan balik (*backpropagation*)[27], [28]. Efisiensi konvergensi, ketahanan terhadap minima lokal, dan stabilitas representasi bobot model deteksi intrusi jaringan sangat bergantung pada pemilihan mekanisme optimasi gradien yang tepat[27].

### 2.15.1 Algoritma SGD
Algoritma *Stochastic Gradient Descent* (SGD) memperbarui parameter $\theta$ secara iteratif ke arah yang berlawanan dengan gradien fungsi kerugian yang dievaluasi pada *mini-batch* data[27]:

$$
\theta_{t+1} = \theta_t - \eta \nabla_\theta \mathcal{L}(\theta_t)
$$

di mana $\eta$ adalah laju pembelajaran (*learning rate*). Meskipun memiliki sifat teoritis yang elegan dan menghasilkan generalisasi akhir yang baik pada data IID, SGD murni rentan mengalami osilasi destruktif pada jurang permukaan fungsi kerugian yang memiliki kelengkungan tajam (*ravines*) dan bergerak sangat lambat pada dataran datar (*saddle points*)[27]. Guna memitigasi keterbatasan ini, mekanisme momentum klasik ($\beta$) diintegrasikan untuk mengakumulasi vektor kecepatan historis $v_t = \beta v_{t-1} + \eta \nabla_\theta \mathcal{L}(\theta_t)$, yang meredam osilasi melintang dan mempercepat laju konvergensi di sepanjang lembah fungsi kerugian[27].

### 2.15.2 Algoritma AdamW
Untuk mengatasi lambatnya adaptasi laju pembelajaran seragam pada SGD dan menyempurnakan kelemahan algoritma Adam standar, penelitian ini memanfaatkan algoritma optimasi **AdamW** (*Adam with Decoupled Weight Decay*)[28]. Algoritma Adam standar mengadaptasikan laju pembelajaran secara individual untuk setiap parameter berdasarkan estimasi momen pertama (rerata bergerak gradien $m_t$) dan momen kedua (rerata bergerak kuadratik gradien $v_t$)[27], [28]. Namun, sebagaimana dibuktikan oleh Loshchilov & Hutter[28], penerapan regularisasi penalti L2 konvensional pada Adam bercampur secara keliru dengan momen kedua gradien adaptif, yang menyebabkan parameter dengan gradien historis besar mengalami penyusutan bobot (*weight decay*) yang jauh lebih kecil daripada yang seharusnya. AdamW memecahkan masalah ini dengan memisahkan penalti pembusukan bobot (*decoupled weight decay*) $\lambda_{\text{wd}}$ secara langsung dari langkah pembaruan momen adaptif[28]:

$$
\begin{aligned}
m_t &= \beta_1 m_{t-1} + (1 - \beta_1) g_t \\
v_t &= \beta_2 v_{t-1} + (1 - \beta_2) g_t^2 \\
\hat{m}_t &= \frac{m_t}{1 - \beta_1^t}, \quad \hat{v}_t = \frac{v_t}{1 - \beta_2^t} \\
\theta_t &= \theta_{t-1} - \eta \left( \frac{\hat{m}_t}{\sqrt{\hat{v}_t} + \epsilon} + \lambda_{\text{wd}} \theta_{t-1} \right)
\end{aligned}
$$

Sebagaimana dibuktikan dalam studi tolok ukur komprehensif oleh Schmidt *et al.*[27], pemisahan pembusukan bobot pada AdamW memberikan stabilitas pelatihan yang superior, mencegah pembesaran magnitudo bobot yang tak terkendali, dan memfasilitasi konvergensi yang lebih cepat dan tangguh pada arsitektur jaringan terdistribusi.

---

## 2.16 Fungsi Aktivasi

Fungsi aktivasi merupakan komponen non-linear esensial dalam jaringan saraf tiruan yang memetakan kombinasi linear dari masukan terbobot pada setiap neuron menuju ruang representasi berikutnya[29], [30]. Tanpa keberadaan fungsi aktivasi non-linear, berapapun jumlah lapisan tersembunyi yang ditumpuk dalam arsitektur jaringan akan selalu dapat direduksi secara matematis menjadi satu transformasi linear tunggal ($W_3(W_2(W_1 x + b_1) + b_2) + b_3 = W'x + b'$), yang melenyapkan kemampuan model dalam mempelajari batas keputusan klasifikasi non-linear yang kompleks pada ruang fitur lalu lintas jaringan[23], [30].

### 2.16.1 Fungsi ReLU
Fungsi aktivasi utama yang diimplementasikan pada lapisan tersembunyi arsitektur MLP adalah *Rectified Linear Unit* (ReLU), yang diperkenalkan secara formal oleh Nair & Hinton[29] dan menjadi standar acuan arsitektur pembelajaran mendalam modern[30]:

$$
f(x) = \max(0, x)
$$

Keunggulan fundamental ReLU terletak pada efisiensi komputasinya yang sangat tinggi, di mana evaluasi fungsi aktivasi hanya membutuhkan operasi perbandingan ambang batas biner sederhana tanpa melibatkan fungsi transendental eksponensial yang membutuhkan daya komputasi intensif[29], [30]. Di samping itu, sebagaimana dianalisis oleh Dubey *et al.*[30], ReLU mengatasi fenomena hilangnya gradien (*vanishing gradient problem*) pada daerah masukan positif ($x > 0$) dengan mempertahankan turunan parsial konstan bernilai $1$ ($\frac{df}{dx} = 1$), memungkinkan sinyal gradien kesalahan merambat secara utuh melintasi lapisan-lapisan jaringan selama fase perambatan balik. Pemotongan nilai masukan negatif tepat pada angka nol ($0$) juga menghasilkan representasi aktivasi yang renggang (*sparse representation*), yang secara efektif menyaring fluktuasi derau (*noise*) pada aliran lalu lintas jaringan dan mempercepat laju konvergensi pelatihan[29], [30].

### 2.16.2 Fungsi Softmax
Pada lapisan keluaran klasifikasi, fungsi **Softmax** diterapkan untuk mentransformasikan vektor logit tak-ternormalisasi $z \in \mathbb{R}^C$ menjadi distribusi probabilitas posterior diskret $\hat{y} \in [0, 1]^C$ yang memenuhi aksioma probabilitas total[30]:

$$
\text{Softmax}(z_i) = \frac{e^{z_i}}{\sum_{j=1}^C e^{z_j}}, \quad \text{dengan } 0 \le \hat{y}_i \le 1 \quad \text{dan} \quad \sum_{j=1}^C \hat{y}_j = 1
$$

Operasi eksponensial pada Softmax memperbesar kontras pembeda antar-skor logit keluaran, sedangkan penyebut normalisasinya menjamin bahwa setiap elemen keluaran merepresentasikan estimasi probabilitas keyakinan model terhadap kelas alur lalu lintas jaringan (BENIGN, SSH-Patator, atau varian serangan DoS)[23], [30].

\newpage

# BAB 3 METODOLOGI

Bab ini menguraikan metode yang digunakan, bahan dan peralatan penelitian, alur urutan pelaksanaan penelitian, tahapan praproses data, arsitektur sistem terdistribusi yang diusulkan, penyetelan hiperparameter Bayesian, matriks skenario pengujian komparatif, mekanisme evaluasi, dan jadwal pelaksanaan kegiatan penelitian. Penelitian ini berfokus pada evaluasi integrasi *Federated Learning* (FL) dan *Continual Learning* (CL) berbasis *Elastic Weight Consolidation* (EWC) pada sistem deteksi intrusi jaringan (*Network Intrusion Detection System* / NIDS). Struktur penyusunan bab ini diselaraskan secara penuh dengan format Buku Pedoman Penyusunan Laporan Tugas/Proyek Akhir Program Sarjana dan Sarjana Terapan Departemen Teknik Elektro, FTEIC, Institut Teknologi Sepuluh Nopember (ITS) berdasarkan SK Rektor No. 280/IT2/T/HK.00.01/2022 serta rujukan tugas akhir alumnus Departemen Teknik Elektro FTEIC ITS ([Referensi-Skripsi-Hafizh.pdf](../Proposal/Referensi-Skripsi-Hafizh.pdf))[16].

---

## 3.1 Metode yang Digunakan

Penelitian ini mengembangkan sistem deteksi intrusi jaringan terdistribusi dan adaptif berbasis *Federated Continual Learning* (FCL) yang menggabungkan algoritma *Federated Averaging* (FedAvg)[3] dan regularisasi *Elastic Weight Consolidation* (EWC)[5] dengan arsitektur *Multilayer Perceptron* (MLP) kompak untuk mengatasi degradasi memori katastrofik (*catastrophic forgetting*) pada kondisi data heterogen (*non-IID*) dan aliran serangan yang muncul secara sekuensial. Metodologi ini dirancang secara khusus untuk mengatasi dua dilema utama dalam keamanan siber modern:
1. **Dilema Privasi dan Isolasi Data:** Keharusan menjaga kerahasiaan data lalu lintas internal tanpa memindahkan rekaman paket mentah ke server eksternal, yang diselesaikan melalui paradigma *Federated Learning*.
2. **Dilema Stabilitas vs Plastisitas (*Stability-Plasticity Dilemma*):** Kecenderungan jaringan saraf tiruan untuk menimpa representasi serangan lama saat mempelajari serangan baru secara berkelanjutan, yang diselesaikan melalui regularisasi penalti kuadratik EWC berbasis Matriks Informasi Fisher diagonal tanpa memerlukan memori penyangga (*replay buffer*).

```mermaid
flowchart TD
    subgraph Enterprise_Network [Topologi Penempatan Sensor NIDS Terdistribusi]
        subgraph Subnet_A [Subnet A: Server Internal Enterprise]
            GW_A[Edge Gateway A / Sensor NIDS Klien A]
            SRV_SSH[Server Autentikasi: Layanan SSH Port 22]
            GW_A -->|Monitoring Aliran Lokal| SRV_SSH
        end
        subgraph Subnet_B [Subnet B: Demilitarized Zone / DMZ]
            GW_B[Edge Gateway B / Sensor NIDS Klien B]
            SRV_WEB[Web Server Publik: Layanan HTTP Port 80]
            GW_B -->|Monitoring Aliran Lokal| SRV_WEB
        end
        subgraph Orchestration_Layer [Lapisan Agregasi Privasi]
            FL_SRV[Server Agregator FedAvg Pusat]
        end
        GW_A <-->|Pertukaran Parameter Bobot Theta_A| FL_SRV
        GW_B <-->|Pertukaran Parameter Bobot Theta_B| FL_SRV
    end
```
*Gambar 3.1 Arsitektur Penempatan Sensor NIDS Terdistribusi dalam Jaringan Enterprise.*

Untuk mengidentifikasi akar penyebab kegagalan NIDS terdistribusi dan merumuskan solusi teknis yang sistematis, disusun diagram sebab-akibat (*Fishbone Diagram*) sebagaimana diilustrasikan pada Gambar 3.2.

![Gambar 3.2 Fishbone Diagram Identifikasi Tantangan NIDS Terdistribusi](../Aset/fishbone_diagram_tantangan_nids.png)  
*Gambar 3.2 Fishbone Diagram Identifikasi Tantangan NIDS Terdistribusi.*

---

## 3.2 Bahan dan Peralatan yang Digunakan

### 3.2.1 Bahan Penelitian (Dataset Publik CIC-IDS2017)
Bahan utama yang digunakan dalam penelitian ini adalah dataset tolok ukur resmi **CIC-IDS2017** dari Canadian Institute for Cybersecurity[7]. Data merekam lalu lintas jaringan nyata selama lima hari kerja (Senin s.d. Jumat). Berkas yang digunakan secara spesifik adalah:
1. `Monday-WorkingHours.pcap_ISCX.csv`: 529.918 baris lalu lintas normal murni (BENIGN).
2. `Tuesday-WorkingHours.pcap_ISCX.csv`: 445.909 baris memuat serangan penetrasi autentikasi SSH (*SSH-Patator*).
3. `Wednesday-workingHours.pcap_ISCX.csv`: 692.703 baris memuat serangan *Denial of Service* (DoS Hulk, GoldenEye, slowloris, slowhttptest).

Berkas hari Kamis dan Jumat dieksklusi karena menderita desinkronisasi timestamp pelabelan yang parah serta kelangkaan sampel mikro ekstrem[13], [14].

### 3.2.2 Peralatan Penelitian (Perangkat Keras dan Perangkat Lunak)
Pengujian dan evaluasi performa sistem dalam penelitian ini dirancang melalui strategi evaluasi dua tahap progresif (*two-stage progressive evaluation strategy*):
1. **Tahap 1: Pengujian dan Validasi Simulasi Lokal (*Local Simulation and Algorithm Verification*):** Dilaksanakan pada mesin kerja pengembang untuk memvalidasi fungsionalitas algoritma, prapengolahan 62 fitur numerik bersih, simulasi multi-klien secara *in-memory* menggunakan Flower *Virtual Client Engine*, penalaan hiperparameter Bayesian EWC ($\lambda$) via Optuna TPE, serta memastikan stabilitas gradien dan konvergensi model sebelum diimplementasikan pada lingkungan klaster server fisik.
2. **Tahap 2: Pengujian Implementasi Testbed Terdistribusi (*Distributed Private Cloud Server Testbed*):** Dilaksanakan pada klaster *private cloud* Proxmox Virtual Environment (PVE) 3-node *bare-metal*. Mengacu pada batasan masalah dan kesepakatan ruang lingkup penelitian, implementasi testbed server **secara khusus menggunakan tiga (3) instans komputasi inti**, yaitu satu Server Agregator dan dua Klien Sensor Terdistribusi. Peniadaan injeksi lalu lintas aktif dan penangkapan paket waktu nyata (*live sniffing*) bertujuan mengeliminasi faktor pengganggu (*confounding variables*) seperti hilangnya paket (*packet drops*), *buffer overrun*, dan fluktuasi latensi (*jitter*), sehingga seluruh node klien membaca data partisi tabular CIC-IDS2017 bersih langsung dari media penyimpanan lokal masing-masing secara terisolasi dan deterministik.

Rincian spesifikasi perangkat keras dan perangkat lunak untuk kedua lingkungan pengujian tersebut disajikan pada Tabel 3.1.

*Tabel 3.1 Spesifikasi Lingkungan Perangkat Keras dan Perangkat Lunak.*

| Lingkungan / Node | Komponen | Spesifikasi Teknis | Peran dan Fungsi Utama |
| :--- | :--- | :--- | :--- |
| **A. Lingkungan Pengujian Lokal (Mesin Pengembang)** | Unit Perangkat | Laptop Komputasi Pengembang | Pengembangan, validasi unit, dan simulasi algoritma awal |
| | Prosesor (CPU) | Intel® Core™ i5-8350U @ 1.70 GHz (4 Cores, 8 Threads, Turbo 3.60 GHz, 6 MB Cache) | Komputasi pelatihan lokal dan kalkulasi FIM berbasis CPU (AVX2) |
| | Memori Utama (RAM) | 16 GB DDR4 (15.84 GB usable, 2400 MHz) | Penyimpanan data latih in-memory dan eksekusi virtual client FL |
| | Kartu Grafis (GPU) | Intel® UHD Graphics 620 (Shared memory) | Rendering visualisasi metrik dan evaluasi grafik analitik |
| | Media Penyimpanan | 512 GB NVMe M.2 SSD | Penyimpanan lokal repositori kode, cache data, dan checkpoint |
| | Sistem Operasi | Microsoft Windows 11 Pro 64-bit | Sistem operasi host pengembangan |
| | Lingkungan & Runtime | Python 3.10+ / 3.11 dalam Virtual Environment (`venv`) | Eksekusi skrip praproses, pemodelan PyTorch, dan optimasi |
| | Kerangka Kerja DL & FL | PyTorch 2.2+[21], Flower (`flwr` $\ge 1.7.0$)[22] | Pembangun arsitektur MLP dan simulasi federasi in-process |
| | Penyetelan Bayesian | Optuna Framework ($\ge 3.5.0$)[25] | Optimasi hiperparameter $\lambda$ EWC dan laju pembelajaran |
| | Pustaka Analisis Data | Pandas, NumPy, Scikit-learn, Matplotlib, Seaborn | Pembersihan data, scaling Z-score, dan kalkulasi metrik evaluasi |
| **B. Lingkungan Testbed Private Cloud Server (Proxmox VE Cluster)** | Infrastruktur Fisik Klaster (*Bare-Metal*) | 3 Node Server Fisik: 2x Dell PowerEdge R630 dan 1x Dell PowerEdge R760xs | Penyedia komputasi tervirtualisasi multi-node terdistribusi |
| | Pengendali Penyimpanan | Dell PERC H755 Adp / H730 RAID Controller, LVM-Thin pools 1.20 TB NVMe/SSD | Provisi disk dinamis dan mekanisme snapshot/rollback |
| | Infrastruktur Jaringan | Dual LACP Bond, Bridge internal L2 datar (subnet `10.10.0.0/16`), Bridge manajemen (`192.168.30.0/24`) | Komunikasi gRPC berlatensi rendah dan isolasi data jaringan |
| | **Server Agregator Global** | Ubuntu Server 24.04 LTS (LXC Container), 4 vCPU, 8 GB RAM, 2 GB Swap, 50 GB Disk | Menjalankan Flower Server (FedAvg), orkestrasi gRPC over TLS (port 8080), agregasi parameter, dan checkpoint model global |
| | **Sensor NIDS Klien A** | Ubuntu Server 24.04 LTS (KVM Virtual Machine), 8 vCPU, 16 GB RAM, 100 GB SCSI Disk | Menjalankan Flower Client Klien A, PyTorch MLP, pelatihan lokal Fase 1 (Normal + SSH-Patator) dan Fase 2 (Normal dengan penalti EWC), serta kalkulasi FIM |
| | **Sensor NIDS Klien B** | Ubuntu Server 24.04 LTS (KVM Virtual Machine), 8 vCPU, 16 GB RAM, 100 GB SCSI Disk | Menjalankan Flower Client Klien B, PyTorch MLP, pelatihan lokal Fase 1 (Normal) dan Fase 2 (Normal + DoS) |
| | Penyimpanan Data Klien | Partisi data offline tabular CIC-IDS2017 pada disk lokal masing-masing VM (~670K sampel Klien A, ~860K sampel Klien B) | Meniadakan risiko dropped-packet dan memastikan replikasi data identik bebas interferensi jaringan eksternal |
| | Pustaka Eksekusi & ML | Python 3.11+, PyTorch 2.x[21], Flower (`flwr` $\ge 1.7.0$)[22], Scikit-learn, Pandas | Runtime eksekusi pelatihan lokal dan pertukaran parameter gRPC |
| *Catatan Batasan Sistem:* | *Eksklusi Komponen Tambahan* | *Pembangkit lalu lintas aktif sintetis dan penangkapan paket live ditiadakan* | *Fokus murni pada optimasi algoritma FL-CL berbasis dataset benchmark terkalibrasi* |

---

## 3.3 Urutan Pelaksanaan Penelitian

Alur urutan pelaksanaan penelitian disusun ke dalam tahapan yang sistematis dan terstruktur mulai dari persiapan data hingga analisis hasil akhir, sebagaimana disajikan pada diagram alir Gambar 3.3.

```mermaid
flowchart TD
    S([Mulai]) --> S1[3.3.1 Praproses Data: 62 Fitur Bersih & Non-IID]
    S1 --> S2[3.3.2 Pengembangan Model Dasar: MLP Kompak 6.211 Param]
    S1 --> S3[3.3.3 Integrasi Sistem Usulan: FedAvg + EWC pada Flower]
    S2 --> S3
    S3 --> S4[3.3.4 Penyetelan Hiperparameter Bayesian: Optuna TPE]
    S4 --> S5[3.3.5 Eksekusi Matriks Pengujian E0 - E4 Multi-Seed]
    S5 --> S6[3.3.6 Evaluasi Metrik Deteksi, BWT, dan Profiling]
    S6 --> E([Selesai])
```
*Gambar 3.3 Diagram Alir Urutan Pelaksanaan Penelitian.*

### 3.3.1 Praproses Data dan Ekstraksi 62 Fitur Numerik
Tahapan praproses data dirancang secara ketat untuk mentransformasikan data mentah menjadi format masukan yang bersih, representatif, dan bebas bias *shortcut learning*.

```mermaid
flowchart TD
    P1[Data Preparation: Akuisisi CSV Senin-Rabu] --> P2[Data Cleaning: Strip Whitespace & Drop Inf/NaN/Duplicates]
    P2 --> P3[Feature Engineering: Drop 10 Konstan, 5 Duplikat, Drop Port]
    P3 --> P4[Data Transformation: Federated Global Feature Scaling Z-Score]
    P4 --> P5[Partisi Data Terdistribusi: 50/50 Normal Non-IID Dua Klien]
    P5 --> P6[Penanganan Ketimpangan Kelas: Weighted Loss & Clipping]
```
*Gambar 3.4 Diagram Alur Global Data Preprocessing.*

1. **Pembersihan Data (*Data Cleaning*):** Nama kolom distandardisasi (*whitespace trimming*). Nilai `+Infinity`, `-Infinity`, dan nilai kosong dikonversi ke `NaN` lalu dieliminasi (1.995 baris). Sebanyak 138.098 baris data duplikat identik dieliminasi secara penuh pada ruang 78 fitur statistik pra-seleksi sehingga tersisa **1.520.488 baris aliran unik bersih** (verifikasi empiris ulang 2026-10-21; angka praproses terdahulu 132.909/1.529.677 berasal dari run sebelumnya dan telah diperbarui). Selama pembersihan, audit eksplisit juga mendeteksi **konflik lintas-label**: baris-baris dengan vektor fitur identik namun label berbeda - 4.486 baris pada 74 grup vektor di ruang 78 fitur (didominasi satu grup besar berisi 3.361 aliran campuran `Normal`/`DoS`; tidak ditemukan konflik pada kelas SSH-Patator). Temuan ini merupakan hasil audit empiris mandiri studi; sebagai konteks cacat dataset, Engelen et al. (2021) telah mendokumentasikan kesalahan konstruksi aliran dan penempelan label pada pipeline ekstraksi CICFlowMeter CIC-IDS2017 (lebih dari 20% *trace* direkonstruksi/relabeled), namun duplikasi vektor fitur lintas-label tidak dibahas secara spesifik dalam paper tersebut - sehingga temuan ini dilaporkan sebagai kontribusi audit mandiri, bukan sebagai reproduksi klaim Engelen et al. Secara default, mekanisme `keep="first"` mempertahankan satu baris pertama tiap grup fitur apa pun labelnya (1.520.488 baris); eliminasi penuh ke-4.486 baris konflik tersedia sebagai opsi eksplisit `--drop-conflicting-labels` pada skrip praproses (menghasilkan 1.520.414 baris), dengan dasar pemilihan perilaku terdokumentasi pada docstring skrip tersebut.
2. **Rekayasa Fitur (*Feature Engineering*):**
   - 10 fitur bernilai konstan 0 dieliminasi (`Bwd PSH Flags`, `Fwd URG Flags`, `Bwd URG Flags`, `CWE Flag Count`, `Fwd Avg Bytes/Bulk`, `Fwd Avg Packets/Bulk`, `Fwd Avg Bulk Rate`, `Bwd Avg Bytes/Bulk`, `Bwd Avg Packets/Bulk`, `Bwd Avg Bulk Rate`).
   - 5 kolom duplikat identik via hash dibuang (`Fwd Header Length.1`, `Subflow Fwd Bytes`, `Subflow Fwd Packets`, `Subflow Bwd Packets`, `SYN Flag Count`).
   - **Eliminasi Destination Port:** Fitur `Destination Port` **secara sengaja dibuang** untuk memitigasi bias *port leakage* dan memaksa model mempelajari karakteristik statistik dinamika paket murni[15].
   - Dihasilkan **62 fitur statistik numerik bersih** ditambah 1 label (Tabel 3.2).
3. **Transformasi Data (*Scaling*):** Pada lingkungan pembelajaran terdistribusi yang menjaga privasi, data mentah tidak boleh disatukan. Untuk menghindari disparitas ruang fitur (*feature space mismatch*) akibat perbedaan sebaran statistik non-IID antar-klien, standardisasi Z-score ($z = \frac{x - \mu}{\sigma}$) dihitung melalui **Federated Global Feature Scaling** berbasis ringkasan statistik agregat terdesentralisasi:
   - Sebelum pelatihan dimulai (Ronde 0), setiap klien $k \in \{A, B\}$ menghitung ringkasan statistik lokal tanpa mentransfer data mentah: jumlah sampel $n_k$, jumlah nilai tiap fitur $S_{1, k} = \sum_{j=1}^{n_k} x_{j}$, dan jumlah kuadrat nilai tiap fitur $S_{2, k} = \sum_{j=1}^{n_k} x_{j}^2$.
   - Server agregator menghitung rata-rata global $\mu_{\text{global}} = \frac{S_{1, A} + S_{1, B}}{n_A + n_B}$ dan variansi global $\sigma_{\text{global}}^2 = \frac{S_{2, A} + S_{2, B}}{n_A + n_B} - \mu_{\text{global}}^2$.
   - Vektor parameter $\mu_{\text{global}}$ dan $\sigma_{\text{global}}$ disiarkan kembali ke seluruh klien untuk mentransformasikan data latih lokal serta disimpan pada server untuk menskalakan *test set* evaluasi global. Seluruh node mengevaluasi model pada ruang representasi fitur yang identik secara seragam tanpa pernah membocorkan data lalu lintas mentah.
4. **Partisi Non-IID dan Alokasi Fase Pembelajaran:** Seluruh aliran `BENIGN` digabungkan; 20% dipisahkan lebih dahulu sebagai *global held-out test* terstratifikasi (264.712 aliran Normal), lalu 50% sisanya dibagi acak untuk **Klien A** (529.424 aliran) dan **Klien B** (529.425 aliran) guna mencegah bias hari perekaman. Klien A bertindak sebagai sensor perimeter subnet internal yang memegang data serangan **SSH-Patator** (3.219 aliran total; 2.575 pada partisi Klien A dan 644 pada held-out test global). Klien B bertindak sebagai sensor perimeter DMZ yang memegang data serangan **DoS** (193.708 aliran total; 154.966 pada partisi Klien B dan 38.742 pada held-out test global). Pembagian data per fase pembelajaran sekuensial dirangkum pada Tabel 3.3. *(Seluruh angka pada butir ini diverifikasi langsung dari artefak parquet hasil praproses, 2026-10-21.)*
5. **Penanganan Ketimpangan Kelas:** Rasio perbandingan kelas Normal terhadap SSH-Patator mencapai $\approx 411 : 1$ (1.323.561 terhadap 3.219 aliran pasca-deduplikasi). Guna mencegah model terbias terhadap kelas mayoritas, diterapkan **Weighted Cross-Entropy Loss** yang dipadukan dengan pemotongan gradien (*Gradient Clipping* norm $\le 1.0$). Bobot penalti kelas $w_c$ **dihitung secara global** dari agregasi total jumlah alur tiap kelas lintas seluruh klien ($N_c = \sum_k n_{k,c}$):

$$
w_c = \frac{N_{\text{total}}}{C \cdot N_c}
$$

di mana $N_{\text{total}} = \sum_{c=0}^{C-1} N_c$ dan $C=3$. Penghitungan bobot secara global ini mutlak diperlukan karena pada partisi non-IID ekstrem, klien tertentu (seperti Klien B pada Fase 1 yang hanya memegang alur Normal) tidak memiliki sampel kelas serangan SSH-Patator, sehingga penghitungan bobot secara lokal akan menghasilkan nilai bobot yang tidak seimbang atau terdefinisi tunggal (inversi frekuensi lokal Normal bernilai 1,0, mengabaikan kelas lainnya).

*Tabel 3.2 Ringkasan 62 Fitur Statistik Numerik Aliran Bersih CIC-IDS2017.*

| Kategori Fitur | Jumlah | Nama Fitur |
| :--- | :---: | :--- |
| **Statistik Waktu & Durasi** | 5 | `Flow Duration`, `Flow IAT Mean`, `Flow IAT Std`, `Flow IAT Max`, `Flow IAT Min` |
| **Inter-Arrival Time (IAT)** | 10 | `Fwd IAT Total`, `Fwd IAT Mean`, `Fwd IAT Std`, `Fwd IAT Max`, `Fwd IAT Min`, `Bwd IAT Total`, `Bwd IAT Mean`, `Bwd IAT Std`, `Bwd IAT Max`, `Bwd IAT Min` |
| **Statistik Paket Maju (Fwd)** | 8 | `Total Fwd Packets`, `Total Length of Fwd Packets`, `Fwd Packet Length Max`, `Fwd Packet Length Min`, `Fwd Packet Length Mean`, `Fwd Packet Length Std`, `Fwd Header Length`, `act_data_pkt_fwd` |
| **Statistik Paket Balik (Bwd)** | 7 | `Total Backward Packets`, `Total Length of Bwd Packets`, `Bwd Packet Length Max`, `Bwd Packet Length Min`, `Bwd Packet Length Mean`, `Bwd Packet Length Std`, `Bwd Header Length` |
| **Kecepatan Transfer (Rates)** | 4 | `Flow Bytes/s`, `Flow Packets/s`, `Fwd Packets/s`, `Bwd Packets/s` |
| **Statistik Ukuran Paket** | 7 | `Min Packet Length`, `Max Packet Length`, `Packet Length Mean`, `Packet Length Std`, `Packet Length Variance`, `Average Packet Size`, `Avg Fwd Segment Size` |
| **Bendera TCP (Flags)** | 7 | `FIN Flag Count`, `RST Flag Count`, `PSH Flag Count`, `ACK Flag Count`, `URG Flag Count`, `ECE Flag Count`, `Fwd PSH Flags` |
| **Karakteristik Segmen & Jendela** | 6 | `Down/Up Ratio`, `Avg Bwd Segment Size`, `Subflow Bwd Bytes`, `Init_Win_bytes_forward`, `Init_Win_bytes_backward`, `min_seg_size_forward` |
| **Aktivitas Temporal Aktif** | 4 | `Active Mean`, `Active Std`, `Active Max`, `Active Min` |
| **Aktivitas Temporal Idle** | 4 | `Idle Mean`, `Idle Std`, `Idle Max`, `Idle Min` |
| **Total Fitur Input** | **62** | *Seluruhnya bertipe numerik kontinu / diskret* |

*Tabel 3.3 Alokasi Partisi Data Non-IID dan Peran Klien pada Setiap Fase Pembelajaran.*

| Entitas / Node | Karakteristik Perimeter Sensor | Fase 1 (Task 1: Penetrasi Autentikasi SSH) | Fase 2 (Task 2: Serangan Volumetrik DoS) | Peran Modul EWC & Retensi Memori |
| :--- | :--- | :--- | :--- | :--- |
| **Klien A** | Sensor Subnet Administrasi Internal | Data Latih: **Normal (50%) + SSH-Patator (100%)** (425.599 sampel: 423.539 Normal + 2.060 SSH) | Data Latih: **Normal (50%)** (423.539 sampel Normal) | Menghitung Matriks Informasi Fisher diagonal $F_A$ pada akhir Fase 1; menerapkan penalti kuadratik EWC pada Fase 2 untuk membatasi pergeseran bobot representasi SSH-Patator. |
| **Klien B** | Sensor Perimeter DMZ / Web Server | Data Latih: **Normal (50%)** (423.539 sampel Normal) | Data Latih: **Normal (50%) + DoS (100%)** (547.512 sampel: 423.539 Normal + 123.973 DoS) | Mempelajari representasi lalu lintas Normal pada Fase 1; mempelajari representasi serangan DoS pada Fase 2; menjaga stabilitas model bersama saat menerima penalti gradien dari model global. |
| **Server Agregator** | Server Agregasi Terpusat (Flower FedAvg) | Mengagregasi pembaruan bobot $\theta_r^A$ dan $\theta_r^B$ selama $R_1$ ronde | Mengagregasi pembaruan bobot $\theta_r^A$ dan $\theta_r^B$ selama $R_2$ ronde | Menghasilkan model global terpadu $\theta$ yang menguasai deteksi Normal, SSH-Patator, dan DoS secara simultan. |

### 3.3.2 Pengembangan Model Dasar MLP Kompak
Model klasifikasi dirancang menggunakan **Multilayer Perceptron (MLP)** kompak tiga lapis terhubung penuh (`Input(62) → Linear(64) → ReLU → Linear(32) → ReLU → Linear(3)`). Model ini hanya memiliki 6.211 parameter bobot ($\approx 24,8$ KB) sehingga sangat ringan untuk pertukaran parameter jaringan pada node klien terdistribusi tanpa membebani kapasitas komputasi maupun *bandwidth* komunikasi.

### 3.3.3 Integrasi Sistem Usulan: FedAvg dan EWC pada Lingkungan Terdistribusi
Mekanisme mitigasi *catastrophic forgetting* diimplementasikan dengan menambahkan modul kalkulasi **Matriks Informasi Fisher (FIM) diagonal** pada klien lokal setelah menyelesaikan pelatihan Task 1[5]. Saat mempelajari Task 2, klien menambahkan penalti kuadratik EWC ke fungsi kerugian lokal sebelum bobot diagregasi oleh server pusat menggunakan algoritma *Federated Averaging* (FedAvg)[3], sebagaimana diilustrasikan pada Gambar 3.5.

```mermaid
graph TB
    subgraph Server_Global [Server Agregator Global Flower]
        GW[Parameter Global W_t]
        ENG[FedAvg Aggregation Engine]
        EVAL[Global Test Evaluation: Held-Out Benchmark Artifact]
    end

    subgraph Client_A [Node Sensor A: Subnet Administrasi]
        DA1[(Fase 1: Normal 50% + SSH)]
        DA2[(Fase 2: Normal 50%)]
        LA["Loss: Weighted-CE + Penalti Kuadratik EWC"]
        MA[MLP Model A: Input 62 - 64 - 32 - 3]
        FA[FIM Calculator Task 1: Fisher F_A]
    end

    subgraph Client_B [Node Sensor B: Perimeter DMZ]
        DB1[(Fase 1: Normal 50%)]
        DB2[(Fase 2: Normal 50% + DoS)]
        LB["Loss: Weighted-CE Loss"]
        MB[MLP Model B: Input 62 - 64 - 32 - 3]
    end

    GW -->|Distribusi Bobot Global| MA
    GW -->|Distribusi Bobot Global| MB
    MA -->|Pembaruan Bobot Lokal Theta_A| ENG
    MB -->|Pembaruan Bobot Lokal Theta_B| ENG
    ENG --> GW
    GW -.-> EVAL
```
*Gambar 3.5 Arsitektur Sistem Federated Continual Learning yang Diimplementasikan.*

**Klarifikasi Evaluasi Global (*Evaluation Benchmark Artifact*):**
Komponen evaluasi global (*Global Test Evaluation*) pada server Flower bukanlah data operasional yang dimiliki oleh server dalam skenario implementasi nyata, melainkan merupakan **artefak tolok ukur eksperimental (*experimental benchmark artifact*)** yang dibentuk dari gabungan 20% data uji terstratifikasi (*held-out test set*) global yang dipisahkan sebelum partisi klien. Data uji ini disimpan terisolasi di sisi server murni untuk mengukur metrik ilmiah (Macro-F1, Recall per-kelas, dan BWT) terhadap representasi model global $\theta_r$ di setiap akhir ronde atau fase, mengadopsi standar metodologis tolok ukur *Federated Learning* (McMahan et al., 2017; Caldas et al., 2018).

**Hipotesis Pengenceran EWC oleh FedAvg (*EWC Dilution Effect*) & Analisis Sensitivitas:**
Karena penalti Fisher $F_A$ ditambatkan pada Klien A, sedangkan Klien B melakukan pembaruan gradien terhadap kelas serangan baru (DoS) dengan volume data yang lebih besar ($n_B \approx 547.512 > n_A \approx 425.599$ berdasarkan jumlah sampel latih aktual), proses agregasi rata-rata tertimbang FedAvg di server berpotensi mengencerkan (*dilute*) efek pengekangan bobot EWC pada model global. Untuk menginvestigasi fenomena ini, penelitian menyertakan **analisis sensitivitas** terhadap: (1) magnitudo hiperparameter penalti $\lambda$ (menguji apakah diperlukan nilai $\lambda$ yang lebih agresif pada FL terdistribusi dibanding sentralisasi untuk mempertahankan retensi memori), dan (2) skema bobot agregasi federasi.

**Klarifikasi Dimensi Spasial vs Temporal (*Spatial Non-IID* vs *Task Sequence*):** Dua mekanisme pembagian dalam desain ini harus dipisahkan secara konseptual. (1) Dimensi **spasial** non-IID - pembagian Klien A (perimeter internal: seluruh data SSH-Patator) versus Klien B (perimeter DMZ: seluruh data DoS) - mengatur *siapa* yang memegang kelas serangan tertentu pada satu titik waktu. (2) Dimensi **temporal** sekuensial - perpindahan Fase 1 → Fase 2 - mengatur *kapan* pengetahuan harus dipertahankan. Pada Klien A, Fase 2 tidak memperkenalkan kelas baru (hanya lalu lintas Normal), sehingga tekanan *catastrophic forgetting* muncul karena bobot global terus diperbarui oleh Klien B yang sedang mempelajari DoS dengan volume data lebih besar - bukan karena Klien A sendiri menerima target baru. Memori temporal dikunci pada akhir Fase 1 di penyimpanan lokal Klien A dalam dua artefak imutabel: parameter jangkar $\theta_1^*$ (ronde $R_1$; lihat baris 8–9 Algoritma 3.1) dan diagonal Matriks Informasi Fisher $F_A$ (baris 10) - keduanya tidak pernah dikirim ke server maupun ke Klien B. Pada setiap ronde Fase 2, penalti EWC bekerja **hanya di ruang gradien lokal** Klien A sebelum pembaruan bobot dikirim ke server; server murni menjalankan agregasi FedAvg rata-rata tertimbang tanpa mengetahui keberadaan Fisher, sehingga efek pengencangan penalti pada model global sepenuhnya bergantung pada bobot agregasi Klien A ($n_A/n$) - inilah dasar hipotesis pengenceran (*EWC Dilution Effect*) yang diinvestigasi pada subbab ini.

Secara matematis dan algoritmik, prosedur eksekusi *Federated Continual Learning* memadukan mekanisme agregasi FedAvg dan regularisasi penalti Fisher lokal EWC, sebagaimana dirumuskan pada Algoritma 3.1.

#### **Algoritma 3.1: Prosedur Pelatihan Federated Continual Learning (FedAvg + EWC)**

```text
Masukan:
  - Partisi Data Klien: D_{A, Fase1} (Normal + SSH), D_{A, Fase2} (Normal),
                        D_{B, Fase1} (Normal), D_{B, Fase2} (Normal + DoS)
  - Ronde Federasi: R1 (Fase 1: SSH-Patator) dan R2 (Fase 2: DoS)
  - Hiperparameter Lokal: Epoch E, Ukuran Batch B, Laju Pembelajaran eta, Penalti EWC lambda

FASE 1: Pelatihan Kolaboratif Terdistribusi Penetrasi Autentikasi SSH
 1: Server menginisialisasi parameter bobot global theta_0
 2: Untuk setiap ronde federasi r = 0, 1, ..., R1 - 1:
 3:     Server menyiarkan parameter global theta_r ke Klien A dan Klien B
 4:     Klien A mengeksekusi: theta_{r+1}^A <- LocalUpdate(A, theta_r, Loss_WCE(D_{A, Fase1}))
 5:     Klien B mengeksekusi: theta_{r+1}^B <- LocalUpdate(B, theta_r, Loss_CE(D_{B, Fase1}))
 6:     Klien A dan B mengirimkan theta_{r+1}^k kembali ke Server
 7:     Server memperbarui bobot global via agregasi FedAvg:
            theta_{r+1} <- (n_A / n) * theta_{r+1}^A + (n_B / n) * theta_{r+1}^B
 8: Server menetapkan parameter referensi optimal Fase 1: theta_1* <- theta_{R1}
 9: Server mengirimkan theta_1* ke Klien A
10: Klien A membekukan theta_1* dan menghitung Matriks Informasi Fisher diagonal F_A:
        F_{A, i} <- (1 / N_fisher) * sum_{n=1}^{N_fisher} [ (d Loss_CE(f(x_n; theta_1*), y_n) / d theta_i) ]^2

FASE 2: Pelatihan Kolaboratif Terdistribusi Serangan Volumetrik DoS dengan Proteksi EWC
11: Untuk setiap ronde federasi r = R1, R1 + 1, ..., R1 + R2 - 1:
12:     Server menyiarkan parameter global theta_r ke Klien A dan Klien B
13:     Klien A mengeksekusi pelatihan lokal dengan penalti kuadratik EWC:
            Loss_total^A(theta) = Loss_CE(theta; D_{A, Fase2}) + (lambda / 2) * sum_i F_{A, i} (theta_i - theta_{1, i}^{\ast})^2
            theta_{r+1}^A <- LocalUpdate(A, theta_r, Loss_total^A)
14:     Klien B mengeksekusi pelatihan lokal serangan DoS:
            Loss_total^B(theta) = Loss_WCE(theta; D_{B, Fase2})
            theta_{r+1}^B <- LocalUpdate(B, theta_r, Loss_total^B)
15:     Klien A dan B mengirimkan theta_{r+1}^k kembali ke Server
16:     Server memperbarui bobot global via agregasi FedAvg:
            theta_{r+1} <- (n_A / n) * theta_{r+1}^A + (n_B / n) * theta_{r+1}^B

Keluaran:
  - Model global terpadu theta_final = theta_{R1 + R2} yang tangguh mendeteksi Normal, SSH-Patator, dan DoS.
```

### 3.3.4 Penyetelan Hiperparameter Bayesian (Optuna TPE)
Penyetelan hiperparameter dijalankan menggunakan kerangka kerja Optuna berbasis algoritma *Tree-structured Parzen Estimator* (TPE)[25] dengan fungsi objektif memaksimalkan Macro-F1 pada subset validasi. Anggaran komputasi (*computational budget*) dialokasikan secara seragam, yaitu tepat **30 trials** untuk masing-masing skenario pengujian (skenario baseline E0, E1, E2, E3 serta skenario EWC E2b dan E4) guna menjamin komparasi yang adil (*fair comparison*). Penyetelan hiperparameter Bayesian ini dijalankan pada satu *random seed* representatif (seed 42) pada subset data validasi *held-out* lokal (20% dari partisi latih). Konfigurasi hiperparameter optimal terbaik yang diperoleh kemudian **dikunci dan diterapkan secara konsisten melintasi seluruh lima *random seed* pengujian independen (42, 43, 44, 45, dan 46)**. Hal ini menjamin bahwa variabilitas skor performa yang diamati pada evaluasi akhir murni mencerminkan stabilitas intrinsik algoritma terhadap perbedaan inisialisasi bobot dan partisi data acak, bukan akibat dari penyesuaian parameter per-seed.

*Tabel 3.4 Konfigurasi Parameter Pelatihan Baseline dan Ruang Pencarian Hiperparameter.*

| Komponen | Hiperparameter | Simbol | Nilai Default Baseline | Ruang Pencarian (*Search Space*) Optuna |
| :--- | :--- | :---: | :---: | :--- |
| **Optimasi Lokal** | Algoritma Optimizer | - | AdamW | AdamW |
| | Laju Pembelajaran | $\eta$ | $10^{-3}$ | $\{10^{-4}, 5 \times 10^{-4}, 10^{-3}\}$ |
| | Peluruhan Bobot (*Weight Decay*) | $\lambda_{\text{wd}}$ | $10^{-4}$ | $\{0, 10^{-5}, 10^{-4}\}$ |
| **Batching & Epoch** | Ukuran Batch | $B$ | 128 | $\{64, 128, 256\}$ |
| | Epoch Lokal Klien | $E$ | 3 | $\{1, 3, 5\}$ |
| **Arsitektur Model** | Dropout Rate | $p$ | 0,2 | $\{0,1, \ 0,2, \ 0,3\}$ |
| **Regularisasi EWC** | Penalti Fisher | $\lambda$ | $10^3$ | $\{10^1, 10^2, 10^3, 10^4, 10^5\}$ |
| | Sampel Estimasi Fisher | $N_{\text{fisher}}$ | 1.000 / kelas | $\{500, 1.000, 2.000\}$ / kelas |
| **Federated Learning** | Ronde Komunikasi Task 1 | $R_1$ | 10 | $\{10, 20\}$ |
| | Ronde Komunikasi Task 2 | $R_2$ | 10 | $\{10, 20\}$ |
| **Stabilitas Gradien** | Batas Pemotongan Gradien | $\gamma$ | 1,0 | Tetap 1,0 (*Norm L2*) |

### 3.3.5 Matriks Skenario Pengujian Komparatif E0–E4
Matriks pengujian komparatif dirancang secara sistematis mencakup lima skenario utama (E0 s.d. E4) untuk menjawab secara langsung Rumusan Masalah 1 (RM1) dan Rumusan Masalah 2 (RM2), sebagaimana disajikan pada Tabel 3.5.

*Tabel 3.5 Matriks Skenario Pengujian Eksperimen E0-E4.*

| Skenario | Topologi Pelatihan | Urutan Data & Tugas | Metode Mitigasi Forgetting | Target Pembuktian Ilmiah & Relevansi Rumusan Masalah |
| :---: | :--- | :--- | :--- | :--- |
| **E0** | Sentralisasi Penuh (1 Node Sentral) | Simultan (Normal, SSH, DoS digabung bersamaan) | Tanpa Proteksi CL (*Joint Training*) | **Batas Atas Teoretis (*Upper Bound*):** Mengukur performa klasifikasi ideal jika seluruh data disatukan tanpa batasan privasi dan tanpa penahapan sekuensial. |
| **E1** | **Lokal Mandiri (Isolated Single-Client)** | Data lokal per klien tanpa komunikasi jaringan | Pelatihan lokal murni | **Menjawab RM1 (Baseline Data Silo):**<br>- **E1a (Klien A Mandiri):** Melatih Normal + SSH-Patator (Fase 1: Normal+SSH, Fase 2: Normal murni).<br>- **E1b (Klien B Mandiri):** Melatih Normal + DoS (Fase 1: Normal murni, Fase 2: Normal+DoS).<br>Membuktikan kelemahan fundamental isolasi data lokal mandiri terhadap kelas ancaman di node lain. |
| **E2** | Sentralisasi Sekuensial (1 Node Sentral) | Sekuensial:<br>Fase 1 (Normal + SSH) $\to$<br>Fase 2 (Normal + DoS) | **E2a:** *Naive Fine-Tuning*<br>**E2b:** Regularisasi EWC ($\lambda$ optimal) | **Isolasi Efek EWC Sentral (Relevansi RM2):** Mengukur degradasi kelupaan katastropik murni (*naive*) dan efektivitas penalti EWC mempertahankan memori lama pada lingkungan terpusat tanpa gangguan heterogenitas jaringan federasi. |
| **E3** | **Federated (2 Klien Non-IID)** | Sekuensial:<br>Fase 1 $\to$ Fase 2 | ***Naive* FedAvg** (tanpa mitigasi EWC) | **Menjawab RM1 & Baseline RM2:**<br>- Membuktikan keunggulan kolaborasi FedAvg dibanding model lokal E1 (kedua serangan berhasil dikenali oleh model global).<br>- Membuktikan terjadinya *catastrophic forgetting* terdistribusi ($BWT \ll 0$) saat Fase 2 menimpa memori SSH-Patator. |
| **E4** | **Federated (2 Klien Non-IID)** | Sekuensial:<br>Fase 1 $\to$ Fase 2 | **FedAvg + EWC (Sistem Usulan TA)** | **Menjawab RM2 (Metode Usulan FCL):** Mengevaluasi efektivitas regularisasi penalti Fisher EWC dalam mempertahankan memori kelas serangan lama (SSH-Patator) di bawah agregasi FedAvg non-IID ($BWT \approx 0$). |

Untuk mencegah bias evaluasi yang meremehkan model lokal E1 (di mana pada pengujian global, model E1a pasti memiliki Recall DoS bernilai 0% karena tidak pernah melihat kelas tersebut), evaluasi performa model dilakukan pada **dua set pengujian terpisah (*Dual-Domain Evaluation*)**:
1. **Global Held-Out Benchmark Test Set (20% gabungan data uji independen):** Mengukur kemampuan generalisasi komprehensif model terpadu dalam mendeteksi seluruh kelas (Normal, SSH-Patator, dan DoS) secara simultan.
2. **Local Client Test Set (20% held-out lokal masing-masing klien):** Mengukur apakah kolaborasi federasi global (E3 dan E4) mampu mempertahankan performa deteksi pada domain spesialis lokal (akurasi Klien A pada trafik lokal Normal+SSH, dan akurasi Klien B pada trafik lokal Normal+DoS) dibandingkan performa model lokal mandiri (E1a dan E1b).

```mermaid
flowchart TD
    subgraph Timeline_Klien_A [Alur Sekuensial Klien A: Subnet Administrasi]
        A1["Fase 1 (Ronde 1 - R1):<br/>Normal 50% + SSH-Patator"] -->|Selesai Fase 1: Kunci Bobot Theta_1* & Hitung Fisher F_A| A2["Fase 2 (Ronde R1+1 - R1+R2):<br/>Normal 50% + Penalti EWC"]
    end
    subgraph Timeline_Klien_B [Alur Sekuensial Klien B: Perimeter DMZ]
        B1["Fase 1 (Ronde 1 - R1):<br/>Normal 50%"] -->|Selesai Fase 1: Terima Bobot Global Theta_1*| B2["Fase 2 (Ronde R1+1 - R1+R2):<br/>Normal 50% + DoS"]
    end
    subgraph Server_FL [Server Agregator FedAvg]
        S1["Agregasi FedAvg Fase 1<br/>Model Global Mampu Deteksi SSH"]
        S2["Agregasi FedAvg Fase 2<br/>Model Global Terpadu Multi-Kelas"]
    end
    A1 -.->|Pembaruan Bobot Theta_A| S1
    B1 -.->|Pembaruan Bobot Theta_B| S1
    S1 -.->|Siarkan Bobot Global Theta_1*| A2
    S1 -.->|Siarkan Bobot Global Theta_1*| B2
    A2 -.->|Pembaruan Bobot Theta_A (EWC)| S2
    B2 -.->|Pembaruan Bobot Theta_B| S2
```
*Gambar 3.6 Diagram Alir Skenario Pengujian Sekuensial Non-IID.*

### 3.3.6 Mekanisme Evaluasi Multi-Seed dan Profiling Komputasi
Setiap skenario dievaluasi melintasi lima *random seed* independen (42, 43, 44, 45, 46) menggunakan metrik evaluasi yang komprehensif:

1. **Performa Deteksi ML:** Macro-F1, *Precision*, *Recall*, dan *Accuracy* dievaluasi pada *test set* global maupun *test set* lokal klien di akhir setiap fase pembelajaran. Indikator $Recall_{\text{SSH-Patator}}$ ditetapkan sebagai metrik evaluasi utama untuk mendeteksi tingkat keparahan *catastrophic forgetting*.
2. **Retensi Continual Learning:** Metrik *Backward Transfer* (BWT) dihitung untuk mengukur retensi memori terhadap tugas masa lalu[10]. Pada paradigma pembelajaran sekuensial dengan $T$ tugas, didefinisikan matriks evaluasi performa $R \in \mathbb{R}^{T \times T}$, di mana elemen $R_{i, j}$ merepresentasikan skor evaluasi (Macro-F1 atau Recall kelas lama) pada data uji Tugas $j$ setelah model menyelesaikan pembelajaran pada Tugas $i$ ($i \ge j$). Formulasi umum BWT dinyatakan sebagai[10]:

$$
\text{BWT} = \frac{1}{T-1} \sum_{j=1}^{T-1} (R_{T, j} - R_{j, j})
$$

Pada skenario dua fase sekuensial penelitian ini ($T=2$), formulasi tereduksi menjadi:

$$
\text{BWT} = R_{2, 1} - R_{1, 1}
$$

di mana $R_{1, 1}$ adalah skor performa pada data uji Task 1 (SSH-Patator) segera setelah Fase 1 selesai, dan $R_{2, 1}$ adalah skor performa pada data uji Task 1 yang sama setelah model menyelesaikan pelatihan Fase 2. Nilai $\text{BWT} < 0$ merefleksikan tingkat keparahan kelupaan katastropik, sedangkan $\text{BWT} \approx 0$ membuktikan keberhasilan retensi representasi memori.

3. **Efisiensi Komputasi & Instance Testbed:**
   - *Inference Time:* Pengukuran waktu inferensi diawali dengan fase pemanasan (*warm-up phase*) sebanyak 100 sampel pertama untuk menstabilkan alokasi *cache* CPU. Selanjutnya, model mengeksekusi inferensi pada 10.000 aliran data uji independen secara sekuensial. Waktu pemrosesan dicatat menggunakan penanda waktu berpresisi tinggi monotonic nanosecond clock (`time.perf_counter_ns()`), dan dilaporkan dalam rata-rata mikrodetik per aliran data ($\mu\text{s/flow}$) beserta deviasi standarnya[16].
   - *Memory Footprint:* Alokasi RAM fisik puncak (*peak RAM usage*) selama fase pelatihan lokal, kalkulasi Matriks Fisher, dan penalti regularisasi diukur menggunakan modul `tracemalloc` dan monitoring kontainer Proxmox VE.
   - *Communication Payload:* Ukuran muatan komunikasi dihitung secara eksak dari representasi bobot numerik Float32 (4 bita per parameter):
     * Model tunggal ($|\theta| = 6.211$ parameter): $6.211 \times 4\text{ B} = 24.844\text{ B} \approx \mathbf{24,84\text{ KB}}$ per transmisi satu arah.
     * Beban per klien per ronde (unduh model global downlink + unggah pembaruan lokal uplink): $2 \times 24,84\text{ KB} = \mathbf{49,69\text{ KB/klien/ronde}}$.
     * Beban komunikasi agregasi server untuk dua klien: $2 \times 49,69\text{ KB} = \mathbf{99,38\text{ KB/ronde}}$.
     * **Status angka:** seluruh nilai di atas adalah **estimasi analitik bobot murni Float32** (belum termasuk overhead serialisasi gRPC/protobuf dan header protokol). Ukuran payload **terukur** pada testbed akan dilaporkan sebagai metrik evaluasi eksperimen (Minggu 13), bukan sebagai hasil pengukuran saat ini.
4. **Estimasi Waktu Komputasi (*Computational Runtime*):**
   Dengan alokasi 3 epoch lokal per ronde federasi pada *batch size* 128, komputasi lokal membutuhkan waktu $\approx 45$–70 detik per ronde per klien pada prosesor multi-core. Total durasi 20 ronde federasi (10 ronde Fase 1 + 10 ronde Fase 2) berkisar $\approx 75$–100 menit per seed. Total waktu eksekusi eksperimen untuk seluruh matriks E0 s.d. E4 melintasi 5 *random seed* diperkirakan mencapai $\approx 35$–45 jam komputasi CPU, yang dijadwalkan secara bertahap pada Minggu ke-9 hingga ke-11.

## 3.4 Jadwal Pelaksanaan Penelitian

Rencana pelaksanaan penelitian dijadwalkan dalam durasi 14 minggu (1 semester) sebagaimana dirangkum pada jadwal kegiatan Tabel 3.6 mengacu pada format Lampiran 5 Buku Pedoman ITS 2022.

*Tabel 3.6 Jadwal Pelaksanaan Penelitian Tugas Akhir.*

| No | Nama Kegiatan | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 |
|:---:|:---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| 1 | Studi Pustaka dan Perumusan Masalah | ■ | ■ | | | | | | | | | | | | |
| 2 | Akuisisi dan Audit Kritis Dataset CIC-IDS2017 | | ■ | ■ | | | | | | | | | | | |
| 3 | Praproses Data & Ekstraksi 62 Fitur Bebas Port Leakage | | | ■ | ■ | | | | | | | | | | |
| 4 | Pengembangan Model Dasar MLP & Lingkungan FL Flower | | | | ■ | ■ | | | | | | | | | |
| 5 | Implementasi Regularisasi EWC dan Matriks Fisher Lokal | | | | | ■ | ■ | | | | | | | | |
| 6 | Penyetelan Hiperparameter Bayesian (Optuna TPE) | | | | | | ■ | ■ | | | | | | | |
| 7 | Penyusunan dan Pelaksanaan Seminar Proposal Tugas Akhir | | | | | | | ■ | ■ | | | | | | |
| 8 | Eksekusi Eksperimen Komparatif E0–E4 (5 Random Seeds) | | | | | | | | | ■ | ■ | ■ | | | |
| 9 | Evaluasi Metrik BWT, Latensi Inferensi, RAM, & Payload | | | | | | | | | | | ■ | ■ | | |
| 10 | Pengujian pada Testbed Server Terdistribusi Proxmox VE | | | | | | | | | | | | ■ | ■ | |
| 11 | Penyusunan Laporan Akhir Skripsi dan Ujian Sidang Akhir | | | | | | | | | | | | | ■ | ■ |

\newpage

# DAFTAR PUSTAKA

[1] Check Point Research, “Q1 2025 Global Cyber Attack Report: An almost 50% surge in cyber threats worldwide,” Check Point Software Technologies, 2025. [Daring]. Tersedia pada: https://blog.checkpoint.com/research/q1-2025-global-cyber-attack-report

[2] Federal Bureau of Investigation, “2023 Internet Crime Report (IC3),” Washington, D.C., 2024. [Daring]. Tersedia pada: https://www.ic3.gov/Media/PDF/AnnualReport/2023_IC3Report.pdf

[3] B. McMahan, E. Moore, D. Ramage, S. Hampson, dan B. A. y Arcas, “Communication-Efficient Learning of Deep Networks from Decentralized Data,” dalam *Proceedings of the 20th International Conference on Artificial Intelligence and Statistics (AISTATS)*, PMLR, vol. 54, hlm. 1273–1282, 2017.

[4] Y. Zhao, M. Li, L. Lai, N. Suda, D. Civin, dan V. Chandra, “Federated Learning with Non-IID Data,” *arXiv preprint arXiv:1806.00582*, 2018.

[5] J. Kirkpatrick, R. Pascanu, N. Rabinowitz, J. Veness, G. Desjardins, A. A. Rusu, K. Milan, J. Quan, T. Ramalho, A. Grabska-Barwinska, D. Hassabis, C. Clopath, D. Kumaran, dan R. Hadsell, “Overcoming catastrophic forgetting in neural networks,” *Proceedings of the National Academy of Sciences (PNAS)*, vol. 114, no. 13, hlm. 3521–3526, 2017. doi: 10.1073/pnas.1611835114.

[6] W. Stallings, *Cryptography and Network Security: Principles and Practice*, edisi ke-7. Boston, MA, USA: Pearson Education, 2017.

[7] I. Sharafaldin, A. H. Lashkari, dan A. A. Ghorbani, “Toward Generating a New Intrusion Detection Dataset and Intrusion Traffic Characterization,” dalam *Proceedings of the 4th International Conference on Information Systems Security and Privacy (ICISSP)*, hlm. 108–116, 2018. doi: 10.5220/0006639801080116.

[8] S. I. Popoola, R. Ande, B. Adebisi, G. Gui, M. Hammoudeh, dan O. Jogunola, “Federated Deep Learning for Zero-Day Botnet Attack Detection in IoT-Edge Devices,” *IEEE Internet of Things Journal*, vol. 9, no. 5, hlm. 3930–3944, 2022. doi: 10.1109/JIOT.2021.3100755.

[9] P. Ruzafa-Alcázar, P. Fernández-Saura, E. Mármol-Campos, A. González-Vidal, J. L. Hernández-Ramos, J. Bernal-Bernabe, dan A. F. Skarmeta, “Intrusion Detection Based on Privacy-Preserving Federated Learning for the Industrial IoT,” *IEEE Transactions on Industrial Informatics*, vol. 19, no. 2, hlm. 1145–1154, 2023. doi: 10.1109/TII.2021.3126728.

[10] D. Lopez-Paz dan M. Ranzato, “Gradient Episodic Memory for Continual Learning,” dalam *Advances in Neural Information Processing Systems (NeurIPS)*, vol. 30, hlm. 6467–6476, 2017.

[11] J. Dong, L. Wang, Z. Fang, G. Sun, S. Xu, X. Wang, dan Q. Zhu, “Federated Class-Incremental Learning,” dalam *Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)*, hlm. 10164–10173, 2022. doi: 10.1109/CVPR52688.2022.00992.

[12] Z. Jin, J. Zhou, B. Li, X. Wu, dan C. Duan, “FL-IIDS: A novel federated learning-based incremental intrusion detection system,” *Future Generation Computer Systems*, vol. 151, hlm. 57–70, 2024. doi: 10.1016/j.future.2023.09.019.

[13] A. Rosay, É. Cheval, F. Carlier, dan P. Leroux, “Network Intrusion Detection: A Comprehensive Analysis of CIC-IDS2017,” dalam *Proceedings of the 8th International Conference on Information Systems Security and Privacy (ICISSP)*, hlm. 25–36, 2022. doi: 10.5220/0010774000003120.

[14] R. Dube, “Faulty use of the CIC-IDS 2017 dataset in information security research,” *Journal of Computer Virology and Hacking Techniques*, vol. 20, no. 1, hlm. 203–211, 2024. doi: 10.1007/s11416-023-00509-7.

[15] G. Engelen, V. Rimmer, dan W. Joosen, “Troubleshooting an Intrusion Detection Dataset: the CICIDS2017 Case Study,” dalam *2021 IEEE Security and Privacy Workshops (SPW)*, San Francisco, CA, USA, hlm. 7–12, 2021. doi: 10.1109/SPW53761.2021.00009.

[16] H. A. Rinandri, “Pendekatan Semi-Supervised Learning untuk Sistem Deteksi Intrusi Jaringan Real-Time Berbasis GNN-AE pada Arsitektur Structemp,” Tugas Akhir, Program Studi Sarjana Teknik Elektro, Departemen Teknik Elektro, Fakultas Teknologi Elektro dan Informatika Cerdas, Institut Teknologi Sepuluh Nopember, Surabaya, 2025.

[17] M. Sarhan, S. Layeghy, dan M. Portmann, “Towards a Standard Feature Set for Network Intrusion Detection System Datasets,” *Mobile Networks and Applications*, vol. 27, no. 1, hlm. 357–370, 2022. doi: 10.1007/s11036-021-01843-0.

[18] G. M. van de Ven, T. Tuytelaars, dan A. S. Tolias, “Three types of incremental learning,” *Nature Machine Intelligence*, vol. 4, hlm. 1185–1197, 2022. doi: 10.1038/s42256-022-00568-3.

[19] H. Ghallab, M. Nasr, dan H. Fahmy, “Mitigating Catastrophic Forgetting in Continual Learning Using the Gradient-Based Approach: A Literature Review,” *International Journal of Advanced Computer Science and Applications (IJACSA)*, vol. 16, no. 4, hlm. 120–130, 2025. doi: 10.14569/IJACSA.2025.0160414.

[20] M. Ring, S. Wunderlich, D. Scheuring, D. Landes, dan A. Hotho, “A survey of network-based intrusion detection data sets,” *Computers & Security*, vol. 86, hlm. 147–167, 2019. doi: 10.1016/j.cose.2019.06.005.

[21] A. Paszke, S. Gross, F. Massa, A. Lerer, J. Bradbury, G. Chanan, T. Killeen, Z. Lin, N. Gimelshteyn, L. Antiga, A. Desmaison, A. Kopf, E. Yang, Z. DeVito, M. Raison, A. Tejani, S. Chilamkurthy, B. Steiner, L. Fang, J. Bai, dan S. Chintala, “PyTorch: An Imperative Style, High-Performance Deep Learning Library,” dalam *Advances in Neural Information Processing Systems (NeurIPS)*, vol. 32, hlm. 8024–8035, 2019.

[22] D. J. Beutel, T. Topal, A. Mathur, X. Qiu, T. Parcollet, P. P. B. de Gusmao, dan N. D. Lane, “Flower: A Friendly Federated Learning Research Framework,” *arXiv preprint arXiv:2007.14390*, 2020.

[23] I. Goodfellow, Y. Bengio, dan A. Courville, *Deep Learning*. Cambridge, MA, USA: MIT Press, 2016.

[24] T. Fawcett, “An introduction to ROC analysis,” *Pattern Recognition Letters*, vol. 27, no. 8, hlm. 861–874, 2006. doi: 10.1016/j.patrec.2005.10.010.

[25] J. Bergstra, R. Bardenet, Y. Bengio, dan B. Kégl, “Algorithms for Hyper-Parameter Optimization,” dalam *Advances in Neural Information Processing Systems (NeurIPS)*, vol. 24, hlm. 2546–2554, 2011.

[26] F. Hutter, L. Kotthoff, dan J. Vanschoren, *Automated Machine Learning: Methods, Systems, Challenges*. Cham, Switzerland: Springer International Publishing, 2019. doi: 10.1007/978-3-030-05318-5.

[27] R. M. Schmidt, F. Schneider, dan P. Hennig, “Descending through a Crowded Valley – Benchmarking Deep Learning Optimizers,” dalam *Proceedings of the 38th International Conference on Machine Learning (ICML)*, PMLR, vol. 139, hlm. 9367–9376, 2021.

[28] I. Loshchilov dan F. Hutter, “Decoupled Weight Decay Regularization,” dalam *International Conference on Learning Representations (ICLR)*, hlm. 1–11, 2019.

[29] V. Nair dan G. E. Hinton, “Rectified Linear Units Improve Restricted Boltzmann Machines,” dalam *Proceedings of the 27th International Conference on Machine Learning (ICML)*, hlm. 807–814, 2010.

[30] S. R. Dubey, S. K. Singh, dan B. B. Chaudhuri, “Activation Functions in Deep Learning: A Comprehensive Survey and Benchmark,” *Neurocomputing*, vol. 503, hlm. 92–108, 2022. doi: 10.1016/j.neucom.2022.06.111.

[31] J. L. Hernandez-Ramos, G. Karopoulos, E. Chatzoglou, V. Kouliaridis, E. Marmol, A. Gonzalez-Vidal, dan G. Kambourakis, “Intrusion Detection Based on Federated Learning: A Systematic Review,” *ACM Computing Surveys*, vol. 57, no. 12, hlm. 1–65, 2025. doi: 10.1145/3731596.

[32] B. Buyuktanir, S. Altinkaya, G. Karatas Baydogmus, dan K. Yildiz, “Federated learning in intrusion detection: advancements, applications, and future directions,” *Cluster Computing*, vol. 28, no. 7, 2025. doi: 10.1007/s10586-025-05325-w.

[33] M. U. Rehman, H. Bahsi, dan R. Kalakoti, “Incremental Federated Learning for Intrusion Detection in IoT Networks under Evolving Threat Landscape,” *arXiv preprint arXiv:2603.10776*, 2026.

[34] P. Hamedi, R. Razavi-Far, dan E. Hallaji, “Federated Continual Learning: Concepts, Challenges, and Solutions,” *arXiv preprint arXiv:2502.07059*, 2025.
