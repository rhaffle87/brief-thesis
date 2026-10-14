# Analisis Rasio Kebaruan dan Mutu Pustaka Referensi

Dokumen ini menyajikan audit formal terhadap profil kebaruan (*freshness ratio*) dan mutu ilmiah dari seluruh **34 referensi** yang disitasi dalam Proposal Penelitian Seminar Tugas Akhir. Audit ini merujuk pada standar akreditasi jurnal nasional (SINTA/Arjuna), pedoman Buku Panduan Tugas Akhir Departemen Teknik Elektro FTEIC ITS, serta standar penilaian akademik internasional.

---

## 1. Ringkasan Eksekutif Rasio Kebaruan

Berdasarkan tahun publikasi (dihitung terhadap tahun acuan berjalan **2026**):

| Kategori Usia Publikasi | Rentang Tahun | Jumlah Referensi | Persentase | Status Pemenuhan Standar |
| :--- | :--- | :--- | :--- | :--- |
| **Sangat Mutakhir / Mutakhir (≤ 5 Tahun)** | **2021 - 2026** | **19 Pustaka** | **55,9%** | **Memenuhi Standar Mutu Akademik (> 50%)** |
| **Pustaka Fondasional / Induk (> 5 Tahun)** | **< 2021** | **15 Pustaka** | **44,1%** | **Justified (Seminal / Groundbreaking)** |
| **Total Seluruh Pustaka** | - | **34 Pustaka** | **100,0%** | **IEEE Sequential Verified [1]-[34]** |

> [!NOTE]
> **Kebijakan Akademik Terkait Rasio Kebaruan:**
> Standar penulisan karya ilmiah mensyaratkan separuh atau lebih pustaka berumur kurang dari 5 tahun (terbitan 2021-2026). Pustaka dengan usia lebih dari 5 tahun diperbolehkan dan diwajibkan secara etika ilmiah apabila berstatus sebagai **pustaka primer induk (*seminal papers*)**, **buku teks standar industri (*canonical textbooks*)**, atau **pencetus pertama suatu algoritma/arsitektur dasar**.

---

## 2. Inventarisasi dan Justifikasi Pustaka Primer Induk (> 5 Tahun)

Sebanyak 15 pustaka dengan tahun terbit sebelum 2021 dipertahankan secara sengaja berdasarkan justifikasi metodologis berikut:

| No | Kunci Sitasi | Penulis & Tahun | Judul Pustaka / Sumber | Justifikasi Metodologis (Tidak Boleh Diganti) |
| :--- | :--- | :--- | :--- | :--- |
| 1 | `[3]` | McMahan dkk. (2017) | *Communication-Efficient Learning of Deep Networks from Decentralized Data* (AISTATS) | **Paper Induk Federated Learning:** Sumber primer penemu algoritma *Federated Averaging* (FedAvg). Wajib dikutip langsung. |
| 2 | `[4]` | Zhao dkk. (2018) | *Federated Learning with Non-IID Data* (arXiv:1806.00582) | **Studi Fondasional Non-IID:** Karya rujukan utama yang membuktikan secara analitis dan empiris penurunan akurasi FedAvg akibat pergeseran bobot lokal pada data non-IID. |
| 3 | `[5]` | Kirkpatrick dkk. (2017) | *Overcoming catastrophic forgetting in neural networks* (PNAS) | **Paper Induk Elastic Weight Consolidation (EWC):** Penemu formulasi regularisasi penalti diagonal Fisher. Wajib dikutip sebagai sumber utama. |
| 4 | `[6]` | Stallings (2017) | *Cryptography and Network Security: Principles and Practice* (Pearson, 7th Ed.) | **Buku Teks Kanonikal Keamanan Jaringan:** Buku acuan standar global untuk definisi formal *CIA Triad* dan dasar keamanan komputer. |
| 5 | `[7]` | Sharafaldin dkk. (2018) | *Toward Generating a New Intrusion Detection Dataset and Intrusion Traffic Characterization* (ICISSP) | **Paper Induk Dataset CIC-IDS2017:** Dokumen resmi pencipta dataset tolok ukur yang digunakan dalam penelitian ini. |
| 6 | `[10]` | Lopez-Paz & Ranzato (2017) | *Gradient Episodic Memory for Continual Learning* (NeurIPS) | **Paper Penemu Metrik Evaluasi Continual Learning:** Sumber primer perumus metrik *Backward Transfer* (BWT) dan analisis stabilitas memori. |
| 7 | `[20]` | Ring dkk. (2019) | *A survey of network-based intrusion detection data sets* (Computers & Security) | **Survei Komprehensif NIDS:** Analisis taksonomi mendalam komparasi dataset IDS jaringan dan pembagian arsitektur HIDS/NIDS serta SIDS/ABDS. |
| 8 | `[21]` | Paszke dkk. (2019) | *PyTorch: An Imperative Style, High-Performance Deep Learning Library* (NeurIPS) | **Paper Resmi PyTorch:** Sumber primer kerangka kerja komputasi tensorial dan *Autograd* yang digunakan dalam implementasi kode. |
| 9 | `[22]` | Beutel dkk. (2020) | *Flower: A Friendly Federated Learning Research Framework* (arXiv:2007.14390) | **Paper Resmi Flower:** Sumber primer kerangka kerja orkestrasi federasi terdistribusi dan simulasi komputasi yang dipakai dalam penelitian. |
| 10 | `[23]` | Goodfellow dkk. (2016) | *Deep Learning* (MIT Press) | **Buku Teks Kanonikal Deep Learning:** Buku babon kecerdasan buatan rujukan dunia untuk landasan teoretis arsitektur *Multilayer Perceptron* (MLP). |
| 11 | `[24]` | Fawcett (2006) | *An introduction to ROC analysis* (Pattern Recognition Letters) | **Paper Induk Analisis Evaluasi Klasifikasi:** Rujukan kanonikal untuk formulasi *Confusion Matrix*, Presisi, Recall, dan F1-Score. |
| 12 | `[25]` | Bergstra dkk. (2011) | *Algorithms for Hyper-Parameter Optimization* (NeurIPS) | **Paper Induk Algoritma TPE:** Sumber orisinal penemu algoritma *Tree-structured Parzen Estimator* yang diimplementasikan pada Optuna. |
| 13 | `[26]` | Hutter dkk. (2019) | *Automated Machine Learning: Methods, Systems, Challenges* (Springer) | **Buku Teks Standar AutoML:** Rujukan komprehensif metodologi optimasi hiperparameter Bayesian pada sistem komputasi cerdas. |
| 14 | `[28]` | Loshchilov & Hutter (2019) | *Decoupled Weight Decay Regularization* (ICLR) | **Paper Induk AdamW:** Sumber orisinal penemu algoritma *decoupled weight decay* yang mengatasi kelemahan penalti L2 pada Adam konvensional. |
| 15 | `[29]` | Nair & Hinton (2010) | *Rectified Linear Units Improve Restricted Boltzmann Machines* (ICML) | **Paper Induk Fungsi Aktivasi ReLU:** Sumber orisinal pengenalan fungsi aktivasi non-linear pemotong nilai negatif pada jaringan saraf tiruan mendalam. |

---

## 3. Distribusi Pustaka Mutakhir (≤ 5 Tahun, 2021 - 2026)

Sebanyak 19 pustaka terkini diterbitkan dalam rentang 5 tahun terakhir, mendominasi studi literatur terkait perkembangan mutakhir *Federated Continual Learning* dan keamanan jaringan:

1. `[1]` Check Point Research (**2025**) - *Q1 2025 Global Cyber Attack Report* (Laporan industri global lonjakan serangan siber).
2. `[2]` Federal Bureau of Investigation (**2024**) - *2024 Internet Crime Report* (Statistik kerugian insiden siber di Amerika Serikat).
3. `[8]` Popoola dkk. (**2022**) - *Federated Deep Learning for Zero-Day Botnet Attack Detection in IoT-Edge Devices* (IEEE Internet of Things Journal).
4. `[9]` Ruzafa-Alcázar dkk. (**2023**) - *Intrusion Detection Based on Privacy-Preserving Federated Learning for the Industrial IoT* (IEEE Transactions on Industrial Informatics).
5. `[11]` Dong dkk. (**2022**) - *Federated Class-Incremental Learning* (CVPR 2022, integrasi FL dan penambahan kelas sekuensial).
6. `[12]` Jin dkk. (**2024**) - *FL-IIDS: A novel federated learning-based incremental intrusion detection system* (Future Generation Computer Systems).
7. `[13]` Rosay dkk. (**2022**) - *Network Intrusion Detection: A Comprehensive Analysis of CIC-IDS2017* (ICISSP 2022, audit dataset).
8. `[14]` Dube (**2024**) - *Faulty use of the CIC-IDS 2017 dataset in information security research* (Journal of Computer Virology and Hacking Techniques).
9. `[15]` Engelen dkk. (**2021**) - *Troubleshooting an Intrusion Detection Dataset: The CICIDS2017 Case Study* (IEEE SPW 2021, analisis konstruksi alur TCP).
10. `[16]` Rinandri (**2025**) - *Pendekatan Semi-Supervised Learning untuk Sistem Deteksi Intrusi Jaringan Real-Time Berbasis GNN-AE pada Arsitektur Structemp* (Tugas akhir rujukan lokal Departemen Teknik Elektro FTEIC ITS).
11. `[17]` Sarhan dkk. (**2022**) - *Towards a Standard Feature Set for Network Intrusion Detection System Datasets* (Mobile Networks and Applications).
12. `[18]` Van de Ven dkk. (**2022**) - *Three types of incremental learning* (Nature Machine Intelligence, taksonomi Task-IL, Domain-IL, dan Class-IL).
13. `[19]` Ghallab dkk. (**2025**) - *Mitigating Catastrophic Forgetting in Continual Learning Using the Gradient-Based Approach: A Literature Review* (IJACSA 2025).
14. `[27]` Schmidt dkk. (**2021**) - *Descending through a Crowded Valley - Benchmarking Deep Learning Optimizers* (ICML 2021).
15. `[30]` Dubey dkk. (**2022**) - *Activation Functions in Deep Learning: A Comprehensive Survey and Benchmark* (Neurocomputing 2022).
16. `[31]` Hernandez-Ramos dkk. (**2025**) - *Intrusion Detection Based on Federated Learning: A Systematic Review* (ACM Computing Surveys).
17. `[32]` Buyuktanir dkk. (**2025**) - *Federated learning in intrusion detection: advancements, applications, and future directions* (Cluster Computing).
18. `[33]` Rehman dkk. (**2026**) - *Incremental Federated Learning for Intrusion Detection in IoT Networks under Evolving Threat Landscape* (arXiv:2603.10776).
19. `[34]` Hamedi dkk. (**2025**) - *Federated Continual Learning: Concepts, Challenges, and Solutions* (arXiv:2502.07059).

---

## 4. Analisis Proporsi Jenis Sumber Pustaka

| Jenis Publikasi | Jumlah | Persentase | Rincian Entri |
| :--- | :--- | :--- | :--- |
| **Jurnal Ilmiah Internasional Bereputasi** (IEEE, Elsevier, Nature, PNAS, Springer, ACM) | **13** | **38,2%** | `[5]`, `[8]`, `[9]`, `[12]`, `[14]`, `[17]`, `[18]`, `[19]`, `[20]`, `[24]`, `[30]`, `[31]`, `[32]` |
| **Prosiding Konferensi Internasional Top-Tier** (NeurIPS, ICML, ICLR, CVPR, AISTATS, ICISSP, IEEE SPW) | **11** | **32,4%** | `[3]`, `[7]`, `[10]`, `[11]`, `[13]`, `[15]`, `[21]`, `[25]`, `[27]`, `[28]`, `[29]` |
| **Repositori Pra-cetak Ilmiah Terverifikasi** (arXiv) | **4** | **11,8%** | `[4]`, `[22]`, `[33]`, `[34]` |
| **Buku Teks Akademik Resmi / Buku Babon** (MIT Press, Pearson, Springer) | **3** | **8,8%** | `[6]`, `[23]`, `[26]` |
| **Laporan Resmi Lembaga Keamanan Siber** (Check Point, FBI) | **2** | **5,9%** | `[1]`, `[2]` |
| **Tugas Akhir Alumnus Departemen (Baseline Komparasi Lokal)** | **1** | **2,9%** | `[16]` |
| **Total** | **34** | **100,0%** | - |

**Kesimpulan:**
- **70,6%** referensi bersumber langsung dari publikasi primer peer-reviewed (*Jurnal Ilmiah Internasional* dan *Konferensi Top-Tier*).
- Sitasi tugas akhir alumnus (`[16]`) dibatasi secara ketat menjadi **1 pustaka saja (2,9%)**, murni ditempatkan pada Sub-bab 2.3 (Tabel 2.1) dan Sub-bab 2.12.3 sebagai tolok ukur komparasi lokal lingkungan Departemen Teknik Elektro FTEIC ITS.
- Seluruh teori dasar, formulasi matematika, arsitektur perangkat lunak, algoritma optimasi, dan metrik evaluasi kini 100% didukung oleh pustaka primer orisinal internasional.
