# ABSTRAK

**INVESTIGASI MITIGASI CATASTROPHIC FORGETTING PADA DETEKSI INTRUSI TERDISTRIBUSI MENGGUNAKAN FEDERATED CONTINUAL LEARNING (EWC) DI BAWAH KONDISI DATA NON-IID**

**Nama Mahasiswa / NRP:** Rafli Alif Ihza Hartono / 5022211233  
**Departemen:** Teknik Elektro  
**Fakultas:** Teknologi Elektro dan Informatika Cerdas (FTEIC)  
**Institusi:** Institut Teknologi Sepuluh Nopember (ITS)  
**Dosen Pembimbing:** Dr.Ir. Achmad Affandi, DEA.  

---

### Abstrak

Perkembangan serangan siber yang dinamis menuntut *Network Intrusion Detection System* (NIDS) untuk mampu beradaptasi mendeteksi varian ancaman baru secara berkelanjutan tanpa mengorbankan privasi data lalu lintas jaringan pengguna. Pendekatan *Federated Learning* (FL) dengan algoritma *Federated Averaging* (FedAvg) memungkinkan kolaborasi pelatihan model lintas node sensor tanpa memusatkan rekaman paket mentah. Namun, ketika node sensor dihadapkan pada aliran data serangan baru yang muncul secara sekuensial pada lingkungan terdistribusi heterogen (*non-Identical and Independently Distributed* / non-IID), model mengalami degradasi memori yang parah terhadap kelas serangan lama, sebuah fenomena yang dikenal sebagai *catastrophic forgetting*.

Penelitian ini menginvestigasi mitigasi *catastrophic forgetting* pada sistem deteksi intrusi terdistribusi menggunakan pendekatan *Federated Continual Learning* (FCL) dengan menyematkan regularisasi penalti kuadratik *Elastic Weight Consolidation* (EWC) pada optimasi model lokal klien. Evaluasi dirancang dalam skenario *Class-Incremental Learning* (Class-IL) menggunakan arsitektur *Multilayer Perceptron* (MLP) kompak (Input 63 $\to$ Linear 64 $\to$ Linear 32 $\to$ Linear 3) pada dataset tolok ukur resmi CIC-IDS2017 (Senin, Selasa, dan Rabu). Dataset dikurasi secara ketat dengan mengeksklusi 10 fitur konstan bervariansi nol, 5 pasangan fitur duplikat identik, serta fitur *Destination Port* guna mengeliminasi bias *shortcut learning*. Seluruh 1.529.677 aliran data bersih dipertahankan tanpa pemangkasan melalui penerapan *Weighted Cross-Entropy Loss* untuk menangani ketimpangan kelas ekstrem antara Normal (1.332.710 aliran), DoS (193.748 aliran), dan SSH-Patator (3.219 aliran). Skenario non-IID disimulasikan menggunakan dua klien independen: Klien A mempelajari Task 1 (Normal + SSH-Patator) dan Klien B mempelajari Task 2 (Normal + DoS), dengan partisi kelas Normal dibagi acak 50/50 dari seluruh hari untuk mencegah *day-of-week confound*.

Pengujian dieksekusi melintasi lima *random seed* (42 s.d. 46) pada matriks eksperimen E0 (Centralized Upper Bound), E1 (Lokal Naive), E2 (Lokal EWC), E3 (FedAvg Naive), dan E4 (FedAvg + EWC). Kinerja dianalisis secara komprehensif menggunakan metrik Macro-F1, per-class Recall, *Backward Transfer* (BWT), *inference latency* per aliran data ($\mu\text{s}$), serta *memory footprint* alokasi RAM. Pendekatan EWC yang diusulkan terbukti mampu membatasi pergeseran bobot parameter kritis melalui kalkulasi matriks informasi Fisher diagonal ($\approx$ puluhan kilobyte), mempertahankan retensi deteksi serangan SSH terdahulu tanpa memerlukan *replay buffer* sampel mentah yang membebani memori, serta mencapai latensi inferensi sub-mikrodetik per aliran data yang membuktikan kesiapan sistem untuk diimplementasikan pada gateway sensor jaringan *near real-time*.

**Kata Kunci:** *Continual Learning*, *Catastrophic Forgetting*, *Elastic Weight Consolidation (EWC)*, *Federated Learning*, *FedAvg*, *Network Intrusion Detection System (NIDS)*, *Non-IID*, *CIC-IDS2017*.
