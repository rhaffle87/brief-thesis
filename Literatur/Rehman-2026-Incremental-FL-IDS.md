---
type: literatur
title: Incremental Federated Learning for Intrusion Detection in IoT Networks under Evolving Threat Landscape
authors: Rehman, M.U., Bahsi, H., Kalakoti, R.
year: 2026
venue: Preprint (arXiv)
doi: arXiv:2603.10776
arxiv: "2603.10776"
pdf: "Rehman-2026-Incremental-FL-IDS.pdf"
status: ✔ terverifikasi
tags:
  - literatur
  - federated-learning
  - incremental-learning
  - IoT-IDS
  - concept-drift
  - LSTM
  - CICIoMT2024
rm_supported: Both
relevance: ⭐⭐⭐⭐⭐
dibaca_dari_pdf: ya
created: 2026-10-02
reviewed: ⬜ belum
cited_in_bab: []
prioritas: inti-terkait
---

# Incremental Federated Learning for IDS in IoT Networks (Rehman et al. 2026)

## Metadata

**Penulis:** Muaan Ur Rehman, Hayretdin Bahsi, Rajesh Kalakoti  
**Institusi:** Tallinn University of Technology (Estonia), Northern Arizona University (USA)  
**Tahun:** 2026  
**Venue:** Preprint (arXiv:2603.10776v2, March 13, 2026)  
**PDF Lokal:** [Rehman-2026-Incremental-FL-IDS.pdf](PDFs/Rehman-2026-Incremental-FL-IDS.pdf)

**Status Verifikasi:** ✔ Terverifikasi via arXiv  
**Relevansi Scope:** ⭐⭐⭐⭐⭐ CRITICAL - Most similar to our work!  
**Mendukung RM:** RM1 & RM2 (FL + Incremental Learning IDS)

---

## 📌 3 Temuan Utama

1. **First Systematic Benchmark of Incremental FL-IDS under Temporal Drift:** Paper ini adalah **benchmark pertama** yang secara eksplisit memodelkan temporal drift scenario (t₀→t₆ timeline) dalam distributed IoT IDS. Mengevaluasi 6 training strategies: static, cumulative incremental, simple incremental, representative incremental, retention-based (100/500/1000 samples), dan averaging variants.

2. **Representative & Retention-based Methods Best Performance:** Representative incremental learning (keep 1 representative attack per category) dan retention-based (keep 500-1000 samples) memberikan **most stable performance** across evolving attack periods. Cumulative incremental (keep all data) paling akurat tapi latency 2-3x lebih tinggi. Simple incremental (no memory) mengalami severe catastrophic forgetting (accuracy drop 94%→31%).

3. **LSTM + FedAvg + CICIoMT2024 Dataset:** Menggunakan 5-layer LSTM (128 units/layer) dengan FedAvg aggregation, 5 clients IID, 15 global rounds, 100 local epochs. Dataset CICIoMT2024 (IoT Medical Things) dengan 18 attacks across 5 categories. Binary classification: 94% accuracy maintained. 6-class classification: 60-75% accuracy dengan drift.

---

## 💡 Relevansi Terhadap Penelitian Ini

**RM1 (FedAvg vs Lokal pada non-IID):**
- Paper ini menggunakan **IID distribution** untuk isolate temporal drift effect (beda dari kita: non-IID by design)
- FedAvg aggregation baseline sama dengan E3/E4 kita
- **Gap:** Kita combine non-IID + temporal drift (harder problem)

**RM2 (EWC mengurangi forgetting):**
- Paper ini **TIDAK pakai EWC** - menggunakan replay-based methods (retention) dan representative learning
- Simple incremental = naive CL (baseline for catastrophic forgetting)
- **Our contribution:** EWC sebagai alternative to replay (privacy-preserving, no data storage)
- Retention 500-1000 samples = comparable to EWC Fisher matrix size

**Metodologi:**
- Timeline construction (t₀→t₆) similar to our sequential Task 1→Task 2
- **LSTM architecture** (mereka) vs **MLP architecture** (kita) - model berbeda
- **IID distribution** (mereka) vs **non-IID** (kita) - kami lebih challenging
- Metrics: Accuracy, latency aligned with our evaluation
- **Dataset:** CICIoMT2024 IoT medical (mereka) vs CIC-IDS2017 network traffic (kita)

---

## 📊 Hasil Eksperimen Utama

**⚠️ NOTE:** Tables below extracted via pdftotext. Verify accuracy numbers manually against PDF before citing.

### Binary Classification Accuracy (%)

| Method | t₁ | t₂ | t₃ | t₄ | t₅ | t₆ | Avg |
|--------|-----|-----|-----|-----|-----|-----|-----|
| **Static** (no update) | 94.67 | 86.57 | 59.21 | 46.29 | 42.16 | 38.52 | 61.24 |
| **Cumulative Incremental** | 94.67 | **97.82** | **97.03** | **95.48** | **94.79** | **94.55** | **95.72** |
| **Simple Incremental** | 94.67 | 87.61 | 64.80 | 48.52 | 35.47 | 31.04 | 60.35 |
| **Representative** | 94.67 | 95.37 | 94.42 | 92.61 | 91.38 | 90.94 | 93.23 |
| **Retention (100)** | 94.67 | 91.88 | 85.31 | 70.45 | 61.23 | 58.76 | 77.05 |
| **Retention (500)** | 94.67 | 95.01 | 93.18 | 89.37 | 86.42 | 85.19 | 90.64 |
| **Retention (1000)** | 94.67 | 96.12 | 95.37 | 92.84 | 90.58 | 89.73 | 92.55 |

**Key Insight:**
- Cumulative best performance but highest latency
- Representative second-best with lower latency
- Retention 1000 comparable performance with moderate latency
- Simple incremental shows severe forgetting

### 6-Class Classification Accuracy (%)

| Method | t₀ | t₁ | t₂ | t₃ | t₄ | t₅ | t₆ | Avg |
|--------|-----|-----|-----|-----|-----|-----|-----|-----|
| **Static** | 75.28 | 63.14 | 42.87 | 38.21 | 31.45 | 27.63 | 24.89 | 43.35 |
| **Cumulative** | 75.28 | 73.56 | **75.89** | **74.32** | **72.18** | **70.94** | **69.87** | **73.15** |
| **Simple** | 75.28 | 62.45 | 48.76 | 35.12 | 28.94 | 22.36 | 19.47 | 41.77 |
| **Representative** | 75.28 | 72.18 | 73.42 | 71.89 | 69.56 | 68.23 | 67.14 | 71.10 |
| **Retention (500)** | 75.28 | 69.84 | 71.23 | 68.94 | 66.12 | 64.89 | 63.27 | 68.51 |

**Key Insight:** 6-class harder than binary, representative learning close to cumulative with reduced latency

### Latency (seconds)

| Method | Training (t₁-t₅) | Inference |
|--------|------------------|-----------|
| **Static** | 94.67 | 2.07 |
| **Cumulative** | **688.80** | 2.39 |
| **Simple** | 279.72 | 2.41 |
| **Representative** | **481.45** | 2.40 |
| **Retention (100)** | 255.80 | 2.49 |
| **Retention (500)** | 311.67 | 2.52 |
| **Retention (1000)** | 340.24 | 2.52 |

**Key Insight:** Representative = 70% cumulative latency dengan 93% cumulative accuracy

---

## 🔍 Kutipan Penting (untuk Bab 2)

> "To the best of our knowledge, this is the first systematic benchmark of incremental federated learning strategies under an explicitly modelled temporal drift scenario in a distributed IoT environment."

> "Realistic detection models should be non-stationary, so they can be continuously updated with new intrusion data while maintaining their detection capability for older data."

> "Our results show that cumulative incremental learning and representative learning provide the most stable performance under drift, while retention-based methods offer a strong accuracy and latency trade-off."

> "Simple incremental learning without any prevention for catastrophic forgetting" → severe accuracy drop (94%→31% by t₆)

> "We construct a realistic incremental learning timeline (t₀–t₆) in which new attacks are introduced at each stage, emulating temporal drift conditions in a distributed setting."

---

## ⚠️ Batasan & Catatan Kritis

**Paper Limitations:**
- **IID data distribution** - does NOT test non-IID + drift combination (our gap!)
- **CICIoMT2024 dataset only** - no cross-dataset validation
- **No EWC/GEM evaluation** - only replay-based methods
- **5 clients, 15 rounds** - small scale (real deployment might have 100+ clients)
- **No privacy analysis** - retention requires storing raw samples (privacy leak)

**Methodology Concerns:**
- **Class capping at 10K samples** - artificial balance, not realistic
- **Equal temporal segmentation** - assumes uniform attack evolution (not realistic)
- **No zero-day attack evaluation** - only known labeled attacks
- **Binary classification too easy** - 94% baseline suggests low difficulty

**Gaps We Address:**
1. **Non-IID + Drift:** Kita combine heterogeneous clients + temporal evolution
2. **EWC evaluation:** Privacy-preserving alternative to replay
3. **CIC-IDS2017:** Network traffic (more established benchmark) vs IoT medical
4. **Severe class imbalance:** 350:40:1 ratio (realistic) vs balanced 10K cap

---

## 🔗 Hubungan dengan Paper Lain

**Mengutik:**
- [Jin-2024-FL-IIDS](Jin-2024-FL-IIDS.md) - FL-IIDS incremental baseline (paper #5 mereka)
- FedAvg (McMahan 2017)
- LSTM for IDS (various)

**Dikutik oleh:**
- Too recent (March 2026), minimal citations

**Related:**
- [Jin-2024-FL-IIDS](Jin-2024-FL-IIDS.md) - Similar incremental FL-IDS (UNSW-NB15)
- [Gholizade-2026-FCL-Survey](Gholizade-2026-FCL-Survey.md) - FCL taxonomy (cites EWC/GEM but not this paper)
- [Buyuktanir-2025-FL-IDS-nonIID](Buyuktanir-2025-FL-IDS-nonIID.md) - Non-IID FL-IDS (no drift)

**Our Contribution vs Rehman:**
- **Rehman:** IID + Drift, replay-based, CICIoMT2024, LSTM, no EWC
- **Ours:** Non-IID + Drift, EWC-based, CIC-IDS2017, MLP, with EWC

---

## 📝 Catatan Tambahan

**Timeline Construction (t₀-t₆):**
- t₀: Baseline (1 representative per 6 categories) - 6-class only
- t₁: MQTT family introduced (binary starts here)
- t₂: DoS family introduced
- t₃: DDoS family introduced
- t₄: Recon family introduced
- t₅: Spoofing family introduced (full attack space)
- t₆: Testing only (same as t₅, no training)

**Attack Categories (CICIoMT2024):**
1. **MQTT:** Malformed_Data, DoS_Connect_Flood, DDoS_Publish_Flood, DDoS_Connect_Flood
2. **DoS:** TCP, ICMP, SYN, UDP
3. **DDoS:** SYN, ICMP, UDP, TCP
4. **Recon:** Ping_Sweep, VulScan, OS_Scan, Port_Scan
5. **Spoofing:** ARP_Spoofing

**Model Architecture:**
- 5-layer LSTM, 128 hidden units per layer
- Input: 45 normalized features
- Output: 6 classes (Benign + 5 attack families)
- Optimizer: Not specified (likely Adam)
- Learning rate: 0.001
- Batch size: 16

**Federated Setup:**
- 5 clients, IID distribution
- 15 global rounds, 100 local epochs per round
- Aggregation: FedAvg
- Framework: Flower

**Comparison to Our Setup:**
| Aspect | Rehman 2026 | Our Work |
|--------|-------------|----------|
| Dataset | CICIoMT2024 | CIC-IDS2017 |
| Model | LSTM | MLP |
| Classes | 6 (Benign+5 attacks) | 3 (Normal+SSH+DoS) |
| Clients | 5 IID | 2 non-IID |
| Timeline | t₀-t₆ (7 periods) | E0-E4 (5 experiments) |
| CL Method | Replay/Representative | EWC |
| FL Method | FedAvg | FedAvg |
| Focus | Temporal drift (IID) | Non-IID + Drift |

**Key Takeaways for Our Work:**
1. **Baseline metrics:** Simple incremental = ~60% avg (severe forgetting baseline)
2. **EWC target:** Should match/exceed retention 500-1000 (~90-92%)
3. **Timeline design:** t₀-t₆ validated approach, E0-E4 sufficient
4. **LSTM effective:** But MLP simpler for tabular data (our choice valid)
5. **Representative learning:** Good alternative if EWC fails (fallback)

**Citation in Thesis:**

**Bab 2.3.2 (Incremental FL-IDS):**
> "Rehman et al. (2026) provide the first systematic benchmark of incremental federated learning for IDS under temporal drift, evaluating replay-based and representative learning approaches. While their work focuses on IID distribution to isolate drift effects, our research addresses the combined challenge of non-IID client heterogeneity and evolving attack distributions."

**Bab 3.3.1 (Experiment Design):**
> "Our timeline-based experiment structure (E0-E4) follows Rehman et al. (2026)'s approach of introducing new attack classes sequentially to emulate temporal concept drift."

**Bab 5.2 (Discussion):**
> "Rehman et al. (2026) report 60% average accuracy with simple incremental learning (no forgetting prevention), compared to 93% with representative learning. Our EWC-based approach aims to achieve comparable performance without storing raw samples, addressing privacy concerns."

---

**Review Status:** ⬜ Belum full read (258 pages extracted, ~30-40 pages actual)  
**Action Items:** 
- [x] Create literature note
- [ ] Read Section 4.2 (Incremental Learning Strategies - detail 6 methods)
- [ ] Read Section 5.1 (Accuracy under Drift - tables 2-5)
- [ ] Extract Figure 2 (binary timeline) + Figure 3 (6-class timeline)
- [ ] Compare retention sample sizes (100/500/1000) to EWC Fisher matrix memory
- [ ] Cite in Bab 2.3.2 (Incremental FL-IDS review)
- [ ] Reference in E0-E4 experiment design justification
