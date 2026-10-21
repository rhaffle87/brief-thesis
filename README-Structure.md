# Struktur Folder Obsidian Vault & Proyek Skripsi (FL-CL IDS)

**Path Vault:** `E:\Projects\thesis\`  
**Path Repo Kode:** `E:\Projects\fl-cl\`  
**Backup Snapshot:** `E:\Projects\thesis_backup_20261002\`  
**Tanggal Update:** 2026-10-04  
**Status Audit:** ✅ Terverifikasi & Tersinkronisasi (0 Broken Links)

---

## 📁 Struktur 14 Folder Utama

```
E:\Projects\thesis/
├── .obsidian/               # Konfigurasi workspace Obsidian
│
├── Dashboard/               # Pusat navigasi, timeline, matriks & checklist
│   ├── Dashboard.md         # Central hub proyek TA
│   ├── Checklist-Selesai.md # Definisi selesai per fase proyek
│   ├── Matriks-E0-E5.md     # Desain perbandingan eksperimen (E0-E5)
│   └── Timeline-16-Minggu.md# Rencana kerja mingguan terstruktur
│
├── Proposal/                # Briefing proposal TA & referensi skripsi
│   ├── Briefing-Scope-TA_ Federated-Continual Learning untuk Deteksi Intrusi.md
│   └── Referensi-Skripsi-Hafizh.pdf
│
├── Literatur/               # Catatan literatur per paper & repositori PDF
│   ├── Daftar-Pustaka.md    # Daftar pustaka format akademik
│   ├── Crosscheck.md        # Verifikasi metadata 25 paper (100% verified)
│   ├── Inventaris-PDF.md    # Inventaris 25 berkas PDF lokal
│   ├── [Paper-Notes].md     # 25 catatan telaah paper individual
│   └── PDFs/                # Berkas PDF fisik (25 berkas)
│       ├── (13 Paper Inti)  # McMahan, Kirkpatrick, Sharafaldin, Rosay, Dube, dll.
│       └── Opsional/        # (12 Paper Pendukung: Avalanche, EWC-DR, GFCL, DeLange, Wang, dll.)
│
├── Metodologi/              # Desain data, EDA, & verifikasi fitur
│   ├── CRITICAL-CIC-IDS2017-Issues.md # Rekapitulasi anomali/bug dataset
│   ├── DATASET-UNAVAILABLE-LYCOS.md   # Dokumentasi status LYCOS-IDS2017 (404)
│   ├── EDA-CIC-IDS2017.md   # Laporan komprehensif EDA & uji port leakage
│   ├── EDA-Verifikasi.md    # Hasil reproduksi verifikasi kolom konstan & duplikat
│   └── *.py                 # Skrip bantu analisis eksplorasi lokal
│
├── Eksperimen/              # Log eksperimen E0-E5 per seed (42-46)
│   └── (Akan diisi bertahap saat training dimulai)
│
├── Hasil/                   # Visualisasi kurva metrik, confusion matrix, tabel BWT
│   └── (Akan diisi setelah eksekusi E0-E4)
│
├── Penulisan/               # Draf naskah buku skripsi (Bab 1 s.d. Bab 5)
│   └── (Akan diisi sesuai template penulisan institusi)
│
├── Bimbingan/               # Log berkala, bahan paparan & panduan tanya-jawab dosen
│   ├── Bahan-Paparan-Pembimbing.md     # Ringkasan slide eksekutif untuk presentasi bimbingan
│   └── Panduan-Tanya-Jawab-Pembimbing.md # Skenario pembelaan & jawaban antisipasi pertanyaan dosen
│
├── Keputusan/               # Rekaman keputusan desain & briefing pembimbing
│   ├── Ringkasan-Untuk-Pembimbing.md    # Dokumen utama: 7 poin konfirmasi
│   ├── Keputusan-Untuk-Pembimbing.md   # Detail justifikasi opsi teknis
│   ├── Keputusan-Pembekuan-CL.md       # Penguncian algoritma CL (EWC only)
│   └── Keputusan-Pembekuan-FL.md       # Penguncian arsitektur FL (FedAvg 2-client)
│
├── Aset/                    # Diagram alur penelitian & arsitektur sistem
│   ├── alur_metode_penelitian.png
│   └── arsitektur_testbed_fl_cl.png
│
├── Laporan/                 # Laporan audit & log sesi terkonsolidasi
│   ├── Audit-Bukti-2026-10-03.md           # Bukti empiris status vault & EDA
│   └── Arsip-Riwayat-Sesi-Konsolidasi.md   # Arsip riwayat seluruh sesi lampau
│
├── Arsip/                   # Dokumen lawas pra-pembekuan scope
│   ├── manuscript.pdf       # Draf naskah awal (out of scope)
│   ├── research_paper.md    # Dokumentasi awal prototype
│   └── Archive-Keputusan-Belum-Disetujui-OLD.md
│
├── Templates/               # Template standar dokumen Obsidian
│   ├── Template-Literatur.md
│   └── Template-Log-Eksperimen.md
│
└── Datasets/                # Repositori data lokal
    ├── CIC-IDS2017/         # CSV mentah resmi UNB (Monday, Tuesday, Wednesday)
    ├── interim/             # Cache parquet hasil dedup (1.520.488 baris)
    └── LYCOS-IDS2017/       # Skrip studi pembanding LycoSTand / Rosay (2022)
```

---

## 📊 Inventaris & Status Berkas per Folder

| Folder | Jumlah Berkas | Status | Keterangan |
|---|---|---|---|
| **Dashboard/** | 4 | ✅ Aktif | Central hub, timeline, checklist, matriks E0-E5 |
| **Proposal/** | 2 | ✅ Lengkap | Briefing scope TA & referensi skripsi kakak tingkat |
| **Literatur/** | 25 md + 25 di PDFs/ | ✅ Terverifikasi | 25 paper terverifikasi 100%, 0 broken links |
| **Metodologi/** | 6 | ✅ Terverifikasi | Dokumentasi EDA 62 fitur, verifikasi & skrip bantu |
| **Eksperimen/** | 1 | ⬜ Menunggu | Alokasi pencatatan log E0-E5 (README panduan siap) |
| **Hasil/** | 1 | ⬜ Menunggu | Alokasi tabel, grafik, & perbandingan BWT (README siap) |
| **Penulisan/** | 1 | ⬜ Menunggu | Alokasi draf Bab 1-5 (README panduan siap) |
| **Bimbingan/** | 2 | ✅ Siap Paparan | Bahan paparan & panduan tanya-jawab pembimbing |
| **Keputusan/** | 4 | ✅ Terkunci | Scope CL/FL dibekukan, ringkasan pembimbing siap |
| **Aset/** | 16 file + README | ✅ Lengkap | 15 gambar/vektor diagram resmi + 1 model ONNX |
| **Laporan/** | 2 | ✅ Terkonsolidasi | Audit-Bukti aktif & Arsip-Riwayat-Sesi-Konsolidasi |
| **Arsip/** | 6 | 📦 Diarsipkan | Naskah lama, draf keputusan awal & catatan historis |
| **Templates/** | 2 | ✅ Lengkap | Template standar catatan literatur & log eksperimen |
| **Datasets/** | 3 subfolder | ✅ Siap | Data mentah & cache parquet 3 kelas |

---

## 🔒 Konvensi Teknis Baku

### 1. Fitur Dataset CIC-IDS2017 (Aturan 62 Fitur)
- **Total Kolom Mentah:** 79 kolom (78 fitur numerik + 1 kolom Label).
- **Kolom Konstan Dibuang (10 kolom zero-variance):**  
  `Bwd PSH Flags`, `Fwd URG Flags`, `Bwd URG Flags`, `CWE Flag Count`, `Fwd Avg Bytes/Bulk`, `Fwd Avg Packets/Bulk`, `Fwd Avg Bulk Rate`, `Bwd Avg Bytes/Bulk`, `Bwd Avg Packets/Bulk`, `Bwd Avg Bulk Rate`.
- **Kolom Duplikat Dibuang (5 kolom 100% identik):**  
  `Fwd Header Length.1`, `Subflow Fwd Bytes`, `Subflow Fwd Packets`, `Subflow Bwd Packets`, `SYN Flag Count`.
- **Fitur Bersih Tersisa:** **62 Fitur Unik + 1 Label** (Total 64 kolom).
- **3 Kolom Nyaris Identik (99,99%) Dicatat untuk Pertimbangan:**  
  `Avg Fwd Segment Size`, `Avg Bwd Segment Size`, `Subflow Bwd Bytes`.

### 2. Aturan Tautan Obsidian
- Penulisan tautan wajib menggunakan format nama berkas tanpa prefiks usang: `[​[Nama-Berkas]​]` (misal `[Dashboard](Dashboard/Dashboard.md)`).
- Seluruh PDF tersimpan di `Literatur/PDFs/` atau `Literatur/PDFs/Opsional/`.
- Validasi tautan dapat dijalankan sewaktu-waktu menggunakan:
  ```bash
  python Skrip/EDA/scan_vault_links.py
  ```

---

## 🔍 Akses Cepat Dokumen Kunci

| Dokumen | Lokasi | Fungsi |
|---|---|---|
| **Ringkasan untuk Pembimbing** | `Keputusan/Ringkasan-Untuk-Pembimbing.md` | Dokumen panduan utama diskusi dosen (7 pertanyaan) |
| **Dashboard Proyek** | `Dashboard/Dashboard.md` | Status timeline mingguan dan matriks |
| **Laporan EDA & Fitur** | `Metodologi/EDA-CIC-IDS2017.md` | Analisis fitur, distribusi label, & port leakage |
| **Verifikasi Literatur** | `Literatur/Crosscheck.md` | Tabel verifikasi metadata 25 paper |
| **Bukti Audit Empiris** | `Laporan/Audit-Bukti-2026-10-03.md` | Catatan eksekusi perintah dan keluaran mentah terminal |
