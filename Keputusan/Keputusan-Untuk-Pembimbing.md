# Keputusan Metodologi untuk Pembimbing

**Last Updated:** 2026-10-06 18:30 UTC+7  
**Status:** **DISETUJUI PEMBIMBING - RESMI TERKUNCI (READY FOR PREPROCESSING DATASETS)**  
**Mahasiswa:** Rafli Alif Ihza Hartono (NRP 5022211233)  
**Departemen:** Teknik Elektro, FTEIC, Institut Teknologi Sepuluh Nopember (ITS)  

---

## 🟢 HASIL BRIEFING & KEPUTUSAN DOSEN PEMBIMBING (2026-10-06)

Berdasarkan sesi tatap muka bimbingan Tugas Akhir, 8 poin keputusan metodologis telah disepakati dan dibekukan secara resmi:

| No | Parameter / Aspek | Pilihan yang Disetujui | Justifikasi & Arahan Dosen Pembimbing |
|:---:|:---|:---|:---|
| **1** | **Injeksi Trafik** | ❌ **TIDAK DIPERLUKAN (Dieliminasi)** | Injeksi trafik riil (VM 400 Hydra/Slowloris) melibatkan terlalu banyak parameter dinamis non-algoritmik (dropped packets, buffer overrun, jitter jaringan) yang mengaburkan fokus analisis FL-CL. |
| **2** | **Staging Testbed** | 💻 **Local First $\to$ Simulasi Server** | Realisasi dan pembuktian arsitektur testbed dieksekusi di workstation/laptop lokal terlebih dahulu (Docker Compose / isolated venv). Setelah pipeline terbukti konvergen dan stabil, baru dideploy ke simulasi server Proxmox VE. |
| **3** | **Keseimbangan Bobot** | ⚖️ **Metode & Parameter Seimbang** | Pembobotan penalti EWC ($\lambda$) harus seimbang dengan loss tugas ($\mathcal{L}_{\text{task}}$), serta pembobotan kelas minoritas pada loss harus proporsional agar tidak terjadi gradient explosion atau plasticity freeze. |
| **4** | **Hyperparameter Tuning** | 🔍 **Tuning Sistematis Diwajibkan** | Wajib menyusun rentang pencarian hyperparameter (learning rate, batch size, EWC $\lambda$, communication rounds, local epochs) dengan validasi multi-seed untuk menjamin ketahanan model. |
| **5** | **Versi Dataset** | 📁 **Solely CIC-IDS2017 Bersih (Opsi A)** | Menggunakan secara eksklusif dataset resmi CIC-IDS2017 (Senin, Selasa, Rabu) dengan pembersihan 62 fitur unik, penghapusan 10 kolom konstan, 5 duplikat, dan penghapusan Destination Port. |
| **6** | **Partisi Data Normal** | 🔀 **Random Split 50/50 All Days (Opsi A)** | Data Normal dari Senin, Selasa, dan Rabu digabung lalu dibagi acak 50% untuk Task 1 dan 50% untuk Task 2 guna mengeliminasi bias pola harian (*day-pattern confound*). |
| **7** | **Komposisi Kelas DoS** | 🌊 **Keep As-Is (Opsi A)** | Mempertahankan distribusi alami 4 subvarian DoS (Hulk ~89%, GoldenEye ~5%, slowloris ~3%, Slowhttptest ~3%) yang digabung menjadi satu kelas "DoS" volumetrik realistis. |
| **8** | **Handling Imbalance** | ⚖️ **Weighted Loss / Keep All Data (Opsi C)** | Mempertahankan seluruh data bersih (~1,53 juta baris unik) tanpa pemangkasan data massal. Ketimpangan kelas diatasi menggunakan Weighted Cross-Entropy Loss dengan bobot invers frekuensi terkalibrasi. |
| **9** | **Parameter Komputasi vs QoS** | 📊 **Profiling Instance & Overhead FL (QoS Ditiadakan)** | QoS jaringan fisik (jitter, packet loss, bandwidth) ditiadakan. Diadopsi profiling instance (RAM footprint EWC vs Replay, CPU duration, latensi inferensi per flow dalam $\mu\text{s}$, dan communication overhead FL) mengacu pada standar skripsi Hafizh (2024). |

---

## 🎯 RINCIAN 4 KEPUTUSAN UTAMA METODOLOGI

### KEPUTUSAN 1: Versi Dataset (DISETUJUI: CIC-IDS2017 Bersih)

* **Keputusan Final:** **CIC-IDS2017 Original** (62 fitur numerik unik + 1 Label).
* **Fitur yang Dibuang:**
  1. **10 Kolom Konstan (Variansi = 0):** `Bwd PSH Flags`, `Fwd URG Flags`, `Bwd URG Flags`, `CWE Flag Count`, `Fwd Avg Bytes/Bulk`, `Fwd Avg Packets/Bulk`, `Fwd Avg Bulk Rate`, `Bwd Avg Bytes/Bulk`, `Bwd Avg Packets/Bulk`, `Bwd Avg Bulk Rate`.
  2. **5 Kolom Duplikat 100% Identik (Hash Match):** `Fwd Header Length.1`, `Subflow Fwd Bytes`, `Subflow Fwd Packets`, `Subflow Bwd Packets`, `SYN Flag Count`.
  3. **1 Kolom Shortcut Leakage:** `Destination Port` dibuang agar model tidak sekadar menghafal nomor port (port 22 vs port 80).
* **Justifikasi Eksklusif Berkas Senin, Selasa, dan Rabu (Eliminasi Kamis & Jumat):**
  - **Senin (Monday):** Menyediakan 529.918 flow **Normal murni** tanpa kontaminasi serangan sebagai baseline.
  - **Selasa (Tuesday):** Menyediakan kelas **SSH-Patator** (3.219 flow bersih) untuk **Task 1 (Client A)**.
  - **Rabu (Wednesday):** Menyediakan kelas **DoS** 4 varian lengkap (193.748 flow bersih) untuk **Task 2 (Client B)**.
  - **Kamis Dieliminasi:** Web Attacks & Infiltration mengalami **kelangkaan sampel ekstrem** (Sql Injection hanya 21 baris, Infiltration hanya 36 baris; tidak layak statistik) serta menderita **cacat desinkronisasi pelabelan pcap parah** (*Rosay et al., 2022*).
  - **Jumat Dieliminasi:** PortScan adalah reconnaissance pasif (bukan intrusi eksploitasi), Botnet ARES cacat fragmentasi alur (Dube et al., 2024), dan DDoS LOIC menimbulkan bias kerancuan (*confounding*) dengan DoS Rabu tanpa menambah sampel SSH/DoS baru.
* **Transparansi Akademik:** Kritik Rosay et al. (2022) dan Dube et al. (2024) dikutip secara transparan di Bab 3 skripsi sebagai konteks integritas riset.

---

### KEPUTUSAN 2: Pemilihan Data Normal untuk Task 1 dan Task 2 (DISETUJUI: Opsi A)

* **Keputusan Final:** **Random Split 50/50 dari Gabungan Normal Semua Hari (Senin, Selasa, Rabu)**.
* **Justifikasi Empiris:** Uji Decision Tree membuktikan klasifikasi Normal Selasa vs Normal Rabu menghasilkan akurasi **62,44% ± 0,34%** (di atas tebakan acak 50%), menandakan adanya variasi latar belakang antar-hari (*day-pattern confound*).
* **Tindakan:** Pembagian acak 50/50 meratakan variasi harian sehingga model fokus murni pada pola serangan intrusi, bukan menghafal hari rekaman.

---

### KEPUTUSAN 3: Komposisi Kelas Serangan DoS (DISETUJUI: Opsi A)

* **Keputusan Final:** **Keep As-Is (Distribusi Alami)**.
* **Distribusi DoS Bersih:**
  - DoS Hulk: 172.849 flow (89,2%)
  - DoS GoldenEye: 10.286 flow (5,3%)
  - DoS slowloris: 5.385 flow (2,8%)
  - DoS Slowhttptest: 5.228 flow (2,7%)
  - **Total DoS:** 193.748 flow.
* **Tindakan:** Seluruh 4 varian disatukan ke dalam satu kelas label `DoS`. Tidak dilakukan pemangkasan buatan ke subvarian terkecil (5.5K) agar karakteristik serangan volumetrik dunia nyata tetap terjaga.

---

### KEPUTUSAN 4: Penanganan Ketimpangan Kelas / Imbalance (DISETUJUI: Opsi C)

* **Keputusan Final:** **Weighted Loss (Keep All Clean Data)**.
* **Distribusi Kelas Bersih (Setelah Dedup 79 Kolom):**
  - Normal: 1.332.710 baris (87,1%)
  - DoS: 193.748 baris (12,7%)
  - SSH-Patator: 3.219 baris (0,2%)
  - **Total Data Bersih:** **1.529.677 baris unik**.
* **Formulasi Loss Berbobot (Weighted Cross-Entropy):**
  $$\mathcal{L}_{\text{CE}}(y, \hat{y}) = - \sum_{c=1}^{C} w_c \cdot y_c \log(\hat{y}_c)$$
  Di mana bobot kelas $w_c$ dikalkulasi berdasarkan frekuensi invers terstandarisasi:
  $$w_c = \frac{N}{|C| \times N_c}$$
* **Catatan Rekayasa:** Seluruh 1,53 juta data dipertahankan untuk pelatihan dan evaluasi utama skripsi. Untuk kebutuhan iterasi cepat saat pengembangan kode (*development/debugging profile*), disiapkan sub-profil mini-batch 5.000 sampel per kelas.

---

## 🛡️ VALIDASI TAMBAHAN TERKAIT SCOPED (Penajaman Skripsi)

Sesuai arahan pembimbing terkait keseimbangan metode, parameter, dan kehati-hatian eksperimen, validasi teknis berikut dibekukan:

### 1. Validasi Keseimbangan Bobot EWC vs. Task Loss ($\lambda$ Balancing)
* **Persamaan Total Loss Continual:**
  $$\mathcal{L}_{\text{total}}(\theta) = \mathcal{L}_{\text{task2}}(\theta) + \frac{\lambda}{2} \sum_{i=1}^{P} F_i (\theta_i - \theta^*_{1,i})^2$$
* **Risiko Ketidakseimbangan:**
  - Jika $\lambda$ terlalu rendah: Terjadi *Catastrophic Forgetting* (Recall SSH jatuh drastis mendekati 0%).
  - Jika $\lambda$ terlalu tinggi: Terjadi *Plasticity Freeze / Intransigence* (Model menolak mempelajari DoS, akurasi Task 2 gagal konvergen).
* **Solusi Validasi:** Menjalankan sweep parameter $\lambda$ pada grid logaritmik: $\lambda \in \{10^1, 10^2, 10^3, 10^4, 10^5\}$ untuk menemukan nilai kesetimbangan optimal antara stabilitas dan plastisitas.

### 2. Validasi Stabilitas Gradien (Gradient Clipping)
* Karena rasio Normal terhadap SSH-Patator mencapai ~414 : 1, penalti gradien kelas minoritas sangat tinggi.
* **Aturan Baku:** Seluruh loop pelatihan PyTorch wajib menyertakan **Gradient Clipping**:
  ```python
  torch.nn.utils.clip_grad_norm_(model.parameters(), max_norm=1.0)
  ```
  Ini mencegah lonjakan bobot ekstrem (*gradient explosion*) saat batch kebetulan memuat sampel SSH-Patator.

### 3. Validasi Anti-Data Leakage pada Normalisasi Fitur
* Pemetaan skala fitur menggunakan `StandardScaler` (Z-score normalization: $\mu=0, \sigma=1$).
* **Aturan Baku:** `StandardScaler.fit()` **HANYA** dieksekusi pada data latih (*training split*). Data uji (*test split*) hanya ditransformasikan menggunakan parameter rata-rata dan deviasi standar yang diperoleh dari data latih:
  $$\text{Train:} \quad X_{\text{train\_scaled}} = \frac{X_{\text{train}} - \mu_{\text{train}}}{\sigma_{\text{train}}}$$
  $$\text{Test:} \quad X_{\text{test\_scaled}} = \frac{X_{\text{test}} - \mu_{\text{train}}}{\sigma_{\text{train}}}$$
  Tidak boleh ada bocoran informasi distribusi data uji ke model.

### 4. Validasi Efisiensi Memori Komputasi Matriks Fisher
* Matriks Informasi Fisher diagonal dihitung melalui ekspektasi kuadrat gradien log-likelihood:
  $$F_i = \frac{1}{N_{\text{fisher}}} \sum_{n=1}^{N_{\text{fisher}}} \left( \frac{\partial \log p(y_n \mid x_n, \theta^*)}{\partial \theta_i} \right)^2$$
* Untuk mencegah kehabisan memori RAM (*Out-Of-Memory* / OOM), perhitungan Fisher dilakukan secara akumulatif streaming menggunakan subsampel representatif terstratifikasi ($N_{\text{fisher}} = 1.000$ flow per kelas) segera setelah Task 1 selesai dilatih.

### 5. Protokol Staging Arsitektur Testbed (Local First $\to$ Server Simulation)
* **Fase 1 (Local Realization):** Seluruh modul algoritma (preprocessing, training loop PyTorch, perhitungan Fisher, klien Flower, strategi agregasi FedAvg) diuji dan diverifikasi secara lokal di laptop (lingkungan Python virtual/Docker lokal).
* **Fase 2 (Server Simulation):** Setelah kode lokal lolos uji unit dan menghasilkan metrik valid pada 5 seed, konfigurasi dideploy ke lingkungan virtual Proxmox VE (Server agregator, VM Client A, VM Client B) untuk pelaporan infrastruktur.

---

### KEPUTUSAN 5 (Tambahan): Parameter Evaluasi Komputasi & Batasan Parameter Jaringan (Mengacu pada Skripsi Hafizh, 2024)

Mengacu pada skripsi [Referensi-Skripsi-Hafizh.pdf](../Proposal/Referensi-Skripsi-Hafizh.pdf) (Hafizh, 2024, Pembimbing: Dr.Ir. Achmad Affandi, DEA) dan arahan pembimbing:
1. **Parameter QoS Jaringan Mentah Ditiadakan (Out of Scope):**  
   - Metrik fisik seperti bandwidth link, throughput, delay, jitter, dan packet loss resmi ditiadakan sejalan dengan eliminasi injeksi trafik langsung.  
   - *Pengganti Relevan untuk FL:* **Communication Overhead FL** (ukuran payload bobot parameter model dalam KB/MB per round agregasi: $2 \times \text{Size}(\theta) \times R$).
2. **Evaluasi Resource Instance Komputasi Diadopsi:**  
   - **Memory Footprint (RAM EWC vs Replay Buffer):** Membuktikan efisiensi EWC yang hanya menyimpan bobot optimal $\theta^*$ dan Fisher diagonal $F_i$ ($\approx$ puluhan KB) dibanding Experience Replay yang membebani RAM/disk dengan ribuan data flow mentah.  
   - **CPU Training Duration per Round:** Mengukur overhead durasi perhitungan penalti EWC per *local epoch*.  
   - **Model Storage Size (.pt & .onnx):** Mengukur ukuran file model siap pakai di edge.
3. **Inference Latency per Flow ($\mu\text{s}$):**  
   - Mengadopsi pengukuran latensi komputasi inferensi seperti pada Hafizh (2024, Hal. 102) yang menghasilkan 10,07 $\mu\text{s}$/flow. Model MLP kita diuji waktu inferensinya per flow untuk membuktikan kesiapan *near real-time detection*.
4. **Hyperparameter Tuning Sistematis (Optuna / 5 Seeds):**  
   - Melakukan tuning sistematis (Bayesian/Grid) untuk bobot penalti $\lambda$ EWC, *learning rate* $\eta$, dan jumlah *local epochs* $E$ melintasi 5 random seed (42 s.d. 46).
5. **Confusion Matrix Komparatif Sebelum vs Sesudah Task 2:**  
   - Menampilkan visualisasi matriks prediksi untuk membuktikan secara empiris bahwa kelas SSH (Task 1) tidak tertimpa/terlupakan setelah model mempelajari serangan DoS (Task 2).

---

## 📋 DAFTAR KELENGKAPAN (CHECKLIST PREPROCESSING DATASET)

Dengan disetujuinya seluruh poin di atas, modul praproses data (`scripts/preprocess_cicids2017.py`) siap dieksekusi dengan spesifikasi keluaran terstandarisasi:

- [x] Sumber input mentah: Berkas CSV resmi UNB (Monday, Tuesday, Wednesday).
- [x] Eliminasi 10 kolom konstan + 5 kolom identik + 1 kolom `Destination Port`.
- [x] Deduplikasi 132.909 baris identik $\to$ tersisa 1.529.677 baris bersih.
- [x] Imputasi nilai `Inf` $\to$ kuantil maksimum / 1e9, dan `NaN` $\to$ 0.
- [x] Partisi Normal 50/50 all-days untuk Task 1 dan Task 2.
- [x] Partisi 2 Client Non-IID:
  - **Client A (Task 1):** 50% Normal + 100% SSH-Patator.
  - **Client B (Task 2):** 50% Normal + 100% DoS (4 subvarian alami).
- [x] Stratified Split: 70% Train, 15% Validation, 15% Test (dikunci dengan seed 42).
- [x] Fitting `StandardScaler` murni pada subset data latih.
- [x] Penyimpanan artefak terkompresi Parquet untuk performa I/O maksimal.

---

## 🚀 STATUS AKHIR: READY FOR PREPROCESSING DATASETS

```
================================================================================
                    STATUS AKHIR: DISETUJUI OLEH PEMBIMBING
            PIPELINE PREPROCESSING CIC-IDS2017 RESMI DINYATAKAN SIAP
================================================================================
```
