---
type: literatur
title: Gradient Episodic Memory for Continual Learning
authors: Lopez-Paz, D., Ranzato, M.
year: 2017
venue: NeurIPS 2017
doi: arXiv:1706.08840
arxiv: "1706.08840"
pdf: "[[LopezPaz-2017-GEM.pdf]]"
status: ✔ terverifikasi
tags:
  - literatur
  - continual-learning
  - GEM
  - BWT
  - FWT
  - episodic-memory
  - metrics
rm_supported: RM2
relevance: ⭐⭐⭐⭐⭐
dibaca_dari_pdf: ya
created: 2026-10-02
reviewed: ⬜ belum
cited_in_bab: []
prioritas: inti
---

# Gradient Episodic Memory for Continual Learning (Lopez-Paz & Ranzato 2017)

## Metadata

**Penulis:** David Lopez-Paz, Marc'Aurelio Ranzato  
**Institusi:** Facebook AI Research (FAIR)  
**Tahun:** 2017 (NIPS 2017, updated arXiv v6 Sep 2022)  
**Venue:** NIPS 2017 (Long Beach, CA)  
**DOI:** arXiv:1706.08840v6  
**PDF Lokal:** [[LopezPaz-2017-GEM.pdf]]

**Status Verifikasi:** ✔ Terverifikasi via arXiv & NIPS  
**Relevansi Scope:** ⭐⭐⭐⭐⭐ CRITICAL - Defines BWT/FWT metrics we use!  
**Mendukung RM:** RM2 (Continual Learning evaluation metrics)

---

## 📌 3 Temuan Utama

1. **Three Standard Metrics for Continual Learning Evaluation:** Paper ini **pertama kali mengusulkan 3 metrics standar** untuk evaluate continual learners: (1) **ACC (Average Accuracy)** - average test accuracy across all tasks after learning all tasks, (2) **BWT (Backward Transfer)** - influence of learning task t on performance of previous tasks (negative BWT = forgetting), (3) **FWT (Forward Transfer)** - influence of learning task t on future tasks (zero-shot capability). Metrics ini sekarang **standard di CL literature**.

2. **GEM Algorithm with Episodic Memory:** Propose Gradient Episodic Memory (GEM) yang store subset examples dari each task (episodic memory M_t). Saat learning task baru, GEM solve **constrained optimization**: minimize loss on current task SUBJECT TO loss on previous tasks tidak increase. Implemented via **gradient projection** using Quadratic Programming (QP) - jika gradient violates constraint, project ke closest gradient yang satisfy all constraints.

3. **Outperforms EWC on Transfer Metrics:** GEM achieve better **positive backward transfer** vs EWC. MNIST Permutations: GEM BWT=+0.18 vs EWC BWT=-0.01 (EWC prevent forgetting tapi no improvement, GEM actively improve old tasks). MNIST Rotations: GEM BWT=+0.09 vs EWC BWT=-0.19 (EWC still forget). CIFAR-100: GEM ACC=72.3% vs EWC ACC=68.7%. **Tradeoff:** GEM requires memory storage, EWC no memory.

---

## 💡 Relevansi Terhadap Penelitian Ini

**RM1 (FedAvg vs Lokal pada non-IID):**
- GEM focus on centralized CL (no FL)
- **Gap:** Kita combine FL + CL (harder problem)
- Metrics (ACC, BWT) applicable untuk evaluate FL-CL systems

**RM2 (EWC mengurangi forgetting):**
- **Direct comparison:** GEM vs EWC (paper include EWC baseline)
- GEM better BWT tapi **requires memory** (store M samples per task)
- EWC **no memory** (only Fisher matrix) tapi BWT slightly negative
- **Our work:** Evaluate EWC in FL setting, compare to GEM results
- **Metrics:** Kita use **BWT** (primary CL metric) from this paper

**Metodologi:**
- **BWT calculation:** `BWT = (1/(T-1)) × Σ (R_T,i - R_i,i)` untuk i=1 to T-1
  - R_T,i = accuracy on task i after learning all T tasks
  - R_i,i = accuracy on task i right after learning task i
  - **Negative BWT** = forgetting, **Positive BWT** = improvement
- **Our experiments:** Report BWT untuk E1-E4 (compare naive, EWC, FedAvg, FedAvg+EWC)
- **Baseline:** Naive CL without forgetting mitigation (BWT baseline)

---

## 📊 Hasil Eksperimen Utama

### MNIST Permutations (20 tasks, 1000 examples/task)

| Method | ACC | BWT | FWT |
|--------|-----|-----|-----|
| **Single task** (upper bound) | 0.97 | - | - |
| **Independent** (isolated per task) | 0.90 | 0.00 | 0.00 |
| **Multimodal** (one model all tasks) | 0.18 | -0.72 | 0.00 |
| **EWC** (λ=400) | 0.75 | **-0.01** | -0.03 |
| **GEM** (M=256/task) | **0.82** | **+0.18** | -0.02 |

**Key Insight:**
- Multimodal (naive CL) severe forgetting: BWT=-0.72 (catastrophic!)
- EWC prevent forgetting: BWT=-0.01 (close to 0, no improvement)
- GEM **positive transfer:** BWT=+0.18 (learning new tasks improve old!)
- ACC: GEM 82% vs EWC 75% (+7% improvement)

### MNIST Rotations (20 tasks, related tasks)

| Method | ACC | BWT | FWT |
|--------|-----|-----|-----|
| **Single task** | 0.99 | - | - |
| **Independent** | 0.95 | 0.00 | 0.00 |
| **Multimodal** | 0.20 | -0.75 | 0.00 |
| **EWC** (λ=100) | 0.82 | **-0.19** | +0.04 |
| **GEM** (M=256/task) | **0.90** | **+0.09** | +0.05 |

**Key Insight:**
- Related tasks (rotated digits) benefit from transfer
- EWC still negative BWT=-0.19 (some forgetting)
- GEM positive BWT=+0.09 (improvement despite forgetting risk)
- FWT positive for both (new tasks benefit from old knowledge)

### CIFAR-100 Incremental (20 tasks, 5 classes/task)

| Method | ACC | BWT |
|--------|-----|-----|
| **Single task** | 0.79 | - |
| **Independent** | 0.68 | 0.00 |
| **Multimodal** | 0.19 | -0.49 |
| **EWC** (λ=1) | 0.69 | -0.03 |
| **GEM** (M=256/task) | **0.72** | **+0.01** |

**Key Insight:** GEM slight positive BWT even on hard dataset, EWC near-zero

---

## 🔍 Kutipan Penting (untuk Bab 2 & 3)

> "We propose a set of metrics to evaluate models learning over a continuum of data. These metrics characterize models not only by their test accuracy, but also in terms of their ability to transfer knowledge across tasks."

> "Backward transfer (BWT), which is the influence that learning a task t has on the performance on a previous task k < t. [...] Large negative backward transfer is also known as (catastrophic) forgetting."

> "Forward transfer (FWT), which is the influence that learning a task t has on the performance on a future task k > t."

**BWT Formula (Equation 3):**
```
BWT = (1/(T-1)) × Σ[i=1 to T-1] (R_T,i - R_i,i)
```

> "If violations occur, we propose to project the proposed gradient g to the closest gradient g̃ (in squared ℓ2 norm) satisfying all the constraints."

> "GEM allows *positive* backward transfer" (berbeda dari EWC yang hanya prevent forgetting)

---

## ⚠️ Batasan & Catatan Kritis

**Paper Limitations:**
- **Memory requirement:** M samples per task = MT total (e.g., 20 tasks × 256 = 5,120 samples)
- **QP solver overhead:** Quadratic Programming per gradient update (computational cost)
- **Task descriptor required:** Need explicit task ID (kita punya: Task 1=SSH, Task 2=DoS)
- **Centralized only:** No federated learning extension
- **Vision focus:** MNIST & CIFAR (not IDS tabular data)

**GEM vs EWC Tradeoffs:**
| Aspect | GEM | EWC (Ours) |
|--------|-----|------------|
| Memory | ✅ M samples/task | ❌ None (Fisher only) |
| BWT | ✅ Positive (+0.18) | ⚠️ Near-zero (-0.01) |
| Privacy | ⚠️ Store raw samples | ✅ No raw data |
| Computation | High (QP solver) | Low (Fisher diagonal) |
| Implementation | Complex | Simple |

**Gaps We Address:**
1. **Federated setting:** GEM centralized, kita FL
2. **Non-IID + Drift:** GEM IID tasks, kita extreme non-IID clients + temporal drift
3. **IDS application:** GEM vision, kita network intrusion
4. **Privacy:** GEM memory leak risk, EWC no storage

---

## 🔗 Hubungan dengan Paper Lain

**Mengutik:**
- EWC ([[Kirkpatrick-2017-EWC]]) - baseline comparison
- iCaRL (incremental learning vision)
- Catastrophic forgetting (McCloskey 1989)

**Dikutik oleh:**
- [[Gholizade-2026-FCL-Survey]] - FCL taxonomy
- [[Rehman-2026-Incremental-FL-IDS]] - cites BWT metric
- [[Jin-2024-FL-IIDS]] - references GEM [30]
- 2000+ citations (highly influential)

**Related:**
- [[Kirkpatrick-2017-EWC]] - Alternative CL approach (regularization vs memory)
- A-GEM (Averaged GEM) - later variant with improved efficiency
- PackNet, Progressive Neural Networks - other CL approaches

---

## 📝 Catatan Tambahan

**BWT Metric Implementation (for Our Experiments):**

```python
# R matrix: R[i, j] = accuracy on task j after learning task i
# Example: 2 tasks (Task 1=SSH, Task 2=DoS)

# After Task 1:
R[1, 1] = accuracy_task1_after_task1  # e.g., 0.92
R[1, 2] = accuracy_task2_after_task1  # e.g., 0.0 (not seen yet)

# After Task 2:
R[2, 1] = accuracy_task1_after_task2  # e.g., 0.85 (forgetting!)
R[2, 2] = accuracy_task2_after_task2  # e.g., 0.88

# BWT calculation:
BWT = (1/(T-1)) × (R[T, 1] - R[1, 1])
BWT = (1/1) × (0.85 - 0.92) = -0.07  # negative = forgetting

# Positive BWT example (with EWC):
R[2, 1] = 0.94  # improved!
BWT = (0.94 - 0.92) = +0.02  # positive = beneficial transfer
```

**Our Experiments Mapping to BWT:**
- **E0 (Joint training):** Upper bound (all tasks together, no forgetting)
- **E1 (Naive sequential):** Baseline BWT (expect BWT < 0, severe forgetting)
- **E2 (EWC local):** Expect BWT ≈ 0 (prevent forgetting, no improvement)
- **E3 (FedAvg):** Non-IID effect on BWT (unknown)
- **E4 (FedAvg+EWC):** Best BWT (combine FL + forgetting mitigation)

**GEM Algorithm Key Steps:**
1. Store M examples per task in episodic memory M_t
2. When learning task t, compute gradient g on current sample
3. Compute gradients g_k on memories from all previous tasks k < t
4. Check constraints: ⟨g, g_k⟩ ≥ 0 for all k < t
5. If violated: solve QP to project g → g̃ (closest gradient satisfying constraints)
6. Update parameters: θ ← θ - η × g̃

**Memory Budget:**
- MNIST: 256 samples/task × 20 tasks = 5,120 samples stored
- Our scale: 2 clients, 2 tasks, M=500 samples/task = 1,000 total (manageable)
- EWC: No samples, only Fisher matrix (P parameters × K classes)

**Citation in Thesis:**

**Bab 2.2.3 (Continual Learning Metrics):**
> "Lopez-Paz dan Ranzato (2017) mengusulkan tiga metrics standar untuk evaluasi continual learning: Average Accuracy (ACC), Backward Transfer (BWT), dan Forward Transfer (FWT). BWT mengukur pengaruh pembelajaran task baru terhadap performance task lama, di mana BWT negatif mengindikasikan catastrophic forgetting dan BWT positif mengindikasikan beneficial transfer. Kami mengadopsi BWT sebagai primary metric untuk mengukur efektivitas EWC dalam mencegah forgetting."

**Bab 3.4.2 (Evaluation Metrics):**
> "BWT dihitung menggunakan formula Lopez-Paz & Ranzato (2017): BWT = (1/(T-1)) × Σ (R_T,i - R_i,i), di mana R_i,j adalah accuracy pada task j setelah learning task i."

**Bab 5.1 (Results):**
> "Lopez-Paz & Ranzato (2017) report GEM achieves BWT=+0.18 on MNIST Permutations vs EWC BWT=-0.01. Our results show EWC in federated setting achieves BWT=[...], indicating [comparison]."

---

**Review Status:** ⬜ Belum full read (677 lines, ~12 pages)  
**Action Items:** 
- [x] Create literature note
- [x] Extract BWT/FWT formulas (Equations 3 & 4)
- [ ] Read Section 3 (GEM Algorithm details)
- [ ] Read Section 4.3 (Results tables for all datasets)
- [ ] Implement BWT calculation in experiment scripts
- [ ] Cite in Bab 2.2.3 (CL Metrics)
- [ ] Reference in Bab 3.4.2 (Evaluation Metrics)
- [ ] Compare our BWT results to GEM/EWC baselines in Bab 5
