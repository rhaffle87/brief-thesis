# BAB 1 PENDAHULUAN

## 1.1 Latar Belakang

Perkembangan teknologi informasi dan transformasi digital yang kian pesat telah meningkatkan ketergantungan infrastruktur enterprise, institusi publik, dan layanan perbankan terhadap integritas jaringan komputer. Namun, eskalasi keterhubungan ini diiringi oleh lonjakan volume dan kompleksitas ancaman siber (*cyber threats*). Menurut laporan global *Check Point Research*, terjadi peningkatan rata-rata serangan siber mingguan sebesar 47% per organisasi di seluruh dunia, dengan sektor telekomunikasi, pendidikan, dan infrastruktur kritikal menjadi sasaran eksploitasi utama[1]. Selain itu, laporan *FBI Internet Crime Complaint Center* (IC3) mencatat total kerugian ekonomi global akibat kejahatan siber telah melampaui triliunan dolar, di mana vektor serangan intrusi jaringan seperti eksploitasi brute-force autentikasi (SSH) dan serangan penolakan layanan (*Denial of Service* / DoS) tetap mendominasi spektrum insiden keamanan operasional[2]. Peningkatan baik dari sisi jumlah maupun kompleksitas teknik serangan ini menuntut sistem pertahanan yang adaptif dan mampu mengamankan jaringan secara berkesinambungan.

Dalam menjaga integritas, kerahasiaan (*confidentiality*), dan ketersediaan (*availability*) aset jaringan, *Network Intrusion Detection System* (NIDS) bertindak sebagai garda pertahanan utama untuk memantau, mendeteksi, dan mengklasifikasikan anomali lalu lintas data secara *near real-time*. Pendekatan NIDS konvensional berbasis *signature* (*Signature-Based Intrusion Detection System* / SIDS) bekerja dengan mencocokkan pola aktivitas terhadap basis data tanda tangan serangan yang telah diketahui, namun rentan mengalami kegagalan deteksi terhadap varian serangan baru (*zero-day attacks*). Sebaliknya, sistem deteksi berbasis anomali menggunakan *Machine Learning* (ML) dan *Deep Learning* (DL) memiliki keunggulan adaptif dalam mengekstraksi representasi statistik aliran data (*bidirectional network flows*) guna mengenali anomali lalu lintas secara otomatis.

Meskipun model pembelajaran mesin terpusat (*centralized learning*) menunjukkan akurasi deteksi yang tinggi, paradigma pengumpulan data secara sentral menghadapi dua tantangan fundamental di dunia nyata, yaitu regulasi privasi data dan keterbatasan lebar pita (*bandwidth*). Lalu lintas jaringan memuat data internal yang sangat sensitif, seperti kredensial, identitas pengguna, dan struktur topologi intranet. Memusatkan rekaman paket mentah (*raw pcap* atau *flow logs*) dari berbagai cabang subnet ke satu server sentral berpotensi melanggar regulasi kepatuhan privasi data, seperti Undang-Undang Pelindungan Data Pribadi (UU PDP No. 27/2022) di Indonesia dan GDPR di tingkat global, serta menimbulkan risiko kerentanan titik kegagalan tunggal (*single point of failure*) terhadap insiden kebocoran data. Di samping itu, mentransfer jutaan aliran paket jaringan berskala gigabita secara berkesinambungan ke server analitik sentral menimbulkan *bandwidth bottleneck* yang membebani kapasitas jaringan operasional enterprise.

Untuk mengatasi batasan privasi dan transmisi data tersebut, paradigma *Federated Learning* (FL), khususnya algoritma *Federated Averaging* (FedAvg), muncul sebagai arsitektur pelatihan terdistribusi yang menjanjikan[3]. Melalui FL, setiap node sensor (klien) melatih model deteksi intrusi secara lokal menggunakan data lalu lintas di perimeter jaringannya sendiri. Node klien kemudian hanya mengirimkan pembaruan parameter bobot model (*gradient/weight updates*) ke server agregator terpusat, tanpa pernah membagikan data lalu lintas mentah.

Kendati demikian, implementasi FL pada domain deteksi intrusi jaringan memicu tantangan baru yang signifikan. Pada kondisi operasional nyata, distribusi data lalu lintas antar-node sensor bersifat sangat heterogen atau *non-Identical and Independently Distributed* (non-IID). Sebagai contoh, node sensor di perimeter subnet server autentikasi internal dominan menghadapi serangan *brute-force* SSH, sedangkan node sensor di zona publik (*Demilitarized Zone* / DMZ) dominan menghadapi serangan volumetrik web DoS (*label skew*). Heterogenitas non-IID terbukti secara teoretis memicu divergensi bobot lokal (*weight divergence*) yang drastis, sehingga agregasi rata-rata konvensional pada FedAvg rentan mengalami degradasi akurasi yang signifikan[4].

Tantangan ini diperparah oleh dinamika temporal dari serangan jaringan. Serangan siber tidak terjadi secara serentak, melainkan muncul secara berkala dan berurutan dari waktu ke waktu (*continuous streaming data*). Ketika model deteksi intrusi dilatih menggunakan kelas serangan baru (seperti DoS pada Task 2) setelah sebelumnya mempelajari kelas serangan terdahulu (seperti SSH-Patator pada Task 1), pembaruan bobot jaringan saraf tiruan cenderung menimpa representasi laten yang telah dipelajari sebelumnya. Fenomena ini dikenal dalam literatur *Continual Learning* (CL) sebagai **catastrophic forgetting**[5]. Akibatnya, sistem IDS mengalami penurunan drastis pada kemampuan mengenali kembali serangan lawas yang sewaktu-waktu dapat dilancarkan kembali oleh penyerang.

Untuk menanggulangi *catastrophic forgetting*, salah satu pendekatan yang paling elegan dan ramah privasi adalah metode berbasis regularisasi parameter, yaitu **Elastic Weight Consolidation (EWC)**. EWC mengkalkulasi signifikansi parameter bobot terhadap tugas masa lalu menggunakan Matriks Informasi Fisher diagonal (*Fisher Information Matrix*). Saat model mempelajari tugas baru, EWC menambahkan fungsi penalti kuadratik yang mengekang perubahan bobot-bobot krusial tersebut. Berbeda dari metode *Experience Replay* yang mengharuskan penyimpanan *buffer* sampel data mentah di memori lokal (yang berpotensi melanggar privasi dan membebani kapasitas RAM perangkat sensor *edge*), EWC bekerja murni pada ruang parameter model, menjadikannya solusi ideal untuk integrasi *Federated Continual Learning* (FCL)[5].

Penelitian mengenai integrasi FL dan CL pada NIDS di bawah distribusi non-IID saat ini masih sangat terbatas dan menghadapi tantangan metodologis yang krusial. Sebagian besar penelitian terdahulu mengasumsikan data terdistribusi secara identik (IID), mengabaikan fenomena kebocoran fitur (*shortcut learning*) akibat penggunaan nomor port layanan, atau menerapkan pemangkasan data (*undersampling*) ekstrem yang merusak realitas operasional ketimpangan kelas (*class imbalance*). 

Oleh karena itu, penelitian tugas akhir ini berfokus pada **analisis kinerja deteksi *network traffic intrusion* menggunakan metode *Federated-Continual Learning* pada *testbed private cloud server*, dengan studi pengaruh *Elastic Weight Consolidation* (EWC) dan *Federated Averaging* (FedAvg) pada distribusi data non-IID dua *client* guna memitigasi *catastrophic forgetting***. Penelitian ini menggunakan dataset tolok ukur resmi CIC-IDS2017 yang dikurasi secara ketat bebas dari kebocoran fitur *Destination Port*, mempertahankan representasi sebaran data bersih melalui fungsi *Weighted Cross-Entropy Loss*, serta dievaluasi melintasi lima *random seed* independen untuk menjamin validitas dan signifikansi temuan ilmiah.

---

## 1.2 Rumusan Masalah

Berdasarkan latar belakang yang telah diuraikan, maka rumusan masalah dalam penelitian tugas akhir ini adalah sebagai berikut:
1. Bagaimana kinerja deteksi intrusi model yang dilatih secara terdistribusi (*Federated Averaging* / FedAvg) dibandingkan dengan model yang dilatih secara lokal pada masing-masing klien dengan distribusi data non-IID?
2. Bagaimana pengaruh metode *Elastic Weight Consolidation* (EWC) terhadap mitigasi *catastrophic forgetting* saat model mempelajari kelas serangan baru secara sekuensial, baik pada skenario pelatihan lokal maupun terdistribusi (FedAvg + EWC)?

---

## 1.3 Batasan Masalah

Dalam pelaksanaan tugas akhir ini, batasan ruang lingkup masalah ditetapkan untuk memberikan arah penelitian yang terfokus. Batasan-batasan masalah tersebut meliputi:
1. **Dataset Penelitian:** Penelitian menggunakan secara eksklusif data lalu lintas jaringan dari dataset tolok ukur resmi Canadian Institute for Cybersecurity, yaitu **CIC-IDS2017** berkas hari Senin (*Monday*), Selasa (*Tuesday*), dan Rabu (*Wednesday*). Berkas hari Kamis dan Jumat dieksklusi karena menderita kelangkaan sampel mikro ekstrem (21–36 baris) serta desinkronisasi pelabelan pcap parah berdasarkan literatur audit saintifik[6], [7].
2. **Cakupan Kelas Klasifikasi:** Klasifikasi dibatasi pada tiga kelas operasional representatif:
   - **BENIGN (Normal):** Aliran data operasional rutin (1.332.710 aliran bersih).
   - **SSH-Patator:** Serangan *brute-force* autentikasi pada Task 1 (3.219 aliran bersih).
   - **DoS (Denial of Service):** Serangan volumetrik penolakan layanan pada Task 2, mencakup empat subvarian alami: Hulk, GoldenEye, slowloris, dan Slowhttptest (193.748 aliran bersih).
3. **Pembersihan Fitur & Pencegahan Shortcut:** Fitur masukan model dibatasi pada **63 fitur numerik unik**. Sebanyak 10 fitur konstan bervariansi nol dan 5 pasangan fitur duplikat identik dieliminasi. Fitur `Destination Port` secara sengaja dibuang guna mencegah bias *shortcut learning* (*port-to-label memorization*).
4. **Penanganan Ketimpangan Kelas:** Seluruh 1.529.677 aliran data bersih dipertahankan tanpa pemangkasan (*no massive undersampling*) dengan menerapkan *Weighted Cross-Entropy Loss* berbasis invers frekuensi kelas terkalibrasi serta *gradient clipping* (norm $\le 1.0$).
5. **Arsitektur Model Pembelajaran Mesin:** Model klasifikasi dibatasi pada arsitektur *Multilayer Perceptron* (MLP) kompak tiga lapis terhubung penuh berkapasitas 6.275 parameter bobot dan bias (lapisan masukan 63 fitur numerik bersih, dua lapisan tersembunyi berdimensi 64 dan 32 neuron dengan fungsi aktivasi ReLU, serta lapisan keluaran 3 logits kelas), sebagaimana dirancang pada diagram arsitektur model ([arsitektur_model_mlp.svg](../Aset/arsitektur_model_mlp.svg)).
6. **Topologi Federated Learning:** Simulasi federasi menggunakan algoritma **Federated Averaging (FedAvg)** dengan topologi 2 node sensor klien non-IID dan 1 server agregator:
   - **Klien A (Task 1):** Mengakses data Normal dan 100% data serangan SSH-Patator.
   - **Klien B (Task 2):** Mengakses data Normal dan 100% data serangan DoS.
   - Kelas Normal dipartisi secara acak 50% untuk Klien A dan 50% untuk Klien B dari gabungan seluruh hari untuk mencegah bias pola harian (*day-of-week confound*).
7. **Skenario Continual Learning:** Model diuji dalam skenario **Class-Incremental Learning (Class-IL)** tanpa penyediaan Task-ID saat inferensi. Metode mitigasi lupa dibatasi pada perbandingan antara **Naive Fine-Tuning** dan **Elastic Weight Consolidation (EWC)**.
8. **Lingkungan Pengujian & Eliminasi Live Traffic:** Pengujian difokuskan murni pada data tolok ukur *offline tabular flow*. Injeksi lalu lintas jaringan aktif (*live traffic injection*) secara resmi ditiadakan dari target evaluasi untuk mengeliminasi variabel gangguan transport/lapisan fisik (sesuai arahan dosen pembimbing).
9. **Metrik Evaluasi:** Evaluasi diukur menggunakan metrik deteksi ML (Macro-F1, per-class Precision, Recall, Accuracy, dan *Backward Transfer* / BWT), serta metrik profil efisiensi komputasi (latensi inferensi per flow dalam $\mu\text{s}$, alokasi memori RAM *footprint*, dan *communication overhead* payload model dalam KB per round).

---

## 1.4 Tujuan

Penelitian ini bertujuan untuk:
1. Menganalisis kinerja deteksi intrusi model yang dilatih secara terdistribusi (*Federated Averaging* / FedAvg) dibandingkan dengan model yang dilatih secara lokal pada masing-masing klien dengan distribusi data non-IID.
2. Menganalisis pengaruh metode *Elastic Weight Consolidation* (EWC) terhadap mitigasi *catastrophic forgetting* serta mengukur efisiensi komputasi model (latensi inferensi per aliran data, alokasi memori RAM *footprint*, dan *communication overhead*) saat mempelajari kelas serangan baru secara sekuensial, baik pada skenario pelatihan lokal maupun terdistribusi (FedAvg + EWC).

---

## 1.5 Manfaat

Pelaksanaan penelitian ini diharapkan dapat memberikan kontribusi dan manfaat teoretis maupun praktis sebagai berikut:
1. **Manfaat Teoretis (Akademik):**
   - Memberikan kontribusi empiris dan analitis mengenai perilaku interaksi antara algoritma agregasi Federated Learning (FedAvg) dan regularisasi Continual Learning (EWC) pada domain keamanan siber di bawah kondisi heterogenitas data non-IID.
   - Memperkaya literatur NIDS mengenai metodologi evaluasi bebas bias *shortcut learning* melalui eliminasi fitur nomor port dan pengujian berbasis multi-seed.
2. **Manfaat Praktis (Teknologi & Industri):**
   - Menyediakan kerangka arsitektur deteksi intrusi adaptif yang aman privasi dan hemat *bandwidth* untuk diaplikasikan pada sensor *edge gateway* jaringan enterprise atau *smart campus*.
   - Membuktikan bahwa pembaruan model keamanan dapat dilakukan secara berkala dan berkesinambungan tanpa perlu mengirimkan log rekaman data mentah pengguna ke server eksternal dan tanpa kehilangan kapabilitas mendeteksi ancaman masa lalu.
