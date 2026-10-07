# Panduan Tanya-Jawab & Skenario Pembelaan (Defense Cheat Sheet) untuk Bimbingan

**Topik:** Analisis Kinerja Deteksi Network Traffic Intrusion Menggunakan Metode Federated-Continual Learning pada Testbed Private Cloud Server  
**Mahasiswa:** Rafli Alif Ihza Hartono (NRP 5022211233)  
**Tujuan:** Panduan siap pakai untuk menjawab pertanyaan kritis dan sanggahan dosen pembimbing saat sesi tatap muka.  

---

## 🛡️ Skenario Antisipasi Pertanyaan Dosen Pembimbing

### Pertanyaan 1: "Mengapa FL hanya menggunakan 2 client dan 3 kelas serangan? Kenapa tidak 5 atau 10 client?"
- **Strategi Jawaban:** *Kombinasi Isolasi Ilmiah & Topologi Realistis Sensor Jaringan.*
- **Poin Jawaban:**
  1. **Representasi Topologi Riil:** 2 client bukan sekadar angka arbitrer, melainkan memodelkan dua titik sensor independen di enterprise:
     - **Client A:** Memodelkan sensor subnet internal yang memantau server autentikasi (Normal + serangan SSH Brute Force).
     - **Client B:** Memodelkan sensor zona DMZ / perimeter publik yang memantau web server (Normal + serangan volumetrik DoS).
  2. **Isolasi Variabel Penelitian:** Sesuai prinsip metodologi, penelitian skripsi S1 ini berfokus pada membuktikan **mekanisme interaksi antara FedAvg dan EWC terhadap non-IID data**. Menggunakan 2 client memastikan pergeseran distribusi (*label-skew*) terisolasi secara murni tanpa terganggu *noise* latensi jaringan, *client dropout*, atau *straggler effect* pada skala ratusan node.
  3. **Keterbukaan Fleksibilitas:** *"Apabila Bapak/Ibu menghendaki, kami dapat menambahkan 1–2 client variasi pada pengujian lanjutan, namun sebagai baseline inti kami menyarankan mengunci 2 client ini."*

---

### Pertanyaan 2: "Di dunia nyata, Destination Port itu parameter nomor satu di firewall/IDS. Mengapa port malah dibuang?"
- **Strategi Jawaban:** *Strategi Dual-Tabel (Integritas Ilmiah vs Relevansi Praktis).*
- **Poin Jawaban:**
  1. **Bukti Shortcut Learning Empiris:** Tunjukkan hasil Decision Tree awal:
     - Hanya dengan 1 fitur (Destination Port), model langsung mencapai **Macro-F1 96,44%**.
     - Mengapa? Karena SSH selalu port 22 dan HTTP DoS selalu port 80. Model syaraf tiruan menjadi "malas" dan hanya menghafal nomor port alih-alih mempelajari dinamika statistik flow paket.
     - Di masa depan, penyerang dapat menjalankan SSH di port non-standar (misal port 2222) atau DoS di port acak, dan model berbasis port akan langsung lumpuh.
  2. **Solusi Kompromi (Dual-Tabel):**
     - Skenario pengujian utama dijalankan pada **62 fitur (tanpa port)** untuk membuktikan model benar-benar mempelajari pola flow statistik intrusi.
     - Kami menyediakan **satu kolom pembanding (dengan port, 63 fitur)** di tabel skripsi untuk memperlihatkan kepada penguji secara transparan seberapa besar efek *shortcut* yang dihasilkan port.

---

### Pertanyaan 3: "EWC itu metode tahun 2017. Mengapa Anda tidak memakai Memory Replay (Experience Replay / GEM) yang performanya sering lebih tinggi?"
- **Strategi Jawaban:** *Kepatuhan Regulasi Privasi Jaringan & Keterbatasan Edge Device.*
- **Poin Jawaban:**
  1. **Prinsip Utama Privasi FL:** Menyimpan data paket/flow trafik masa lalu ke dalam buffer memori lokal bertentangan dengan filosofi *privacy-preserving* FL dan regulasi perlindungan data (UU PDP / GDPR). Trafik jaringan memuat muatan data sensitif pengguna yang tidak boleh di-cache secara permanen.
  2. **Keterbatasan Memori Sensor Tepi:** Sensor IDS di perangkat jaringan memiliki alokasi memori terbatas. Jika setiap kali ada serangan baru sensor harus menyimpan ribuan sampel lama, kapasitas penyimpanan akan cepat habis.
  3. **EWC sebagai Solusi Regulasi Parameter Murni:** EWC memproteksi pengetahuan lama hanya dengan mengunci bobot via penalti matriks Fisher, tanpa pernah menyimpan sebaris pun data paket mentah masa lalu.
  4. **Referensi Mutakhir:** Paper terkini (*Rehman et al., 2026; Liu & Chang, 2026*) menegaskan bahwa EWC tetap menjadi tolok ukur standar (*gold standard*) untuk continual learning berbasis regularisasi arsitektur.

---

### Pertanyaan 4: "Mengapa menggunakan dataset CIC-IDS2017 yang banyak dikritik memiliki bug (Rosay 2022)? Kenapa tidak pakai CSE-CIC-IDS2018 atau dataset lain?"
- **Strategi Jawaban:** *Transparansi Metodologi & Ketersediaan Benchmark Internasional.*
- **Poin Jawaban:**
  1. **Standar Komparasi Terbanyak:** CIC-IDS2017 adalah dataset paling banyak dikutip dalam literatur FL-IDS (ribuan sitasi), sehingga hasil eksperimen ini memiliki basis pembanding (*baseline*) yang kuat terhadap paper-paper lain.
  2. **Ketiadaan Alternatif Bebas Bug (Kasus LYCOS):** Dataset hasil perbaikan Rosay 2022 (LYCOS-IDS2017) saat ini berstatus *404 Not Found* di server Universitas Le Mans dan tidak dapat diakses publik.
  3. **Sikap Ilmiah yang Benar:** Mengikuti rekomendasi Dube et al. (2024), alih-alih menyembunyikan kelemahan dataset, kami mengauditnya secara terbuka di Bab 3, membuang 10 kolom konstan nol-variansi dan 5 kolom duplikat 100%, serta fokus pada analisis komparatif relatif (E1 vs E2 vs E3 vs E4), bukan sekadar klaim akurasi absolut 99%.

---

### Pertanyaan 5: "Bagaimana status pengujian Live Traffic (E5) di Proxmox? Apakah ini wajib diselesaikan?"
- **Status Akhir Bimbingan (2026-10-06):** *Resmi Ditiadakan oleh Dosen Pembimbing.*
- **Poin Kesepakatan:**
  1. **Eliminasi Parameter Noise:** Dosen pembimbing menegaskan bahwa injeksi live traffic (menggunakan VM 400 generator serangan) membawa terlalu banyak parameter dinamis non-algoritmik (dropped packets, timing jitter, buffer overrun, bridge throughput limits) yang berisiko mengaburkan fokus pembuktian ilmiah algoritma FL-CL.
  2. **Fokus Riset Terkunci:** Seluruh target skripsi E0 s.d. E4 diselesaikan 100% menggunakan data benchmark berlabel CIC-IDS2017 pada skenario terdistribusi non-IID 2 client.
  3. **Staging Testbed:** Realisasi testbed dieksekusi bertahap: local first (Docker Compose / isolated venv), kemudian dilanjutkan simulasi server VM pada Proxmox VE.

---

### Pertanyaan 6: "Mengapa dataset yang dipakai hanya Senin, Selasa, dan Rabu? Mengapa berkas Kamis dan Jumat tidak digunakan?"
- **Strategi Jawaban:** *Kesesuaian Ruang Lingkup 3 Kelas, Validitas Statistik Sampel, dan Mitigasi Cacat Labeling.*
- **Poin Jawaban:**
  1. **Korespondensi Penuh dengan 3 Kelas Penelitian:**
     - Tugas akhir ini secara spesifik membatasi lingkup pada 3 kelas: **Normal, SSH-Patator (Task 1), dan DoS (Task 2)**.
     - **Senin:** Menyediakan 529.918 flow **Normal murni** (tanpa serangan) sebagai baseline aktivitas rutin.
     - **Selasa:** Menyediakan serangan **SSH-Patator** (3.219 flow unik bersih) untuk Client A / Task 1.
     - **Rabu:** Menyediakan serangan **DoS** 4 varian lengkap (193.748 flow unik bersih) untuk Client B / Task 2.
     - Ketiga berkas hari ini sudah mencakup **100% kelas penelitian** secara lengkap dan berimbang.
  2. **Kelangkaan Sampel Ekstrem pada Hari Kamis:**
     - Hari Kamis memuat Web Attacks dan Infiltration, dengan volume serangan mikro: *Sql Injection hanya 21 baris*, *Infiltration hanya 36 baris*, dan *XSS hanya 652 baris*.
     - Kuantitas sekecil ini secara metodologis **tidak memenuhi syarat daya statistik (*statistical power*)** untuk dipartisi ke dalam 2 client non-IID, 3 split (train 70%, val 15%, test 15%), dan 5 random seed tanpa memicu overfitting parah atau kegagalan konvergensi.
  3. **Cacat Desinkronisasi Pelabelan Parah pada Hari Kamis (Rosay et al., 2022):**
     - Literatur audit dataset (*Rosay et al., 2022*) membuktikan bahwa berkas hari Kamis menderita *pcap timestamp offset* parah, di mana ribuan paket normal salah diberi label serangan dan sebaliknya. Menyertakan hari Kamis justru merusak integritas evaluasi model.
  4. **Karakteristik Trafik Hari Jumat Tidak Sesuai Desain Skenario:**
     - *PortScan (158K flow):* Merupakan reconnaissance scanning, bukan intrusi eksploitasi aktif.
     - *Botnet ARES (1,9K flow):* Menderita bug fragmentasi alur TCP pada CICFlowMeter (Dube et al., 2024).
     - *DDoS LOIC (128K flow):* Secara konseptual tumpang tindih dengan DoS Rabu, namun membawa fingerprint alat LOIC yang memicu bias kerancuan (*confounding*): model tidak bisa dibedakan apakah lupa karena catastrophic forgetting atau karena perbedaan signature alat serang.
  5. **Efisiensi Komputasi:**
     - Memasukkan Kamis dan Jumat akan menambah 1,16 juta baris data tanpa menyumbang satupun sampel SSH atau DoS baru, melainkan hanya memperlambat waktu komputasi pelatihan 5 seed secara sia-sia.

---

## 📋 Checklist Berkas yang Dibawa Saat Bimbingan

1. **Cetakan Fisik / PDF Siap Tampil (2–3 Halaman):**  
   - Buka: [Bahan-Paparan-Pembimbing](Bahan-Paparan-Pembimbing.md) atau [Ringkasan-Untuk-Pembimbing](../Keputusan/Ringkasan-Untuk-Pembimbing.md).
2. **Naskah Proposal Lengkap (Referensi Detail):**  
   - Buka: [Briefing-Scope-TA](../Proposal/Briefing-Scope-TA.md).
3. **Dokumen Bukti Empiris Data (Jika Dosen Minta Angka Riil):**  
   - Buka: [EDA-CIC-IDS2017](../Metodologi/EDA-CIC-IDS2017.md) (menunjukkan tabel 10 kolom konstan, grafik port leakage 96,44%, dan distribusi DoS).
4. **Daftar Pustaka 5 Tahun Terakhir:**  
   - Buka: [Daftar-Pustaka](../Literatur/Daftar-Pustaka.md) dan [Crosscheck](../Literatur/Crosscheck.md) (menunjukkan 13 paper 2021–2026 yang 100% PDF-nya sudah tersedia di laptop).
