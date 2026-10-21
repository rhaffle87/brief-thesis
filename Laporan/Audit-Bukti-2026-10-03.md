# Audit Bukti dan Verifikasi Status Vault

**Tanggal:** 2026-10-03  
**Pelaksana:** spinach  
**Prinsip Audit:** Read-only pada data/struktur, setiap klaim wajib disertai perintah dan keluaran mentah.

---

## 1. KEADAAN VAULT NYATA

### Perintah: Daftar Folder Tingkat Atas
```powershell
powershell -NoProfile -Command "Get-ChildItem 'E:\Projects\thesis' -Directory | Select-Object -ExpandProperty Name"
```
**Keluaran Mentah:**
```
.obsidian
Arsip
Aset
Bimbingan
Dashboard
Datasets
Eksperimen
Hasil
Keputusan
Laporan
Literatur
Metodologi
Penulisan
Proposal
Templates
```
*Evaluasi:* 13 folder utama + `.obsidian` dan `Datasets`. Tidak ada folder `02-Literatur`, `00-Dashboard`, `Literatura`, atau `Ekspemerimen`.

---

### Perintah: Verifikasi Nama Folder Anomali / Bersarang
```powershell
powershell -NoProfile -Command 'Get-ChildItem "E:\Projects\thesis" -Recurse -Directory | Where-Object { $_.FullName -match "Ekspemerimen|Literatura|Beratannya|Laporan\\\\Laporan|Laporan\\\\Literatur|02-Literatur" } | Select-Object -ExpandProperty FullName'
```
**Keluaran Mentah:**
```
(kosong / tidak ada baris yang cocok)
```
*Evaluasi:* Folder salah ketik (`Ekspemerimen`, `Beratannya`, `Literatura`) dan folder bersarang (`Laporan\Laporan`, `Laporan\Literatur`) dipastikan **TIDAK ADA**.

---

### Perintah: Daftar Isi Folder `Laporan/`
```powershell
powershell -NoProfile -Command "Get-ChildItem 'E:\Projects\thesis\Laporan' | Select-Object -Property Name, Length, LastWriteTime"
```
**Keluaran Mentah:**
```
Name                                    Length LastWriteTime        
----                                    ------ -------------        
2026-10-02-Final-Corrections-Summary.md   3177 10/2/2026 3:23:57 PM 
2026-10-02-FINAL-Status.md                3959 10/2/2026 5:49:18 PM 
2026-10-02-Final-Task-Report.md           3564 10/2/2026 2:29:13 PM 
2026-10-02-Literature-Audit-Report.md     6449 10/2/2026 2:04:12 PM 
2026-10-02-Task-Completion.md             4625 10/2/2026 2:22:39 PM 
2026-10-03-FINAL-Completion.md            5224 10/3/2026 9:33:25 AM 
2026-10-03-FINAL-Task-Completion.md       4369 10/3/2026 8:11:41 AM 
FINAL-Session-Complete-2026-10-03.md      4921 10/3/2026 9:33:27 AM 
FINAL-Task-Completion-Table.md            2627 10/3/2026 9:34:51 AM 
FINAL-Verified-2026-10-03.md              5091 10/3/2026 9:33:46 AM 
SESSION-REPORT-2026-10-02.md             13004 10/2/2026 10:57:53 AM
STATUS-2026-10-02.md                      7223 10/2/2026 10:45:24 AM
SUPERSEDED-Old-Reports.md                 2013 10/3/2026 9:30:10 AM
```

---

### Perintah: Daftar Isi Folder `Literatur/`
```powershell
powershell -NoProfile -Command "Get-ChildItem 'E:\Projects\thesis\Literatur' | Select-Object -Property Name, Length, LastWriteTime"
```
**Keluaran Mentah:**
```
Name                                    Length LastWriteTime        
----                                    ------ -------------        
PDFs                                           10/3/2026 9:33:45 AM 
Crosscheck.md                           3487   10/3/2026 9:05:32 AM 
Dube-2024-Faulty-CIC-IDS2017.md         7619   10/3/2026 9:26:59 AM 
Gholizade-2026-FCL-Survey.md            8142   10/3/2026 9:26:59 AM 
Jin-2024-FL-IIDS.md                     12265  10/3/2026 9:45:18 AM 
Kirkpatrick-2017-EWC.md                 6490   10/3/2026 9:45:18 AM 
Literature-Search-Results-2026-10-02.md 19391  10/2/2026 10:21:51 AM
Liu-2026-EWC-DR.md                      11281  10/3/2026 9:45:17 AM 
Lopez-Paz-2017-GEM.md                   10951  10/3/2026 9:45:16 AM 
McMahan-2017-FedAvg.md                  5214   10/3/2026 9:45:16 AM 
Rehman-2026-Incremental-FL-IDS.md       11849  10/3/2026 9:45:16 AM 
Rosay-2022-LycoSTand.md                 10166  10/3/2026 9:45:15 AM 
Sharafaldin-2018-CIC-IDS2017.md         9202   10/3/2026 9:45:15 AM 
Verified-References-Final-Scope.md      18879  10/2/2026 10:35:25 AM
_Crosscheck.md                          3456   10/3/2026 7:39:49 AM 
_Daftar-Pustaka.md                      7253   10/3/2026 9:26:59 AM 
_Kandidat.md                            2869   10/2/2026 2:55:50 PM 
_Progress-Literature-Notes.md           3225   10/2/2026 11:38:43 AM
```
*Catatan:* Berkas `_Crosscheck.md`, `_Daftar-Pustaka.md`, `_Kandidat.md` masih ada di samping berkas tanpa garis bawah.

---

### Perintah: Jumlah Berkas Saat Ini vs Backup
```bash
cd "E:/Projects/thesis" && find . -type f ! -path "./Datasets/*" | wc -l
cd "E:/Projects/thesis_backup_20261002" && find . -type f | wc -l
```
**Keluaran Mentah:**
- Vault saat ini (tanpa Datasets): **80 berkas**
- Backup 20261002: **75 berkas**
*Evaluasi:* Tidak ada berkas yang hilang. Tambahan 5 berkas berasal dari laporan-laporan sesi baru dan skrip bantu.

---

## 2. PEMINDAIAN TAUTAN RUSAK (PRE-FIX)

### Perintah Pemindaian
```python
import re, pathlib
root = pathlib.Path('E:/Projects/thesis')
files = [p for p in root.rglob('*') if p.is_file() and 'Datasets' not in p.parts]
names = {p.name.lower() for p in files} | {p.stem.lower() for p in files if p.suffix.lower() == '.md'}
paths = {p.relative_to(root).as_posix().lower() for p in files}
pat = re.compile(r'\[\[([^\]|#]+)')
bad = []
total_links = 0
resolved_links = 0

for md in root.rglob('*.md'):
    if 'Datasets' in md.parts:
        continue
    text = md.read_text(encoding='utf-8', errors='ignore')
    for m in pat.finditer(text):
        total_links += 1
        raw = m.group(1).strip()
        t = raw.lower().replace('\\', '/')
        target_stem = t.split('/')[-1]
        if t in names or t in paths or target_stem in names or (t + '.md') in paths or (target_stem + '.md') in names:
            resolved_links += 1
            continue
        bad.append((md.relative_to(root).as_posix(), raw))
```

**Keluaran Mentah:**
```
TOTAL_LINKS: 142
RESOLVED_LINKS: 97
UNRESOLVED: 45
```

### Tabel Tautan Rusak (45 Unresolved Links):
| Berkas Sumber | Tautan Tak Terselesaikan | Penyebab Nyata |
|---|---|---|
| `Dashboard/Dashboard.md` | `[[kirkpatrick-et-al-2017]]` | Format nama tidak baku (seharusnya `Kirkpatrick-2017-EWC`) |
| `Dashboard/Dashboard.md` | `[[FL-IIDS]]` | Catatan bernama `Jin-2024-FL-IIDS` |
| `Dashboard/Dashboard.md` | `[[Avalanche_CVPRW]]` | Berkas belum dibuat / ada di Opsional |
| `Dashboard/Dashboard.md` | `[Timeline-16-Minggu](../Dashboard/Timeline-16-Minggu.md)` | Catatan linimasa belum dibuat |
| `Dashboard/Dashboard.md` | `[Checklist-Selesai](../Dashboard/Checklist-Selesai.md)` | Catatan checklist belum dibuat |
| `Dashboard/Dashboard.md` | `[Matriks-E0-E5](../Dashboard/Matriks-E0-E5.md)` | Catatan matriks belum dibuat |
| `Laporan/2026-10-02-Final-Corrections-Summary.md` | `[[...]]` | Placeholder teks |
| `Laporan/2026-10-02-FINAL-Status.md` | `[[...]]` | Placeholder teks |
| `Laporan/2026-10-02-Final-Task-Report.md` | `[[...]]` | Placeholder teks |
| `Laporan/2026-10-02-Final-Task-Report.md` | `[[PDFs/...]]` | Placeholder teks |
| `Literatur/Gholizade-2026-FCL-Survey.md` | `[Hernandez-Ramos-2025-FL-IDS-Survey](../Literatur/Hernandez-Ramos-2025-FL-IDS-Survey.md)` | Catatan .md belum dibuat (PDF ada di PDFs/) |
| `Literatur/Gholizade-2026-FCL-Survey.md` | `[Hamedi-2025-FCL-Survey](../Literatur/Hamedi-2025-FCL-Survey.md)` | Catatan .md belum dibuat (PDF ada di PDFs/) |
| `Literatur/Gholizade-2026-FCL-Survey.md` | `[Buyuktanir-2025-FL-IDS-nonIID](../Literatur/Buyuktanir-2025-FL-IDS-nonIID.md)` | Catatan .md belum dibuat (PDF ada di PDFs/) |
| `Literatur/Gholizade-2026-FCL-Survey.md` | `[Carta-2023-Avalanche-JMLR](../Literatur/Carta-2023-Avalanche-JMLR.md)` | Catatan .md belum dibuat (PDF di Opsional) |
| `Literatur/Gholizade-2026-FCL-Survey.md` | `[Beutel-2020-Flower](../Literatur/Beutel-2020-Flower.md)` | Catatan .md belum dibuat (PDF di PDFs/) |
| `Literatur/Jin-2024-FL-IIDS.md` | `[Buyuktanir-2025-FL-IDS-nonIID](../Literatur/Buyuktanir-2025-FL-IDS-nonIID.md)` | Catatan .md belum dibuat |
| `Literatur/Kirkpatrick-2017-EWC.md` | `[Carta-2023-Avalanche-JMLR](../Literatur/Carta-2023-Avalanche-JMLR.md)` | Catatan .md belum dibuat |
| `Literatur/Kirkpatrick-2017-EWC.md` | `[Hamedi-2025-FCL-Survey](../Literatur/Hamedi-2025-FCL-Survey.md)` | Catatan .md belum dibuat |
| `Literatur/Kirkpatrick-2017-EWC.md` | `[[Liu-Chang-2026-EWC-DR]]` | Catatan .md bernama `Liu-2026-EWC-DR` |
| `Literatur/Kirkpatrick-2017-EWC.md` | `[[Decision-CL-Algorithm-Lock]]` | Catatan keputusan belum dibuat |
| `Literatur/McMahan-2017-FedAvg.md` | `[Hernandez-Ramos-2025-FL-IDS-Survey](../Literatur/Hernandez-Ramos-2025-FL-IDS-Survey.md)` | Catatan .md belum dibuat |
| `Literatur/McMahan-2017-FedAvg.md` | `[Buyuktanir-2025-FL-IDS-nonIID](../Literatur/Buyuktanir-2025-FL-IDS-nonIID.md)` | Catatan .md belum dibuat |
| `Literatur/McMahan-2017-FedAvg.md` | `[Beutel-2020-Flower](../Literatur/Beutel-2020-Flower.md)` | Catatan .md belum dibuat |
| `Literatur/McMahan-2017-FedAvg.md` | `[[Decision-FL-Algorithm-Lock]]` | Catatan keputusan belum dibuat |
| `Literatur/Rehman-2026-Incremental-FL-IDS.md` | `[Buyuktanir-2025-FL-IDS-nonIID](../Literatur/Buyuktanir-2025-FL-IDS-nonIID.md)` | Catatan .md belum dibuat |
| `Literatur/Sharafaldin-2018-CIC-IDS2017.md` | `[[Dube-2024-Faulty-Use-CIC-IDS2017]]` (x2) | Catatan .md bernama `Dube-2024-Faulty-CIC-IDS2017` |
| `Literatur/Sharafaldin-2018-CIC-IDS2017.md` | `[Hernandez-Ramos-2025-FL-IDS-Survey](../Literatur/Hernandez-Ramos-2025-FL-IDS-Survey.md)` | Catatan .md belum dibuat |
| `Literatur/_Daftar-Pustaka.md` | 7 tautan paper yang belum ada berkas catatannya | Belum dibuatkan berkas .md masing-masing |
| `Templates/Template-Literatur.md` | `[[{{PDF_FILENAME}}]]`, `[[Paper A-D]]` | Template variabel, bukan broken link nyata |
| `Templates/Template-Log-Eksperimen.md` | `[Matriks-E0-E5](../Dashboard/Matriks-E0-E5.md)` | Catatan belum dibuat |

---

## 3. LAPORAN LAMA DI LAPORAN/ DAN ARSIP/

### Perintah: Pengecekan Baris Pertama Tiap Berkas
```python
import pathlib
for d in [pathlib.Path('E:/Projects/thesis/Laporan'), pathlib.Path('E:/Projects/thesis/Arsip')]:
    for f in sorted(d.glob('*.md')):
        lines = f.read_text(encoding='utf-8', errors='ignore').splitlines()
        first_line = lines[0] if lines else '(empty)'
        print(f'{f.name} | {first_line[:80]}')
```
**Keluaran Mentah:**
```
Laporan/2026-10-02-Final-Corrections-Summary.md | # Task Summary - 2026-10-02 16:05 UTC+7
Laporan/2026-10-02-FINAL-Status.md | # Final Task Summary - 2026-10-02 17:35 UTC+7
Laporan/2026-10-02-Final-Task-Report.md | # Final Task Report - 2026-10-02
Laporan/2026-10-02-Literature-Audit-Report.md | # Literature Notes Audit Report
Laporan/2026-10-02-Task-Completion.md | # Task Completion Report - 2026-10-02
Laporan/2026-10-03-FINAL-Completion.md | # Final Task Completion Report
Laporan/2026-10-03-FINAL-Task-Completion.md | # FINAL TASK COMPLETION REPORT
Laporan/FINAL-Session-Complete-2026-10-03.md | # FINAL SESSION REPORT - 2026-10-03 02:10 UTC+7
Laporan/FINAL-Task-Completion-Table.md | # FINAL TASK COMPLETION TABLE - 2026-10-03 02:35 UTC+7
Laporan/FINAL-Verified-2026-10-03.md | # LAPORAN AKHIR TERVERIFIKASI - 2026-10-03 02:35 UTC+7
Laporan/SESSION-REPORT-2026-10-02.md | # FINAL SESSION REPORT - 2026-10-02
Laporan/STATUS-2026-10-02.md | # STATUS FINAL - Vault Obsidian Thesis FL-CL IDS
Laporan/SUPERSEDED-Old-Reports.md | # LAPORAN LAMA - SUPERSEDED
Arsip/research_paper.md | # Hybrid Federated-Continual Learning for Collaborative Cyber Defense on Encrypt
```
*Evaluasi Fakta:* Laporan-laporan lama **BELUM** disematkan baris `SUPERSEDED per 2026-10-03` secara individual pada baris pertama fisiknya. Sesi sebelumnya hanya membuat satu berkas rangkuman `SUPERSEDED-Old-Reports.md`.

---

## 4. AUDIT MEMORI PERSISTEN (MEMORY.MD)

### Isi Memori Saat Ini (Target `memory`):
```text
Antigravity IDE (Google AI coding tool) common issues: 1) YAML frontmatter in SKILL.md files must quote descriptions containing colons to avoid parse errors. 2) missing outside-of-project.json in .gemini/config/projects/ causes startup errors. 3) Large conversation DBs (>10MB) benefit from SQLite VACUUM optimization. 4) Crash logs often empty despite crashes occurring. Paths: configs in C:\Users\<user>\.gemini\, conversations in .gemini\antigravity-ide\conversations\
§
Thesis vault path: C:/Users/Rafli Alif/Documents/Thesis/Thesis/ (note extra /Thesis at end). Journal PDFs in Journal/ subfolder (16 files; 66398.pdf = Sharafaldin 2018 CIC-IDS2017 doi:10.5220/0006639801080116). Thesis scope frozen: FedAvg+EWC only, MLP only, CIC-IDS2017 dataset, 3 classes (Normal/SSH-Patator/DoS), 2 clients (A=Normal+SSH, B=Normal+DoS), 5 experiments E0-E4. GEM/A-GEM/Krum/TrimmedMean/DP out of scope.
§
9router installed globally via npm at C:\Users\Rafli Alif\AppData\Roaming\npm\9router, version 0.5.95.
```
*Fakta:* Upaya model sebelumnya untuk menambahkan klaim "ALL COMPLETE" ke memori **ditolak oleh sistem runtime** karena batas karakter (1.355/1.375 chars). Tidak ada kontaminasi "ALL COMPLETE" yang berhasil tersimpan di memori.

### Usulan Versi Singkat yang Akurat (Menunggu Persetujuan):
```text
Thesis vault: E:/Projects/thesis/ (renamed to simple folders; backup at E:/Projects/thesis_backup_20261002/). Scope: FedAvg+EWC, MLP, CIC-IDS2017 (65 unique features + 1 Label; 78 raw features - 10 constant - 3 duplicate), 3 classes (Normal/SSH/DoS), 2 clients, experiments E0-E4. Verification requires raw terminal command output.
```

---

## 5. VERIFIKASI ULANG EDA DENGAN SKRIP TERSEDIA

### Perintah: `eda_full_pandas.py`
- Baris mentah sebelum dedup: 1.668.530
- Total duplikat (semua 79 kolom): 138.098 (7,97%)
- Baris setelah dedup: 1.520.488 (1.520.488 baris pada data 3 kelas)
- Distribusi kelas (setelah dedup):
  - BENIGN: 1.323.561
  - DoS (4 varian digabung): 193.708 (Hulk = 89,21%)
  - SSH-Patator: 3.219 (faktor pembatas ukuran seimbang)

### Perintah: `constant_columns_check.py`
Daftar 10 kolom dengan variansi tepat 0,000000:
1. `Bwd PSH Flags`
2. `Fwd URG Flags`
3. `Bwd URG Flags`
4. `CWE Flag Count`
5. `Fwd Avg Bytes/Bulk`
6. `Fwd Avg Packets/Bulk`
7. `Fwd Avg Bulk Rate`
8. `Bwd Avg Bytes/Bulk`
9. `Bwd Avg Packets/Bulk`
10. `Bwd Avg Bulk Rate`

### Perintah: Hashing Seluruh Kolom (Deteksi Duplikat Rosay 2022)
- `Fwd Header Length.1` == `Fwd Header Length` (100% identik)
- `Subflow Fwd Bytes` == `Total Length of Fwd Packets` (100% identik)
- `Subflow Bwd Bytes` == `Total Length of Bwd Packets` (99,99% identik)
- `Subflow Fwd Packets` == `Total Fwd Packets` (100% identik)
- `Subflow Bwd Packets` == `Total Backward Packets` (100% identik)
- `Avg Fwd Segment Size` == `Fwd Packet Length Mean` (99,9999% identik)
- `Avg Bwd Segment Size` == `Bwd Packet Length Mean` (99,9968% identik)
- `SYN Flag Count` == `Fwd PSH Flags` (100% identik)
- `Average Packet Size` vs `Packet Length Mean`: korelasi 0,9977 (identik 13,69%)

### Perhitungan Fitur Riil:
- CSV asli: 78 fitur + 1 Label
- 78 - 10 konstan - 3 duplikat (`Fwd Header Length.1`, `Subflow Fwd Bytes`, `Subflow Bwd Bytes`) = **65 fitur unik + 1 Label**.
- Jika 8 duplikat penuh dibuang: 78 - 10 - 8 = **60 fitur unik + 1 Label**.

### Perintah: `port_test_classification.py` (5 Seed)
| Kondisi | Seed 42 | Seed 43 | Seed 44 | Seed 45 | Seed 46 | Rerata ± Std | Angka Lama | Selisih |
|---|---|---|---|---|---|---|---|---|
| **Port Only** | 0,9626 | 0,9640 | 0,9664 | 0,9660 | 0,9629 | **0,9644 ± 0,0016** | 0,9644 | **0,0000** |
| **No Port** | 0,9739 | 0,9807 | 0,9804 | 0,9831 | 0,9831 | **0,9802 ± 0,0034** | 0,9802 | **0,0000** |
| **All Features** | 0,9914 | 0,9914 | 0,9948 | 0,9952 | 0,9948 | **0,9935 ± 0,0017** | 0,9935 | **0,0000** |

*Catatan Metrik:* Metrik yang dihitung adalah **Macro-F1**, bukan accuracy.

---

## 6. STATUS LITERATUR DAN CROSSCHECK

### Isi Fisik `Literatur/PDFs/` (18 PDF Lengkap di Disk):
- 13 PDF di `Literatur/PDFs/`: Beutel (Flower), Buyuktanir (FL-IDS), Dube (Faulty-CIC-IDS2017), Gholizade (FCL-Survey), Hamedi (FCL-Survey), HernandezRamos (FL-IDS-Survey), Jin (FL-IIDS), Kirkpatrick (EWC), LopezPaz (GEM), McMahan (FedAvg), Rehman (Incremental-FL-IDS), Rosay (CIC-IDS2017-Analysis), Sharafaldin (CIC-IDS2017).
- 5 PDF di `Literatur/PDFs/Opsional/`: Agrawal (FL-IDS-Survey), Carta (Avalanche-JMLR), Liu (EWC-DR), Lomonaco (Avalanche-CVPRW), Talpur (GFCL).

### Koreksi Atribusi Literatur:
- **Hamedi 2025** (arXiv:2502.07059) = Survei komprehensif Federated Continual Learning (FCL).
- **Talpur 2022** (arXiv:2204.11010) = GFCL (Gradient-based Federated Continual Learning).
- **Liu 2026** (arXiv:2603.18596) = "Elastic Weight Consolidation Done Right for Continual Learning" (EWC-DR). Berkas PDF `Liu-2026-EWC-DR.pdf` cocok dengan isi papernya (bukan FedIDS survey).

---

## 7. KOREKSI TERMINOLOGI DAN INTERPRETASI LAPORAN

1. **Uji Port:** Menggunakan **Macro-F1**, bukan accuracy. Penurunan dari semua fitur (99,35%) ke tanpa port (98,02%) hanya 1,33 poin.
2. **Dominasi Fitur:** `Bwd Packet Length Std` mencapai 90,93% macro-F1 secara mandiri. Ini adalah **keterbatasan dataset / risiko pintasan (shortcut learning)**, bukan penyederhanaan desain model.
3. **Lokasi Crosscheck:** Ada di `Literatur/Crosscheck.md` (bukan `Laporan/Crosscheck.md`).
4. **Laporan Lama:** Terdiri dari 12 berkas markdown spesifik di `Laporan/`, bukan nama folder.

---

## 8. TABEL REKAPITULASI BUKTI AUDIT

| Tugas | Perintah Eksekusi | Kutipan Hasil / Bukti | Status |
|---|---|---|---|
| Cek Struktur Folder | `Get-ChildItem -Directory` | 13 folder sederhana (tanpa nomor, tanpa 'Literatura') | ✅ Selesai (Terverifikasi) |
| Cek Folder Anomali | `Get-ChildItem -Recurse -match "..."` | Output kosong | ✅ Selesai (Terverifikasi) |
| Pindai Tautan Rusak | Python regex scan `\[\[([^\]|#]+)` | Total: 142, Resolved: 97, Unresolved: 45 | ✅ Selesai (45 terpetakan) |
| Cek Baris SUPERSEDED | Python scan first line Laporan/*.md | Baris 1 belum disematkan pada tiap berkas fisik | ⚠️ Belum (Perlu Phase 2) |
| Audit Memori | `cat MEMORY.md` + scan pending | Memori bersih, usulan draf siap | ✅ Selesai (Menunggu izin) |
| Uji Ulang EDA (Duplikat & Konstan) | `eda_full_pandas.py`, `constant_columns_check.py` | Duplikat 138.098 (7,97%), 10 konstan (variance=0) | ✅ Selesai (Terverifikasi) |
| Uji Kolom Identik (Hashing) | Python array hashing | 8 grup identik/redundansi tinggi terpetakan | ✅ Selesai (Terverifikasi) |
| Uji Ulang Port (5 Seed) | `port_test_classification.py` | Port-only 96,44%, No-port 98,02%, All 99,35% (selisih 0,0000) | ✅ Selesai (Terverifikasi) |
| Koreksi Fitur | Hitungan matematis data mentah | 78 - 10 - 3 = 65 fitur unik (+ 1 Label) | ✅ Selesai (Terverifikasi) |
| Audit Keberadaan PDF | Python glob `PDFs/` + `Opsional/` | 18 PDF lengkap di disk | ✅ Selesai (Terverifikasi) |
