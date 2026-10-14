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
2.4 Federated Learning .............................................................................................................. 10  
2.5 Continual Learning ................................................................................................................ 12  
2.6 Deteksi Intrusi ................................................................................................................. 13  
2.7 PyTorch ......................................................................................................................... 14  
2.8 Flower .......................................................................................................................... 14  
2.9 Multilayer Perceptron .......................................................................................................... 15  
2.10 Regularisasi EWC ............................................................................................................... 16  
2.11 Dataset .......................................................................................................................... 17  
2.12 Evaluasi Metrik ................................................................................................................. 19  
2.13 Hyperparameter Tuning ...................................................................................................... 20  
2.14 Optimizer .......................................................................................................................... 21  
2.15 Fungsi Aktivasi ................................................................................................................. 22  
**BAB 3 METODOLOGI** ................................................................................................................ 23  
3.1 Metode yang Digunakan .......................................................................................................... 23  
3.2 Bahan dan Peralatan yang Digunakan ....................................................................................... 25  
3.2.1 Bahan Penelitian .................................................................................................................... 25  
3.2.2 Peralatan Penelitian ............................................................................................................... 25  
3.3 Urutan Pelaksanaan Penelitian ................................................................................................. 26  
3.3.1 Praproses Data dan Ekstraksi 63 Fitur Numerik .................................................................... 26  
3.3.2 Pengembangan Model Dasar MLP Kompak .......................................................................... 29  
3.3.3 Integrasi Sistem Usulan: FedAvg dan EWC pada Lingkungan Terdistribusi ......................... 30  
3.3.4 Penyetelan Hiperparameter Bayesian (Optuna TPE) ............................................................. 31  
3.3.5 Matriks Skenario Pengujian Komparatif E0–E4 .................................................................... 32  
3.3.6 Mekanisme Evaluasi Multi-Seed dan Profiling Komputasi ................................................... 33  
3.4 Jadwal Pelaksanaan Penelitian ................................................................................................ 34  

**DAFTAR PUSTAKA** ................................................................................................................... 35  

---

# DAFTAR GAMBAR

<br>

Gambar 2.1 Model CIA Triad Keamanan Informasi ............................................................................ 6  
Gambar 2.2 Siklus Pelatihan dan Agregasi Bobot pada Federated Learning (FedAvg) .................... 10  
Gambar 2.3 Taksonomi Pendekatan Mitigasi Catastrophic Forgetting pada Continual Learning ...... 12  
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
Tabel 3.1 Spesifikasi Lingkungan Perangkat Keras dan Perangkat Lunak ...................................... 25  
Tabel 3.2 Ringkasan 63 Fitur Statistik Numerik Aliran Bersih CIC-IDS2017 ................................. 28  
Tabel 3.3 Konfigurasi Parameter Pelatihan Baseline dan Ruang Pencarian Hiperparameter ..... 31  
Tabel 3.4 Matriks Skenario Pengujian Eksperimen E0–E4 .............................................................. 32  
Tabel 3.5 Jadwal Pelaksanaan Penelitian Tugas Akhir ................................................................... 34  

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
