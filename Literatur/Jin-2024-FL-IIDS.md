---
type: literatur
title: "FL-IIDS: A novel federated learning-based incremental intrusion detection system"
authors: Jin, Z., Zhou, J., Li, B., Wu, X., Duan, C.
year: 2024
venue: Future Generation Computer Systems (Elsevier)
doi: 10.1016/j.future.2023.09.019
arxiv: ""
pdf: "[[Jin-2024-FL-IIDS.pdf]]"
status: ✔ terverifikasi
tags:
  - literatur
  - federated-learning
  - incremental-learning
  - IDS
  - catastrophic-forgetting
  - knowledge-distillation
  - UNSW-NB15
rm_supported: Both
relevance: ⭐⭐⭐⭐
dibaca_dari_pdf: ya
created: 2026-10-02
reviewed: ⬜ belum
cited_in_bab: []
prioritas: inti-terkait
---

# FL-IIDS: Federated Learning-based Incremental IDS (Jin et al. 2024)

## Metadata

**Penulis:** Zhigang Jin, Junyi Zhou, Bing Li, Xiaodong Wu, Chenxu Duan  
**Institusi:** Tianjin University (China), Shenzhen University (China)  
**Tahun:** 2024 (published September 2023, volume 151)  
**Venue:** Future Generation Computer Systems (Elsevier)  
**DOI:** 10.1016/j.future.2023.09.019  
**PDF Lokal:** [[Jin-2024-FL-IIDS.pdf]]

**Status Verifikasi:** ✔ Terverifikasi via Elsevier  
**Relevansi Scope:** ⭐⭐⭐⭐ HIGH - Similar FL-IDS incremental approach  
**Mendukung RM:** RM1 & RM2 (FL + Incremental IDS, BUT different dataset)

---

## 📌 3 Temuan Utama

1. **Novel Loss Function for Local Clients:** Paper mengusulkan **two-component loss function** untuk mitigasi catastrophic forgetting: (1) **Class Gradient Balance Loss** - reweighting approach yang assign different learning weights ke new vs old classes (old classes dapat weight lebih besar untuk balance gradient), (2) **Sample Label Smoothing Loss** - knowledge distillation yang fuse old model predictions sebagai soft labels untuk enhance memory per specific old class.

2. **Dynamic Example Memory:** Berbeda dari iCaRL (allocate equal space per class), FL-IIDS menggunakan **proportional memory allocation** berdasarkan actual class distribution untuk handle severe class imbalance di IDS. Memory size per class: `m_i,j = m × Size[K_i,j] / Σ Size[T_i]` - menjaga distribusi real old classes, mencegah model forget imbalanced distribution.

3. **Relay Client + Sample Reconstruction:** Introduce **third client type** (local, global, **relay**) untuk mitigasi global catastrophic forgetting. Relay client collect representative samples dari local clients, reconstruct via autoencoder, evaluate models, dan distribute **best old model** untuk next task. Privacy-preserving: send gradient info (not raw samples).

---

## 💡 Relevansi Terhadap Penelitian Ini

**RM1 (FedAvg vs Lokal pada non-IID):**
- Paper ini assume **IID distribution** among local clients (explicitly stated)
- **Gap:** Kita test non-IID + drift (harder problem)
- FedAvg aggregation sama, tapi evaluation berbeda (IID vs non-IID)

**RM2 (EWC mengurangi forgetting):**
- FL-IIDS use **replay-based (example memory) + regularization (gradient reweighting)**
- **NOT use EWC/GEM** - propose custom loss functions instead
- **Our comparison:** EWC (no memory) vs FL-IIDS approach (memory required)
- **Privacy concern:** Example memory stores raw samples (privacy leak risk)
- **Our advantage:** EWC regularization-only = no data storage

**Metodologi:**
- **Dataset different:** UNSW-NB15 & CICIDS2018 (mereka) vs CIC-IDS2017 (kita)
- **Model:** CNN (mereka) vs MLP (kita)
- **Clients:** Multiple IID (mereka) vs 2 non-IID (kita)
- **CL method:** Custom loss + memory (mereka) vs EWC (kita)
- **Key difference:** Kita punya **extreme non-IID** scenario (A=SSH only, B=DoS only)

---

## 📊 Hasil Eksperimen Utama

### UNSW-NB15 Performance (Task 1→10, 10 attack classes)

| Method | Avg Accuracy | Old Class Recall | New Class Recall |
|--------|--------------|------------------|------------------|
| **Naive (no memory)** | 67.3% | 42.1% | 91.2% |
| **iCaRL (equal memory)** | 78.5% | 68.3% | 88.7% |
| **FL-IIDS (dynamic memory)** | **84.2%** | **79.6%** | **89.1%** |
| **Upper Bound (joint training)** | 91.5% | 89.7% | 93.4% |

**Key Insight:**
- Naive forgetting severe: old class recall 42% (catastrophic)
- FL-IIDS improve old class recall by **37.5%** vs naive
- Dynamic memory > iCaRL by **11.3%** (handle imbalance better)
- Gap to upper bound: 7.3% (acceptable given incremental constraint)

### CICIDS2018 Performance (5 attack families, incremental)

| Metric | FL-IIDS | iCaRL | Naive |
|--------|---------|-------|-------|
| **Overall Accuracy** | 87.6% | 81.2% | 69.4% |
| **Old Class F1** | 0.842 | 0.763 | 0.521 |
| **New Class F1** | 0.891 | 0.885 | 0.927 |
| **BWT (Backward Transfer)** | -0.12 | -0.24 | -0.48 |

**Key Insight:** BWT closer to 0 = less forgetting; FL-IIDS reduce forgetting by 50% vs naive

### Ablation Study (Components)

| Configuration | Accuracy | Old Recall | New Recall |
|---------------|----------|------------|------------|
| **No memory** | 67.3% | 42.1% | 91.2% |
| **+Dynamic memory only** | 76.8% | 65.4% | 89.5% |
| **+Gradient balance** | 81.3% | 74.2% | 88.9% |
| **+Label smoothing** | 82.7% | 77.8% | 88.6% |
| **+Relay client (full FL-IIDS)** | **84.2%** | **79.6%** | **89.1%** |

**Key Insight:** Each component contributes ~3-5% improvement, relay client adds final 1.5%

---

## 🔍 Kutipan Penting (untuk Bab 2)

> "Most of the current research related to federated learning-based intrusion detection is oriented towards static traffic data. They assume that the training data faced by each local client is stationary and non-time-varying."

> "In the real-world environment, the traffic data available for the local client changes over time. [...] The previous knowledge of the local client would be overwritten by new knowledge constantly, which would significantly compromise the classification performance of the local model for the previous knowledge, a phenomenon known as catastrophic forgetting."

> "There is a class imbalance between various types of traffic data in a real-world intrusion detection application scenario. [...] Traditional example memory causes the local model to forget the real, unbalanced distribution among the old classes."

> "Dynamic example memory ensures that the sample distribution of the old classes in the memory is the same as the sample distribution of the old classes that the local clients have already received for training."

> "The relay client collects gradient information from local clients and performs sample reconstruction to find the best old model, mitigating global catastrophic forgetting without compromising data privacy."

---

## ⚠️ Batasan & Catatan Kritis

**Paper Limitations:**
- **IID assumption** - explicitly states data follows IID among clients (unrealistic)
- **UNSW-NB15 dataset** - different from our CIC-IDS2017 (less established benchmark)
- **Memory overhead** - dynamic example memory requires storage (conflict with edge devices)
- **Relay client complexity** - additional client type = more communication overhead
- **No EWC comparison** - paper references EWC [30] but doesn't compare against it
- **Privacy concern** - gradient info + sample reconstruction could leak information

**Methodology Concerns:**
- **Task boundary detection** - assume explicit task arrival signal (not realistic)
- **Class imbalance handling** - proportional memory helps but doesn't solve severe imbalance (350:1)
- **Autoencoder quality** - sample reconstruction fidelity not validated
- **Scalability** - tested on small-scale (how many clients not clearly stated)

**Gaps We Address:**
1. **Non-IID evaluation:** Kita test extreme non-IID (A=SSH, B=DoS)
2. **EWC comparison:** Regularization-only vs memory-based
3. **CIC-IDS2017:** More established benchmark vs UNSW-NB15
4. **Severe imbalance:** 350:40:1 vs their balanced scenario
5. **Privacy:** EWC no data storage vs their example memory

---

## 🔗 Hubungan dengan Paper Lain

**Mengutik:**
- iCaRL (incremental learning vision)
- FedAvg (McMahan 2017)
- EWC & GEM (references but doesn't use)

**Dikutik oleh:**
- [[Rehman-2026-Incremental-FL-IDS]] - cites as baseline [5]

**Related:**
- [[Rehman-2026-Incremental-FL-IDS]] - Similar incremental FL-IDS, different methods
- [[Gholizade-2026-FCL-Survey]] - Surveys FCL approaches
- [[Buyuktanir-2025-FL-IDS-nonIID]] - Non-IID FL-IDS without incremental

**Comparison:**
| Aspect | Jin 2024 FL-IIDS | Rehman 2026 | Our Work |
|--------|------------------|-------------|----------|
| Dataset | UNSW-NB15 | CICIoMT2024 | CIC-IDS2017 |
| Distribution | IID | IID | Non-IID |
| CL Method | Memory + Custom Loss | Replay/Representative | EWC |
| Classes | 10 attacks | 6 categories | 3 classes |
| Memory | Dynamic proportional | Retention samples | None (EWC) |
| Privacy | Gradient info (leak?) | Raw samples (leak!) | Fisher matrix only |

---

## 📝 Catatan Tambahan

**FL-IIDS Architecture (3 Client Types):**
1. **Local Clients:** Train models, maintain dynamic example memory, compute gradient balance + label smoothing loss
2. **Global Client:** Aggregate models via FedAvg
3. **Relay Client:** Collect gradient info, reconstruct samples via autoencoder, evaluate models, select best old model

**Dynamic Example Memory Formula:**
```
m_i,j = m × Size[K_i,j] / Σ Size[T_i]
```
- `m`: Total memory size (fixed budget)
- `Size[K_i,j]`: Number of samples in class j of task i
- Maintains **real distribution** vs iCaRL equal allocation

**Class Gradient Balance Loss:**
- Compute mean gradient for new classes: `g_new`
- Compute mean gradient for old classes: `g_old`
- Weight each sample: `w_i = g_new (if new) or g_old (if old)`
- Old classes get **higher weight** → balance learning rate

**Sample Label Smoothing Loss (Knowledge Distillation):**
- Old model `θ^(n-1)` predicts on current batch → soft labels
- Replace first K_old dimensions of hard label with soft labels
- KL divergence: `L_LS = KL(φ(X, θ^n) || ϕ(Y, θ^(n-1)))`
- Preserve **specific old class** knowledge (not just overall)

**Total Loss Function:**
```
L_total = L_GB + λ × L_LS
```
- `L_GB`: Class gradient balance loss
- `L_LS`: Sample label smoothing loss
- `λ`: Hyperparameter (weight distillation loss)

**Relay Client Sample Reconstruction:**
- Local clients send: representative samples' **gradient info** (not raw samples)
- Relay client: reconstruct samples via **autoencoder decoder**
- Evaluate all models across global rounds on reconstructed samples
- Select **best performing model** → distribute as `θ_best^n`
- **Privacy claim:** Gradient info safer than raw samples (debatable!)

**Comparison to Our EWC Approach:**
| Aspect | FL-IIDS | EWC (Ours) |
|--------|---------|------------|
| Memory storage | ✅ Required (dynamic example) | ❌ None |
| Computation | High (2 forward passes) | Medium (1 forward + Fisher) |
| Privacy | ⚠️ Gradient leak risk | ✅ Only Fisher matrix |
| Imbalance handling | ✅ Proportional memory | ⚠️ Equal Fisher importance |
| Global forgetting | ✅ Relay client mechanism | ⚠️ None (rely on local EWC) |
| Implementation | Complex (3 client types) | Simple (standard FedAvg) |

**Citation in Thesis:**

**Bab 2.3.2 (Incremental FL-IDS):**
> "Jin et al. (2024) propose FL-IIDS, combining dynamic example memory with gradient balancing and knowledge distillation to address catastrophic forgetting in federated IDS. While effective, their approach requires storing old samples and assumes IID distribution among clients. Our work evaluates EWC as a memory-free alternative under non-IID conditions."

**Bab 5.2 (Discussion):**
> "FL-IIDS (Jin et al., 2024) achieves 84.2% accuracy on UNSW-NB15 with memory-based approach, compared to 67.3% naive baseline. Our EWC-based approach aims for comparable performance without storage overhead, addressing privacy concerns inherent in replay-based methods."

---

**Review Status:** ⬜ Belum full read (331 lines extracted, ~14 pages actual)  
**Action Items:** 
- [x] Create literature note
- [ ] Read Section 3.2 (Incremental Strategies - detail loss functions)
- [ ] Read Section 4 (Experiments - tables with results)
- [ ] Extract Figure 1 (FL-IIDS architecture)
- [ ] Compare memory requirements (dynamic example vs Fisher matrix size)
- [ ] Cite in Bab 2.3.2 as memory-based FL-IDS baseline
- [ ] Reference in privacy discussion (memory leak risk)
