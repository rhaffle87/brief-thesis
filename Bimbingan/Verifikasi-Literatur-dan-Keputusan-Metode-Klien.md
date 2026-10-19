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
| 10 | SCAFFOLD, FedNova, Online EWC, SI, MAS, LwF, PackNet, LoRA-CL, A-GEM, Experience Replay | Berbagai | Nama & tahun sesuai pengetahuan umum bidang, **belum dijalankan verifikasi DOI satu-satu** (dihentikan karena akan sangat panjang) | ⏸️ Verifikasi penuh belum dilakukan — lakukan sebelum sidang jika nama-nama ini dikutip eksplisit di naskah |

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
| Relevansi ke temuan sendiri | **Bisa langsung menguji hipotesis "EWC Dilution Effect"** (poin 8, briefing sebelumnya): apakah berbagi Fisher ke server memperbaiki atau memperburuk pengenceran gradien akibat ketimpangan data Client A (~670K) vs Client B (~860K) | Tidak menjawab hipotesis spesifik ini |

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

## 4. Ringkasan Tindak Lanjut

1. ✅ Pakai FedWeIT, GLFC, FedCurv, Ditto sebagai rujukan taksonomi Bab 2 — aman, sudah terverifikasi.
2. ⚠️ Koreksi venue TARGET ke ICCV 2023.
3. ⚠️ Pisahkan atribusi pFedMe (Dinh et al.) dan Per-FedAvg (Fallah et al.) jika keduanya disebut.
4. ❌ Buang klaim "Jin et al. 2-5 klien" — terbukti fabrikasi dari catatan literatur sendiri.
5. ⚠️ Verifikasi ulang klaim statistik Hernandez-Ramos dan jumlah klien Ruzafa-Alcázar sebelum dikutip sebagai angka pasti.
6. ⚠️ Selesaikan konflik DOI Hernandez-Ramos antara `Daftar-Pustaka.md`/`Crosscheck.md` vs catatan individual.
7. ✅ Usulkan E4b (FedAvg + FedCurv) sebagai eksperimen opsional ke dosen.
8. ✅ Pakai argumen cross-silo (Kairouz et al. 2021) + tabel perbandingan jumlah klien studi sejenis sebagai jawaban utama atas pertanyaan "kenapa cuma 2 klien".
