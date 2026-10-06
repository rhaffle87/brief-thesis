# CRITICAL FINDINGS - CIC-IDS2017 Dataset Issues (Rosay et al. 2022)

**Source:** Rosay-2022-LycoSTand-CIC-IDS2017.pdf  
**Paper:** Network Intrusion Detection: A Comprehensive Analysis of CIC-IDS2017  
**DOI:** 10.5220/0010774000003120  
**Tool:** LycoSTand - http://lycos-ids.univ-lemans.fr/

---

## 🚨 5 MAJOR PROBLEMS IN CIC-IDS2017 CSV FILES

### 1. Feature Duplication (4 duplicates)
- "Average Packet Size" = "Packet Length Mean"
- "Fwd Packet Length Mean" = "Fwd Segment Size Avg"
- "Bwd Packet Length Mean" = "Bwd Segment Size Avg"
- "Fwd Header Length" = "Fwd Header Length.1"

### 2. Feature Miscalculations (34 features affected, 21 non-duplicates)
- **Integer division bug:** 11 features (bulks, subflows, ratio) use int instead of float
- **Bulk features:** Forward bulk never updated, backward bulk always updated (wrong)
- **Subflow count:** Misplaced parenthesis → count increased EVERY packet (should be conditional)
- **First packet counted twice:** Affects mean, std, total packet length (3 features)
- **TCP flags inverted:** SYN ↔ PSH swapped, FIN ↔ URG swapped
- **PSH/URG never updated:** Forward and backward counts always 0
- **Initial TCP window (backward):** Overwritten with last value instead of initial

### 3. Wrong Protocol Detection
- **Ethertype ignored:** ARP/LLDP/CDP packets misclassified as IPv4
- **Payload misinterpreted:** Byte sequences that look like headers → false protocol
- **ICMP classified randomly:** Sometimes TCP, sometimes UDP, sometimes neither
- **UDP fragments:** Not recognized as UDP (except first packet)

### 4. Inconsistent TCP Termination
- **FIN closes flow immediately:** Creates 3 separate flows for 4-way handshake
- **Label inconsistency:** Same handshake packets labeled as benign OR attack randomly
- **RST ignored:** Flows not closed by RST → future traffic merged incorrectly
- **Timeout issues:** Last FIN packet often closed by 120s timeout instead of flag

### 5. Labeling Issues
- **Portscan discrepancies:** Website says "with/without firewall", dataset only has firewall IP
- **Benign mislabeled as attack:** Flows from attacker IP (205.174.165.73) labeled benign despite portscan pattern
- **Infiltration phase confusion:** Phase 2 (portscan after download) labeled as benign
- **No public labeling tool:** Proprietary package, impossible to reproduce

---

## 📊 IMPACT ON CLASS DISTRIBUTION

**CIC-IDS2017 Original vs LYCOS-IDS2017 (Corrected):**

| Class | CIC-IDS2017 | LYCOS-IDS2017 | Change |
|-------|-------------|---------------|--------|
| BENIGN | 2,273,097 | 1,395,659 | **-38.6%** |
| DoS Hulk | 231,073 | 158,988 | -31.2% |
| DDoS | 128,027 | 95,683 | -25.3% |
| DoS GoldenEye | 10,293 | 6,765 | -34.3% |
| DoS Slowloris | 5,796 | 5,674 | -2.1% |
| DoS Slowhttptest | 5,499 | 4,866 | -11.5% |
| FTP-PATATOR | 7,938 | 4,003 | **-49.6%** |
| Bot | 1,966 | 735 | -62.6% |
| Heartbleed | 11 | 11 | 0% |

**Key Insight:** TCP termination bug creates **38% more benign flows** from handshake fragments!

---

## ✅ LycoSTand Corrections

1. **Protocol detection:** Uses Ethertype + IP protocol field correctly
2. **TCP termination:** Close on FIN/RST, drop subsequent handshake packets
3. **Feature calculation:** Fixed integer division, subflow logic, flag counts
4. **Labeling:** Time + IP/port based labeling with Wireshark validation
5. **Open source:** C program + Python labeling at http://lycos-ids.univ-lemans.fr/

**Performance:** All ML algorithms improve with LYCOS-IDS2017
- Random Forest: >99.5% accuracy, precision, recall
- LDA: 88% → 96% accuracy
- SVM/QDA: Previously poor, now competitive

---

## ⚠️ IMPLICATIONS FOR OUR THESIS

### CRITICAL DECISIONS NEEDED

**Option 1: Use CIC-IDS2017 CSV (Original) ⚠️**
- Pro: Standard benchmark, widely used, reproducible
- Con: 34 miscalculated features, 38% inflated benign flows, TCP handshake noise
- Risk: Results may not reflect true model capability

**Option 2: Use LYCOS-IDS2017 CSV (Corrected) ✅**
- Pro: Fixed features, correct TCP flows, better labels
- Con: Less citations (2022), need to justify choice in Bab 3
- Benefit: More reliable results, honest methodology

**Option 3: Re-extract from PCAP using LycoSTand 🔧**
- Pro: Full control, can verify Rosay's claims
- Con: 16 hours processing time, need to install libpcap on Windows
- Benefit: Best practice, reproducible pipeline

### RECOMMENDED: Option 2 (LYCOS-IDS2017) with justification

**Rationale (for Bab 3.2):**
1. CIC-IDS2017 CSV has **proven bugs** (Rosay 2022, peer-reviewed ICISSP)
2. Using buggy data undermines thesis validity (metodologi soundness)
3. LYCOS-IDS2017 publicly available, open source, reproducible
4. Other papers affected: CSE-CIC-IDS2018, CIC-DDoS2019 also use CICFlowMeter

**Citation Strategy:**
- Cite Sharafaldin 2018 as **dataset design** (testbed, attack scenarios)
- Cite Rosay 2022 as **preprocessing justification** (why we use corrected version)
- Mention Dube 2024 (once downloaded) as **additional validation** of CSV issues

---

## 📝 ACTION ITEMS

### Immediate (Week 3)
- [ ] Download LYCOS-IDS2017 CSV from http://lycos-ids.univ-lemans.fr/
- [ ] Download Dube 2024 PDF (Springer paywall - try ResearchGate)
- [ ] EDA: Compare class distribution CIC vs LYCOS
- [ ] Verify SSH-Patator and DoS classes exist in LYCOS

### Week 4 (Preprocessing)
- [ ] Feature selection: Which of 82 features to keep?
- [ ] Client partition: A=Normal+SSH, B=Normal+DoS (validate non-IID)
- [ ] Task sequence: T1 vs T2 data leakage check
- [ ] Handle remaining imbalance (Normal still 10x larger than attacks)

### Documentation (Bab 3.2.2)
- [ ] Subsection: "Dataset CIC-IDS2017 dan Koreksi LYCOS-IDS2017"
- [ ] Table: Feature miscalculations (21 features affected)
- [ ] Figure: Class distribution comparison (CIC vs LYCOS)
- [ ] Justification: Why LYCOS instead of original (methodology rigor)

---

## 🔗 LINKS

- **LYCOS-IDS2017 Dataset:** http://lycos-ids.univ-lemans.fr/
- **LycoSTand Source (C):** http://lycos-ids.univ-lemans.fr/ (same page)
- **Original CIC-IDS2017:** https://www.unb.ca/cic/datasets/ids-2017.html
- **Kaggle Mirror:** https://www.kaggle.com/datasets/hcavsi/cicids2017-dataset

---

**Status:** 2/3 critical papers downloaded (Zhang, Rosay ✅ | Dube ⬜)  
**Next:** Download Dube PDF + LYCOS dataset + EDA
