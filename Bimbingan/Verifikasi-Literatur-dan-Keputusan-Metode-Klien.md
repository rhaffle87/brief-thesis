# Verifikasi Literatur Lanjutan & Keputusan: Metode Pembanding + Jumlah Klien

**Tujuan Dokumen:** Menindaklanjuti `Pembahasan-Menyeluruh-Bimbingan-Lanjutan.md` dengan (1) audit verifikasi sumber primer untuk setiap nama metode baru yang diajukan sebagai metode "serupa/linier" dengan FCL, dan (2) keputusan final mengenai metode pembanding tambahan serta justifikasi ilmiah jumlah klien, siap dipakai pada pertemuan bimbingan berikutnya.

**Metode Verifikasi:** Web search terhadap sumber primer (arXiv abstract page, halaman proceedings ICML/CVPR/ICCV/NeurIPS, DOI Crossref) — setara dengan proses yang sudah dipakai di `Literatur/Crosscheck.md`.

---

## 1. Tabel Verifikasi Nama Metode (Rumpun Linier FCL)

| No | Metode | Klaim Semula | Hasil Verifikasi | Status |
|---|---|---|---|---|
| 1 | **FedWeIT** | Yoon et al., ICML 2021 | Yoon, Jeong, Lee, Yang, Hwang. *"Federated Continual Learning with Weighted Inter-client Transfer."* PMLR 139:12073-12086, 2021. arXiv:2003.03196 | ✅ Terverifikasi — sesuai |
| 2 | **GLFC** | Dong et al., CVPR 2022 | Dong, Wang, Fang, Sun, Xu, Wang, Zhu. *"Federated Class-Incremental Learning"* (memperkenalkan model GLFC). CVPR 2022. DOI: 10.1109/CVPR52688.2022.00992. arXiv:2203.11473 | ✅ Terverifikasi — sesuai |
| 3 | **FedCurv** | Shoham et al., arXiv 2019 | Shoham, Avidor, Keren, Israel, Benditkis, Mor-Yosef, Zeitak. *"Overcoming Forgetting in Federated Learning on Non-IID Data."* arXiv:1910.07796 (17 Okt 2019) | ✅ Terverifikasi — sesuai |
| 4 | **Ditto** | Li et al., ICML 2021 | Li, Hu, Beirami, Smith. *"Ditto: Fair and Robust Federated Learning Through Personalization."* ICML 2021. arXiv:2012.04221 | ✅ Terverifikasi — sesuai |
| 5 | **TARGET** | Zhang et al., **CVPR** 2023 | Zhang, Chen, Zhuang, Lv/Lyu. *"TARGET: Federated Class-Continual Learning via Exemplar-Free Distillation."* **ICCV 2023** (bukan CVPR). DOI: 10.1109/ICCV51070.2023.00441. arXiv:2303.06937 | ⚠️ **Venue salah** — koreksi ke ICCV 2023 |
| 6 | **pFedMe** | Disebut sebagai "pFedMe/Per-FedAvg (Fallah et al., NeurIPS 2020)" | **pFedMe** = Dinh, Tran, Nguyen. *"Personalized Federated Learning with Moreau Envelopes."* NeurIPS 2020. arXiv:2006.08848. **Per-FedAvg** = Fallah, Mokhtari, Ozdaglar — paper **terpisah** (meta-learning/MAML based) | ⚠️ **Dua paper digabung jadi satu atribusi** — pisahkan jika dipakai keduanya |
| 7 | **Ruzafa-Alcázar et al.** | "2-4 klien IIoT" | Ruzafa-Alcázar, Fernández-Saura, Mármol-Campos, González-Vidal, Hernández-Ramos, Bernal-Bernabé, Skarmeta. *"Intrusion Detection Based on Privacy-Preserving Federated Learning for the Industrial IoT."* IEEE Trans. Industrial Informatics, 2023, Vol 19(2):1145-1154. DOI: 10.1109/TII.2021.3126728 | ✅ Paper nyata, **tapi klaim "2-4 klien" belum diverifikasi ke isi paper** — cek dulu sebelum dipakai sebagai angka pasti |
| 8 | **"Jin et al. (2024) pakai 2-5 klien"** | Klaim jumlah klien spesifik | Dicek langsung ke `Literatur/Jin-2024-FL-IIDS.md` (catatan hasil baca PDF sendiri) — tertulis eksplisit: *"Scalability - tested on small-scale (**how many clients not clearly stated**)"* | ❌ **Fabrikasi — JANGAN DIPAKAI**. Paper ini sendiri tidak menyebutkan jumlah klien |
| 9 | **"Hernandez-Ramos: >60% eksperimen FL-NIDS pakai 2-10 klien"** | Klaim statistik dari survei | Tidak ditemukan di `Literatur/Hernandez-Ramos-2025-FL-IDS-Survey.md` | ⚠️ **Belum terverifikasi** — perlu baca ulang PDF primer sebelum dipakai sebagai statistik ke dosen |
| 10 | SCAFFOLD, FedNova, Online EWC, SI, MAS, LwF, PackNet, LoRA-CL, A-GEM, Experience Replay | Berbagai | **Selesai diverifikasi penuh 2026-10-21** (Crossref + arXiv + PMLR + CVF + prosiding NeurIPS) — rincian di Bagian 4.1–4.3: 3 nama terbukti bukan judul paper yang ada, 5 venue salah, 1 atribusi tercampur | ✅ Selesai — terapkan koreksi Bagian 4 sebelum dikutip di naskah |

### ⚠️ Temuan tambahan (bukan dari metode baru, ditemukan saat proses verifikasi ini)

**Konflik DOI internal di vault sendiri:** `Literatur/Daftar-Pustaka.md` dan `Literatur/Crosscheck.md` mencatat Hernandez-Ramos et al. (2025) sebagai **ACM Computing Surveys, DOI 10.1145/3731596**, sedangkan `Literatur/Hernandez-Ramos-2025-FL-IDS-Survey.md` mencatat **IEEE Communications Surveys & Tutorials, DOI 10.1109/COMST.2024.3499824**. Dua venue dan DOI berbeda untuk klaim paper yang sama — **perlu diselesaikan sebelum Bab 2 difinalisasi**, karena kalau penguji mengecek DOI dan tidak cocok, ini jadi temuan kredibilitas yang buruk.

---

## 2. Keputusan: Metode Pembanding Tambahan

### Rekomendasi Utama: **FedCurv (Shoham et al., 2019)**

| Kriteria | FedCurv | FedWeIT / GLFC / TARGET |
|---|---|---|
| Kedekatan konseptual | Perluasan langsung EWC ke federated setting — pakai Fisher Information Matrix yang sama persis dengan yang sudah dihitung di Client A & B | Arsitektur berbeda total (parameter decomposition, proxy server, generator sintetis) |
| Biaya implementasi | Kecil — tinggal mengirim diagonal Fisher lokal ke server sebagai penalti konsensus tambahan, tanpa redesign MLP | Besar — butuh sparse mask per-task (FedWeIT), proxy server + distillation (GLFC), atau generator tambahan (TARGET) |
| Kesesuaian privasi | Tetap zero-raw-data (hanya kirim nilai Fisher, bukan sampel) | GLFC & TARGET didesain untuk benchmark vision besar, bukan tabular IDS ringan |
| Relevansi ke temuan sendiri | **Bisa langsung menguji hipotesis "EWC Dilution Effect"** (poin 8, briefing sebelumnya): apakah berbagi Fisher ke server memperbaiki atau memperburuk pengenceran gradien akibat ketimpangan data Client A (425.599 baris train) vs Client B (547.512 baris train, hasil praproses 2026-10-21) | Tidak menjawab hipotesis spesifik ini |

**Usulan konkret:** tambahkan **E4b: FedAvg + FedCurv** sebagai eksperimen opsional di samping E4 (FedAvg + EWC lokal) pada Matriks E0-E4.

### Alternatif (jika dosen minta pembanding dari sisi optimasi non-IID, bukan CL): **FedProx (Li et al., 2020)**

- Sudah ada di `Daftar-Pustaka.md` dan **sudah terverifikasi** — nol biaya verifikasi tambahan.
- Implementasi minimal: tambah satu suku proksimal $\frac{\mu}{2}\|\theta-\theta^t\|^2$.
- Menguji apakah *client drift* (bukan *forgetting*) berkontribusi ke gap performa non-IID di RM1.

### Yang TIDAK direkomendasikan sebagai eksperimen wajib

FedWeIT, GLFC, TARGET — kompleksitas desain (dekomposisi parameter, proxy server, generator sintetis) tidak sepadan dengan skala MLP 6.211 parameter dan batas waktu 14-16 minggu. Cukup disebut di Bab 2 sebagai *positioning statement*:

> "Penelitian ini tidak mengadopsi arsitektur dekomposisi-parameter (FedWeIT) atau distilasi generatif (TARGET/GLFC) karena kompleksitas komputasi tambahan tidak sepadan dengan skala model MLP tabular ringan yang menjadi fokus efisiensi edge pada riset ini."

---

## 3. Keputusan: Jumlah Klien (Justifikasi Ilmiah)

### Argumen 1 — Kategori FL yang tepat: Cross-Silo, bukan Cross-Device

Rujukan: **Kairouz et al. (2021), "Advances and Open Problems in Federated Learning"**, Foundations and Trends in Machine Learning, Vol. 14, Issue 1-2. arXiv:1912.04977. (Paper rujukan standar FL, disusun oleh peneliti FL utama Google Research dkk.)

Paper ini membagi FL menjadi dua rezim:
- **Cross-device FL:** jutaan klien tidak-reliable (smartphone, IoT murah) — skala besar relevan.
- **Cross-silo FL:** sedikit klien yang reliable (organisasi, data center, institusi) — literatur pada umumnya memakai **2 sampai puluhan klien**.

Testbed penelitian ini (Proxmox VE, sensor gateway sektor dengan daya komputasi tetap, bukan perangkat mobile yang hilang-sambung) **jelas cross-silo**, bukan cross-device. Argumen "180 hektar butuh banyak sensor fisik" tidak otomatis berarti "butuh banyak klien FL" — satu **Edge Gateway Sektor** dapat mengagregasi puluhan sensor fisik di bawahnya; jumlah *FL client* yang relevan secara statistik adalah jumlah **gateway**, bukan jumlah sensor mentah.

### Argumen 2 — Perbandingan dengan jumlah klien di studi FL-IDS/IIoT nyata

| Studi | Domain | Jumlah Klien |
|---|---|---|
| D̈ıoT (arXiv:1804.07474) | FL anomaly detection untuk IoT | 2 – 15 klien |
| Lightweight Cluster-Based FL-IDS (arXiv:2602.12543) | FL-IDS untuk IoT heterogen | 20 klien |
| FL untuk anomaly detection pompa industri (arXiv:2110.08202) | Industrial IoT | 10 klien |
| FL-BCID (arXiv:2505.15376) | FL + blockchain IDS untuk IIoT | 10 klien |
| **Penelitian ini** | FL-CL IDS, testbed private cloud | **2 klien (ekstrem non-IID)** |

Kesimpulan: 2 klien berada di ujung bawah rentang yang lazim (2-20) untuk riset cross-silo FL-IDS/IIoT, bukan angka yang asal dipilih.

### Argumen 3 — Desain eksperimen terkontrol, bukan keterbatasan

2 klien dengan partisi ekstrem non-IID (Client A murni SSH-Patator, Client B murni DoS, **zero overlap kelas**) adalah *controlled worst-case design* — dipilih untuk mengisolasi dan membuktikan secara jelas apakah EWC mampu menahan *catastrophic forgetting* pada kondisi paling ekstrem, sebelum diklaim bekerja pada skenario yang lebih realistis dan kompleks. Pola yang sama dipakai pada paper fondasional non-IID yang sudah ada di korpus (Hsu et al., 2019, Dirichlet partition) — mulai dari kondisi ekstrem terkontrol, baru digeneralisasi.

### Jalan keluar jika dosen tetap mendesak skalabilitas

Tunjukkan bahwa arsitektur Flower + partisi Dirichlet($\alpha$) yang sudah disiapkan **siap diskalakan ke K=4 atau K=8** tanpa perubahan desain inti, tetapi hal ini diposisikan sebagai **future work eksplisit di Bab 5**, bukan kewajiban skripsi ini — karena menambah K akan melipatgandakan waktu komputasi tanpa mengubah kesimpulan inti mengenai efektivitas EWC terhadap forgetting.

---

## 4. Hasil Verifikasi Lengkap Seluruh Nama (Crossref + arXiv, 2026-10-21)

Verifikasi primer via Crossref REST API, arXiv export API, PMLR, CVF Open Access, prosiding NeurIPS/ICLR, dan source code CICFlowMeter (UNBCIC/CICFlowMeter). Melengkapi Bagian 1 (yang sebelumnya menunda 10 nama pada baris 10).

### 4.1 Rumpun Continual Learning

| Metode | Sitasi Benar (penulis, judul, venue) | Identifier | Status |
|---|---|---|---|
| EWC | Kirkpatrick et al., *"Overcoming catastrophic forgetting in neural networks"*, PNAS 114(13), 2017 | DOI 10.1073/pnas.1611835114 | ✅ (sudah di Crosscheck baris 3) |
| "Online EWC" (Schwarz 2018) | Schwarz et al., *"Progress & Compress: A scalable framework for continual learning"*, ICML 2018. **"Online EWC" hanya julukan** untuk regularizer di dalamnya — bukan judul paper | arXiv:1805.06370 | ⚠️ Kutip sebagai *Progress & Compress* |
| SI | Zenke, Poole, Ganguli, *"Continual Learning Through Synaptic Intelligence"*, ICML 2017 | arXiv:1703.04200 | ✅ |
| MAS | Aljundi et al., *"Memory Aware Synapses: Learning What (not) to Forget"*, **ECCV 2018** | DOI 10.1007/978-3-030-01219-9_9 | ⚠️ Venue ECCV, bukan CVPR/TPAMI |
| LwF | Li & Hoiem, *"Learning Without Forgetting"*, **ECCV 2016**; versi jurnal TPAMI (online 2017, issue 2018) | ECCV: 10.1007/978-3-319-46493-0_37 · TPAMI: 10.1109/tpami.2017.2773081 | ⚠️ Bukan "CVPR 2017" |
| **"Federated LwF (Li & Hoiem, 2017)"** | **Tidak ada paper** dengan nama itu. LwF (2016/2018) single-machine dan mendahului FL. Kandidat nyata FL+distilasi: Ma et al., *"Continual Federated Learning Based on Knowledge Distillation"*, IJCAI 2022 | DOI 10.24963/ijcai.2022/303 | ❌ **Nama fabrikasi — jangan dikutip** |
| PackNet | Mallya & Lazebnik, *"PackNet: Adding Multiple Tasks to a Single Network by Iterative Pruning"*, CVPR 2018 | DOI 10.1109/cvpr.2018.00810 | ✅ |
| **"LoRA-CL (Hu et al., 2022)"** | Hu et al. 2022 = *"LoRA: Low-Rank Adaptation of Large Language Models"*, ICLR 2022 — **bukan continual learning**. Tidak ada method paper bernama "LoRA-CL". Kandidat nyata LoRA→CL: Chitale et al., arXiv:2311.02428 | LoRA: arXiv:2106.09685 | ❌ **Salah atribusi — jangan dikutip** |
| A-GEM | Chaudhry et al., *"Efficient Lifelong Learning with A-GEM"*, **ICLR 2019** | arXiv:1812.00420 | ⚠️ Venue ICLR, bukan ICML |
| Experience Replay (Chaudhry) | Chaudhry et al., *"On Tiny Episodic Memories in Continual Learning"*, 2019 | arXiv:1902.10486 | ✅ (judul ≠ "Experience Replay" generik) |
| GEM | Lopez-Paz & Ranzato, *"Gradient Episodic Memory for Continual Learning"*, **NeurIPS 2017** | arXiv:1706.08840 | ⚠️ Venue NeurIPS (Crosscheck baris 6 sudah benar) |

### 4.2 Rumpun Federated Learning

| Metode | Sitasi Benar | Identifier | Status |
|---|---|---|---|
| FedWeIT | Yoon et al., *"Federated Continual Learning with Weighted Inter-client Transfer"*, ICML 2021 | arXiv:2003.03196 | ✅ |
| FedCurv | Shoham et al., *"Overcoming Forgetting in Federated Learning on Non-IID Data"*, 2019 (NeurIPS 2019 FL workshop; nama metode FedCurv ada di dalam paper, bukan di judul) | arXiv:1910.07796 | ✅ |
| GLFC | Dong et al., ***"Federated Class-Incremental Learning"***, CVPR 2022 — "GLFC" adalah **nama framework di dalam paper**, bukan judul | DOI 10.1109/CVPR52688.2022.00992 · arXiv:2203.11473 | ⚠️ Judul klaim "Global-Local Forgetting Compensation" tidak ada di indeks mana pun — kutip judul paper yang benar |
| TARGET | Zhang et al., *"TARGET: Federated Class-Continual Learning via **Exemplar-Free Distillation**"*, **ICCV 2023** | DOI 10.1109/ICCV51070.2023.00441 | ⚠️ Venue dan judul keduanya salah di klaim awal |
| Ditto | Li et al., *"Ditto: Fair and Robust Federated Learning Through Personalization"*, **ICML 2021** | arXiv:2012.04221 | ✅ (klaim asli benar; dugaan NeurIPS keliru) |
| pFedMe | **Dinh, Tran & Nguyen**, *"Personalized Federated Learning with Moreau Envelopes"*, NeurIPS 2020 | arXiv:2006.08848 | ⚠️ **Bukan Fallah et al.** |
| Per-FedAvg | Fallah, Mokhtari, Ozdaglar, *"Personalized Federated Learning with Theoretical Guarantees: A Model-Agnostic Meta-Learning Approach"*, NeurIPS 2020 | prosiding NeurIPS 2020 | ✅ (paper terpisah dari pFedMe) |
| SCAFFOLD | Karimireddy et al., *"SCAFFOLD: Stochastic Controlled Averaging for Federated Learning"*, ICML 2020 | arXiv:1910.06378 | ✅ |
| FedNova | **Wang (Jianyu) et al.**, *"Tackling the Objective Inconsistency Problem in Heterogeneous Federated Optimization"*, NeurIPS 2020 | arXiv:2007.07481 | ⚠️ "Federated Learning with Matched Averaging" (H. Wang, ICLR 2020, arXiv:2002.06440) adalah **algoritma berbeda** — jangan digabung |
| FedProx | Li et al., *"Federated Optimization in Heterogeneous Networks"*, MLSys 2020 | arXiv:1812.06127 | ✅ (sudah di Crosscheck baris 22) |
| APFL | Deng, Kamani, Mahdavi, *"Adaptive Personalized Federated Learning"*, 2020 (versi kanonik arXiv; tidak ada versi jurnal terindeks) | arXiv:2003.13461 | ✅ |
| Kairouz et al. | *"Advances and Open Problems in Federated Learning"*, Foundations and Trends in ML 14(1-2):1–210, 2021. §2.2 eksplisit "Cross-Silo Federated Learning" vs cross-device — **mengonfirmasi argumen silo di Bagian 3** | DOI 10.1561/2200000083 · arXiv:1912.04977 | ✅ |

### 4.3 Klaim Empiris Jumlah Klien, Nama Taksonomi, dan Angka Teknis

| Klaim | Hasil | Status |
|---|---|---|
| Ruzafa-Alcazar et al. (2023), "2-4 klien IIoT" | Paper nyata: *"Intrusion Detection Based on Privacy-Preserving Federated Learning for the Industrial IoT"*, IEEE TII 19(2):1145–1154. Dari PDF: ToN_IoT dibagi 6 pihak (0–5), entropy filter memilih **4 klien FL**. Angka "2-4" tidak dinyatakan di paper | ⚠️ Paper nyata, **angka salah** — kutip sebagai 4 klien (dari 6 pihak) |
| DioT, 2-15 klien | Nguyen et al., *"DıoT: A Federated **Self-learning** Anomaly Detection System for IoT"*, ICDCS 2019. PDF: "ranging from 2 to 15" klien — **angka terkonfirmasi**; judul klaim ("adaptive") salah | ✅ Angka benar, ⚠️ judul dikoreksi |
| "FL anomaly detection pompa industri, 10 klien" (arXiv:2110.08202) | Paper asli: Holly et al., *"Evaluation of Hyperparameter-Optimization Approaches in an Industrial Federated Learning System"* — topik HPO, bukan deteksi anomali itu sendiri; "10 klien" hanya berlaku untuk partisi **MNIST** di paper tersebut, bukan setup pompa | ⚠️ **Salah karakterisasi** — reformulasi atau ganti sumber |
| FL-BCID, N=10 (arXiv:2505.15376) | Ali et al., *"Federated Learning-Enhanced Blockchain Framework for Privacy-Preserving Intrusion Detection in Industrial IoT"*. PDF: "10 edge nodes (N = 10) and a single aggregator" | ✅ **Terkonfirmasi penuh** |
| "Lightweight cluster-based FL-IDS, 20 klien" (tanpa sitasi) | **Izadi & Ahmadi**, *"Lightweight Cluster-Based Federated Learning for Intrusion Detection in Heterogeneous IoT Networks"*, arXiv:2602.12543 (2026). PDF: "3 cluster nodes, 20 clients and a single server" | ✅ Ditemukan sitasi kanoniknya |
| Swarm Learning (tanpa sitasi di taksonomi) | Warnat-Herresthal et al., *"Swarm Learning for decentralized and confidential clinical machine learning"*, **Nature 593:265–270 (2021)** | ✅ DOI 10.1038/s41586-021-03583-3 |
| "FTRL-FL", "Online FedAvg", "Dynamic Online FL" | Pencarian exact-phrase di arXiv: **0 hit** untuk ketiganya — label taksonomi, bukan nama paper | ❌ **Bukan sitasi** — hapus atau ganti karya nyata (McMahan 2013 FTRL-Proximal; karya online-FL nyata: arXiv:2102.10861, arXiv:2503.15210) |
| "Jin et al. (2024) pakai 2-5 klien" | Tidak ada di catatan vault; catatan sendiri menulis *"how many clients not clearly stated"* | ❌ **Fabrikasi** (sudah dipastikan di Bagian 1 baris 8) |
| "Hernandez-Ramos: >60% eksperimen pakai 2-10 klien" | Tidak ditemukan di `Literatur/Hernandez-Ramos-2025-FL-IDS-Survey.md` | ❌ **Tidak terverifikasi — jangan dipakai** |
| CICFlowMeter "inactive timeout 120 detik" | Source code UNBCIC/CICFlowMeter: `flowTimeout=120s`, tetapi **`activityTimeout`(inaktivitas)=5 detik**, flow bidirectional. Repo ahlamer/unb-celab lama sudah 404 | ❌ **Kontradiktibel** — 120 s adalah *total flow timeout*, bukan inaktivitas. Argumen "deteksi slowloris tertunda 120 detik" harus diargumen ulang atau dibuang |

### 4.4 Temuan Struktural (bukan sitasi eksternal)

1. **Konflasi "Jin 2024" di dalam vault:** `Crosscheck.md` baris 5 = Jin, **Dai**, Xiao, Li, *"…collaborative intrusion detection against concept drift"*, Computers & Security, DOI 10.1016/j.cose.2023.103577 — sedangkan `Literatur/Jin-2024-FL-IIDS.md` = Jin, **Zhou**, Li, Wu, Duan, *"FL-IIDS…"*, Future Generation Computer Systems, DOI 10.1016/j.future.2023.09.019. **Dua paper berbeda** (penulis, judul, venue, DOI berbeda) dikunci di bawah kunci "Jin 2024" yang sama di Dashboard. Beri kunci sitasi terpisah sebelum Bab 2 menulis "Jin et al. (2024)".
2. **Dokumen taksonomi yang dikirim ke dosen** (`Pembahasan-Menyeluruh-Bimbingan-Lanjutan.md`) masih memuat error yang sudah dikoreksi di Bagian 1 — termasuk "pFedMe/Per-FedAvg (Fallah)" sebagai satu entri dan TARGET sebagai CVPR 2023, plus nama-nama fabrikasi ("Federated LwF", "LoRA-CL", "FTRL-FL", "Online FedAvg", "Dynamic Online FL"). Perbaiki sebelum dipakai di pertemuan berikutnya.

---

## 5. Ringkasan Tindak Lanjut (diperbarui 2026-10-21)

1. ✅ **Aman dikutip dengan metadata Bagian 4:** FedWeIT, FedCurv, Ditto, SCAFFOLD, FedProx, APFL, Per-FedAvg, Kairouz et al., SI, PackNet, Experience Replay (judul asli), FL-BCID, DioT (judul dikoreksi), Izadi & Ahmadi 2026, Swarm Learning.
2. ⚠️ **Koreksi wajib sebelum kutip:** TARGET → ICCV 2023 + judul *Exemplar-Free Distillation*; pFedMe → Dinh et al.; FedNova → Wang et al. NeurIPS 2020 (arXiv:2007.07481); MAS → ECCV 2018; LwF → ECCV 2016/TPAMI 2018; A-GEM → ICLR 2019; GEM → NeurIPS 2017; "Online EWC" → kutip *Progress & Compress* (ICML 2018); GLFC → kutip judul *Federated Class-Incremental Learning* (CVPR 2022).
3. ❌ **Buang dari naskah:** "Federated LwF", "LoRA-CL (Hu 2022)", "FTRL-FL", "Online FedAvg", "Dynamic Online FL", klaim "Jin 2-5 klien", klaim ">60% Hernandez-Ramos", angka "2-4 klien" Ruzafa-Alcazar (ganti: 4 klien), karakterisasi "10 klien pompa" (ganti sumber atau reformulasi).
4. ❌ **Argumen teknis poin 5 briefing salah:** "inactive timeout 120 detik" — CICFlowMeter memakai inaktivitas 5 s + total 120 s. Re-argumentasi (mis. fitur flow baru dihitung ulang saat flow ditutup timeout) atau hapus.
5. ⚠️ **Selesaikan konflasi Jin 2024** (Bagian 4.4) — dua kunci sitasi terpisah.
6. ✅ **Keputusan metode & klien tetap berlaku** (Bagian 2–3): FedCurv sebagai E4b opsional, FedProx sebagai alternatif; argumen cross-silo Kairouz + tabel klien terverifikasi (DioT 2–15, Izadi 20, FL-BCID 10, Ruzafa-Alcazar 4) sebagai jawaban "kenapa 2 klien".
7. ✅ Konflik DOI Hernandez-Ramos dinyatakan selesai — catatan individual kini cocok dengan Crosscheck (ACM CSUR, DOI 10.1145/3731596).
