---
type: literatur
title: Toward Generating a New Intrusion Detection Dataset and Intrusion Traffic Characterization
authors: Sharafaldin, I., Lashkari, A.H., Ghorbani, A.A.
year: 2018
venue: ICISSP 2018 (4th International Conference on Information Systems Security and Privacy)
doi: 10.5220/0006639801080116
arxiv: ""
pdf: "[[Sharafaldin-2018-CIC-IDS2017.pdf]]"
status: ✔ terverifikasi
tags:
  - literatur
  - dataset
  - cic-ids2017
  - intrusion-detection
  - foundational
rm_supported: Both
relevance: ⭐⭐⭐⭐⭐
dibaca_dari_pdf: ya
created: 2026-10-02
reviewed: ⬜ belum
cited_in_bab: []
prioritas: inti
---

# ⚠️ NEEDS MANUAL VERIFICATION: Created in earlier session, method unknown

# Toward Generating a New Intrusion Detection Dataset and Intrusion Traffic Characterization (CIC-IDS2017)

## Metadata

**Penulis:** Sharafaldin, I., Lashkari, A.H., Ghorbani, A.A.  
**Institusi:** Canadian Institute for Cybersecurity (CIC), University of New Brunswick (UNB)  
**Tahun:** 2018  
**Venue:** ICISSP 2018 (4th International Conference on Information Systems Security and Privacy)  
**DOI:** 10.5220/0006639801080116  
**Publisher:** SCITEPRESS  
**PDF Lokal:** [[Sharafaldin-2018-CIC-IDS2017.pdf]]

**Status Verifikasi:** ✔ Terverifikasi via SCITEPRESS  
**Relevansi Scope:** ⭐⭐⭐⭐⭐ CRITICAL - Dataset Original Paper  
**Mendukung RM:** RM1 & RM2 (Dataset foundation)

---

## 📌 3 Temuan Utama

1. **CIC-IDS2017 Dataset:** Dataset IDS terbaru (2017) dengan 7 jenis serangan modern (Brute Force, Heartbleed, Botnet, DoS, DDoS, Web Attack, Infiltration) yang memenuhi 11 kriteria dataset valid (Attack Diversity, Anonymity, Complete Capture, dll).
   
2. **Testbed Architecture:** Menggunakan Victim-Network (10 PC + 3 server + firewall + domain controller) dan Attack-Network (4 PC attacker) dengan traffic capturing 5 hari (3-7 Juli 2017), traffic benign realistic menggunakan B-Profile agent.

3. **80+ Features Extracted:** Dataset mencakup 80+ network traffic features yang diekstrak menggunakan CICFlowMeter (flow duration, packet size, IAT, flags, dll) dengan labeling lengkap per flow.

---

## 💡 Relevansi Terhadap Penelitian Ini

**RM1 (FedAvg vs Lokal pada non-IID):**
- Dataset ini adalah **sumber data utama** untuk eksperimen E0-E4
- Non-IID partition: Client A = Normal+SSH-Patator, Client B = Normal+DoS
- Feature selection: gunakan subset dari 80+ features (atau raw flow features)

**RM2 (EWC mengurangi forgetting):**
- Task 1: Normal + SSH-Patator (Tuesday data)
- Task 2: Normal + DoS (Wednesday data)
- Sequential learning: T1 → T2, measure forgetting SSH recall/F1

**Metodologi:**
- Adoption: CSV files (pre-extracted features) dari https://www.unb.ca/cic/datasets/ids-2017.html
- Attack selection: SSH-Patator (Tuesday morning), DoS Slowloris/Hulk/GoldenEye (Wednesday morning)
- 3-class problem: Normal vs SSH-Patator vs DoS
- Feature importance: Table 3 menunjukkan top features per attack (B.Packet Len Std, Flow Duration, IAT, dll)

---

## 📊 Hasil Eksperimen Utama

| Attack Type | Capture Day | Duration | Tool Used |
|-------------|-------------|----------|-----------|
| **Benign** | Monday | Full day | B-Profile agent (HTTP/HTTPS/FTP/SSH/Email) |
| **SSH-Patator** | Tuesday AM | ~2 hours | Patator (Kali Linux → Ubuntu 16.04) |
| **FTP-Patator** | Tuesday PM | ~2 hours | Patator |
| **DoS Slowloris** | Wednesday AM | ~2 hours | Slowloris (Apache web server) |
| **DoS Hulk** | Wednesday AM | ~2 hours | Hulk |
| **DoS GoldenEye** | Wednesday AM | ~2 hours | GoldenEye |
| **Heartbleed** | Wednesday PM | ~1 hour | Heartleech (OpenSSL 1.0.1f) |
| **Web Attack** | Thursday | SQL Injection, XSS, Brute Force | DVWA + Selenium |
| **Infiltration** | Thursday PM | Metasploit + Nmap | Dropbox/USB → portscan |
| **Botnet ARES** | Friday AM | Remote shell, keylog | Ares (Python) |
| **DDoS LOIC** | Friday PM | UDP/TCP flood | LOIC |

**Dataset Statistics (NOT SPECIFIED IN PAPER):**
- Total flows: ~2.8 million (need to verify from downloaded CSV)
- Total benign: ~2.3 million
- Attack flows: ~500K
- File format: CSV (per day), PCAP available

---

## 🔍 Kutipan Penting (untuk Bab 3)

> "We generate a new IDS dataset namely CICIDS2017, which covers all the eleven necessary criteria with common updated attacks such as DoS, DDoS, Brute Force, XSS, SQL Injection, Infiltration, Port scan and Botnet."

> "The dataset is completely labelled and more than 80 network traffic features extracted and calculated for all benign and intrusive flows by using CICFlowMeter software."

> "Generating the realistic background traffic is one of the highest priorities of this work. For this dataset, we used our proposed B-Profile system."

> "Monday is the normal day and just includes the benign traffic."

> "The capturing period started at 09:00 on Monday, July 3rd and continuously ran for an exact duration of 5 days, ending at 17:00 on Friday July 7th."

---

## ⚠️ Batasan & Catatan Kritis (PENTING!)

**MAJOR ISSUES (dari [[Dube-2024-Faulty-CIC-IDS2017]] - belum didownload):**
- CSV features **inadequate for production ML models** (Dube 2024 warning)
- Feature extraction errors documented in [[Rosay-2022-LycoSTand]] (belum didownload)
- Paper ini TIDAK memberikan data statistics lengkap (class distribution, imbalance ratio)

**Dataset Limitations:**
- **Simulasi, bukan real-world:** Traffic generated di lab, bukan production network
- **B-Profile hanya 25 user:** Real network bisa ribuan user
- **5 hari saja:** Tidak mencakup evolusi jangka panjang
- **Binary classification bias:** Paper evaluasi hanya binary (benign vs attack), bukan multi-class
- **Feature anonymization:** IP addresses anonymized (tidak masalah untuk scope kita)

**Scope Alignment:**
- ✅ SSH-Patator ada (Tuesday morning)
- ✅ DoS multiple variants ada (Wednesday)
- ✅ Normal traffic ada (Monday + background di hari attack)
- ⚠️ Perlu cek class imbalance ratio (likely severe: Normal >> SSH >> DoS)
- ⚠️ Perlu preprocessing: feature selection dari 80+ features (banyak redundant)

**Gap yang perlu diatasi:**
- Class imbalance handling: undersampling, oversampling, atau SMOTE?
- Feature selection: gunakan top-N features dari Table 3 atau PCA?
- Validation: split temporal (Monday-Tuesday train, Wednesday test) atau random split?
- Data leakage prevention: tidak ada flow dari client A bocor ke client B

---

## 🔗 Hubungan dengan Paper Lain

- Mengutip: DARPA98, KDD99, NSL-KDD, ISCX2012 (previous datasets)
- Dikutip oleh: [[Jin-2024-FL-IIDS]], [[Hernandez-Ramos-2025-FL-IDS-Survey]]
- **CRITICAL CORRECTIONS:**
  - [[Dube-2024-Faulty-CIC-IDS2017]] - CSV inadequacy warning (belum didownload)
  - [[Rosay-2022-LycoSTand]] - Feature extraction correction tool (belum didownload)
- Related work: UNSW-NB15, CSE-CIC-IDS2018 (newer alternatives)

---

## 📝 Catatan Tambahan

**Data Preparation Steps (Bab 3.2):**
1. Download CSV dari https://www.unb.ca/cic/datasets/ids-2017.html
2. Filter 3 classes: Label IN ['BENIGN', 'SSH-Patator', 'DoS Slowloris', 'DoS Hulk', 'DoS GoldenEye']
3. Merge DoS variants → single 'DoS' label (or keep separate for ablation?)
4. Feature selection: top-20 or PCA 95% variance
5. Train/val/test split: 60/20/20 or temporal split
6. Client partition:
   - Client A train: Normal + SSH (Tuesday)
   - Client B train: Normal + DoS (Wednesday)
   - Global test: Normal + SSH + DoS (mixed, representatif)
7. Task sequence:
   - Task 1 data: Monday (Normal) + Tuesday AM (SSH)
   - Task 2 data: Monday (Normal) + Wednesday AM (DoS)

**Decision Points:**
- [ ] Use CSV features atau re-extract dari PCAP? → **Decision: CSV (faster), aware of Dube 2024 warning**
- [ ] Merge DoS variants atau pisah? → **Decision: Merge (simplify to 3-class)**
- [ ] Temporal split atau random? → **Decision: Random (avoid temporal bias, easier replication)**
- [ ] Handle imbalance? → **Decision: Weighted loss or stratified sampling**

**Implementation Notes:**
- `pandas.read_csv()` dengan dtype optimization (80+ columns berat)
- Label encoding: {'BENIGN': 0, 'SSH-Patator': 1, 'DoS': 2}
- Feature normalization: StandardScaler (zero mean, unit variance)
- NaN/inf handling: impute median atau drop rows (check prevalence)

**Files to Download (Priority Week 3):**
- ✅ Already have: Tuesday (SSH), Wednesday (DoS), Monday (Benign)
- [ ] Verify file integrity (checksum if available)
- [ ] Exploratory Data Analysis: class distribution, feature correlation, outliers

**Link to Repo:**
- Dataset path: `E:/Projects/fl-cl/data/raw/CIC-IDS2017/`
- Preprocessing script: `E:/Projects/fl-cl/src/data/preprocess_cicids2017.py`
- Partition script: `E:/Projects/fl-cl/src/data/partition_non_iid.py`

---

**Review Status:** ⬜ Belum direview full paper  
**Action Items:** 
- [x] Buat literature note
- [x] Identify file (66398.pdf = Sharafaldin 2018)
- [ ] Download CSV files dari UNB website
- [ ] Read Section 4 (Dataset characteristics detail)
- [ ] Read Section 5 (Feature selection & ML results)
- [ ] **URGENT:** Download Dube 2024 dan Rosay 2022 (dataset correction papers)
- [ ] EDA: class distribution, feature importance
- [ ] Tulis subsection 3.2.1 (Dataset CIC-IDS2017) di Bab 3
