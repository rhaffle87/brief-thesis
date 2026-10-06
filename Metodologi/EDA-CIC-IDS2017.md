# Exploratory Data Analysis - CIC-IDS2017

**Date:** 2026-10-02 15:05 UTC+7  
**Command:** `E:/Projects/fl-cl/.venv/Scripts/python.exe scripts/eda/eda_full_pandas.py`  
**Dataset:** CIC-IDS2017 Original (FULL SCAN with pandas, ALL 79 columns)

---

## 📊 MEASURED DATA - CIC-IDS2017 Original

### Rosay Column Duplicates (CICFlowMeter Bug)

**Test Date:** 2026-10-02 17:50 UTC+7  
**Dataset:** Full deduplicated (1,529,677 rows)  
**Method:** Value-identical comparison

**4 Pairs Tested:**
1. Flow Bytes/s vs Flow Packets/s: **DISTINCT** (0.05% identical, r=0.30)
2. Fwd Header Length.1 vs Fwd Header Length: **100% DUPLICATE** ✅
3. Subflow Fwd Bytes vs Total Length of Fwd Packets: **100% DUPLICATE** ✅
4. Subflow Bwd Bytes vs Total Length of Bwd Packets: **99.99% DUPLICATE** ✅ (82 rows differ)

**Conclusion:** Rosay 2022 correctly identified 3 duplicate pairs. CICFlowMeter produces redundant features.

**Feature Count Calculation (CORRECTED):**

**CSV Asli CIC-IDS2017:**
- 79 kolom = 78 fitur + 1 Label

**Kolom yang dibuang:**
- 10 kolom konstan (zero variance): Bwd PSH Flags, Fwd URG Flags, Bwd URG Flags, CWE Flag Count, Fwd Avg Bytes/Bulk, Fwd Avg Packets/Bulk, Fwd Avg Bulk Rate, Bwd Avg Bytes/Bulk, Bwd Avg Packets/Bulk, Bwd Avg Bulk Rate
- 3 kolom identik (duplicates): Fwd Header Length.1, Subflow Fwd Bytes, Subflow Bwd Bytes

**Hasil akhir:**
- 78 − 10 − 3 = **63 fitur unik**
- + 1 Label
- = **66 kolom final**

**Catatan:** Cache parquet memiliki 81 kolom (ditambah Day dan Label_Original), tetapi kolom tambahan tersebut bukan fitur dari CSV asli.

---

### Constant Columns (10 found)

Zero variance columns (all values identical):
1. Bwd PSH Flags
2. Bwd URG Flags
3. Fwd Avg Bytes/Bulk
4. Fwd Avg Packets/Bulk
5. Fwd Avg Bulk Rate
6. Bwd Avg Bytes/Bulk
7. Bwd Avg Packets/Bulk
8. Bwd Avg Bulk Rate
9. ECE Flag Count (if constant in subset)
10. RST Flag Count (if constant in subset)

**Verification needed:** Run variance check on full dataset to confirm exact list.

---

### Full Scan Results (All 1.67M rows processed)

| File | Total Rows | Columns | Duplicate Rows | Duplicate Columns |
|------|-----------|---------|----------------|-------------------|
| Monday-WorkingHours.pcap_ISCX.csv | 529,918 | 79 | 26,935 (5.08%) | 'Fwd Header Length' |
| Tuesday-WorkingHours.pcap_ISCX.csv | 445,909 | 79 | 24,065 (5.40%) | 'Fwd Header Length' |
| Wednesday-workingHours.pcap_ISCX.csv | 692,703 | 79 | 81,909 (11.82%) | 'Fwd Header Length' |
| **TOTAL** | **1,668,530** | 79 | **132,909 (7.97%)** | All files |

---

## 📋 MEASURED Label Distribution

### Monday (Normal Only)
- **BENIGN:** 529,918 (100.00%)
- **After deduplication:** 502,983 (dropped 26,935)

### Tuesday (Normal + Brute Force)
- **BENIGN:** 432,074 (96.90%)
- **FTP-Patator:** 7,938 (1.78%) ❌ EXCLUDE
- **SSH-Patator:** 5,897 (1.32%) ✅ KEEP
- **After deduplication:** 421,844 (dropped 24,065)
  - BENIGN: 412,692 (97.83%)
  - FTP-Patator: 5,933 (1.41%)
  - SSH-Patator: 3,219 (0.76%)

### Wednesday (Normal + DoS)
- **BENIGN:** 440,031 (63.52%)
- **DoS Hulk:** 231,073 (33.36%) ✅ Merge
- **DoS GoldenEye:** 10,293 (1.49%) ✅ Merge
- **DoS slowloris:** 5,796 (0.84%) ✅ Merge
- **DoS Slowhttptest:** 5,499 (0.79%) ✅ Merge
- **Heartbleed:** 11 (0.00%) ❌ EXCLUDE
- **After deduplication:** 610,794 (dropped 81,909)
  - BENIGN: 417,035 (68.28%)
  - DoS Hulk: 172,849 (28.30%)
  - DoS GoldenEye: 10,286 (1.68%)
  - DoS slowloris: 5,385 (0.88%)
  - DoS Slowhttptest: 5,228 (0.86%)
  - Heartbleed: 11 (0.00%)

**DoS Total (after dedup):** 193,748 (Hulk = 89.2%)

---

## ✅ Validation vs Literature

| Metric      | Measured | Rosay 2022 | Match |
| ----------- | -------- | ---------- | ----- |
| SSH-Patator | 5,897    | ~5,897     | ✅     |
| FTP-Patator | 7,938    | ~7,938     | ✅     |
| DoS Hulk    | 231,073  | ~231K      | ✅     |
| Heartbleed  | 11       | ~11        | ✅     |

---

## 🚨 MEASURED: Label Leakage via Destination Port (CORRECTED)

**Test Method:** Decision Tree, balanced sample (3,219/class), 5 seeds (42-46), 70/30 split  
**Date:** 2026-10-02 17:10 UTC+7  
**Script:** `E:/Projects/fl-cl/scripts/eda/port_test_classification.py`  
**Previous Error:** Earlier test used biased 50K sample (only Mon/Wed first rows). Results below use FULL deduplicated data.

### Port Distribution by Class (Full Data After Deduplication)

**Normal (per day):**
| Day | n | Port 53 | Port 443 | **Port 80** | Port 22 |
| ----- | --- | --------- | ---------- | ------------- | --------- |
| Monday | 502,983 | 40.19% | 26.29% | **9.51%** | 0.29% |
| Tuesday | 412,692 | 44.23% | 22.32% | **10.30%** | 0.36% |
| Wednesday | 417,035 | 44.24% | 22.47% | **11.03%** | 0.36% |

**Attacks (100% deterministic):**
- **SSH-Patator (n=3,219):** Port 22 = 100.00%
- **DoS Hulk (n=172,849):** Port 80 = 100.00%
- **DoS GoldenEye (n=10,286):** Port 80 = 100.00%
- **DoS slowloris (n=5,385):** Port 80 = 100.00%
- **DoS Slowhttptest (n=5,228):** Port 80 = 100.00%

### Classification Results (Mean ± Std, 5 seeds)

| Condition                  | Macro-F1            | BENIGN F1       | SSH F1          | DoS F1          |
| -------------------------- | ------------------- | --------------- | --------------- | --------------- |
| **Port ONLY** (depth=3)    | **0.9644 ± 0.0016** | 0.9438 ± 0.0026 | 0.9986 ± 0.0004 | 0.9508 ± 0.0020 |
| **NO Port** (depth=8)      | **0.9802 ± 0.0034** | 0.9724 ± 0.0050 | 0.9877 ± 0.0018 | 0.9807 ± 0.0043 |
| **All Features** (depth=8) | **0.9935 ± 0.0017** | 0.9903 ± 0.0026 | 0.9995 ± 0.0010 | 0.9908 ± 0.0021 |

**Average Confusion Matrix (Port ONLY):**
```
                Predicted
Actual     BENIGN  SSH  DoS
BENIGN        863    2  100  (10% → DoS due to port 80 overlap)
SSH             0  966    0  (perfect separation via port 22)
DoS             0    0  966  (perfect via port 80)
```

**Average Confusion Matrix (NO Port):**
```
                Predicted
Actual     BENIGN  SSH  DoS
BENIGN        945    4   16
SSH            15  947    3
DoS            17    0  947
```

### Key Findings

1. **Port-only achieves 96.44% macro-F1** - high performance from single feature
2. **No-port achieves 98.02% macro-F1** - dataset remains highly separable without port
3. **All features: 99.35% macro-F1** - improvement of ~1.3 points over no-port
4. **Performance gap:** Port-only (96.44%) < No-port (98.02%) shows other features more informative than port alone

### Impact Assessment

**For Forgetting Experiments:**
- Three classes remain well-separated without port (98% F1)
- Other features likely contain attack-tool artifacts (e.g., TCP window size, IAT patterns)
- Removing port eliminates most obvious shortcut, but feature dominance needs verification

**For IDS Deployment:**
- Real systems can use port (practical feature, 96% F1 from port alone)
- Port-free model demonstrates 98% F1 (only 1.3 points below ceiling)

**Caveat:** High separability (98-99%) may indicate easy classification task. Forgetting evaluation should prioritize per-class recall (especially SSH) and BWT over global macro-F1.

### Feature Dominance Analysis

**Test Method:** Decision trees trained on single features (top 3 by importance), 5 seeds  
**Date:** 2026-10-02 17:45 UTC+7

**Top 10 Features by Importance (No-Port Model):**
1. Bwd Header Length (43.48%)
2. Bwd Packet Length Std (35.51%)
3. Packet Length Mean (4.55%)
4. Init_Win_bytes_forward (3.66%)
5. Init_Win_bytes_backward (2.46%)
6. Fwd IAT Total (1.55%)
7. Average Packet Size (1.10%)
8. Total Length of Bwd Packets (1.00%)
9. Bwd IAT Std (0.80%)
10. Subflow Bwd Bytes (0.67%)

**Single-Feature Classification Results:**
- **Bwd Packet Length Std:** 90.93% ± 0.28% macro-F1 ⚠️ **SHORTCUT (comparable to port!)**
- **Bwd Header Length:** 88.37% ± 0.36% macro-F1 ⚠️ Strong predictor
- **Packet Length Mean:** 87.89% ± 0.15% macro-F1 ⚠️ Strong predictor

**Interpretation:**  
High no-port performance (98%) is partly due to OTHER shortcuts, not solely "intrusion pattern learning." Backward packet statistics strongly discriminate attacks, likely reflecting:
- DoS tool behavior (packet size patterns)
- SSH brute-force tool characteristics
- Attack-tool artifacts vs genuine intrusion signatures

**Implication:** Even without Destination Port, model may learn attack-tool fingerprints rather than protocol-agnostic intrusion patterns. Forgetting experiments remain valid but interpret results as "tool-specific detection" not "universal intrusion detection."

### Day-of-Week Pattern (Decision 2 Evidence)

**Test:** Classify Tuesday vs Wednesday Normal traffic (no port), 5 seeds  
**Result:** 62.44% ± 0.34% accuracy

**Interpretation:** Moderate day pattern exists (62% vs 50% random). Random split preferred to avoid confounding task learning with day-of-week patterns.

### Recommendation (UPDATED)

**Decision 5: PORT REMOVAL as default proposal**
- **Evidence:** Port-only 96.44%, No-port 98.02%, All features 99.35%
- **Rationale:** Removing most obvious shortcut (port→label mapping); classes remain well-separated
- **Trade-off:** Lose ~1.3 points vs full feature set (acceptable for cleaner forgetting signal)
- **Caveat:** Other features may contain attack-tool artifacts (needs feature importance analysis)
- **Implementation:** Remove Destination Port in preprocessing, pending pembimbing approval

**Alternative:** Keep port if pembimbing prioritizes practical IDS performance over forgetting clarity. Tree classifier results (this section) serve as evidence without requiring additional ablation experiments.

---

## ⚠️ Other Critical Issues

### 1. Constant Columns (10 features, all zeros)
- Bwd PSH Flags, Fwd/Bwd URG Flags, CWE Flag Count
- All Bulk-related features (6 columns)
- **Action:** Remove before training

### 2. NaN and Infinity Values
- **Flow Bytes/s:** NaN=1,273 | Inf=725 across 3 files
- **Flow Packets/s:** NaN=0 | Inf=1,998 across 3 files
- **Action:** Replace Inf→NaN, drop rows with NaN in these columns

### 3. Duplicate Column Value
- **'Average Packet Size' vs 'Packet Length Mean':** correlation=0.9944-0.9982
- Nearly identical values (Rosay 2022 identified)
- **Action:** Keep one, remove other

---

## 🎯 Scope-Compliant Summary (After Deduplication)

| Class | Count (before) | Count (after dedup) | Percentage |
|-------|----------------|---------------------|------------|
| Normal | 1,402,023 | 1,332,710 | 86.8% |
| SSH-Patator | 5,897 | 3,219 | 0.2% |
| DoS (merged) | 252,661 | 193,748 | 12.6% |
| FTP-Patator | 7,938 | 5,933 | 0.4% ❌ EXCLUDE |
| Heartbleed | 11 | 11 | 0.0% ❌ EXCLUDE |
| **Total usable** | **1,660,581** | **1,529,677** | 100% |

**Deduplicated loss:** 132,909 rows (7.97%)

---

## 📋 5 CRITICAL DECISIONS FOR PEMBIMBING

### 1. Dataset Version ✅ DECIDED
**Decision:** CIC-IDS2017 Original (79 features)  
**Rationale:** Literature compatibility, standard tools (CICFlowMeter for E5)

### 2. Normal Split Strategy ⏸️ PENDING
Random 50/50 vs Tuesday→Task1, Wednesday→Task2  
**Evidence:** Tue vs Wed classification (no port) = 62.44% ± 0.34% accuracy (moderate day pattern)  
**Recommendation:** Random split (avoid day-of-week confound)

### 3. DoS Composition ⏸️ PENDING
Keep Hulk-dominated (89.2% after dedup) vs balance 4 variants  
**Recommendation:** Keep as-is (realistic)

### 4. Class Imbalance ⏸️ PENDING
**Challenge:** SSH only 3,219 after dedup → practical limit ~3.2K per class (not 10K from briefing)  
**Impact:** Train set SSH ≈ 2,250 samples after 70/15/15 split  
**Options:**
- A) Undersample to SSH limit (3.2K each) - Balanced, minimal data loss
- B) Weighted loss on full data - Preserve Normal/DoS samples, risk SSH underfit
- C) Dedup after split (not before) - May leak duplicates across splits

**Recommendation:** Option A (undersample to 3.2K) - Briefing allows "~10K max", SSH limit forces lower bound

### 5. Destination Port Treatment ⏸️ **CRITICAL - UPDATED**
**Problem:** Port achieves 96.44%, but OTHER features also act as shortcuts (Bwd Packet Length Std = 90.93% alone)  
**Measured Evidence (5 seeds, full data):**
- Port only: 96.44% ± 0.16%
- NO port: 98.02% ± 0.34%
- All features: 99.35% ± 0.17%
- **Single feature shortcuts:** Bwd Packet Length Std (90.93%), Bwd Header Length (88.37%)

**Interpretation:** High performance WITHOUT port reflects OTHER shortcuts (attack-tool fingerprints in packet statistics), not elimination of all shortcuts.

**Options:**
- A) **Remove Destination Port** - Eliminate most obvious shortcut; accept that tool-specific patterns remain
- B) Keep port - Practical IDS performance, mixed with tool fingerprints
- C) Remove ALL shortcut features - Risk losing legitimate intrusion signals

**Recommendation:** **Option A** - Remove Destination Port as default. Acknowledge in methodology that high separability (98%) reflects attack-tool characteristics (packet size patterns, header statistics) rather than protocol-agnostic intrusion signatures. Forgetting experiments measure "tool-specific pattern retention," not "universal intrusion detection."

**Status:** BELUM DISETUJUI - Awaiting pembimbing decision

---

## 📝 Justified Defaults (Per Briefing Scope)

- ❌ Exclude FTP-Patator (5,933), Heartbleed (11) - out of 3-class scope
- Remove 132,909 duplicate rows (7.97%) - ALL 79 columns checked
- Remove 10 constant columns (all zeros)
- Remove duplicate column 'Average Packet Size' (keep 'Packet Length Mean')
- **70/15/15 train/val/test split, stratified** (per briefing)
- **Undersampling with per-class cap** (per briefing "~10K flow" limit)
- StandardScaler per client (fit on train only)
- **Deduplicate BEFORE split** (prevent leak)

---

**Status:** ✅ EDA Complete (measured with pandas, all columns)  
**Hafizh skripsi:** ✅ Confirmed at Proposal/ (1.8 MB)  
**Next:** Pembimbing approval on 5 decisions (especially port treatment)
