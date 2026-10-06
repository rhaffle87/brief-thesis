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

## 📋 Checklist Berkas yang Dibawa Saat Bimbingan

1. **Cetakan Fisik / PDF Siap Tampil (2–3 Halaman):**  
   - Buka: [[Bahan-Paparan-Pembimbing]] atau [[Ringkasan-Untuk-Pembimbing]].
2. **Naskah Proposal Lengkap (Referensi Detail):**  
   - Buka: [[Briefing Scope TA]].
3. **Dokumen Bukti Empiris Data (Jika Dosen Minta Angka Riil):**  
   - Buka: [[EDA-CIC-IDS2017]] (menunjukkan tabel 10 kolom konstan, grafik port leakage 96,44%, dan distribusi DoS).
4. **Daftar Pustaka 5 Tahun Terakhir:**  
   - Buka: [[Daftar-Pustaka]] dan [[Crosscheck]] (menunjukkan 13 paper 2021–2026 yang 100% PDF-nya sudah tersedia di laptop).
