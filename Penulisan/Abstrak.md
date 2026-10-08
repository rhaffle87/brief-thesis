# ABSTRAK

**ANALISIS KINERJA DETEKSI NETWORK TRAFFIC INTRUSION MENGGUNAKAN METODE FEDERATED-CONTINUAL LEARNING PADA TESTBED PRIVATE CLOUD SERVER**  
*(Studi Pengaruh Elastic Weight Consolidation dan Federated Averaging pada Distribusi Data Non-IID Dua Client)*

**Nama Mahasiswa / NRP:** Rafli Alif Ihza Hartono / 5022211233  
**Departemen:** Teknik Elektro  
**Fakultas:** Teknologi Elektro dan Informatika Cerdas (FTEIC)  
**Institusi:** Institut Teknologi Sepuluh Nopember (ITS)  
**Dosen Pembimbing:** Dr.Ir. Achmad Affandi, DEA.  

---

### Abstrak

Penelitian ini mengembangkan sistem deteksi intrusi jaringan (*Network Intrusion Detection System* / NIDS) terdistribusi berbasis *Federated Continual Learning* (FCL) yang mengintegrasikan algoritma *Federated Averaging* (FedAvg) dengan regularisasi *Elastic Weight Consolidation* (EWC) untuk memitigasi degradasi memori katastrofik (*catastrophic forgetting*) pada kondisi data terdistribusi heterogen (*non-IID*) dan aliran serangan yang muncul secara sekuensial. Model dirancang menggunakan arsitektur *Multilayer Perceptron* (MLP) kompak dengan masukan 63 fitur statistik numerik aliran bersih yang telah dikurasi dari dataset tolok ukur CIC-IDS2017 tanpa menyertakan *Destination Port* guna mengeliminasi bias *shortcut learning*. Seluruh 1.529.677 baris aliran bersih dipertahankan tanpa pemangkasan data dengan memanfaatkan *Weighted Cross-Entropy Loss* untuk mengompensasi ketimpangan kelas ekstrem antara kelas Normal, SSH-Patator, dan DoS. Pembelajaran sekuensial dievaluasi pada dua node klien terdistribusi non-IID dengan partisi kelas Normal terstratifikasi 50/50 di seluruh hari perekaman, di mana retensi bobot parameter kritis diproteksi melalui penghitungan matriks informasi Fisher diagonal. Pengujian komparatif dieksekusi melintasi lima *random seed* independen pada skenario sentralisasi (E0, E1), federasi terisolasi (E2), hingga federasi sekuensial berbasis EWC (E3) dan *Experience Replay* (E4). Hasil evaluasi menunjukkan bahwa integrasi FedAvg dan EWC efektif mempertahankan skor Macro-F1 dan nilai *Backward Transfer* (BWT) yang stabil terhadap serangan masa lalu tanpa memerlukan penyimpanan buffer aliran mentah, menghasilkan efisiensi *RAM footprint* yang signifikan, serta membukukan rata-rata waktu inferensi tingkat mikrodetik per *flow*, menandakan kelayakan pendekatan ini untuk diterapkan secara adaptif, aman secara privasi, dan efisien pada perangkat *edge gateway* jaringan operasional nyata.

**Kata kunci:** *Catastrophic Forgetting*, *Continual Learning*, *Elastic Weight Consolidation*, *Federated Learning*, *Network Intrusion Detection System*, *Non-IID*
