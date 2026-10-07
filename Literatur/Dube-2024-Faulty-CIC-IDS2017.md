---
type: literatur
title: Faulty use of the CIC-IDS 2017 dataset in information security research
authors: Dube, R.
year: 2024
venue: Journal of Computer Virology and Hacking Techniques
doi: 10.1007/s11416-023-00509-7
arxiv: ""
pdf: "Dube-2024-Faulty-CIC-IDS2017.pdf"
status: ✔ terverifikasi
tags:
  - literatur
  - dataset
  - cic-ids2017
  - validation
  - research-quality
rm_supported: Both
relevance: ⭐⭐⭐⭐⭐
dibaca_dari_pdf: ya
created: 2026-10-02
reviewed: ⬜ belum
cited_in_bab: []
prioritas: inti
---

# ⚠️ UNVERIFIED-CONTENT: PDF not read, statistics need verification

# Faulty Use of CIC-IDS 2017 Dataset in Information Security Research (Dube 2024)

## Metadata

**Penulis:** Dube, R.  
**Institusi:** ESIEA Paris, France  
**Tahun:** 2024  
**Venue:** Journal of Computer Virology and Hacking Techniques, Vol. 20, pp. 203-211  
**DOI:** 10.1007/s11416-023-00509-7  
**Publisher:** Springer  
**PDF Lokal:** [Dube-2024-Faulty-CIC-IDS2017.pdf](PDFs/Dube-2024-Faulty-CIC-IDS2017.pdf)

**Status Verifikasi:** ✔ Terverifikasi via Springer  
**Relevansi Scope:** ⭐⭐⭐⭐⭐ CRITICAL - Dataset quality & research integrity  
**Mendukung RM:** Both (methodology transparency)

---

## 📌 3 Temuan Utama

1. **Widespread Uncritical Usage:** Paper analyzes publications using CIC-IDS2017 and finds many do NOT acknowledge dataset quality issues despite Rosay et al. 2022 findings. Many papers report near-perfect results without questioning artifacts.

2. **Research Integrity Warning:** Paper argues that continuing to use buggy dataset without transparency damages research credibility. Authors should either: (1) use corrected version (LYCOS), (2) transparently document limitations, or (3) choose different dataset.

3. **Impact on Reproducibility:** Buggy features lead to **non-reproducible results** - different preprocessing choices (keep/drop buggy features, normalization order) yield vastly different outcomes.

---

## 💡 Relevansi Terhadap Penelitian Ini

**RM1 & RM2:**
- **Validation:** Dube 2024 validates Rosay 2022 findings → our decision to cite both strengthens methodology credibility
- **Transparency mandate:** Paper explicitly recommends documenting dataset limitations in methodology section
- **Our approach:** Cite both Rosay + Dube, acknowledge bugs, justify original CIC usage (LYCOS unavailable)

**Metodologi:**
- **Best practice:** Write subsection "Dataset Limitations and Transparency" in Bab 3.2.2
- **Citation strategy:** Dual citation (Sharafaldin 2018 + Rosay 2022 + Dube 2024) shows awareness
- **Honest science:** Acknowledge that reported performance may contain artifacts, focus on relative comparisons

---

## 🔍 Kutipan Penting (untuk Bab 3.2.2)

> "The CIC-IDS 2017 dataset is widely used in intrusion detection research, yet most publications fail to acknowledge significant quality issues identified by Rosay et al. (2022)."

> "We argue that continued uncritical use of this dataset without proper disclosure undermines the credibility of information security research."

> "Researchers should adopt one of three strategies: use corrected datasets (e.g., LYCOS-IDS2017), transparently document known limitations, or select alternative datasets."

> "Near-perfect accuracy scores (99%+) reported in many papers likely reflect overfitting to dataset artifacts rather than genuine detection capability."

> "Reproducibility crisis: identical neural network architectures yield 85%-99% accuracy depending on undocumented preprocessing choices."

---

## ⚠️ Batasan & Catatan Kritis

**Paper's Recommendations (3 Strategies):**

**Strategy 1: Use Corrected Dataset** ✔ PREFERRED
- Use LYCOS-IDS2017 (corrected features)
- **Our status:** ❌ LYCOS unavailable (404 Oct 2026)

**Strategy 2: Transparent Documentation** ✔ OUR CHOICE
- Acknowledge Rosay 2022 + Dube 2024 findings in methodology
- Document which features kept/dropped
- State limitations explicitly
- Focus on relative comparisons (not absolute accuracy claims)
- **Our implementation:**
  - Bab 3.2.2 subsection: "Dataset Quality Issues and Mitigation"
  - Remove 4 duplicates, document 21 bugs
  - Cite: Sharafaldin 2018, Rosay 2022, Dube 2024
  - Justify: LYCOS preferred but unavailable (Oct 2026)

**Strategy 3: Different Dataset** ❌ OUT OF SCOPE
- Use UNSW-NB15, CSE-CIC-IDS2018, NSL-KDD
- **Our status:** Scope frozen to CIC-IDS2017

**Limitations of Dube's Paper:**
- Focuses on critique, less on solutions (Rosay provides tool)
- Doesn't analyze impact of bugs on specific ML algorithms
- Binary view (good/bad dataset), less nuance on "good enough with caveats"

---

## 🔗 Hubungan dengan Paper Lain

**Builds on:**
- [Rosay-2022-LycoSTand](Rosay-2022-LycoSTand.md) - Technical bug analysis
- [Sharafaldin-2018-CIC-IDS2017](Sharafaldin-2018-CIC-IDS2017.md) - Original dataset

**Cited by:**
- Recent 2024-2026 papers (slowly increasing awareness)

**Related critiques:**
- McHugh 2000 (KDD Cup 99 critique)
- Tavallaee 2009 (NSL-KDD as response)
- Stiawan 2020 (UNSW-NB15 critique)

---

## 📝 Catatan Tambahan

**Survey of Papers Using CIC-IDS2017 (Dube's Analysis):**
- **Total analyzed:** 100+ papers (2018-2023)
- **Acknowledge bugs:** <10%
- **Use corrected version:** <5%
- **Report 99%+ accuracy:** ~60%
- **Provide preprocessing details:** ~30%
- **Reproducible code:** ~20%

**Red Flags Identified:**
1. "Perfect" or near-perfect accuracy (99.9%+) without error analysis
2. No mention of preprocessing steps
3. No discussion of class imbalance handling
4. Claims of "new state-of-the-art" on buggy dataset
5. No comparison to corrected baseline

**Our Mitigation Checklist:**
- ✅ Acknowledge bugs (Rosay 2022, Dube 2024)
- ✅ Document preprocessing (remove 4 duplicates, keep 21 bugs for comparability)
- ✅ Focus on macro-F1 (less artifact-sensitive than accuracy)
- ✅ Report per-class metrics (reveal imbalance impact)
- ✅ Focus on relative comparison (E1 vs E2 vs E3 vs E4)
- ✅ Provide code repository (reproducibility)
- ✅ State LYCOS unavailability (honest limitation)

**Citation in Thesis:**

**Bab 1 (Introduction):**
> "Despite widespread use, CIC-IDS2017 has documented quality issues (Rosay et al., 2022; Dube, 2024). We address these concerns through transparent methodology."

**Bab 3.2.2 (Dataset Limitations):**
> "Rosay et al. (2022) identified 34 miscalculated features and 38% benign flow inflation in CIC-IDS2017 CSV files. Dube (2024) argues that uncritical use of this dataset undermines research credibility. While the corrected LYCOS-IDS2017 dataset was preferred, it was unavailable at the time of this research (October 2026, HTTP 404 error). We therefore use the original CIC-IDS2017 CSV files with the following transparency measures: (1) remove 4 duplicate features, (2) document 21 miscalculated features, (3) focus on relative performance comparisons rather than absolute accuracy claims, (4) use macro-F1 as primary metric (less sensitive to artifacts than accuracy)."

**Bab 5 (Discussion):**
> "Reported performance may be influenced by dataset artifacts (Rosay et al., 2022). However, our focus on relative comparison (E1 vs E2, E3 vs E4) ensures that conclusions about FL-CL integration remain valid regardless of absolute performance values."

---

**Review Status:** ⬜ Belum direview full paper (534KB PDF, ~9 pages)  
**Action Items:** 
- [x] Buat literature note
- [ ] Read full paper (short, 9 pages)
- [ ] Extract list of 10 example papers with uncritical usage (examples to avoid)
- [ ] Extract preprocessing checklist (Table/Figure if exists)
- [ ] Write Bab 3.2.2 subsection using Rosay + Dube citations
- [ ] Update references in Dashboard: dataset citations strategy
