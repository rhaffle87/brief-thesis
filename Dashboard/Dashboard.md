---
type: dashboard
status: active
created: 2026-10-02
updated: 2026-10-06
---
# Dashboard Tugas Akhir - FL-CL IDS

**Judul:** Analisis Kinerja Deteksi Network Traffic Intrusion Menggunakan Metode Federated-Continual Learning pada Testbed Private Cloud Server

**Mahasiswa:** Rafli Alif Ihza Hartono  
**Program Studi:** Teknik Elektro, ITS  
**Pembimbing:** [Nama Dosen]  

---

## 🎯 Rumusan Masalah (FINAL)

1. **RM1:** Bagaimana performa deteksi intrusi model yang dilatih secara federated (FedAvg) dibandingkan model yang dilatih lokal pada masing-masing client dengan distribusi data non-IID?

2. **RM2:** Bagaimana pengaruh Elastic Weight Consolidation (EWC) terhadap catastrophic forgetting ketika model menerima jenis serangan baru secara sekuensial, baik pada pelatihan lokal maupun federated (FedAvg+EWC)?

---

## 🔒 TITIK PEMBEKUAN (Anti Scope Creep)

| Komponen | Keputusan Final | Dibekukan Minggu |
|----------|-----------------|------------------|
| **Dataset** | CIC-IDS2017 (3 kelas: Normal, SSH-Patator, DoS; **62 fitur unik + 1 Label**; Weighted Loss - Keep All Clean Data) | Minggu 4 (TERKUNCI) |
| **Model** | MLP only (Input: 62 → 64 → 32 → Output: 3) + Hyperparameter Tuning | Minggu 6 |
| **FL Algorithm** | FedAvg only (2 client + 1 server, Local First → Proxmox Simulation) | Minggu 10 |
| **CL Algorithm** | EWC only vs naive fine-tuning (Balanced Weighting λ) | Minggu 8 |

**Diluar Scope (Resmi Dieliminasi Pembimbing):**
- ❌ Injeksi Trafik Riil (VM 400 Hydra/Slowloris ditiadakan)
- ❌ GEM, A-GEM, LwF (Memory replay dilarang demi privasi)
- ❌ Krum, TrimmedMean, Byzantine attacks
- ❌ Differential Privacy, Secure Aggregation
- ❌ CNN, Transformer
- ❌ ONNX, MLflow, Kubernetes
- ❌ Dataset baru, fitur kustom (JA3/JA4)

---

## 📊 Matriks Eksperimen

| Kode | FL | CL | Keterangan | Status | File Output |
|------|----|----|------------|--------|-------------|
| E0 | – | – | Joint/centralized (upper bound) | ⬜ TODO | - |
| E1 | Tidak | Naive | Lokal sekuensial tanpa CL | ⬜ TODO | - |
| E2 | Tidak | EWC | Lokal sekuensial dengan EWC | ⬜ TODO | - |
| E3 | FedAvg | Naive | Federated tanpa CL | ⬜ TODO | - |
| E4 | FedAvg | EWC | **FL-CL (Target Utama Skripsi)** | ⬜ TODO | - |
| E5 | – | – | Validasi live traffic | ❌ DIELIMINASI | Injeksi trafik ditiadakan pembimbing |

**Target Seed:** 5 kali pengulangan per eksperimen (seed: 42, 43, 44, 45, 46)  
**Metrik Utama:** Macro-F1, per-class recall/F1, BWT (Backward Transfer)

**Perbandingan Inti:**
- E1 vs E2 → Efek EWC
- E1 vs E3 → Efek FL
- E3 vs E4 → Nilai tambah CL pada FL

---

## 📅 Timeline 16 Minggu

| Minggu | Target | Status | Catatan |
|--------|--------|--------|---------|
| **1-2** | Finalisasi desain, studi literatur, audit EDA, bimbingan dosen | ✅ DONE | **Keputusan Resmi Disetujui Pembimbing** |
| **3-4** | Preprocessing CIC-IDS2017, partisi client/task | 🟢 READY TO RUN | **Dataset freeze** (62 fitur, Weighted Loss, All Days 50/50) |
| **5-6** | Baseline MLP training & tuning (E0) | ⬜ TODO | Baseline valid |
| **7-8** | Naive vs EWC lokal (E1, E2) | ⬜ TODO | Forgetting selesai |
| **9-10** | FL Flower + FedAvg lokal & Proxmox (E3) | ⬜ TODO | FL berjalan |
| **11-12** | FL+EWC dan eksperimen inti (E4) | ⬜ TODO | Core selesai |
| **13** | Multi-seed aggregation (5 seeds) | ⬜ TODO | Mean ± std |
| **14** | Analisis hasil, grafik, tabel | ⬜ TODO | Draft hasil |
| **15-16** | Penulisan buku TA, revisi, sidang | ⬜ TODO | Final |

**Minggu Saat Ini:** Minggu 2 (2026-10-06)  
**Progress:** 15.0% (Tahap Keputusan Metodologi Selesai 100%)

---

## 📚 Literatur Progress

**Status:** ✅ 25/25 Paper Terverifikasi & Tersedia Lengkap (100% PDF lokal)  
**Rincian:** 13 Paper Inti (`Literatur/PDFs/`) + 12 Paper Pendukung (`Literatur/PDFs/Opsional/`)

### ✅ Paper Inti (13 Dokumen)
1. ✅ McMahan et al. (2017) - FedAvg [McMahan-2017-FedAvg](../Literatur/McMahan-2017-FedAvg.md)
2. ✅ Kirkpatrick et al. (2017) - EWC [Kirkpatrick-2017-EWC](../Literatur/Kirkpatrick-2017-EWC.md)
3. ✅ Sharafaldin et al. (2018) - CIC-IDS2017 [Sharafaldin-2018-CIC-IDS2017](../Literatur/Sharafaldin-2018-CIC-IDS2017.md)
4. ✅ Rosay et al. (2022) - LycoSTand / CIC-IDS2017 [Rosay-2022-LycoSTand](../Literatur/Rosay-2022-LycoSTand.md)
5. ✅ Dube et al. (2024) - Faulty CIC-IDS2017 [Dube-2024-Faulty-CIC-IDS2017](../Literatur/Dube-2024-Faulty-CIC-IDS2017.md)
6. ✅ Jin et al. (2024) - FL-IIDS Concept Drift [Jin-2024-FL-IIDS](../Literatur/Jin-2024-FL-IIDS.md)
7. ✅ Rehman et al. (2026) - Incremental FL-IDS [Rehman-2026-Incremental-FL-IDS](../Literatur/Rehman-2026-Incremental-FL-IDS.md)
8. ✅ Hernandez-Ramos et al. (2025) - FL-IDS Survey [Hernandez-Ramos-2025-FL-IDS-Survey](../Literatur/Hernandez-Ramos-2025-FL-IDS-Survey.md)
9. ✅ Buyuktanir et al. (2025) - FL-IDS non-IID [Buyuktanir-2025-FL-IDS-nonIID](../Literatur/Buyuktanir-2025-FL-IDS-nonIID.md)
10. ✅ Hamedi et al. (2025) - FCL Survey [Hamedi-2025-FCL-Survey](../Literatur/Hamedi-2025-FCL-Survey.md)
11. ✅ Gholizade et al. (2026) - FCL Survey [Gholizade-2026-FCL-Survey](../Literatur/Gholizade-2026-FCL-Survey.md)
12. ✅ Beutel et al. (2020) - Flower Framework [Beutel-2020-Flower](../Literatur/Beutel-2020-Flower.md)
13. ✅ Lopez-Paz & Ranzato (2017) - GEM [Lopez-Paz-2017-GEM](../Literatur/Lopez-Paz-2017-GEM.md)

### 📂 Paper Pendukung / Framework (Opsional - 12 Dokumen)
14. 📂 Carta et al. (2023) - Avalanche JMLR [Carta-2023-Avalanche-JMLR](../Literatur/Carta-2023-Avalanche-JMLR.md)
15. 📂 Lomonaco et al. (2021) - Avalanche CVPRW [Lomonaco-2021-Avalanche-CVPRW](../Literatur/Lomonaco-2021-Avalanche-CVPRW.md)
16. 📂 Liu & Chang (2026) - EWC-DR [Liu-2026-EWC-DR](../Literatur/Liu-2026-EWC-DR.md)
17. 📂 Agrawal et al. (2021) - FL-IDS Concepts [Agrawal-2021-FL-IDS-Concepts](../Literatur/Agrawal-2021-FL-IDS-Concepts.md)
18. 📂 Talpur et al. (2022) - GFCL [Talpur-2022-GFCL](../Literatur/Talpur-2022-GFCL.md)
19. 📂 Engelen et al. (2021) - Troubleshooting CICIDS2017 [Engelen-2021-Troubleshooting](../Literatur/Engelen-2021-Troubleshooting.md)
20. 📂 Zhao et al. (2018) - FL with Non-IID Data [Zhao-2018-FL-NonIID](../Literatur/Zhao-2018-FL-NonIID.md)
21. 📂 Hsu et al. (2019) - Non-IID Dirichlet [Hsu-2019-NonIID-Dirichlet](../Literatur/Hsu-2019-NonIID-Dirichlet.md)
22. 📂 Li et al. (2020) - FedProx [Li-2020-FedProx](../Literatur/Li-2020-FedProx.md)
23. 📂 De Lange et al. (2021) - Continual Learning Survey [DeLange-2021-CL-Survey](../Literatur/DeLange-2021-CL-Survey.md)
24. 📂 van de Ven & Tolias (2019) - Three Scenarios for CL [VandeVen-2019-CL-Scenarios](../Literatur/VandeVen-2019-CL-Scenarios.md)
25. 📂 Wang et al. (2023) - Comprehensive Survey of CL [Wang-2023-CL-Survey](../Literatur/Wang-2023-CL-Survey.md)

---

## 🗂️ Struktur Vault

```
E:\Projects\thesis/
├── Dashboard/          # Central hub, timeline, checklist, matriks
├── Proposal/           # Briefing proposal TA & referensi skripsi
├── Literatur/          # Catatan per paper & PDFs/ (18 file PDF)
├── Metodologi/         # Desain dataset, analisis EDA, verifikasi fitur
├── Eksperimen/         # Log eksperimen E0-E5 per seed
├── Hasil/              # Tabel, grafik, visualisasi metrik
├── Penulisan/          # Draf skripsi Bab 1-5
├── Bimbingan/          # Log & notula bimbingan dosen
├── Keputusan/          # Dokumen keputusan & ringkasan untuk pembimbing
├── Aset/               # Diagram alur & arsitektur testbed
├── Laporan/            # Laporan audit & log sesi (lama: SUPERSEDED)
├── Arsip/              # Naskah lama (manuscript, preliminary study)
├── Templates/          # Template catatan literatur & eksperimen
└── Datasets/           # CIC-IDS2017 raw CSVs & interim parquet
```

---

## ⚠️ Risiko & Mitigasi

| Risiko | Dampak | Mitigasi | Status |
|--------|--------|----------|--------|
| Dataset freeze tertunda | Timeline mundur | Gunakan subset CIC-IDS2017 (Monday, Tuesday, Wednesday) | ✅ Terkunci |
| Proxmox infrastruktur bermasalah | E3-E4 gagal | Fallback Docker lokal / standalone VM | ✅ Siap |
| EWC tidak mengurangi forgetting | Hasil negatif | Hasil perbandingan tetap valid secara ilmiah | ✅ Diterima |
| Scope creep (GEM, Byzantine, DP) | Timeline overrun | 4 titik pembekuan ditegakkan ketat | ✅ Terkunci |

---

## 📝 Quick Links

- [Ringkasan-Untuk-Pembimbing](../Keputusan/Ringkasan-Untuk-Pembimbing.md) (7 pertanyaan & bukti untuk dosen pembimbing)
- [Briefing-Scope-TA](../Proposal/Briefing-Scope-TA.md) (Dokumen final scope TA)
- [EDA-CIC-IDS2017](../Metodologi/EDA-CIC-IDS2017.md) (Laporan lengkap EDA & port leakage test)
- [Crosscheck](../Literatur/Crosscheck.md) (Tabel verifikasi metadata 18 paper)
- [Timeline-16-Minggu](Timeline-16-Minggu.md) (Jadwal detail 16 minggu)
- [Checklist-Selesai](Checklist-Selesai.md) (Definisi selesai per fase)
- [Matriks-E0-E5](Matriks-E0-E5.md) (Rincian matriks eksperimen)

---

## 📊 Statistik

**Created:** 2026-10-02  
**Last Updated:** 2026-10-04  
**Days Until Week 4 Freeze:** ~8 days  
**Days Until Final Submission:** ~110 days
