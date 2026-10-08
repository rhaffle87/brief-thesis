# BAB 1 PENDAHULUAN

## 1.1 Latar Belakang

Perkembangan teknologi informasi dan transformasi digital yang kian pesat telah meningkatkan ketergantungan infrastruktur enterprise, institusi publik, dan layanan perbankan terhadap integritas jaringan komputer. Namun, eskalasi keterhubungan ini diiringi oleh lonjakan volume dan kompleksitas ancaman siber (*cyber threats*). Menurut laporan global *Check Point Research* [1], terjadi peningkatan rata-rata serangan siber mingguan sebesar 47% per organisasi di seluruh dunia, dengan sektor telekomunikasi, pendidikan, dan infrastruktur kritikal menjadi sasaran eksploitasi utama. Selain itu, laporan *FBI Internet Crime Complaint Center* (IC3) [2] mencatat total kerugian ekonomi global akibat kejahatan siber telah melampaui triliunan dolar, di mana vektor serangan intrusi jaringan seperti eksploitasi brute-force autentikasi (SSH) dan serangan penolakan layanan (*Denial of Service* / DoS) tetap mendominasi spektrum insiden keamanan operasional.

Dalam menjaga integritas, kerahasiaan (*confidentiality*), dan ketersediaan (*availability*) aset jaringan, *Network Intrusion Detection System* (NIDS) bertindak sebagai garda pertahanan utama untuk memantau, mendeteksi, dan mengklasifikasikan anomali lalu lintas data secara *near real-time*. Pendekatan NIDS konvensional berbasis *signature* (*Signature-Based Intrusion Detection System* / SIDS) hanya mampu mencocokkan pola lalu lintas terhadap basis data serangan yang telah diketahui, sehingga rentan mengalami kegagalan deteksi terhadap varian serangan baru (*zero-day attacks*). Sebaliknya, sistem deteksi berbasis pembelajaran mesin (*Machine Learning* / ML) dan *Deep Learning* (DL) memiliki keunggulan adaptif dalam mengekstraksi representasi statistik aliran data (*bidirectional network flows*) guna mengenali anomali lalu lintas secara otomatis.

Meskipun model pembelajaran mesin terpusat (*centralized learning*) menunjukkan akurasi tinggi, paradigma pengumpulan data terpusat menghadapi dua tantangan fundamental di dunia nyata:
1. **Regulasi Privasi dan Kebocoran Data:** Lalu lintas jaringan memuat data internal yang sangat sensitif (kredensial, identitas pengguna, struktur topologi intranet). Memusatkan rekaman paket mentah (*raw pcap/flow logs*) dari berbagai cabang subnet ke satu server sentral melanggar regulasi kepatuhan privasi (seperti UU Pelindungan Data Pribadi / UU PDP di Indonesia dan GDPR secara global), serta menimbulkan risiko kerentanan kebocoran data tunggal (*single point of failure/data breach*).
2. **Keterbatasan Bandwidth Jaringan:** Mentransfer jutaan aliran paket jaringan berskala gigabyte secara terus-menerus ke server analitik sentral menimbulkan *bandwidth bottleneck* yang membebani kapasitas jaringan operasional enterprise.

Untuk mengatasi batasan privasi dan transmisi data tersebut, paradigma *Federated Learning* (FL), khususnya algoritma *Federated Averaging* (FedAvg) yang diperkenalkan oleh McMahan et al. [3], muncul sebagai arsitektur pelatihan terdistribusi yang menjanjikan. Melalui FL, setiap node sensor (klien) melatih model deteksi intrusi secara lokal menggunakan data lalu lintas di perimeter jaringannya sendiri. Node klien kemudian hanya mengirimkan pembaruan parameter bobot model (*gradient/weight updates*) ke server agregator terpusat, tanpa pernah membagikan data lalu lintas mentah.

Kendati demikian, implementasi FL pada domain deteksi intrusi jaringan memicu tantangan baru yang signifikan. Pada kondisi operasional nyata, distribusi data lalu lintas antar-node sensor bersifat sangat heterogen atau *non-Identical and Independently Distributed* (non-IID). Sebuah node sensor di perimeter subnet server autentikasi internal dominan menghadapi serangan *brute force* SSH, sedangkan node sensor di zona publik (*Demilitarized Zone* / DMZ) dominan menghadapi serangan volumetrik web DoS (*label skew*). Zhao et al. [4] membuktikan secara teoretis bahwa heterogenitas non-IID memicu divergensi bobot lokal (*weight divergence*) yang drastis, sehingga agregasi rata-rata konvensional pada FedAvg rentan mengalami degradasi akurasi yang signifikan.

Tantangan ini diperparah oleh dinamika temporal dari serangan jaringan. Serangan siber tidak terjadi secara serentak, melainkan muncul secara berkala dan berurutan dari waktu ke waktu (*continuous streaming data*). Ketika model deteksi intrusi dilatih menggunakan kelas serangan baru (misal: DoS pada Task 2) setelah sebelumnya mempelajari kelas serangan terdahulu (misal: SSH-Patator pada Task 1), pembaruan bobot jaringan saraf tiruan cenderung menimpa representasi laten yang telah dipelajari sebelumnya. Fenomena ini dikenal dalam literatur *Continual Learning* (CL) sebagai **catastrophic forgetting** [5]. Akibatnya, sistem IDS menjadi "lupa" dan gagal mendeteksi kembali serangan lawas yang sewaktu-waktu dapat dilancarkan kembali oleh peretas.

Untuk menanggulangi *catastrophic forgetting*, salah satu pendekatan yang paling elegan dan ramah privasi adalah metode berbasis regularisasi parameter, yaitu **Elastic Weight Consolidation (EWC)** [5]. EWC mengkalkulasi signifikansi parameter bobot terhadap tugas masa lalu menggunakan Matriks Informasi Fisher diagonal (*Fisher Information Matrix*). Saat model mempelajari tugas baru, EWC menambahkan fungsi penalti kuadratik yang mengekang perubahan bobot-bobot krusial tersebut. Berbeda dari metode *Experience Replay* yang mengharuskan penyimpanan *buffer* sampel data mentah di memori lokal—yang berpotensi melanggar privasi dan membebani kapasitas RAM perangkat sensor *edge*—EWC bekerja murni pada ruang parameter model, menjadikannya solusi ideal untuk integrasi *Federated Continual Learning* (FCL).

Penelitian mengenai integrasi FL dan CL pada NIDS di bawah distribusi non-IID masih sangat terbatas dan menghadapi tantangan metodologis yang krusial. Sebagian besar penelitian terdahulu (1) mengasumsikan data terdistribusi secara identik (IID), (2) mengabaikan fenomena kebocoran fitur (*shortcut learning*) akibat penggunaan nomor port layanan, atau (3) menerapkan pemangkasan data (*undersampling*) ekstrem yang merusak realitas operasional ketimpangan kelas (*class imbalance*). 

Oleh karena itu, penelitian tugas akhir ini berfokus pada **investigasi komprehensif mitigasi catastrophic forgetting pada deteksi intrusi jaringan terdistribusi menggunakan Federated Continual Learning berbasis EWC di bawah kondisi data non-IID**. Penelitian ini menggunakan dataset tolok ukur resmi CIC-IDS2017 yang dikurasi secara ketat bebas dari kebocoran fitur *Destination Port*, mempertahankan seluruh data bersih melalui fungsi *Weighted Cross-Entropy Loss*, dan dievaluasi melintasi lima *random seed* independen untuk menjamin validitas dan signifikansi temuan ilmiah.

---

## 1.2 Rumusan Masalah

Berdasarkan latar belakang yang telah diuraikan, rumusan masalah dalam penelitian tugas akhir ini adalah:
1. **Bagaimana efektivitas kinerja deteksi intrusi model yang dilatih secara terdistribusi menggunakan Federated Learning (FedAvg) dibandingkan dengan pelatihan model lokal mandiri di bawah kondisi distribusi data non-IID (*label skew*)?**
2. **Sejauh mana penerapan metode regularisasi Elastic Weight Consolidation (EWC) pada klien lokal mampu memitigasi fenomena *catastrophic forgetting* (mempertahankan metrik *Backward Transfer* / BWT) saat model mempelajari jenis serangan baru secara sekuensial tanpa menyimpan *buffer* data mentah?**

---

## 1.3 Batasan Masalah

Untuk menjaga fokus penelitian, mencegah pelebaran ruang lingkup (*scope creep*), serta menjamin kedalaman analisis ilmiah yang dapat dipertanggungjawabkan, batasan masalah ditetapkan sebagai berikut:
1. **Dataset Penelitian:** Penelitian menggunakan secara eksklusif data lalu lintas jaringan dari dataset tolok ukur resmi Canadian Institute for Cybersecurity, yaitu **CIC-IDS2017** berkas hari Senin (*Monday*), Selasa (*Tuesday*), dan Rabu (*Wednesday*). Berkas hari Kamis dan Jumat dieksklusi karena menderita kelangkaan sampel mikro ekstrem (21–36 baris) serta desinkronisasi pelabelan pcap parah berdasarkan literatur audit saintifik [6], [7].
2. **Cakupan Kelas Klasifikasi:** Klasifikasi dibatasi pada tiga kelas operasional representatif:
   - **BENIGN (Normal):** Aliran data operasional rutin (1.332.710 aliran bersih).
   - **SSH-Patator:** Serangan *brute-force* autentikasi pada Task 1 (3.219 aliran bersih).
   - **DoS (Denial of Service):** Serangan volumetrik penolakan layanan pada Task 2, mencakup empat subvarian alami: Hulk, GoldenEye, slowloris, dan Slowhttptest (193.748 aliran bersih).
3. **Pembersihan Fitur & Pencegahan Shortcut:** Fitur masukan model dibatasi pada **63 fitur numerik unik**. Sebanyak 10 fitur konstan bervariansi nol dan 5 pasangan fitur duplikat identik dieliminasi. Fitur `Destination Port` secara sengaja dibuang guna mencegah bias *shortcut learning* (*port-to-label memorization*).
4. **Penanganan Ketimpangan Kelas:** Seluruh 1.529.677 aliran data bersih dipertahankan tanpa pemangkasan (*no massive undersampling*) dengan menerapkan *Weighted Cross-Entropy Loss* berbasis invers frekuensi kelas terkalibrasi serta *gradient clipping* (norm $\le 1.0$).
5. **Arsitektur Model Pembelajaran Mesin:** Model klasifikasi dibatasi pada arsitektur *Multilayer Perceptron* (MLP) kompak tiga lapis (`Input(63) → Linear(64) → ReLU → Linear(32) → ReLU → Linear(3)`).
6. **Topologi Federated Learning:** Simulasi federasi menggunakan algoritma **Federated Averaging (FedAvg)** dengan topologi 2 node sensor klien non-IID dan 1 server agregator:
   - **Klien A (Task 1):** Mengakses data Normal dan 100% data serangan SSH-Patator.
   - **Klien B (Task 2):** Mengakses data Normal dan 100% data serangan DoS.
   - Kelas Normal dipartisi secara acak 50% untuk Klien A dan 50% untuk Klien B dari gabungan seluruh hari untuk mencegah bias pola harian (*day-of-week confound*).
7. **Skenario Continual Learning:** Model diuji dalam skenario **Class-Incremental Learning (Class-IL)** tanpa penyediaan Task-ID saat inferensi. Metode mitigasi lupa dibatasi pada perbandingan antara **Naive Fine-Tuning** dan **Elastic Weight Consolidation (EWC)**.
8. **Lingkungan Pengujian & Eliminasi Live Traffic:** Pengujian difokuskan murni pada data tolok ukur *offline tabular flow*. Injeksi lalu lintas jaringan aktif (*live traffic injection*) secara resmi ditiadakan dari target evaluasi untuk mengeliminasi variabel gangguan transport/lapisan fisik (sesuai arahan dosen pembimbing).
9. **Metrik Evaluasi:** Evaluasi diukur menggunakan metrik deteksi ML (Macro-F1, per-class Precision, Recall, Accuracy, dan *Backward Transfer* / BWT), serta metrik profil komputasi (latensi inferensi per flow dalam $\mu\text{s}$, alokasi memori RAM *footprint*, dan *communication overhead* payload model dalam KB per round).

---

## 1.4 Tujuan Penelitian

Tujuan yang ingin dicapai melalui pelaksanaan penelitian tugas akhir ini adalah:
1. Merancang, membangun, dan menganalisis arsitektur sistem deteksi intrusi terdistribusi berbasis Federated Learning (FedAvg) pada data lalu lintas non-IID untuk mengevaluasi generalisasi model dibandingkan model pelatihan lokal mandiri.
2. Mengintegrasikan dan mengevaluasi efektivitas regularisasi Elastic Weight Consolidation (EWC) pada optimasi model klien lokal dalam menekan laju *catastrophic forgetting* terhadap kelas serangan SSH-Patator terdahulu setelah model mempelajari kelas serangan DoS baru.
3. Mengukur efisiensi komputasi sistem usulan mencakup rata-rata waktu inferensi per aliran data ($\mu\text{s}$), konsumsi alokasi memori RAM (*memory footprint*) antara metode penalti parameter EWC versus *replay buffer*, serta *communication overhead* bobot model per putaran federasi.

---

## 1.5 Manfaat

Pelaksanaan penelitian ini diharapkan dapat memberikan kontribusi dan manfaat teoretis maupun praktis:
1. **Manfaat Teoretis (Akademik):**
   - Memberikan kontribusi empiris dan analitis mengenai perilaku interaksi antara algoritma agregasi Federated Learning (FedAvg) dan regularisasi Continual Learning (EWC) pada domain keamanan siber di bawah kondisi heterogenitas data non-IID.
   - Memperkaya literatur NIDS mengenai metodologi evaluasi bebas bias *shortcut learning* melalui eliminasi fitur nomor port dan pengujian berbasis multi-seed.
2. **Manfaat Praktis (Teknologi & Industri):**
   - Menyediakan kerangka arsitektur deteksi intrusi adaptif yang aman privasi dan hemat *bandwidth* untuk diaplikasikan pada sensor *edge gateway* jaringan enterprise atau *smart campus*.
   - Membuktikan bahwa pembaruan model keamanan dapat dilakukan secara berkala dan berkesinambungan tanpa perlu mengirimkan log rekaman data mentah pengguna ke server eksternal dan tanpa kehilangan kapabilitas mendeteksi ancaman masa lalu.
