# ⚠️ DATASET ISSUE - LYCOS-IDS2017 Not Available

**Date:** 2026-10-02  
**Status:** LYCOS-IDS2017 website returns 404 Not Found

---

## Problem

LYCOS-IDS2017 corrected dataset (recommended by Rosay et al. 2022) is **NOT accessible**:
- URL: http://lycos-ids.univ-lemans.fr/LYCOS-IDS2017.zip
- Status: 404 Not Found (Apache server error)
- File downloaded: 286 bytes (HTML error page, not actual 1.5GB dataset)

**Possible reasons:**
1. Website moved or down temporarily
2. Dataset removed from public access
3. Requires registration/request form (not documented in paper)

---

## Alternative Options

### Option 1: CIC-IDS2017 Original (UNB Official) ⚠️
**Source:** https://www.unb.ca/cic/datasets/ids-2017.html  
**Size:** ~2GB (MachineLearningCSV.zip)  
**Pros:** Official source, widely used benchmark  
**Cons:** 34 buggy features (Rosay 2022), 38% inflated benign flows

**Citation impact:**
- Can cite Sharafaldin 2018 as primary dataset source
- Must acknowledge Rosay 2022 findings in Bab 3 (methodology limitations)
- Mention LYCOS unavailability as justification

### Option 2: CIC-IDS2017 from Kaggle
**Source:** https://www.kaggle.com/datasets/cicdataset/cicids2017  
**Size:** ~500MB (pre-processed)  
**Pros:** Fast download, preprocessed  
**Cons:** Unknown version (could be original buggy CSV or community fix)

### Option 3: Re-extract from PCAP using CICFlowMeter ⚠️ HIGH EFFORT
**Source:** Download PCAP files from UNB, run CICFlowMeter locally  
**Time:** 16 hours processing (per Rosay paper)  
**Pros:** Full control, can verify features  
**Cons:** Windows libpcap setup complex, time-consuming

### Option 4: Use Different Dataset (OUT OF SCOPE)
**Examples:** UNSW-NB15, CSE-CIC-IDS2018, CIC-DDoS2019  
**Status:** ❌ REJECTED - scope frozen to CIC-IDS2017

---

## Recommendation: Use CIC-IDS2017 Original with Caveats

**Decision:** Proceed with **Option 1** (CIC-IDS2017 original from UNB)

**Rationale:**
1. LYCOS-IDS2017 unavailable (404 error)
2. Original CIC-IDS2017 is standard benchmark (thousands of citations)
3. We can **acknowledge limitations** in Bab 3.2.2:
   - Cite Rosay 2022 findings
   - Document 34 miscalculated features
   - Note 38% benign inflation from TCP termination
   - State that LYCOS was preferred but unavailable
4. Results remain **valid for comparison** (most FL-IDS papers use original)
5. **Honest methodology** = document known issues transparently

**Tradeoffs accepted:**
- ⚠️ Feature quality lower than LYCOS
- ✅ Reproducible (everyone can download)
- ✅ Comparable to existing literature
- ✅ Time-efficient (no 16-hour PCAP processing)

---

## Updated Methodology (Bab 3.2.2)

### Preprocessing Pipeline with Bug Awareness

**Step 1:** Download CIC-IDS2017 MachineLearningCSV.zip from UNB

**Step 2:** Filter 3 classes + merge DoS variants
- Keep: BENIGN, SSH-Patator, DoS Slowloris, DoS Hulk, DoS GoldenEye
- Merge DoS variants → single 'DoS' class

**Step 3:** Feature cleaning (address Rosay findings)
- **Remove 4 duplicates:**
  - Keep "Packet Length Mean", drop "Average Packet Size"
  - Keep "Fwd Packet Length Mean", drop "Fwd Segment Size Avg"
  - Keep "Bwd Packet Length Mean", drop "Bwd Segment Size Avg"
  - Keep "Fwd Header Length", drop "Fwd Header Length.1"

- **Known miscalculations (document, but keep):**
  - Bulk features (6): incorrect forward/backward logic
  - Subflow features (4): parenthesis bug (always increment)
  - Flag counts: SYN↔PSH swapped, FIN↔URG swapped, PSH/URG never updated
  - Initial TCP window (backward): contains last value not initial
  - **Rationale:** Dropping these would change comparison basis vs literature

**Step 4:** Handle NaN, inf, zero-variance
- Replace inf with NaN
- Drop rows with NaN (or median imputation)
- Remove features with std=0

**Step 5:** Feature selection
- Top-20 features by importance (Random Forest or mutual info)
- OR PCA 95% variance
- **Rationale:** Reduce redundancy from buggy features

**Step 6:** Normalization, encoding, split
- StandardScaler (zero mean, unit variance)
- Label encoding: BENIGN=0, DoS=1, SSH-Patator=2
- Stratified 60/20/20 split

---

## Citation Strategy (Updated)

**Primary dataset citation:**
```
Sharafaldin, I., Lashkari, A.H., Ghorbani, A.A. (2018). 
Toward Generating a New Intrusion Detection Dataset and Intrusion Traffic Characterization.
ICISSP 2018. DOI: 10.5220/0006639801080116
```

**Methodology transparency citation:**
```
Rosay, A., Cheval, E., Carlier, F., Leroux, P. (2022).
Network Intrusion Detection: A Comprehensive Analysis of CIC-IDS2017.
ICISSP 2022. DOI: 10.5220/0010774000003120

"We acknowledge the feature extraction issues identified by Rosay et al. (2022),
including 34 miscalculated features and TCP termination artifacts. The corrected
LYCOS-IDS2017 dataset was unavailable at the time of this research (October 2026).
We use the original CIC-IDS2017 CSV files with duplicate feature removal and 
transparent documentation of known limitations."
```

**Additional validation:**
```
Dube, R. (2024). Faulty use of the CIC-IDS 2017 dataset in information security research.
Journal of Computer Virology and Hacking Techniques, 20, 203-211.
DOI: 10.1007/s11416-023-00509-7
```

---

## Action Plan

### Immediate (Today)
1. ✅ Document LYCOS unavailability (this file)
2. ⬜ Download CIC-IDS2017 from UNB or Kaggle
3. ⬜ Update preprocessing script for original CSV format
4. ⬜ Run preprocessing with duplicate removal

### Week 3-4
5. ⬜ EDA: Compare class distribution with Rosay's LYCOS stats
6. ⬜ Write Bab 3.2.2 subsection: "Dataset Limitations and Mitigation"
7. ⬜ Create decision log: "Decision-Dataset-CIC-Original.md"

---

## Download Links

**Option 1 (Official UNB):**
```
https://www.unb.ca/cic/datasets/ids-2017.html
→ Click "Download Dataset" button
→ Fill form (name, email, institution)
→ Receive download link via email
→ MachineLearningCSV.zip (~2GB)
```

**Option 2 (Kaggle - requires Kaggle account):**
```
https://www.kaggle.com/datasets/cicdataset/cicids2017
→ Sign in with Google/GitHub
→ Download button (top right)
→ Faster than UNB (no email wait)
```

**Option 3 (Kaggle CLI - if kaggle API configured):**
```bash
pip install kaggle
kaggle datasets download -d cicdataset/cicids2017
unzip cicids2017.zip -d E:/Projects/fl-cl/data/raw/CIC-IDS2017/
```

---

**Status:** Waiting for user decision on download option  
**Preprocessing script:** Ready, needs update for duplicate removal  
**Impact:** Minor methodology adjustment, full transparency in thesis
