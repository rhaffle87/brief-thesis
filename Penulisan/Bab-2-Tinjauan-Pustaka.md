# BAB 2 TINJAUAN PUSTAKA

## 2.1 Keamanan Jaringan dan Sistem Deteksi Intrusi (NIDS)

Keamanan jaringan komputer merupakan pilar utama dalam menjaga kelangsungan operasional sistem komputasi modern. Prinsip dasar keamanan informasi berakar pada model triad **Confidentiality, Integrity, and Availability (CIA Triad)**:
1. **Confidentiality (Kerahasiaan):** Menjamin bahwa data transmisi dan konfigurasi sistem hanya dapat diakses oleh entitas yang memiliki otoritas sah.
2. **Integrity (Integritas):** Memastikan bahwa paket data dan aliran komunikasi tidak mengalami modifikasi, pemalsuan (*tampering*), atau penyisipan tanpa izin selama transit.
3. **Availability (Ketersediaan):** Menjamin bahwa sumber daya jaringan, layanan komputasi, dan kanal komunikasi tetap dapat diakses oleh pengguna yang berhak setiap saat dibutuhkan.

Untuk menegakkan prinsip CIA Triad, infrastruktur jaringan menerapkan mekanisme pertahanan berlapis (*defense-in-depth*). Salah satu komponen pertahanan aktif yang paling krusial adalah **Network Intrusion Detection System (NIDS)**. NIDS ditempatkan secara strategis pada segmen perimeter jaringan atau *gateway* sakelar (*switch*) untuk memantau, menganalisis, dan menginspeksi aliran data lalu lintas secara kontinu. NIDS beroperasi secara pasif melalui penyadapan paket (*port mirroring* atau TAP) sehingga proses deteksi tidak mengganggu transmisi data produksi.

Secara taksonomi, NIDS diklasifikasikan ke dalam dua paradigma operasional utama:
- **Signature-Based Intrusion Detection System (SIDS):** Bekerja dengan mencocokkan muatan paket atau pola aliran data terhadap basis data aturan (*signature database*) yang telah diketahui sebelumnya (misalnya aturan Snort atau Suricata). SIDS memiliki akurasi sangat tinggi terhadap serangan yang telah terdaftar dengan tingkat alarm palsu (*false positive*) yang rendah. Namun, kelemahan fundamental SIDS adalah ketidakmampuannya mendeteksi serangan baru (*zero-day attacks*) atau varian serangan yang mengalami polimorfisme kode.
- **Anomaly-Based Intrusion Detection System (ABDS):** Bekerja dengan memodelkan perilaku normal lalu lintas jaringan (*baseline profile*), kemudian mengidentifikasi deviasi signifikan dari pola normal tersebut sebagai indikasi potensi intrusi. Pendekatan ABDS modern memanfaatkan teknik *Machine Learning* (ML) dan *Deep Learning* (DL) yang dilatih menggunakan data statistik aliran bidirectional (*bidirectional network flows*). Keunggulan utama ABDS adalah kemampuan generalisasinya dalam mengenali varian serangan yang belum pernah dilihat sebelumnya.

---

## 2.2 Karakteristik Serangan Siber

Penelitian ini memfokuskan investigasi pada tiga kelas representatif lalu lintas jaringan yang memodelkan interaksi antara aktivitas normal dan ancaman intrusi kritis di lingkungan enterprise:

### 2.2.1 Trafik Normal (BENIGN)
Trafik normal merepresentasikan aktivitas komunikasi sah pengguna dan layanan jaringan, mencakup protokol penelusuran web (HTTP/HTTPS), pertukaran surat elektronik (SMTP/IMAP), kueri domain (*Domain Name System* / DNS), resolusi alamat (ARP), dan transfer berkas rutin. Karakteristik statistik dari trafik normal ditandai oleh distribusi panjang paket (*packet length*) yang proporsional, durasi koneksi (*flow duration*) yang variatif, serta interval waktu kedatangan antar-paket (*inter-arrival time* / IAT) yang mengikuti dinamika interaksi manusia dan transfer data acak.

### 2.2.2 Serangan Brute-Force SSH (SSH-Patator)
Protokol *Secure Shell* (SSH) yang beroperasi pada port standar 22 merupakan protokol utama untuk administrasi jarak jauh (*remote server management*). Serangan **SSH-Patator** merupakan serangan berbasis perangkat lunak audit penetrasi multi-utas (*multi-threaded tool*) yang melancarkan tebakan kombinasi nama pengguna (*username*) dan kata sandi (*password*) secara berulang (*dictionary attack* atau *brute force*).  
Secara karakteristik statistik alur (*flow statistics*), serangan SSH-Patator ditandai oleh:
- Volume aliran koneksi TCP yang tinggi dalam interval waktu singkat menuju satu server target.
- Durasi aliran yang sangat pendek (*short flow duration*) karena koneksi langsung dihentikan melalui flag RST atau FIN segera setelah proses *handshake* autentikasi ditolak oleh server.
- Pola ukuran paket yang seragam pada tahap pertukaran enkripsi kunci awal dan kegagalan sesi.

### 2.2.3 Serangan Penolakan Layanan (Denial of Service / DoS)
Serangan **Denial of Service (DoS)** bertujuan untuk melumpuhkan ketersediaan (*availability*) server korban dengan membanjiri sumber daya komputasi (CPU, memori, atau koneksi soket jaringan) sehingga layanan tidak dapat diakses oleh pengguna yang sah. Penelitian ini mempertahankan komposisi alami dari empat subvarian serangan DoS lapisan aplikasi (*application-layer DoS*) yang ada pada CIC-IDS2017:
1. **DoS Hulk:** Serangan pembanjiran permintaan HTTP GET bervolume masif yang memanipulasi *header user-agent* acak untuk melewati sistem *caching* server web dan memaksa alokasi memori berulang pada server target.
2. **DoS GoldenEye:** Serangan penolakan layanan HTTP yang memanfaatkan kombinasi *keep-alive* berkepanjangan dan manipulasi *cache-control* untuk mempertahankan soket koneksi terbuka secara masif hingga kapasitas *pool worker* server web habis (*exhaustion*).
3. **DoS slowloris:** Serangan tingkat rendah berkecepatan lambat (*low-and-slow attack*) yang mengirimkan fragmen *header* HTTP secara tidak lengkap dengan jeda berkala, menahan soket koneksi tetap terbuka selama mungkin tanpa memicu alarm deteksi berbasis batas ambang volume (*threshold*).
4. **DoS Slowhttptest:** Serangan yang mengeksploitasi mekanisme penanganan permintaan HTTP yang lambat (melalui pengiriman *body* HTTP POST secara sangat lambat) untuk menghabiskan sumber daya *buffer* antrean koneksi server web.

---

## 2.3 Dataset Deteksi Intrusi dan Isu Kritis CIC-IDS2017

Dataset **CIC-IDS2017** yang dikembangkan oleh Canadian Institute for Cybersecurity (Sharafaldin et al., 2018) merupakan salah satu dataset tolok ukur (*benchmark dataset*) paling populer di dunia dalam riset sistem deteksi intrusi jaringan berbasis pembelajaran mesin. Dataset ini dibangun di atas arsitektur jaringan *testbed* nyata yang memisahkan antara *Victim Network* (jaringan korban yang mencakup server web, server manajemen, dan workstation pengguna) dan *Attack Network* (jaringan penyerang eksternal) dengan perekaman lalu lintas data penuh (*full packet capture* / pcap) selama lima hari kerja berturut-turut (Senin s.d. Jumat).

### 2.3.1 Isu Kritis dan Cacat Data Berdasarkan Literatur Audit
Meskipun digunakan secara luas dalam ribuan publikasi, audit komprehensif mutakhir mengungkap sejumlah anomali dan cacat pelabelan serius pada CIC-IDS2017 yang wajib dimitigasi secara metodologis:
1. **Desinkronisasi Pelabelan Hari Kamis (Rosay et al., 2022):** Rosay et al. (2022) membuktikan bahwa berkas pcap hari Kamis menderita desinkronisasi waktu (*timestamp offset*) parah antara log waktu penyerangan aktual dan jam sistem perekaman. Akibatnya, ribuan aliran data normal salah dilabeli sebagai serangan web (*Web Attacks*), dan sebaliknya.
2. **Kelangkaan Sampel Ekstrem Kelas Hari Kamis (Dube et al., 2024):** Berkas hari Kamis memuat jumlah sampel serangan yang sangat tidak memadai untuk daya statistik (*statistical power*): *Sql Injection* hanya memuat 21 baris dan *Infiltration* hanya memuat 36 baris. Volume sekecil ini tidak valid untuk dipartisi ke dalam pelatihan terdistribusi multi-klien dan pembagian *train/val/test*.
3. **Redundansi Aliran dan Duplikasi Data:** Ditemukan 132.909 baris data (7,97%) yang identik 100% pada berkas mentah. Membiarkan duplikat ini akan mendistorsi pembagian data dan memicu *data leakage* antar-partisi.
4. **Fitur Konstan Berkelanjutan:** Sebanyak 10 kolom fitur numerik memiliki nilai $0$ absolut di seluruh baris data (variansi $\sigma^2 = 0$). Kolom konstan ini tidak menyumbangkan entropi informasi klasifikasi namun membebani komputasi matriks bobot dan inversi matriks Fisher.
5. **Kolom Duplikat Identik via Hash:** Terdapat 5 pasang kolom yang memiliki nilai sama persis 100%, seperti `Fwd Header Length.1` terhadap `Fwd Header Length`, yang memicu multikolinearitas sempurna ($r = 1.0$).

### 2.3.2 Fenomena Port Leakage dan Shortcut Learning
Isu paling kritis pada CIC-IDS2017 diidentifikasi oleh Engelen et al. (2021), yaitu fenomena **Port Leakage** yang memicu **shortcut learning**. Pada dataset mentah, fitur `Destination Port` memuat nomor port tujuan protokol. Karena serangan SSH dilancarkan pada port standar 22 dan serangan DoS dilancarkan pada port standar 80, model pembelajaran mesin cenderung mengambil "jalan pintas" dengan menghafal nomor port:
$$\text{Prediksi} = \begin{cases} \text{SSH-Patator}, & \text{jika } \text{Port} = 22 \\ \text{DoS}, & \text{jika } \text{Port} = 80 \\ \text{Normal}, & \text{lainnya} \end{cases}$$
Pengujian empiris membuktikan bahwa model *Decision Tree* yang hanya diberikan 1 fitur `Destination Port` mampu mencapai skor Macro-F1 sebesar **96,44%**. Penggunaan nomor port ini berbahaya karena tidak mencerminkan kecerdasan algoritma dalam menganalisis dinamika aliran paket. Jika penyerang memindahkan layanan SSH ke port non-standar (misal port 2222), sistem deteksi akan lumpuh total. Oleh karena itu, eliminasi fitur `Destination Port` secara sengaja adalah keputusan metodologis mutlak untuk memaksa model mengekstraksi pola statistik paket murni.

---

## 2.4 Penelitian Terdahulu (State-of-the-Art)

Perkembangan mutakhir sistem deteksi intrusi berbasis kolaborasi terdistribusi (*Federated Learning*) dan pembelajaran sekuensial adaptif (*Continual Learning*) dalam lima tahun terakhir dirangkum pada Tabel 2.1:

| Penulis & Tahun | Judul Penelitian | Metode / Pendekatan | Dataset | Temuan Kunci & Keterbatasan Teridentifikasi |
|---|---|---|---|---|
| **McMahan et al. (2017)** | *Communication-Efficient Learning of Deep Networks from Decentralized Data* | Federated Averaging (FedAvg) | MNIST, CIFAR-10 | Menjadi fondasi dasar FL terdistribusi; membuktikan efisiensi komunikasi agregasi bobot lokal, namun belum menguji dinamika forgetting sekuensial. |
| **Kirkpatrick et al. (2017)** | *Overcoming catastrophic forgetting in neural networks* | Elastic Weight Consolidation (EWC) | MNIST Permutasi, Atari 2600 | Memperkenalkan penalti kuadratik berbasis Matriks Informasi Fisher untuk memitigasi forgetting tanpa buffer sampel mentah. |
| **Zhao et al. (2018)** | *Federated Learning with Non-IID Data* | FedAvg Non-IID Analysis | CIFAR-10 | Membuktikan teorema *Weight Divergence* akibat non-IID data distribution yang diukur via Earth Mover's Distance (EMD). |
| **Van de Ven & Tolias (2019)** | *Three Scenarios for Continual Learning* | Taksonomi CL Scenarios | Split MNIST | Mengklasifikasikan 3 skenario CL: Task-IL, Domain-IL, dan Class-IL; menegaskan bahwa Class-IL adalah skenario tersulit dan paling realistis. |
| **Engelen et al. (2021)** | *Troubleshooting an Intrusion Detection Dataset: The CICIDS2017 Case Study* | Forensik Dataset IDS | CIC-IDS2017 | Membuktikan secara empiris anomali pelabelan dan kebocoran fitur *Destination Port* yang memicu *shortcut learning*. |
| **De Lange et al. (2021)** | *A Continual Learning Survey: Defying Forgetting in Classification Tasks* | Taksonomi CL Komparatif | Berbagai Vision Benchmark | Mengklasifikasikan metode CL ke dalam regulasi parameter, replay buffer, dan alokasi arsitektur modular. |
| **Rosay et al. (2022)** | *A Systematic Analysis of the CIC-IDS2017 Dataset* | Kurasi Dataset IDS | CIC-IDS2017 | Mengidentifikasi 34 anomali data pada CIC-IDS2017 termasuk desinkronisasi jam pcap hari Kamis dan duplikasi aliran. |
| **Jin et al. (2024)** | *FL-IIDS: A novel federated learning-based incremental intrusion detection system* | FL + Replay Inkremental | UNSW-NB15 | Menggabungkan FL dan deteksi inkremental, namun mengasumsikan distribusi data antar-klien bersifat IID dan memerlukan buffer rekonstruksi sampel. |
| **Dube et al. (2024)** | *Faulty use of the CIC-IDS 2017 dataset in information security research* | Audit Metodologi NIDS | CIC-IDS2017 | Mengkritik publikasi NIDS yang mengabaikan pembersihan data dan duplikasi flow; merekomendasikan pelaporan transparan. |
| **Buyuktanir et al. (2025)** | *Federated learning in intrusion detection: advancements, applications, and future directions* | Survei Komprehensif FL-IDS | Berbagai Dataset IDS | Menyoroti tantangan *label skew* non-IID dan pergeseran ancaman jaringan baru sebagai celah riset utama FL-IDS. |
| **Hernandez-Ramos et al. (2025)** | *Intrusion Detection Based on Federated Learning: A Systematic Review* | Systematic Literature Review | Multi-Dataset | Menganalisis lebih dari 150 arsitektur FL-IDS; menyimpulkan perlunya integrasi mekanisme adaptasi memori jangka panjang. |
| **Hamedi et al. (2025)** | *Federated Continual Learning: Concepts, Challenges, and Solutions* | Survei Teori FCL | Teoretis FCL | Merumuskan konsep *Dual Forgetting* (lupa lokal pada klien vs lupa global saat agregasi server) pada arsitektur FCL. |
| **Rehman et al. (2026)** | *Incremental Federated Learning for Intrusion Detection Systems* | FL + EWC vs GEM | CIC-IDS2017 | Menguji komparasi EWC dan GEM pada FL-IDS; menegaskan keunggulan efisiensi komputasi EWC tanpa pelanggaran buffer privasi. |
| **Liu & Chang (2026)** | *Elastic Weight Consolidation Done Right for Continual Learning* | EWC-DR Fisher Optimization | CL Benchmark | Menganalisis estimasi kestabilan kalkulasi Matriks Fisher empiris pada skenario sekuensial. |

---

## 2.5 Federated Learning dan Algoritma Federated Averaging (FedAvg)

### 2.5.1 Arsitektur Terdistribusi Federated Learning
Federated Learning (FL) adalah paradigma pembelajaran mesin terdistribusi yang memungkinkan sejumlah $K$ node klien lokal secara kolaboratif melatih sebuah model global bersama di bawah orkestrasi server pusat tanpa perlu membagikan data pelatihan mentah ($\mathcal{D}_k$).

Secara formal, tujuan optimasi dari Federated Learning adalah meminimalkan fungsi objektif global:
$$\min_{w} f(w) = \sum_{k=1}^{K} \frac{n_k}{n} F_k(w)$$
di mana:
- $w \in \mathbb{R}^d$ adalah vektor parameter bobot model global.
- $K$ adalah total jumlah klien yang berpartisipasi dalam federasi.
- $n_k = |\mathcal{D}_k|$ adalah jumlah sampel data lokal pada klien ke-$k$.
- $n = \sum_{k=1}^K n_k$ adalah total seluruh sampel data lintas klien.
- $F_k(w) = \frac{1}{n_k} \sum_{i \in \mathcal{D}_k} \ell(w; x_i, y_i)$ adalah fungsi kerugian (*local loss function*) pada klien ke-$k$.

### 2.5.2 Mekanisme Siklus Algoritma FedAvg
Algoritma **Federated Averaging (FedAvg)** (McMahan et al., 2017) menyelesaikan optimasi terdistribusi melalui putaran komunikasi (*communication rounds*) $t = 1, 2, \dots, T$:
1. **Server Broadcast:** Server menginisialisasi parameter bobot global $w_t$ dan mengirimkannya kepada seluruh klien yang aktif.
2. **Local Client Training:** Setiap klien $k$ menginisialisasi model lokalnya $w_t^k = w_t$, kemudian menjalankan algoritma optimasi gradien (*Stochastic Gradient Descent* / SGD atau Adam) selama $E$ *local epochs* menggunakan ukuran *mini-batch* $B$ dan laju pembelajaran $\eta$:
   $$w_{t+1}^k \leftarrow w_t^k - \eta \nabla F_k(w_t^k)$$
3. **Weight Aggregation:** Klien mengirimkan parameter bobot lokal yang telah diperbarui $w_{t+1}^k$ kembali ke server. Server melakukan agregasi bobot rata-rata terbobot (*weighted average*) proporsional terhadap ukuran data klien:
   $$w_{t+1} = \sum_{k=1}^{K} \frac{n_k}{n} w_{t+1}^k$$

### 2.5.3 Tantangan Heterogenitas Data Non-IID dan Divergensi Bobot
Pada skenario ideal di mana data terdistribusi secara independen dan identik (IID), gradien lokal $\nabla F_k(w)$ merupakan estimasi yang tidak bias (*unbiased estimate*) dari gradien global $\nabla f(w)$. Namun, pada skenario non-IID (*label skew*), gradien lokal antar-klien saling bertolak belakang menuju titik optimum lokal masing-masing yang berjauhan:
$$\mathbb{E}[\nabla F_k(w)] \neq \nabla f(w)$$
Zhao et al. (2018) membuktikan bahwa heterogenitas non-IID memicu **Weight Divergence**:
$$\|w_{\text{FedAvg}} - w_{\text{Centralized}}\| > 0$$
Tingkat divergensi bobot ini berbanding lurus dengan jarak distribusi probabilitas data lokal terhadap distribusi populasi global yang diukur melalui *Earth Mover's Distance* (EMD). Semakin besar nilai *local epoch* ($E$) sebelum agregasi, semakin parah pergeseran bobot model, yang dapat memicu osilasi atau penurunan akurasi pada model global.

---

## 2.6 Continual Learning dan Fenomena Catastrophic Forgetting

### 2.6.1 Dilema Stabilitas-Plastisitas
Pembelajaran mesin konvensional beroperasi di bawah asumsi data stasioner (*stationary distribution*), di mana model dilatih satu kali pada seluruh data yang tersedia. Sebaliknya, **Continual Learning (CL)** atau *Lifelong Learning* menuntut model saraf tiruan untuk dapat mempelajari aliran tugas baru secara berkelanjutan ($\mathcal{T}_1, \mathcal{T}_2, \dots, \mathcal{T}_M$) tanpa kehilangan performa pada tugas-tugas yang telah dipelajari sebelumnya.

Hal ini memunculkan tantangan fundamental yang dikenal sebagai **Dilema Stabilitas-Plastisitas (Stability-Plasticity Dilemma)**:
- **Plastisitas (Plasticity):** Kemampuan model untuk mengintegrasikan dan mempelajari representasi pengetahuan baru secara efektif.
- **Stabilitas (Stability):** Kemampuan model untuk mempertahankan representasi bobot yang telah dipelajari sebelumnya agar tidak terhapus.

Ketika jaringan saraf tiruan standar dilatih secara naif (*naive fine-tuning*) pada tugas baru $\mathcal{T}_2$, pembaruan gradien akan menimpa bobot parameter yang sebelumnya krusial untuk tugas $\mathcal{T}_1$, memicu terjadinya **catastrophic forgetting**.

### 2.6.2 Taksonomi Tiga Skenario Continual Learning
Van de Ven & Tolias (2019) mengklasifikasikan pengujian continual learning ke dalam tiga skenario formal:
1. **Task-Incremental Learning (Task-IL):** Model diberikan informasi identitas tugas (*Task-ID*) saat inferensi. Model dapat menggunakan kepala keluaran (*output head*) terpisah untuk setiap tugas. Ini merupakan skenario paling sederhana.
2. **Domain-Incremental Learning (Domain-IL):** Struktur tugas dan kelas keluaran tetap sama, namun distribusi fitur masukan mengalami pergeseran domain. Task-ID tidak diberikan saat inferensi.
3. **Class-Incremental Learning (Class-IL):** Model harus mampu mendiskriminasikan seluruh kelas dari seluruh tugas yang telah dipelajari menggunakan satu kepala keluaran bersama (*shared single output head*) tanpa pernah diberikan Task-ID saat inferensi.

Penelitian deteksi intrusi ini mengadopsi skenario **Class-Incremental Learning (Class-IL)**. Pada saat sensor NIDS beroperasi di jaringan nyata, sistem tidak pernah mengetahui sebelumnya apakah paket yang masuk berasal dari Task 1 atau Task 2; sistem harus secara mandiri mengklasifikasikan apakah paket tersebut adalah Normal, SSH-Patator, atau DoS.

---

## 2.7 Elastic Weight Consolidation (EWC)

### 2.7.1 Formulasi Matematis Regularisasi EWC
Metode **Elastic Weight Consolidation (EWC)** (Kirkpatrick et al., 2017) menyelesaikan masalah *catastrophic forgetting* dari perspektif probabilitas Bayesian. Berdasarkan teorema Bayes, distribusi posterior parameter $\theta$ setelah mengamati data tugas kedua $\mathcal{D}_2$ yang melanjutkan tugas pertama $\mathcal{D}_1$ dirumuskan sebagai:
$$\log p(\theta \mid \mathcal{D}_1, \mathcal{D}_2) = \log p(\mathcal{D}_2 \mid \theta) + \log p(\theta \mid \mathcal{D}_1) - \log p(\mathcal{D}_2)$$
Distribusi posterior tugas pertama, $\log p(\theta \mid \mathcal{D}_1)$, memuat seluruh informasi mengenai parameter mana yang paling penting untuk tugas $\mathcal{D}_1$. Karena distribusi posterior eksak sulit dihitung secara analitis (*intractable*), EWC mengaproksimasinya menggunakan distribusi Gaussian yang berpusat pada parameter optimal tugas pertama $\theta_1^*$, dengan presisi yang diukur melalui **Matriks Informasi Fisher (Fisher Information Matrix)** $F$:

Fungsi kerugian optimasi EWC saat melatih tugas baru $\mathcal{D}_2$ didefinisikan sebagai:
$$\mathcal{L}_{\text{EWC}}(\theta) = \mathcal{L}_{\text{task2}}(\theta) + \sum_{i} \frac{\lambda}{2} F_{i} (\theta_i - \theta_{1, i}^*)^2$$
di mana:
- $\mathcal{L}_{\text{task2}}(\theta)$ adalah fungsi kerugian klasifikasi standar untuk data tugas kedua (*Weighted Cross-Entropy Loss*).
- $\lambda$ adalah hiperparameter penyeimbang regularisasi yang menentukan seberapa ketat model mempertahankan memori tugas lama dibandingkan mempelajari tugas baru.
- $\theta_{1, i}^*$ adalah nilai parameter optimal ke-$i$ yang diperoleh setelah menyelesaikan pelatihan tugas pertama $\mathcal{D}_1$.
- $F_i$ adalah elemen diagonal ke-$i$ dari Matriks Informasi Fisher.

### 2.7.2 Matriks Informasi Fisher Diagonal
Matriks Informasi Fisher mengukur kelengkungan (*curvature*) dari fungsi log-likelihood di sekitar parameter optimal $\theta^*$. Nilai $F_i$ yang besar menandakan bahwa parameter $\theta_i$ sangat sensitif; sedikit perubahan pada nilai bobot tersebut akan menyebabkan lonjakan besar pada kerugian tugas pertama $\mathcal{D}_1$. Sebaliknya, jika $F_i$ bernilai kecil, parameter tersebut berada pada manifold fungsi yang datar (*flat direction*) sehingga bebas disesuaikan untuk mempelajari tugas kedua $\mathcal{D}_2$.

Secara empiris, elemen diagonal matriks Fisher dihitung melalui ekspektasi kuadrat gradien log-likelihood:
$$F_i = \frac{1}{N_{\text{fisher}}} \sum_{n=1}^{N_{\text{fisher}}} \left( \frac{\partial \log p(y_n \mid x_n, \theta_1^*)}{\partial \theta_i} \right)^2$$
Penelitian ini mengimplementasikan kalkulasi Fisher secara *streaming* pada sampel terstratifikasi ($N_{\text{fisher}} = 1.000$ per kelas) segera setelah penyelesaian Task 1, sehingga kebutuhan memori komputasi tetap sangat efisien dan terhindar dari *Out-Of-Memory* (OOM).

---

## 2.8 Model Klasifikasi Multilayer Perceptron (MLP)

Untuk memenuhi batasan komputasi perangkat sensor *edge* dan menghindari *overparameterization*, model pembelajaran mesin yang digunakan dirancang kompak berbasis arsitektur **Multilayer Perceptron (MLP)** dengan tiga lapis terhubung penuh (*Fully Connected Layers*):

$$\begin{aligned}
h_1 &= \text{ReLU}(W_1 x + b_1), \quad W_1 \in \mathbb{R}^{64 \times 63}, \ b_1 \in \mathbb{R}^{64} \\
h_2 &= \text{ReLU}(W_2 h_1 + b_2), \quad W_2 \in \mathbb{R}^{32 \times 64}, \ b_2 \in \mathbb{R}^{32} \\
z &= W_3 h_2 + b_3, \quad W_3 \in \mathbb{R}^{3 \times 32}, \ b_3 \in \mathbb{R}^{3} \\
\hat{y} &= \text{Softmax}(z)
\end{aligned}$$

Fungsi aktivasi *Rectified Linear Unit* (ReLU), $\text{ReLU}(v) = \max(0, v)$, digunakan pada lapisan tersembunyi karena komputasinya efisien dan mencegah *vanishing gradient*. Lapisan keluaran menghasilkan distribusi probabilitas terstandarisasi untuk 3 kelas klasifikasi (Normal, SSH-Patator, DoS). Total parameter model ini hanya berjumlah **6.275 parameter terbobot** ($\approx 25$ KB dalam format presisi *float32*), menjadikannya sangat ideal untuk pertukaran federasi yang hemat bandwidth.

---

## 2.9 Penanganan Imbalance Data: Weighted Cross-Entropy Loss

Distribusi kelas pada dataset jaringan nyata ditandai oleh ketimpangan kelas yang sangat ekstrem (*severe class imbalance*). Pada dataset penelitian ini, kelas Normal berjumlah 1.332.710 aliran, sedangkan kelas SSH-Patator hanya berjumlah 3.219 aliran (rasio ketimpangan mencapai $\approx 414 : 1$). Jika fungsi kerugian standar digunakan, gradien akan didominasi oleh kelas mayoritas, menyebabkan model mengabaikan kelas minoritas.

Penelitian ini menerapkan **Weighted Cross-Entropy Loss** yang memberikan pembobotan invers frekuensi terkalibrasi untuk setiap kelas $c \in \{0, 1, 2\}$:
$$w_c = \frac{N_{\text{total}}}{C \cdot N_c}$$
di mana $N_{\text{total}}$ adalah total aliran, $C = 3$ adalah jumlah kelas, dan $N_c$ adalah jumlah sampel kelas ke-$c$. Fungsi kerugian dirumuskan sebagai:
$$\mathcal{L}_{\text{task}}(y, \hat{y}) = - \sum_{c=1}^{C} w_c \cdot y_c \log(\hat{y}_c)$$
Untuk mencegah gradien kelas minoritas meledak (*gradient explosion*) saat dikalikan dengan bobot $w_c$ yang besar, teknik **Gradient Clipping** diterapkan pada seluruh optimasi lokal:
$$\text{if } \|\mathbf{g}\|_2 > \gamma, \quad \mathbf{g} \leftarrow \frac{\gamma}{\|\mathbf{g}\|_2} \mathbf{g}, \quad \text{dengan } \gamma = 1.0$$

---

## 2.10 Metrik Evaluasi Deteksi dan Profil Komputasi

### 2.10.1 Metrik Deteksi Pembelajaran Mesin
Kinerja klasifikasi dievaluasi menggunakan metrik berbasis *Confusion Matrix*:
- **Precision:** $P = \frac{TP}{TP + FP}$
- **Recall:** $R = \frac{TP}{TP + FN}$
- **F1-Score:** $F1 = 2 \cdot \frac{P \cdot R}{P + R}$
- **Macro-Averaged F1 (Macro-F1):** Memberikan bobot evaluasi yang setara pada setiap kelas tanpa memandang jumlah sampel:
  $$\text{Macro-F1} = \frac{1}{C} \sum_{c=1}^{C} F1_c$$

### 2.10.2 Metrik Continual Learning: Backward Transfer (BWT)
Metrik **Backward Transfer (BWT)** (Lopez-Paz & Ranzato, 2017) mengukur pengaruh pembelajaran tugas baru terhadap retensi performa tugas masa lalu:
$$\text{BWT} = R_{2, 1} - R_{1, 1}$$
di mana $R_{1, 1}$ adalah skor evaluasi (F1-Score) pada Task 1 (SSH-Patator) sesaat setelah Task 1 selesai dilatih, dan $R_{2, 1}$ adalah skor evaluasi pada Task 1 setelah model selesai mempelajari Task 2 (DoS).
- $\text{BWT} < 0$: Mengindikasikan terjadinya *catastrophic forgetting* (semakin negatif nilainya, semakin parah degradasi memori).
- $\text{BWT} = 0$: Memori tugas lama dipertahankan secara sempurna.
- $\text{BWT} > 0$: Terjadi transfer positif (*positive backward transfer*), di mana pembelajaran tugas baru justru meningkatkan performa tugas lama.

### 2.10.3 Metrik Profiling Komputasi dan Instance
Mengacu pada metodologi Hafizh (2024, Hal. 102), efisiensi komputasi dievaluasi menggunakan:
1. **Inference Latency per Flow ($\mu\text{s}$):** Rata-rata waktu eksekusi komputasi yang dibutuhkan model untuk memprediksi satu sampel aliran data.
2. **Memory Footprint (Alokasi RAM):** Pengukuran konsumsi memori fisik antara metode EWC (vektor Fisher $\approx 25$ KB) terhadap metode *Experience Replay* (buffer sampel $\approx$ puluhan MB).
3. **Communication Overhead FL:** Ukuran payload pertukaran bobot parameter model antar-klien dan server per putaran federasi:
   $$\text{Overhead} = 2 \times \text{Size}(w) \times R \text{ (dalam KB)}$$

---

## 2.11 Optimasi Hyperparameter Menggunakan Optuna

Mengacu pada arahan dosen pembimbing dan metodologi Hafizh (2024, Hal. 80), optimasi *hyperparameter* dilakukan secara sistematis menggunakan kerangka kerja **Optuna** berbasis algoritma *Tree-structured Parzen Estimator* (TPE) Bayesian Optimization. Ruang pencarian (*search space*) mencakup:
- Bobot penalti EWC: $\lambda \in [10^2, 10^6]$
- Laju pembelajaran lokal: $\eta \in [10^{-4}, 10^{-2}]$
- Jumlah *local epoch* per round federasi: $E \in [1, 5]$
- Ukuran *mini-batch*: $B \in [64, 256]$

Konfigurasi parameter terbaik dipilih berdasarkan skor Macro-F1 tertinggi pada *validation set* dan dikunci melintasi lima *random seed* (42 s.d. 46) untuk menjamin signifikansi statistik temuan.
