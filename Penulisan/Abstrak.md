# ABSTRAK

**ANALISIS KINERJA DETEKSI NETWORK TRAFFIC INTRUSION MENGGUNAKAN METODE FEDERATED-CONTINUAL LEARNING PADA TESTBED PRIVATE CLOUD SERVER**  
*(Studi Pengaruh Elastic Weight Consolidation dan Federated Averaging pada Distribusi Data Non-IID Dua Client)*

**Nama Mahasiswa / NRP:** Rafli Alif Ihza Hartono / 5022211233  
**Departemen:** Teknik Elektro  
**Fakultas:** Teknologi Elektro dan Informatika Cerdas (FTEIC)  
**Institusi:** Institut Teknologi Sepuluh Nopember (ITS)  
**Dosen Pembimbing:** Dr.Ir. Achmad Affandi, DEA.  

---

### Abstrak (Versi Proposal)

Eskalasi serangan siber menuntut *Network Intrusion Detection System* (NIDS) untuk mampu mendeteksi variasi serangan baru secara dinamis tanpa mengorbankan privasi data lalu lintas jaringan. Namun, sentralisasi data mentah melanggar regulasi privasi, sementara model terdistribusi yang mempelajari serangan baru secara berurutan rentan mengalami *catastrophic forgetting* terhadap serangan terdahulu. Penelitian ini bertujuan menganalisis kinerja deteksi intrusi berbasis *Federated Continual Learning* (FCL) yang mengintegrasikan *Federated Averaging* (FedAvg) dan *Elastic Weight Consolidation* (EWC) pada kondisi data non-IID dua klien. Pengujian akan menggunakan dataset CIC-IDS2017 bersih (Senin hingga Rabu) dengan membuang fitur *Destination Port* guna mengeliminasi *shortcut learning* serta menghasilkan 63 fitur numerik. Seluruh 1.529.677 aliran data dipertahankan menggunakan *Weighted Cross-Entropy Loss* dan *gradient clipping* untuk mengatasi ketimpangan kelas ekstrem antara Normal, SSH-Patator, dan DoS. Skenario *Class-Incremental Learning* disimulasikan pada dua klien dengan partisi kelas Normal terstratifikasi 50/50 di seluruh hari perekaman. Model klasifikasi menggunakan arsitektur *Multilayer Perceptron* (MLP) kompak tiga lapis berkapasitas 6.275 parameter guna menjamin efisiensi komputasi *edge*. Klien lokal akan menghitung Matriks Informasi Fisher diagonal untuk memproteksi bobot kritis tugas terdahulu sebelum agregasi global oleh server Flower. Penerapan regularisasi EWC diharapkan mampu menekan *catastrophic forgetting* dengan mempertahankan skor Macro-F1 dan *Backward Transfer* (BWT) yang stabil. Model ini diproyeksikan mencapai efisiensi alokasi RAM yang unggul dibanding *replay buffer* serta menghasilkan waktu inferensi tingkat mikrodetik per *flow*. Penelitian ini berkontribusi menyediakan arsitektur NIDS adaptif yang aman privasi dan hemat bandwidth untuk gerbang jaringan enterprise operasional.

**Kata kunci:** *Catastrophic Forgetting*, *Continual Learning*, *Elastic Weight Consolidation*, *Federated Learning*, *Network Intrusion Detection System*, *Non-IID*

---

### Pemetaan Struktur Abstrak (Total 231 Kata / 11 Kalimat):

1. **Latar Belakang (2 Kalimat):**
   - *Kalimat 1:* Eskalasi serangan siber menuntut *Network Intrusion Detection System* (NIDS) untuk mampu mendeteksi variasi serangan baru secara dinamis tanpa mengorbankan privasi data lalu lintas jaringan.
   - *Kalimat 2:* Namun, sentralisasi data mentah melanggar regulasi privasi, sementara model terdistribusi yang mempelajari serangan baru secara berurutan rentan mengalami *catastrophic forgetting* terhadap serangan terdahulu.
2. **Tujuan (1 Kalimat):**
   - *Kalimat 3:* Penelitian ini bertujuan menganalisis kinerja deteksi intrusi berbasis *Federated Continual Learning* (FCL) yang mengintegrasikan *Federated Averaging* (FedAvg) dan *Elastic Weight Consolidation* (EWC) pada kondisi data non-IID dua klien.
3. **Metode (5 Kalimat):**
   - *Kalimat 4:* Pengujian akan menggunakan dataset CIC-IDS2017 bersih (Senin hingga Rabu) dengan membuang fitur *Destination Port* guna mengeliminasi *shortcut learning* serta menghasilkan 63 fitur numerik.
   - *Kalimat 5:* Seluruh 1.529.677 aliran data dipertahankan menggunakan *Weighted Cross-Entropy Loss* dan *gradient clipping* untuk mengatasi ketimpangan kelas ekstrem antara Normal, SSH-Patator, dan DoS.
   - *Kalimat 6:* Skenario *Class-Incremental Learning* disimulasikan pada dua klien dengan partisi kelas Normal terstratifikasi 50/50 di seluruh hari perekaman.
   - *Kalimat 7:* Model klasifikasi menggunakan arsitektur *Multilayer Perceptron* (MLP) kompak tiga lapis berkapasitas 6.275 parameter guna menjamin efisiensi komputasi *edge*.
   - *Kalimat 8:* Klien lokal akan menghitung Matriks Informasi Fisher diagonal untuk memproteksi bobot kritis tugas terdahulu sebelum agregasi global oleh server Flower.
4. **Hasil yang Diharapkan / Hipotesis (2 Kalimat):**
   - *Kalimat 9:* Penerapan regularisasi EWC diharapkan mampu menekan *catastrophic forgetting* dengan mempertahankan skor Macro-F1 dan *Backward Transfer* (BWT) yang stabil.
   - *Kalimat 10:* Model ini diproyeksikan mencapai efisiensi alokasi RAM yang unggul dibanding *replay buffer* serta menghasilkan waktu inferensi tingkat mikrodetik per *flow*.
5. **Signifikansi / Kontribusi (1 Kalimat):**
   - *Kalimat 11:* Penelitian ini berkontribusi menyediakan arsitektur NIDS adaptif yang aman privasi dan hemat bandwidth untuk gerbang jaringan enterprise operasional.

---

### Abstrak (Versi Laporan Akhir Tugas Akhir — Tanpa Kata "Akan")

Eskalasi serangan siber menuntut *Network Intrusion Detection System* (NIDS) untuk mampu mendeteksi variasi serangan baru secara dinamis tanpa mengorbankan privasi data lalu lintas jaringan. Namun, sentralisasi data mentah melanggar regulasi privasi, sementara model terdistribusi yang mempelajari serangan baru secara berurutan rentan mengalami *catastrophic forgetting* terhadap serangan terdahulu. Penelitian ini bertujuan menganalisis kinerja deteksi intrusi berbasis *Federated Continual Learning* (FCL) yang mengintegrasikan *Federated Averaging* (FedAvg) dan *Elastic Weight Consolidation* (EWC) pada kondisi data non-IID dua klien. Pengujian menggunakan dataset CIC-IDS2017 bersih (Senin hingga Rabu) dengan membuang fitur *Destination Port* guna mengeliminasi *shortcut learning* serta menghasilkan 63 fitur numerik. Seluruh 1.529.677 aliran data dipertahankan menggunakan *Weighted Cross-Entropy Loss* dan *gradient clipping* untuk mengatasi ketimpangan kelas ekstrem antara Normal, SSH-Patator, dan DoS. Skenario *Class-Incremental Learning* disimulasikan pada dua klien dengan partisi kelas Normal terstratifikasi 50/50 di seluruh hari perekaman. Model klasifikasi menggunakan arsitektur *Multilayer Perceptron* (MLP) kompak tiga lapis berkapasitas 6.275 parameter guna menjamin efisiensi komputasi *edge*. Klien lokal menghitung Matriks Informasi Fisher diagonal untuk memproteksi bobot kritis tugas terdahulu sebelum agregasi global oleh server Flower. Penerapan regularisasi EWC terbukti mampu menekan *catastrophic forgetting* dengan mempertahankan skor Macro-F1 dan *Backward Transfer* (BWT) yang stabil. Model ini membuktikan efisiensi alokasi RAM yang unggul dibanding *replay buffer* serta menghasilkan waktu inferensi tingkat mikrodetik per *flow*. Penelitian ini berkontribusi menyediakan arsitektur NIDS adaptif yang aman privasi dan hemat bandwidth untuk gerbang jaringan enterprise operasional.
