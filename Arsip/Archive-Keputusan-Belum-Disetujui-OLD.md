# Keputusan Metodologi Belum Disetujui

**Last Updated:** 2026-10-02 14:05 UTC+7  
**Status:** MENUNGGU PERSETUJUAN PEMBIMBING

---

## 📋 Keputusan Pending

### 1. Dataset Choice: CIC-IDS2017 Original vs LYCOS

**Context:**
- LYCOS-IDS2017 (corrected version) unavailable (404 Not Found, Oct 2026)
- CIC-IDS2017 original has 34 documented bugs (Rosay 2022)

**Proposed Decision:**
Use CIC-IDS2017 original with transparency strategy:
- Document all 34 buggy features in Bab 3
- Cite Rosay 2022 + Dube 2024 for research integrity
- Remove 4 duplicate features
- Use macro-F1 (less artifact-sensitive than accuracy)
- Focus on relative comparisons (E1 vs E2 vs E3 vs E4) not absolute performance

**Alternative Options:**
1. Wait for LYCOS mirror availability
2. Use different dataset (UNSW-NB15, CICIoMT2024)
3. Kaggle version (needs verification if modified)

**Status:** ⏸️ BELUM DISETUJUI  
**Action Required:** Diskusi dengan pembimbing minggu ke-3

---

### 2. Train/Val/Test Split Strategy

**Context:**
- Briefing Scope: "split train/val/test stratified (misalnya 70/15/15)"
- Question: Random split or temporal split?

**Proposed Decision:**
Random stratified split (70/15/15):
- Rationale: Avoid concept drift confound (focus on non-IID + forgetting only)
- Consistent with scope (no live traffic as primary data)
- Easier reproduction

**Alternative Options:**
1. Temporal split (Monday train, Tuesday val, Wednesday test)
   - Pro: More realistic
   - Con: Introduces concept drift variable (not in scope)
2. Per-client split (each client splits own data)
   - Pro: Preserves local distribution
   - Con: Test set becomes non-IID (harder to compare)

**Status:** ⏸️ BELUM DISETUJUI  
**Action Required:** Diskusi dengan pembimbing minggu ke-4 (saat dataset lock)

---

### 3. Subsampling Strategy for Class Imbalance

**Context:**
- Expected distribution: Normal ~1.4M, SSH-Patator ~5.9K, DoS ~170K (ratio 237:1:29)
- Severe class imbalance

**Proposed Decision:**
Undersample majority class (Normal) to match minority:
- Limit: ~6K samples per class (follow SSH-Patator count)
- Method: Random undersampling
- Total dataset: ~18K flows (6K × 3 classes)

**Alternative Options:**
1. Keep original distribution + weighted loss
2. SMOTE oversampling (out of scope per briefing)
3. Different limits per class (e.g., 10K Normal, 6K SSH, 10K DoS)

**Status:** ⏸️ BELUM DISETUJUI  
**Action Required:** Confirm with preprocessing trial (minggu ke-4)

---

### 4. Feature Selection Method

**Context:**
- CIC-IDS2017 has 82 features
- Scope: "sekitar 15 sampai 30 fitur terpilih"
- Need to remove 4 duplicates + 34 buggy features

**Proposed Decision:**
Correlation-based selection:
1. Remove 4 duplicates (Rosay 2022 list)
2. Remove 34 buggy features (or mark as "buggy-kept" if critical)
3. Correlation analysis on remaining ~44 features
4. Select top-20 by correlation with label + low inter-feature correlation

**Alternative Options:**
1. PCA (harder to interpret for IDS)
2. Mutual information
3. Tree-based feature importance (XGBoost)
4. Keep all non-buggy features (48 features)

**Status:** ⏸️ BELUM DISETUJUI  
**Action Required:** Trial run during preprocessing (minggu ke-4)

---

## 🔒 Keputusan Approved (from Briefing Scope)

These are LOCKED per scope freeze:

1. ✅ **Dataset:** CIC-IDS2017 (freeze minggu ke-4)
2. ✅ **Classes:** 3 only (Normal, SSH-Patator, DoS)
3. ✅ **Model:** MLP only (no CNN/Transformer)
4. ✅ **FL Algorithm:** FedAvg only (no Krum/TrimmedMean)
5. ✅ **CL Algorithm:** EWC only (no GEM/A-GEM)
6. ✅ **Clients:** 2 clients + 1 server
7. ✅ **Non-IID:** Client A = Normal+SSH, Client B = Normal+DoS
8. ✅ **Task Sequence:** Task 1 = Normal+SSH, Task 2 = Normal+DoS
9. ✅ **Experiments:** E0-E4 (5 configurations)
10. ✅ **Primary Metric:** Macro-F1, BWT

---

## 📝 Notes

**Decision Log Purpose:**
Separate "scope requirements" (locked) from "implementation choices" (need approval).

**Review Cadence:**
- Minggu ke-3: Dataset choice
- Minggu ke-4: Preprocessing decisions (split, sampling, features)
- Post-approval: Move to "Keputusan-Disetujui.md"

**Pembimbing Approval Required Before:**
- Dataset download (decision #1)
- Preprocessing script execution (decisions #2, #3, #4)
- Dataset lock (minggu ke-4)
