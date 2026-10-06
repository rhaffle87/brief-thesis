# Keputusan Metodologi untuk Pembimbing

**Last Updated:** 2026-10-02 14:45 UTC+7  
**Status:** MENUNGGU PERSETUJUAN PEMBIMBING

**Based on:** Full EDA (1.67M rows scanned), Scope TA (3 kelas, FedAvg+EWC), Rosay 2022 bugs

---

## 🎯 4 KEPUTUSAN KRITIS (Perlu Diskusi Pembimbing)

### KEPUTUSAN 1: Versi Dataset

**Pilihan:**
- **A) CIC-IDS2017 Original** (79 kolom = 78 fitur + 1 Label; 63 fitur unik setelah eliminasi 10 konstan dan 5 identik, bug terdokumentasi)
- **B) LYCOS-IDS2017 Corrected** (83 fitur, bug diperbaiki)

**Perbandingan:**

| Aspek | CIC Original | LYCOS Corrected |
|-------|--------------|-----------------|
| **Jumlah fitur** | 78 (63 fitur unik setelah filtering) | 83 |
| **Bug features** | 34 fitur (Rosay 2022) | Diperbaiki |
| **Kolom duplikat** | 4 fitur | 0 |
| **Literatur** | Banyak (basis perbandingan) | Jarang (sulit compare) |
| **E5 live traffic** | CICFlowMeter (standard) | LycoSTand (khusus) |
| **Transparensi** | Cite Rosay+Dube, akui bugs | Clean tapi kurang literatur |

**Usulan:** **CIC-IDS2017 Original** dengan transparansi penuh (cite Rosay 2022, dokumentasi bugs, fokus comparative analysis bukan absolute accuracy)

**Alasan:**
1. Lebih banyak paper pakai CIC → baseline comparison lebih mudah
2. Rosay 2022 + Dube 2024 provide transparency framework
3. E5 live traffic pakai CICFlowMeter (tool standard)
4. Bug terdokumentasi → bisa di-cite, tidak melanggar research integrity

---

### KEPUTUSAN 2: Pemilihan Normal untuk Task 1 dan Task 2

**Masalah:** 1.4M Normal harus dipartisi untuk dua task. Bagaimana cara split supaya tidak belajar pola hari?

**Pilihan:**

**A) Random Split 50/50 dari All Days**
- Mix Monday + Tuesday + Wednesday Normal
- Split acak → 50% Task 1, 50% Task 2
- **Pro:** Hindari day-of-week bias
- **Con:** Less realistic (Normal asli tidak bercampur antar hari)

**B) Tuesday Normal → Task 1, Wednesday Normal → Task 2**
- Task 1: Tuesday Normal (432K) + SSH
- Task 2: Wednesday Normal (440K) + DoS
- **Pro:** Temporal realism
- **Con:** Model bisa belajar pola hari (time features, flow patterns per day)

**C) Monday-only Normal, Split Acak**
- Pakai hanya Monday Normal (529K) untuk both tasks
- **Pro:** Pure normal, no attack contamination
- **Con:** Tuesday/Wednesday Normal (872K) terbuang

**Usulan:** **Pilihan A (Random split all days)** 

**Alasan:**
1. Scope fokus pada "non-IID + forgetting", bukan "temporal drift"
2. Hindari confound: apakah model belajar attack pattern atau day pattern?
3. Random split preserve distribusi tanpa bias temporal

---

### KEPUTUSAN 3: Komposisi Kelas DoS

**Hasil EDA:**
- DoS Hulk: 231,073 (91.5% dari DoS)
- DoS GoldenEye: 10,293 (4.1%)
- DoS slowloris: 5,796 (2.3%)
- DoS Slowhttptest: 5,499 (2.2%)

**Pilihan:**

**A) Keep As-Is (Hulk-Dominated)**
- Merge 4 varian jadi satu label "DoS"
- Distribusi asli: Hulk 91.5%, others 8.5%
- **Pro:** Realistic, cukup sampel semua varian
- **Con:** "DoS" praktis = Hulk saja

**B) Balance 4 Variants (Sample 5.5K Each)**
- Sample 5,499 dari tiap varian (match terkecil)
- Total DoS: 22K (balanced)
- **Pro:** Representasi semua subtipe equal
- **Con:** Lose 230K Hulk samples, less realistic

**Usulan:** **Pilihan A (Keep as-is)**

**Alasan:**
1. Distribusi realistis (Hulk dominan di real attacks)
2. Cukup sampel untuk semua varian (>5K each)
3. Total DoS 252K adequate untuk training
4. Scope tidak specify "balanced DoS subtypes"

---

### KEPUTUSAN 4: Metode Handling Class Imbalance

**Distribusi setelah exclude FTP + Heartbleed:**
- Normal: 1,402,023 (84.5%)
- DoS: 252,661 (15.2%)
- SSH: 5,897 (0.4%)
- **Ratio:** 238:43:1

**Pilihan:**

**A) Undersample to SSH Level (~6K each)**
- Normal: 1.4M → 6K (loss 99.6%)
- DoS: 252K → 6K (loss 97.6%)
- SSH: 5.9K → keep all
- **Total:** 18K rows (loss 98.9% data!)
- **Pro:** Perfect balance
- **Con:** Massive data loss, SSH distribusi tidak representatif

**B) Undersample to Moderate Level (50K each)**
- Normal: 1.4M → 50K (loss 96.4%)
- DoS: 252K → 50K (loss 80.2%)
- SSH: 5.9K → 5.9K or augment
- **Total:** 105.9K rows (loss 93.6%)
- **Pro:** Better balance, less extreme loss
- **Con:** Still lose banyak data

**C) Weighted Loss (Keep All Data)**
- Keep full distribution
- Loss function dengan class weights:
  - Normal: weight = 0.0007
  - DoS: weight = 0.004
  - SSH: weight = 0.17
- **Total:** 1.66M rows (no data loss)
- **Pro:** Preserve all data, standard practice
- **Con:** Model bisa bias ke majority jika weight kurang tepat

**Usulan:** **Pilihan C (Weighted loss)**

**Alasan:**
1. Briefing Scope: "batas maksimum ±10 ribu flow per kelas" adalah **batas atas**, bukan **target balance**
2. Weighted loss standard untuk severe imbalance
3. Preserve semua data → better generalization
4. Scope metrics = **macro-F1** (already handles imbalance better than accuracy)
5. Tuning class weights part of hyperparameter optimization

---

## 📝 DEFAULT YANG DIUSULKAN (Bukan Keputusan, Justifikasi Sudah Jelas)

### 1. Eksklusi Otomatis (Scope 3 Kelas)
- ❌ **FTP-Patator:** 7,938 rows - Di luar 3 kelas (Normal, SSH, DoS)
- ❌ **Heartbleed:** 11 rows - Terlalu sedikit, tidak cukup untuk training/testing

**Justifikasi:** Scope locked "3 kelas: Normal, SSH-Patator, DoS". FTP dan Heartbleed di luar scope.

### 2. Duplicate Removal
- **Duplicate rows:** 263,252 (15.8%) - Remove semua
- **Duplicate column:** 'Fwd Header Length' muncul 2x - Remove 1

**Justifikasi:** Duplikat inflate metrics, standard practice remove before training.

### 3. Feature Selection
- **Target:** 20-30 fitur (dari 79)
- **Method:** 
  1. Remove 4 Rosay-identified duplicates
  2. Remove high-NaN columns (>50% missing)
  3. Correlation analysis (remove high inter-feature correlation >0.95)
  4. Domain knowledge (keep attack-relevant features)

**Justifikasi:** Scope: "sekitar 15 sampai 30 fitur terpilih". Correlation-based = simple, interpretable.

### 4. Split Strategy
- **Train/Val/Test:** 60/20/20
- **Method:** Stratified random (maintain class distribution)
- **Seed:** Fixed for reproducibility

**Justifikasi:** Standard ML practice, allow proper validation. 70/15/15 alternative jika butuh lebih banyak training data.

### 5. Normalization
- **Method:** StandardScaler per client (fit on train only)
- **Scope:** Feature-wise Z-score normalization
- **Handling Inf:** Replace `Inf` in Flow Bytes/s, Flow Packets/s with 1e9 before scaling

**Justifikasi:** MLP requires normalized input, per-client scaling preserve non-IID property.

---

## 📋 RINGKASAN STATUS

| Item | Status | Action |
|------|--------|--------|
| **Keputusan 1: Dataset version** | ⏸️ BELUM DISETUJUI | Diskusi pembimbing |
| **Keputusan 2: Normal split** | ⏸️ BELUM DISETUJUI | Diskusi pembimbing |
| **Keputusan 3: DoS composition** | ⏸️ BELUM DISETUJUI | Diskusi pembimbing |
| **Keputusan 4: Imbalance method** | ⏸️ BELUM DISETUJUI | Diskusi pembimbing |
| **Defaults 1-5** | ⏸️ CONFIRMATION NEEDED | Konfirmasi tertulis |

---

## 🚀 NEXT STEPS

**After Approval:**
1. Update preprocessing script with approved decisions
2. Test on 5K sample per class
3. Generate full trainable CSVs (client_a_train.csv, etc.)
4. Verify data quality (NaN check, distribution check)
5. Begin E0-E4 experiments

**Timeline:** Week 4 (dataset lock per scope)

---

**Prepared by:** Hermes Agent (automated analysis)  
**Based on:** Full EDA (1,668,530 rows scanned), Rosay 2022, Briefing Scope TA  
**Contact:** Discuss in pembimbing meeting minggu ke-3
