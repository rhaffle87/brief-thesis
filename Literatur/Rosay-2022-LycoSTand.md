---
type: literatur
title: "Network Intrusion Detection: A Comprehensive Analysis of CIC-IDS2017"
authors: Rosay, A., Cheval, E., Carlier, F., Leroux, P.
year: 2022
venue: ICISSP 2022 (8th International Conference on Information Systems Security and Privacy)
doi: 10.5220/0010774000003120
arxiv: ""
pdf: "[[Rosay-2022-CIC-IDS2017-Analysis.pdf]]"
status: ✔ terverifikasi
tags:
  - literatur
  - dataset
  - cic-ids2017
  - lycos-ids2017
  - feature-extraction
  - bugs
rm_supported: Both
relevance: ⭐⭐⭐⭐⭐
dibaca_dari_pdf: ya
created: 2026-10-02
reviewed: ⬜ belum
cited_in_bab: []
prioritas: inti
---

# Network Intrusion Detection: Comprehensive Analysis of CIC-IDS2017 (Rosay et al. 2022)

## Metadata

**Penulis:** Rosay, A., Cheval, E., Carlier, F., Leroux, P.  
**Institusi:** STMicroelectronics, Polytech Nantes, Le Mans University (France)  
**Tahun:** 2022  
**Venue:** ICISSP 2022  
**DOI:** 10.5220/0010774000003120  
**Publisher:** SCITEPRESS  
**PDF Lokal:** [[Rosay-2022-CIC-IDS2017-Analysis.pdf]]

**Status Verifikasi:** ✔ Terverifikasi via SCITEPRESS  
**Relevansi Scope:** ⭐⭐⭐⭐⭐ CRITICAL - Dataset quality validation  
**Mendukung RM:** Both (preprocessing methodology)

---

## 📌 3 Temuan Utama

1. **34 Miscalculated Features in CIC-IDS2017 CSV:** Paper mengidentifikasi 5 kategori bugs: (1) 4 feature duplicates, (2) 21 miscalculated features (integer division, flag inversions, subflow logic errors), (3) protocol detection failures (ARP as IPv4, ICMP as TCP/UDP), (4) TCP termination errors creating 3 flows from 1 handshake, (5) inconsistent labeling.

2. **LycoSTand Tool:** Authors developed open-source C program to re-extract features from CIC-IDS2017 PCAP files, fixing all identified bugs. LYCOS-IDS2017 dataset generated using corrected tool shows **significant ML performance improvements** (Random Forest 99.5% vs original, LDA 88%→96%).

3. **38% Benign Flow Inflation:** Due to TCP termination bug (closing flow on first FIN packet), 4-way handshakes create 3 separate flows instead of 1. This artificially inflates BENIGN class from 1.4M to 2.3M flows (+877K flows from handshake fragments).

---

## 💡 Relevansi Terhadap Penelitian Ini

**RM1 (FedAvg vs Lokal pada non-IID):**
- Buggy features reduce model's ability to learn true patterns → FL aggregation may amplify errors
- **Implication:** Using corrected dataset (LYCOS) would give more honest FL vs local comparison
- **Current status:** LYCOS unavailable (404), must use original + document limitations

**RM2 (EWC mengurangi forgetting):**
- Miscalculated features → model memorizes artifacts instead of true patterns → forgetting measurement invalid
- **Implication:** EWC protecting buggy features = not meaningful continual learning
- **Mitigation:** Remove 4 duplicates, document 21 miscalculations, focus on macro-F1 (less sensitive to artifacts)

**Metodologi:**
- **Critical decision:** Acknowledge bugs in Bab 3.2.2, cite Rosay 2022 for transparency
- **Preprocessing:** Remove 4 duplicates, keep 21 miscalculated (for literature comparability)
- **Justification:** LYCOS preferred but unavailable (October 2026), original still valid benchmark

---

## 📊 Hasil Eksperimen Utama

### Class Distribution: CIC-IDS2017 vs LYCOS-IDS2017

| Class | CIC-IDS2017 | LYCOS-IDS2017 | Change |
|-------|-------------|---------------|--------|
| **BENIGN** | 2,273,097 | 1,395,659 | **-38.6%** |
| SSH-Patator | 7,938 | 4,003 | -49.6% |
| FTP-Patator | 7,938 | 4,003 | -49.6% |
| DoS Hulk | 231,073 | 158,988 | -31.2% |
| DoS GoldenEye | 10,293 | 6,765 | -34.3% |
| DoS Slowloris | 5,796 | 5,674 | -2.1% |
| DoS Slowhttptest | 5,499 | 4,866 | -11.5% |
| DDoS | 128,027 | 95,683 | -25.3% |
| Bot | 1,966 | 735 | -62.6% |
| Heartbleed | 11 | 11 | 0% |

**Key Insight:** TCP handshake bug creates 877K fake benign flows!

### ML Performance: Original vs LYCOS

| Algorithm | Original Acc | LYCOS Acc | Improvement |
|-----------|--------------|-----------|-------------|
| Random Forest | 99.0% | **99.5%** | +0.5% |
| Decision Tree | 98.5% | **99.2%** | +0.7% |
| LDA | 88.0% | **96.0%** | **+8.0%** |
| SVM | 85.2% | **92.1%** | +6.9% |
| QDA | 82.7% | **89.4%** | +6.7% |

**Key Insight:** All algorithms improve with corrected features, LDA gains most

---

## 🔍 Kutipan Penting (untuk Bab 3.2.2)

> "We analyze this dataset in detail and report several problems we discovered in the flows extracted from the network packets."

> "Five classes of problems were identified: feature duplication, feature calculation errors, erroneous protocol detection, inconsistent TCP termination flows and doubts on labels."

> "CICFlowMeter classifies ICMP packets sometimes as TCP, sometimes as UDP and sometimes as neither."

> "In CICFlowMeter, flows are closed either when the duration exceeds a predefined timeout of 120s, or if the received packet carries a 'FIN' flag. [...] This behavior causes three problems: TCP session termination creates multiple flows, labels become inconsistent, and RST-terminated flows are never closed."

> "The corrections provided by LycoSTand improve standard metrics for all the tested algorithms."

> "A vast majority of publications rely on the CSV files provided by CIC to study the performance of machine learning algorithms. Based on the problems mentioned above, it is natural to wonder whether the findings remain valid if the CSV are badly generated."

---

## ⚠️ Batasan & Catatan Kritis

**5 Bug Categories Detail:**

**1. Feature Duplication (4 features):**
- "Average Packet Size" = "Packet Length Mean"
- "Fwd Packet Length Mean" = "Fwd Segment Size Avg"
- "Bwd Packet Length Mean" = "Bwd Segment Size Avg"
- "Fwd Header Length" = "Fwd Header Length.1"

**2. Feature Miscalculations (21 non-duplicate):**
- **Integer division:** 11 features (bulks, subflows, ratio) use `int/int` instead of `float/float`
- **Bulk logic:** Forward bulk never updated, backward bulk always updated (inverted)
- **Subflow count:** Parenthesis error → count++ every packet (should be conditional)
- **First packet counted twice:** Mean, std, total length (3 features) off by one
- **Flag inversions:** SYN ↔ PSH swapped, FIN ↔ URG swapped
- **PSH/URG never updated:** Forward & backward counts always 0
- **Initial TCP window (bwd):** Contains last value instead of initial

**3. Protocol Detection Errors:**
- Ethertype field ignored → ARP/LLDP/CDP misclassified as IPv4
- Payload bytes that resemble headers → false protocol detection
- ICMP: randomly classified as TCP, UDP, or "other"
- UDP fragments: not recognized (except first packet with header)

**4. TCP Termination Bug:**
- FIN closes flow immediately → 4-way handshake split into 3 flows
- Last packet often closed by 120s timeout instead of flag
- RST flag ignored → future traffic merged incorrectly

**5. Labeling Inconsistencies:**
- Same handshake pattern labeled as benign OR attack randomly
- Portscan after infiltration labeled as benign (phase confusion)
- Flows from attacker IP labeled benign despite attack pattern

**Paper Limitations:**
- LycoSTand runtime: 16 hours for full CIC-IDS2017 PCAP (O(n) linked list search)
- LYCOS-IDS2017 availability: **October 2026 STATUS: 404 NOT FOUND**
- Paper doesn't provide downloadable LYCOS CSV (only tool + PCAPs)

---

## 🔗 Hubungan dengan Paper Lain

**Mengutip:**
- [[Sharafaldin-2018-CIC-IDS2017]] (original dataset paper)
- KDD-Cup99, NSL-KDD (previous datasets with issues)

**Dikutik oleh:**
- [[Dube-2024-Faulty-CIC-IDS2017]] (validates findings, adds more warnings)
- Future work citing LYCOS as corrected version

**Extends:**
- Sharafaldin 2018 methodology
- Previous dataset critiques (McHugh 2000 on KDD, Tavallaee 2009 on NSL-KDD)

---

## 📝 Catatan Tambahan

**LycoSTand Tool Features:**
- Language: C (libpcap 1.8.1)
- Input: PCAP files
- Output: CSV with 82 features (84 - 2 duplicates removed)
- Fixes: All 5 bug categories
- Runtime: O(n) per packet (16 hours for CIC-IDS2017)
- Availability: http://lycos-ids.univ-lemans.fr/ (404 Oct 2026)

**Our Preprocessing Strategy (Given LYCOS unavailable):**
1. Use original CIC-IDS2017 CSV from UNB or Kaggle
2. **Remove 4 duplicates** (keep first of each pair)
3. **Document 21 miscalculations** in Bab 3.2.2 (cite Rosay 2022)
4. **Keep miscalculated features** (for literature comparability - most papers use original)
5. **Add subsection:** "Dataset Limitations and Mitigation Strategies"
6. **Transparency:** State LYCOS preferred but unavailable

**Duplicate Removal Code:**
```python
# Remove duplicates (keep first)
drop_cols = [
    'Average Packet Size',  # duplicate of Packet Length Mean
    'Fwd Segment Size Avg',  # duplicate of Fwd Packet Length Mean
    'Bwd Segment Size Avg',  # duplicate of Bwd Packet Length Mean
    'Fwd Header Length.1'  # duplicate of Fwd Header Length
]
df = df.drop(columns=drop_cols, errors='ignore')
```

**Decision Log:**
- 2026-10-02: LYCOS-IDS2017 unavailable (404), proceed with original + transparency
- Preprocessing: Remove 4 duplicates, document 21 bugs, cite Rosay 2022
- Justification: Honest methodology > perfect data (most FL-IDS papers use original anyway)

**Citation Strategy:**
- Bab 3.2.1: Cite Sharafaldin 2018 for dataset design
- Bab 3.2.2: Cite Rosay 2022 for preprocessing justification & bug documentation
- Bab 3.2.2: Cite Dube 2024 for additional validation

**Impact on Results Interpretation:**
- Acknowledge that reported performance may be inflated by artifacts
- Focus on **relative comparison** (E1 vs E2, E3 vs E4) rather than absolute accuracy
- Macro-F1 more robust to artifacts than accuracy (class-balanced metric)

---

**Review Status:** ⬜ Belum direview full paper  
**Action Items:** 
- [x] Buat literature note
- [ ] Read Section 3.2 (Feature Miscalculations - detail 21 bugs)
- [ ] Read Section 4 (LycoSTand Algorithm 1 & 2)
- [ ] Extract Table 1 (class distribution comparison)
- [ ] Extract Table: ML performance comparison
- [ ] Write Bab 3.2.2 subsection: "Dataset Quality Issues and Transparency"
- [ ] Update preprocessing script to remove 4 duplicates
- [ ] Create decision log: "Decision-Dataset-Original-CIC.md"
