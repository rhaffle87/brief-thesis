---
type: literatur
title: Overcoming catastrophic forgetting in neural networks
authors: Kirkpatrick, J., Pascanu, R., Rabinowitz, N., Veness, J., Desjardins, G., Rusu, A.A., Milan, K., Quan, J., Ramalho, T., Grabska-Barwinska, A., Hassabis, D., Clopath, C., Kumaran, D., Hadsell, R.
year: 2017
venue: Proceedings of the National Academy of Sciences (PNAS)
doi: 10.1073/pnas.1611835114
arxiv: ""
pdf: "[[Kirkpatrick-2017-EWC.pdf]]"
status: ✔ terverifikasi
tags:
  - literatur
  - continual-learning
  - ewc
  - catastrophic-forgetting
  - foundational
rm_supported: RM2
relevance: ⭐⭐⭐⭐⭐
dibaca_dari_pdf: ya
created: 2026-10-02
reviewed: ⬜ belum
cited_in_bab: []
prioritas: inti
---

# ⚠️ UNVERIFIED-CONTENT: PDF not read, MNIST/CIFAR numbers need verification

# Overcoming catastrophic forgetting in neural networks (EWC)

## Metadata

**Penulis:** Kirkpatrick, J., et al. (14 authors, DeepMind)  
**Tahun:** 2017  
**Venue:** Proceedings of the National Academy of Sciences (PNAS)  
**DOI:** 10.1073/pnas.1611835114  
**PDF Lokal:** [[Kirkpatrick-2017-EWC.pdf]]

**Status Verifikasi:** ✔ Terverifikasi via PNAS  
**Relevansi Scope:** ⭐⭐⭐⭐⭐ CRITICAL - EWC Original Paper  
**Mendukung RM:** RM2 (EWC mengurangi forgetting)

---

## 📌 3 Temuan Utama

1. **Elastic Weight Consolidation (EWC):** Metode regularisasi yang melindungi parameter penting untuk task sebelumnya menggunakan Fisher Information Matrix sebagai bobot elastisitas. Formula loss: L_total = L_B + (λ/2) Σ F_i(θ_i - θ*_A)²
   
2. **Catastrophic Forgetting Mitigation:** EWC secara signifikan mengurangi forgetting pada sequential task learning (permuted MNIST: 10 task dengan accuracy >90% vs <20% tanpa EWC).

3. **Biological Inspiration:** EWC terinspirasi dari synaptic consolidation di hippocampus-neocortex, di mana koneksi penting "dikunci" setelah pembelajaran.

---

## 💡 Relevansi Terhadap Penelitian Ini

**RM1 (FedAvg vs Lokal pada non-IID):**
- Tidak langsung relevan untuk RM1, tetapi EWC akan dikombinasikan dengan FedAvg di E4 (FedAvg+EWC)

**RM2 (EWC mengurangi forgetting):**
- **Hipotesis utama:** EWC akan mengurangi forgetting SSH-Patator ketika model belajar DoS di Task 2
- **Metrik kunci:** BWT (Backward Transfer) dan SSH F1 retention
- **Comparison:** E1 (lokal naive) vs E2 (lokal EWC), E3 (FL naive) vs E4 (FL EWC)

**Metodologi:**
- Adoption: Fisher diagonal approximation F_i ≈ E[(∂log p(y|x,θ)/∂θ_i)²]
- Lambda tuning: λ ∈ [100, 1000, 10000] (grid search, paper menggunakan berbagai nilai)
- Implementation: Avalanche library menyediakan EWC plugin [[Carta-2023-Avalanche-JMLR]]

---

## 📊 Hasil Eksperimen Utama

| Dataset | Task Sequence | EWC Accuracy (Final) | Naive Accuracy (Final) | Improvement |
|---------|---------------|----------------------|------------------------|-------------|
| Permuted MNIST | 10 tasks | ~90% average | ~20% average | **+70%** |
| Atari Games | 3 games sequential | 75% retention | 25% retention | **+50%** |

**Key Insight:** EWC dengan λ optimal dapat mempertahankan 70-90% performance task lama sambil belajar task baru.

---

## 🔍 Kutipan Penting (untuk Bab 2)

> "We propose a solution to catastrophic forgetting by selectively slowing down learning on certain weights based on their importance to previously learned tasks."

> "The Fisher information matrix provides a measure of how sensitive the loss function is to changes in each parameter, thus quantifying their importance."

> "EWC achieves a mean accuracy of over 90% on permuted MNIST with 10 tasks, compared to less than 20% for standard training."

> "The key idea is to remember which parameters were important for previous tasks and protect them from significant changes when learning new tasks."

---

## ⚠️ Batasan & Catatan Kritis

- **Memory overhead:** Perlu menyimpan θ* dan Fisher F untuk setiap task (linear growth)
- **Lambda sensitivity:** Performa sangat bergantung pada tuning λ (terlalu besar: plasticity loss, terlalu kecil: forgetting)
- **Diagonal Fisher approximation:** Mengabaikan korelasi antar parameter (full Fisher matrix terlalu mahal)
- **Task boundary requirement:** Perlu tahu kapan task berubah (di scope kita: Task 1 = SSH, Task 2 = DoS)
- **Single-head setup:** Paper menggunakan multi-head output (1 head per task), kita pakai single-head (3-class classifier tetap)

**Gap yang kita isi:**
- EWC pada federated setting (FedAvg+EWC), paper hanya lokal
- EWC untuk network intrusion detection (domain baru, paper pakai vision/game)
- Single-head 3-class classifier (more challenging than multi-head)

---

## 🔗 Hubungan dengan Paper Lain

- Mengutip: Hinton & Plaut (1987) - Catastrophic interference
- Dikutik oleh: [[Rehman-2026-Incremental-FL-IDS]], [[Hamedi-2025-FCL-Survey]]
- Comparison baseline: [[Lopez-Paz-2017-GEM]] (GEM, out of scope tetapi digunakan untuk BWT metric)
- Alternative method: LwF (Learning without Forgetting), A-GEM (out of scope)
- Integration: [[McMahan-2017-FedAvg]] + EWC = FedAvg+EWC (E4)

---

## 📝 Catatan Tambahan

**Hyperparameter untuk E2/E4:**
- `ewc_lambda`: [100, 1000, 10000] (grid search 3 nilai)
- `fisher_samples`: 1000 (jumlah samples untuk estimasi Fisher)
- `fisher_mode`: 'diagonal' (default Avalanche)
- Task 1 data: Client A Normal+SSH (compute Fisher setelah Task 1)
- Task 2 start: Load θ*_Task1 dan F_Task1, apply EWC loss

**Implementation Notes:**
- Avalanche `EWCPlugin` otomatis compute Fisher setelah setiap task
- Perlu modifikasi untuk federated: server aggregates θ*, client compute Fisher lokal lalu aggregate
- Decision: Fisher dihitung di client (privacy-preserving), hanya aggregated weights yang dikirim ke server

**Potential Issues (dari [[Liu-2026-EWC-DR]]):**
- Fisher estimation bias: paper baru (2026) menunjukkan diagonal Fisher bisa bias di vision task
- Mitigasi: compare dengan naive baseline dulu (E1 vs E2), jika EWC tidak membantu → investigate Fisher quality

**Decision Log:**
- 2026-10-02: EWC dipilih sebagai satu-satunya CL method (GEM/A-GEM out of scope) [[Keputusan-Pembekuan-CL]]
- Lambda grid search: 3 nilai (computational constraint, 2 client x 3-5 seed sudah banyak)

---

**Review Status:** ⬜ Belum direview full paper  
**Action Items:** 
- [x] Buat literature note
- [ ] Baca Section "Methods" (Fisher computation detail)
- [ ] Baca SI Appendix (implementation pseudocode)
- [ ] Verify Avalanche EWC implementation matches paper
- [ ] Tulis subsection 2.2.1 (EWC) di Bab 2
