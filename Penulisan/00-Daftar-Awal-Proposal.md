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
2.1 Keamanan Jaringan dan Model Pertahanan Berlapis ................................................................. 6  
2.2 Klasifikasi Serangan Siber (BENIGN, SSH-Patator, DoS) ......................................................... 7  
2.3 Hasil Penelitian Terdahulu ....................................................................................................... 8  
2.4 Federated Learning dan Algoritma FedAvg .............................................................................. 10  
2.5 Continual Learning dan Fenomena Catastrophic Forgetting ..................................................... 12  
2.6 Network Intrusion Detection System (NIDS) ............................................................................ 13  
2.7 PyTorch dan Framework Flower ............................................................................................... 14  
2.8 Multilayer Perceptron (MLP) Kompak .................................................................................... 15  
2.9 Elastic Weight Consolidation (EWC) ........................................................................................ 16  
2.10 Karakteristik Dataset Tolok Ukur CIC-IDS2017 ..................................................................... 17  
2.11 Metrik Evaluasi Kinerja ......................................................................................................... 19  
2.12 Bayesian Hyperparameter Tuning (Optuna TPE) .................................................................... 20  
2.13 Algoritma Pengoptimal AdamW ............................................................................................. 21  
2.14 Fungsi Aktivasi ReLU dan Softmax ....................................................................................... 22  

**BAB 3 METODOLOGI** ................................................................................................................ 23  
3.1 Metode yang Digunakan .......................................................................................................... 23  
3.2 Bahan dan Peralatan yang Digunakan ....................................................................................... 25  
3.3 Urutan Pelaksanaan Penelitian ................................................................................................. 26  
3.3.1 Pemilihan Data Publik CIC-IDS2017 ................................................................................... 26  
3.3.2 Praproses Data dan Ekstraksi 63 Fitur Numerik .................................................................... 27  
3.3.3 Arsitektur Sistem Terdistribusi yang Diusulkan ................................................................... 31  
3.3.4 Rancangan Sistem untuk Penerapan Real-Time ..................................................................... 32  
3.3.5 Matriks Skenario Pengujian Komparatif E0–E4 .................................................................... 33  
3.3.6 Mekanisme Evaluasi Multi-Seed dan Profiling Komputasi ................................................... 34  
3.4 Jadwal Pelaksanaan Penelitian ................................................................................................ 35  

**DAFTAR PUSTAKA** ................................................................................................................... 36  

---

# DAFTAR GAMBAR

<br>

Gambar 2.1 Model CIA Triad dan Konsep Pertahanan Berlapis Jaringan .......................................... 6  
Gambar 2.2 Siklus Pelatihan dan Agregasi Bobot pada Federated Learning (FedAvg) .................... 10  
Gambar 2.3 Taksonomi Pendekatan Mitigasi Catastrophic Forgetting ............................................. 12  
Gambar 2.4 Mekanisme Regularisasi EWC Membatasi Pergeseran Bobot Kritis ............................. 16  
Gambar 2.5 Struktur Dasar Confusion Matrix untuk Evaluasi Deteksi Biner dan Multi-kelas .......... 19  
Gambar 3.1 Arsitektur Penempatan Sensor NIDS Terdistribusi dalam Jaringan Enterprise ............. 23  
Gambar 3.2 Fishbone Diagram Identifikasi Tantangan NIDS Terdistribusi ..................................... 24  
Gambar 3.3 Diagram Alir Urutan Pelaksanaan Penelitian .............................................................. 26  
Gambar 3.4 Diagram Alur Global Data Preprocessing ................................................................... 27  
Gambar 3.5 Arsitektur Sistem Federated Continual Learning yang Diimplementasikan ................. 31  
Gambar 3.6 Rancangan Sistem Konseptual untuk Penerapan Real-Time pada Edge Gateway ......... 32  
Gambar 3.7 Diagram Alir Skenario Pengujian Sekuensial Non-IID ................................................. 34  

---

# DAFTAR TABEL

<br>

Tabel 2.1 Perbandingan Penelitian Terdahulu dalam Domain FL, Continual Learning, dan NIDS ..... 8  
Tabel 3.1 Ringkasan 63 Fitur Statistik Numerik Aliran Bersih CIC-IDS2017 ................................. 28  
Tabel 3.2 Spesifikasi Lingkungan Perangkat Keras dan Perangkat Lunak ...................................... 25  
Tabel 3.3 Matriks Skenario Pengujian Eksperimen E0–E4 .............................................................. 33  
Tabel 3.4 Jadwal Pelaksanaan Penelitian (Gantt Chart) .................................................................. 35  

---

# DAFTAR SINGKATAN

<br>

| Singkatan | Kepanjangan / Definisi |
|---|---|
| **ABDS** | *Anomaly-Based Detection System* |
| **BWT** | *Backward Transfer* |
| **CIA** | *Confidentiality, Integrity, and Availability* |
| **CIC** | *Canadian Institute for Cybersecurity* |
| **CL** | *Continual Learning* |
| **DMZ** | *Demilitarized Zone* |
| **DoS** | *Denial of Service* |
| **EWC** | *Elastic Weight Consolidation* |
| **FCL** | *Federated Continual Learning* |
| **FedAvg** | *Federated Averaging* |
| **FIM** | *Fisher Information Matrix* |
| **FL** | *Federated Learning* |
| **HIDS** | *Host-Based Intrusion Detection System* |
| **IAT** | *Inter-Arrival Time* |
| **IID** | *Independent and Identically Distributed* |
| **ITS** | Institut Teknologi Sepuluh Nopember |
| **MLP** | *Multilayer Perceptron* |
| **NIDS** | *Network Intrusion Detection System* |
| **Non-IID** | *Non-Independent and Identically Distributed* |
| **PVE** | *Proxmox Virtual Environment* |
| **SGD** | *Stochastic Gradient Descent* |
| **SIDS** | *Signature-Based Intrusion Detection System* |
| **SSH** | *Secure Shell* |
| **TPE** | *Tree-structured Parzen Estimator* |
