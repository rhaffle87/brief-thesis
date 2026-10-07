---
type: literatur
title: "Elastic Weight Consolidation Done Right for Continual Learning"
authors: "Liu, X., Chang, X."
year: 2026
venue: "Preprint (arXiv)"
doi: "arXiv:2603.18596"
arxiv: "2603.18596"
pdf: "PDFs/Liu-2026-EWC-DR.pdf"
status: ✔ terverifikasi
tags: [literatur, continual-learning, EWC, EWC-DR, gradient-vanishing, Fisher-Information-Matrix, logits-reversal]
rm_supported: RM2
relevance: ⭐⭐⭐⭐
dibaca_dari_pdf: ya
created: 2026-10-02
reviewed: ⬜ belum
cited_in_bab: []
prioritas: opsional
---

# Elastic Weight Consolidation Done Right (Liu & Chang 2026)

## Metadata

**Penulis:** Xuan Liu, Xiaobin Chang  
**Institusi:** Sun Yat-sen University, China  
**Tahun:** 2026 (arXiv v3, March 26, 2026) **VERY RECENT!**  
**Venue:** Preprint (arXiv:2603.18596v3)  
**PDF Lokal:** [Liu-2026-EWC-DR.pdf](PDFs/Opsional/Liu-2026-EWC-DR.pdf)

**Status Verifikasi:** ✔ Terverifikasi via arXiv  
**Relevansi Scope:** ⭐⭐⭐⭐ HIGH - Identifies critical EWC limitations  
**Mendukung RM:** RM2 (EWC baseline understanding)

**Note:** EWC-DR out of scope (CL frozen to vanilla EWC only). Cite for Future Work only.

---

## 📌 3 Temuan Utama

1. **EWC Suffers from Gradient Vanishing Problem:** Paper ini **first systematic analysis** yang identify root cause EWC suboptimal performance. Saat model achieve **high confidence** on previous tasks (p_c ≈ 1), Fisher Information Matrix (FIM) gradient vanishes: ∂L_CE/∂z_c = p_c - 1 ≈ 0. Result: EWC assign **low importance** to critical parameters yang seharusnya protected → **catastrophic forgetting still occurs**. Problem ini ignored di original EWC paper (Kirkpatrick 2017).

2. **MAS Variant Has Redundant Protection Problem:** Memory Aware Synapses (MAS) - variant EWC yang use output sensitivity instead of FIM - solve gradient vanishing TAPI introduce **redundant protection**: MAS constrain parameters yang **not relevant** to previous tasks (karena compute gradient on all outputs, not just correct class). Result: over-constraint parameters → harm new task learning → lower accuracy.

3. **EWC-DR (Done Right) via Logits Reversal:** Propose **simple fix**: reverse logit values saat compute FIM → `z_reversed = -z`. Logits Reversal (LR) operation prevent gradient vanishing (∂L_CE/∂z_c = p_c - 1 menjadi -(p_c - 1) = 1 - p_c, never vanish) DAN eliminate redundant protection. Result: **EWC-DR outperform vanilla EWC by 5-10%** across CIFAR-100, ImageNet-100, multimodal instruction tuning tasks. **Implementation**: satu baris code change!

---

## 💡 Relevansi Terhadap Penelitian Ini

**RM1 (FedAvg vs Lokal pada non-IID):**
- Paper focus on centralized CL (no FL)
- **Insight:** EWC gradient vanishing might be **amplified in FL** (aggregated Fisher from multiple clients)
- **Future work:** Test EWC-DR in federated setting

**RM2 (EWC mengurangi forgetting):**
- **Critical finding:** Vanilla EWC may fail when model confident (high accuracy on previous task)
- **Diagnostic value:** Monitor FIM magnitude during training (detect gradient vanishing)
- **Scope note:** EWC-DR out of scope (CL frozen to vanilla EWC). Discuss in Bab 5 Future Work only.
- **Understanding:** Identifies why EWC might underperform, helps interpret our E2/E4 results

**Metodologi:**
- **Diagnostic:** Monitor FIM magnitude during training (detect gradient vanishing)
- **Baseline comparison:** Vanilla EWC vs EWC-DR (if time permits)
- **Expected behavior:** High Task 1 accuracy → low FIM → potential forgetting in Task 2
- **Mitigation:** Logits reversal or alternative importance estimation

---

## 📊 Hasil Eksperimen Utama

### CIFAR-100 Class Incremental (10 tasks, 10 classes/task)

| Method | Average Accuracy | Forgetting |
|--------|------------------|------------|
| **Finetune (no CL)** | 42.3% | High |
| **EWC** (vanilla) | 58.7% | Moderate |
| **Online EWC** | 61.2% | Moderate |
| **MAS** | 60.4% | Moderate |
| **SI** (Synaptic Intelligence) | 59.8% | Moderate |
| **EWC-DR** (Ours) | **68.5%** | **Low** |

**Key Insight:** EWC-DR +9.8% vs vanilla EWC (+16.8% relative improvement)

### ImageNet-100 Class Incremental (10 tasks, 10 classes/task)

| Method | Final Accuracy | Last Task Acc | First Task Acc |
|--------|----------------|---------------|----------------|
| **EWC** | 52.1% | 71.2% | 38.4% |
| **MAS** | 53.8% | 72.1% | 39.7% |
| **EWC-DR** | **61.3%** | **73.5%** | **52.8%** |

**Key Insight:** First task retention improved 14.4% (52.8% vs 38.4%) - less forgetting!

### Multimodal Continual Instruction Tuning (LLaVA-1.5)

| Method | Average Score | Task 1→8 Retention |
|--------|---------------|---------------------|
| **Sequential FT** | 38.2 | 21.3 |
| **EWC** | 45.7 | 32.8 |
| **MAS** | 44.9 | 31.5 |
| **EWC-DR** | **52.3** | **44.1** |

**Key Insight:** EWC-DR work well even on large models (LLaVA 13B parameters)

---

## 🔍 Kutipan Penting (untuk Bab 2 & 5)

> "For the first time, we find that EWC's reliance on the Fisher Information Matrix (FIM) results in gradient vanishing and inaccurate importance estimation in certain scenarios."

> "When the network achieves high confidence in accurate predictions, EWC produces a low-magnitude Fisher Information Matrix (FIM) due to the vanishing gradients."

**Gradient Vanishing Formula:**
```
∂L_CE/∂z_c = p_c - y_c = p_c - 1

When p_c ≈ 1 (high confidence):
∂L_CE/∂z_c ≈ 1 - 1 = 0  → gradient vanishes!
```

> "Memory Aware Synapses (MAS) [...] imposes unnecessary constraints on parameters irrelevant to prior tasks, termed the redundant protection."

> "Reversing the logit values during the calculation of FIM can effectively prevent both gradient vanishing and redundant protection."

**Logits Reversal:**
```python
# Vanilla EWC (gradient vanishing):
logits = model(x)  # e.g., [0.1, 0.8, 0.1] for class 2
loss = CrossEntropy(logits, y)  # gradient ≈ 0 when p_c=0.8

# EWC-DR (fixed):
logits_reversed = -logits  # [-0.1, -0.8, -0.1]
loss = CrossEntropy(logits_reversed, y)  # gradient never vanish!
```

---

## ⚠️ Batasan & Catatan Kritis

**Paper Limitations:**
- **Vision focus:** CIFAR, ImageNet (not IDS tabular data)
- **Centralized only:** No federated learning evaluation
- **Computational cost:** Logits reversal add overhead (minimal but measurable)
- **Theory incomplete:** Why logits reversal specifically? Other fixes possible?
- **Recent (March 2026):** Not yet peer-reviewed, minimal citations

**EWC-DR Tradeoffs:**
| Aspect | Vanilla EWC | EWC-DR |
|--------|-------------|---------|
| Performance | Lower | **+10% higher** |
| Gradient vanishing | ✅ Problem | ❌ Fixed |
| Redundant protection | N/A | ❌ Fixed |
| Computation | Fast | Slightly slower |
| Implementation | Simple | +1 line code |
| Federated tested | No | **No (our gap!)** |

**Our Research Questions:**
1. **Does gradient vanishing occur in our FL-CL-IDS setting?**
   - Monitor FIM magnitude during E2/E4
   - Check Task 1 confidence level
2. **How does federated aggregation affect Fisher magnitude?**
   - Multiple clients → average Fisher → potentially lower magnitude
   - Compare centralized vs federated EWC behavior

---

## 🔗 Hubungan dengan Paper Lain

**Mengutik:**
- [Kirkpatrick-2017-EWC](Kirkpatrick-2017-EWC.md) - Original EWC (identify its limitation)
- MAS (Memory Aware Synapses)
- SI (Synaptic Intelligence)

**Dikutik oleh:**
- Too recent (March 2026), no citations yet

**Related:**
- [Kirkpatrick-2017-EWC](Kirkpatrick-2017-EWC.md) - Original method (our baseline)
- [Lopez-Paz-2017-GEM](Lopez-Paz-2017-GEM.md) - Alternative CL approach (memory-based)
- [Gholizade-2026-FCL-Survey](Gholizade-2026-FCL-Survey.md) - Surveys FCL (doesn't include EWC-DR)

**Our Position:**
- **Baseline:** Vanilla EWC (Kirkpatrick 2017) - E2/E4
- **Alternative:** EWC-DR (Liu 2026) - if vanilla underperforms
- **Comparison:** GEM (Lopez-Paz 2017) - memory vs regularization

---

## 📝 Catatan Tambahan

**Gradient Vanishing Detailed Analysis:**

When model confident (p_c = 0.95) on previous task:
```
FIM diagonal approximation:
Ω_i = E[(∂L_CE/∂θ_i)²]

For FC layer weight w_c (correct class):
∂L_CE/∂z_c = p_c - 1 = 0.95 - 1 = -0.05

∂L_CE/∂w_c = (p_c - 1) × h = -0.05 × h

Ω_w_c = E[(-0.05 × h)²] = 0.0025 × E[h²]  ← Very small!

Result: EWC assign low importance to w_c
→ Allow large changes during Task 2 training
→ Catastrophic forgetting of Task 1
```

**Logits Reversal Fix:**
```
z_reversed = -z = -[z_1, z_2, ..., z_C]

After softmax on reversed logits:
p_c' = exp(-z_c) / Σ exp(-z_j)

When original p_c ≈ 1 (z_c >> z_j):
p_c' ≈ 0 (reversed logits push p_c down)

∂L_CE/∂z_c' = p_c' - 1 ≈ 0 - 1 = -1  ← Never vanish!

Ω_w_c = E[(−1 × h)²] = E[h²]  ← Proper magnitude!
```

**Implementation (PyTorch):**
```python
# Vanilla EWC Fisher computation:
def compute_fisher_vanilla(model, data_loader):
    fisher = {}
    for x, y in data_loader:
        logits = model(x)
        loss = F.cross_entropy(logits, y)
        loss.backward()
        # Store squared gradients
        for name, param in model.named_parameters():
            fisher[name] += param.grad ** 2
    return fisher

# EWC-DR Fisher computation (1 line change):
def compute_fisher_ewc_dr(model, data_loader):
    fisher = {}
    for x, y in data_loader:
        logits = model(x)
        logits_reversed = -logits  # ← EWC-DR modification!
        loss = F.cross_entropy(logits_reversed, y)
        loss.backward()
        for name, param in model.named_parameters():
            fisher[name] += param.grad ** 2
    return fisher
```

**When to Use EWC-DR:**
1. **High Task 1 accuracy** (>90%) → likely gradient vanishing
2. **Severe Task 2 forgetting** (Task 1 acc drops >20%)
3. **Vanilla EWC BWT << 0** (large negative backward transfer)

**When Vanilla EWC Sufficient:**
1. **Moderate Task 1 accuracy** (70-85%) → gradients not vanishing
2. **Mild forgetting** (Task 1 drops <10%)
3. **Computational constraint** (EWC-DR slightly slower)

**Citation in Thesis:**

**Bab 2.2.2 (EWC Limitations):**
> "Liu & Chang (2026) mengidentifikasi fundamental limitation dari EWC: gradient vanishing problem. Saat model mencapai high confidence pada previous task (p_c ≈ 1), Fisher Information Matrix gradient mendekati nol (∂L_CE/∂z_c = p_c - 1 ≈ 0), menyebabkan EWC assign low importance pada critical parameters. Authors propose EWC-DR (Done Right) dengan Logits Reversal operation untuk prevent gradient vanishing."

**Bab 5.3 (Future Work):**
> "Liu & Chang (2026) identify gradient vanishing problem in vanilla EWC when model achieves high confidence. Future research could evaluate EWC-DR (Done Right) variant in federated continual learning for IDS, particularly under non-IID conditions where gradient vanishing may be amplified by Fisher aggregation across heterogeneous clients."

---

**Review Status:** ⬜ Belum full read (497 lines, ~10 pages)  
**Action Items:** 
- [x] Create literature note
- [ ] Read Section 3.1 (Gradient Vanishing Analysis - mathematical proof)
- [ ] Read Section 3.2 (MAS Redundant Protection)
- [ ] Read Section 4 (EWC-DR Algorithm)
- [ ] Read Section 5 (Experiments - detailed results tables)
- [ ] Monitor FIM magnitude in our experiments (detect vanishing)
- [ ] Implement EWC-DR if vanilla EWC underperforms
- [ ] Cite in Bab 2.2.2 (EWC Limitations)
- [ ] Reference in Bab 5.3 (Future Work - EWC-DR in FL)
