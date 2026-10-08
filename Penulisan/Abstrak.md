# ABSTRAK

**ANALISIS KINERJA DETEKSI NETWORK TRAFFIC INTRUSION MENGGUNAKAN METODE FEDERATED-CONTINUAL LEARNING PADA TESTBED PRIVATE CLOUD SERVER**  
*(Studi Pengaruh Elastic Weight Consolidation dan Federated Averaging pada Distribusi Data Non-IID Dua Client)*

**Nama Mahasiswa / NRP:** Rafli Alif Ihza Hartono / 5022211233  
**Departemen:** Teknik Elektro  
**Fakultas:** Teknologi Elektro dan Informatika Cerdas (FTEIC)  
**Institusi:** Institut Teknologi Sepuluh Nopember (ITS)  
**Dosen Pembimbing:** Dr.Ir. Achmad Affandi, DEA.  

---

### Abstrak (Versi Proposal — Tepat 200 Kata)

Eskalasi serangan siber menuntut *Network Intrusion Detection System* (NIDS) mampu mendeteksi variasi ancaman baru tanpa mengorbankan privasi data pengguna. Namun, sentralisasi trafik melanggar regulasi privasi, sedangkan model terdistribusi sekuensial rentan mengalami *catastrophic forgetting* terhadap ancaman terdahulu. Penelitian ini bertujuan menganalisis kinerja deteksi intrusi berbasis *Federated Continual Learning* yang mengintegrasikan *Federated Averaging* (FedAvg) dan *Elastic Weight Consolidation* (EWC) pada data non-IID. Pengujian akan menggunakan dataset CIC-IDS2017 bersih (Senin-Rabu) dengan mengeksklusi *Destination Port* guna mencegah *shortcut learning* dan menghasilkan 63 fitur. Seluruh 1.529.677 aliran dipertahankan menggunakan *Weighted Cross-Entropy Loss* dan *gradient clipping* untuk mengatasi ketimpangan kelas ekstrem antara Normal, SSH-Patator, dan DoS. Skenario *Class-Incremental Learning* disimulasikan pada dua klien dengan partisi kelas Normal 50/50 di seluruh hari perekaman. Model klasifikasi menggunakan *Multilayer Perceptron* (MLP) kompak tiga lapis berkapasitas 6.275 parameter guna efisiensi komputasi *edge*. Klien lokal akan menghitung Matriks Informasi Fisher diagonal untuk memproteksi bobot kritis tugas terdahulu sebelum agregasi global Flower. Penerapan EWC diharapkan mampu menekan *catastrophic forgetting* dengan mempertahankan skor Macro-F1 dan *Backward Transfer* yang stabil. Model diproyeksikan menghasilkan efisiensi RAM yang unggul dibanding *replay buffer* serta latensi inferensi tingkat mikrodetik per *flow*. Penelitian ini berkontribusi menyediakan arsitektur NIDS adaptif yang aman privasi dan hemat bandwidth untuk gerbang jaringan enterprise.

**Kata kunci:** *Catastrophic Forgetting*, *Continual Learning*, *Elastic Weight Consolidation*, *Federated Learning*, *Network Intrusion Detection System*, *Non-IID*

---

### Pemetaan Struktur Abstrak (Tepat 200 Kata / 11 Kalimat):

1. **a. Latar Belakang (2 Kalimat):**
   - *Kalimat 1:* Eskalasi serangan siber menuntut *Network Intrusion Detection System* (NIDS) mampu mendeteksi variasi ancaman baru tanpa mengorbankan privasi data pengguna.
   - *Kalimat 2:* Namun, sentralisasi trafik melanggar regulasi privasi, sedangkan model terdistribusi sekuensial rentan mengalami *catastrophic forgetting* terhadap ancaman terdahulu.
2. **b. Tujuan (1 Kalimat):**
   - *Kalimat 3:* Penelitian ini bertujuan menganalisis kinerja deteksi intrusi berbasis *Federated Continual Learning* yang mengintegrasikan *Federated Averaging* (FedAvg) dan *Elastic Weight Consolidation* (EWC) pada data non-IID.
3. **c. Metode (5 Kalimat):**
   - *Kalimat 4:* Pengujian akan menggunakan dataset CIC-IDS2017 bersih (Senin-Rabu) dengan mengeksklusi *Destination Port* guna mencegah *shortcut learning* dan menghasilkan 63 fitur.
   - *Kalimat 5:* Seluruh 1.529.677 aliran dipertahankan menggunakan *Weighted Cross-Entropy Loss* dan *gradient clipping* untuk mengatasi ketimpangan kelas ekstrem antara Normal, SSH-Patator, dan DoS.
   - *Kalimat 6:* Skenario *Class-Incremental Learning* disimulasikan pada dua klien dengan partisi kelas Normal 50/50 di seluruh hari perekaman.
   - *Kalimat 7:* Model klasifikasi menggunakan *Multilayer Perceptron* (MLP) kompak tiga lapis berkapasitas 6.275 parameter guna efisiensi komputasi *edge*.
   - *Kalimat 8:* Klien lokal akan menghitung Matriks Informasi Fisher diagonal untuk memproteksi bobot kritis tugas terdahulu sebelum agregasi global Flower.
4. **d. Hasil yang Diharapkan / Hipotesis (2 Kalimat):**
   - *Kalimat 9:* Penerapan EWC diharapkan mampu menekan *catastrophic forgetting* dengan mempertahankan skor Macro-F1 dan *Backward Transfer* yang stabil.
   - *Kalimat 10:* Model diproyeksikan menghasilkan efisiensi RAM yang unggul dibanding *replay buffer* serta latensi inferensi tingkat mikrodetik per *flow*.
5. **e. Signifikansi / Kontribusi (1 Kalimat):**
   - *Kalimat 11:* Penelitian ini berkontribusi menyediakan arsitektur NIDS adaptif yang aman privasi dan hemat bandwidth untuk gerbang jaringan enterprise.

---

### Abstrak (Versi Laporan Akhir Tugas Akhir — Tepat 200 Kata, Tanpa Kata "Akan")

Eskalasi serangan siber menuntut *Network Intrusion Detection System* (NIDS) mampu mendeteksi variasi ancaman baru tanpa mengorbankan privasi data pengguna. Namun, sentralisasi trafik melanggar regulasi privasi, sedangkan model terdistribusi sekuensial rentan mengalami *catastrophic forgetting* terhadap ancaman terdahulu. Penelitian ini bertujuan menganalisis kinerja deteksi intrusi berbasis *Federated Continual Learning* yang mengintegrasikan *Federated Averaging* (FedAvg) dan *Elastic Weight Consolidation* (EWC) pada data non-IID. Pengujian empiris menggunakan dataset CIC-IDS2017 bersih (Senin-Rabu) dengan mengeksklusi *Destination Port* guna mencegah *shortcut learning* dan menghasilkan 63 fitur. Seluruh 1.529.677 aliran dipertahankan menggunakan *Weighted Cross-Entropy Loss* dan *gradient clipping* untuk mengatasi ketimpangan kelas ekstrem antara Normal, SSH-Patator, dan DoS. Skenario *Class-Incremental Learning* disimulasikan pada dua klien dengan partisi kelas Normal 50/50 di seluruh hari perekaman. Model klasifikasi dirancang menggunakan *Multilayer Perceptron* (MLP) kompak tiga lapis berkapasitas 6.275 parameter guna efisiensi komputasi *edge*. Klien lokal menghitung Matriks Informasi Fisher diagonal untuk memproteksi bobot kritis tugas terdahulu sebelum agregasi global Flower. Penerapan EWC terbukti mampu menekan *catastrophic forgetting* dengan mempertahankan skor Macro-F1 dan *Backward Transfer* yang stabil. Model terbukti menghasilkan efisiensi RAM yang unggul dibanding *replay buffer* serta latensi inferensi tingkat mikrodetik per *flow*. Penelitian ini berkontribusi menyediakan arsitektur NIDS adaptif yang aman privasi dan hemat bandwidth untuk gerbang jaringan enterprise.
