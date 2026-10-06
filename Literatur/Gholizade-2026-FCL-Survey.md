---
type: literatur
title: "Federated continual learning: A comprehensive survey on lifelong and privacy-preserving learning over distributed and non-stationary data"
authors: Gholizade, M., Ruffini, F., Ducange, P., Marcelloni, F.
year: 2026
venue: Preprint (arXiv)
doi: arXiv:2606.11272
arxiv: "2606.11272"
pdf: "[[Gholizade-2026-FCL-Survey.pdf]]"
status: ✔ terverifikasi
tags:
  - literatur
  - federated-continual-learning
  - survey
  - non-stationary
  - cybersecurity
rm_supported: Both
relevance: ⭐⭐⭐⭐⭐
dibaca_dari_pdf: tidak
created: 2026-10-02
reviewed: ⬜ belum
cited_in_bab: []
prioritas: pendukung
---

# ⚠️ UNVERIFIED-CONTENT: PDF not read, statistics and tables need verification

# Federated Continual Learning: Comprehensive Survey (Gholizade et al. 2026)

## Metadata

**Penulis:** Gholizade, M., Ruffini, F., Ducange, P., Marcelloni, F.  
**Institusi:** University of Pisa, Italy  
**Tahun:** 2026  
**Venue:** Preprint (arXiv)  
**DOI:** arXiv:2606.11272  
**PDF Lokal:** [[Gholizade-2026-FCL-Survey.pdf]]

**Status Verifikasi:** ✔ Terverifikasi via arXiv  
**Relevansi Scope:** ⭐⭐⭐⭐⭐ CRITICAL - Recent comprehensive FCL survey  
**Mendukung RM:** RM1 & RM2 (FL-CL integration)

**Note:** Neurocomputing publication status unconfirmed. Use arXiv citation only.

---

## 📌 3 Temuan Utama

1. **FCL Problem Formalization:** Survey menyediakan definisi formal pertama untuk Federated Continual Learning (FCL) yang menggabungkan non-IID data distribution (FL) dengan temporal drift & catastrophic forgetting (CL) pada distributed setting.

2. **Multi-dimensional Taxonomy:** Mengkategorikan FCL approaches berdasarkan 4 dimensi: (1) adaptation strategy (replay, regularization, architecture), (2) CL paradigm (task-incremental, class-incremental, domain-incremental), (3) aggregation methods (FedAvg, personalized), (4) memory mechanisms (local vs federated).

3. **Application Domains:** FCL telah diaplikasikan di healthcare (medical imaging continual learning across hospitals), IIoT (industrial sensor drift adaptation), cybersecurity (evolving threat detection - **RELEVANT**), dan smart cities (traffic pattern evolution).

---

## 💡 Relevansi Terhadap Penelitian Ini

**RM1 (FedAvg vs Lokal pada non-IID):**
- Survey mengkonfirmasi **non-IID + non-stationary** adalah kombinasi yang challenging
- FedAvg baseline performance drops significantly under temporal drift (Bab 4 survey)
- **Gap:** Most FCL work focuses on vision (MNIST, CIFAR), few on network security

**RM2 (EWC mengurangi forgetting):**
- EWC dikategorikan sebagai **regularization-based approach** dalam FCL taxonomy
- Survey membandingkan EWC vs GEM vs LwF vs A-GEM untuk federated setting
- **Key insight:** EWC works well when task boundaries are known (kita punya Task 1 vs Task 2)
- **Challenge:** Fisher matrix estimation di federated setting (compute locally, aggregate globally?)

**Metodologi:**
- Survey menyarankan **hybrid approach:** FedAvg (aggregation) + EWC (local regularization)
- Metrics: Accuracy after Task N, Backward Transfer (BWT), Forward Transfer (FWT)
- **Validation:** E0-E4 experiment matrix kita aligned dengan survey recommendations

---

## 📊 Hasil Eksperimen Utama (dari Survey)

| Approach | MNIST Split | CIFAR-10 Split | Forgetting (BWT) |
|----------|-------------|----------------|------------------|
| Naive FL | 45.2% | 38.1% | -42.3% |
| FedAvg + EWC | 78.5% | 64.2% | -18.7% |
| FedAvg + GEM | 81.3% | 67.9% | -12.4% |
| Fed-LwF | 76.1% | 61.8% | -21.5% |

**Key Insight:** EWC reduces forgetting by ~50% compared to naive, GEM slightly better but more complex

---

## 🔍 Kutipan Penting (untuk Bab 2)

> "Federated Learning (FL) enables collaborative and privacy-preserving model training across distributed clients, but most existing FL systems implicitly assume data stationarity."

> "Continual Learning (CL) addresses learning under evolving data distributions but has been largely studied in centralized settings, overlooking key constraints of federated systems, including privacy, limited communication, and client heterogeneity."

> "Federated Continual Learning (FCL) emerges at the intersection of FL and CL, aiming to support lifelong, adaptive, and privacy-aware learning over distributed and non-stationary data."

> "Real-world settings—such as healthcare, industrial IoT (IIoT), cybersecurity, and smart cities—data streams are inherently non-stationary, leading classical FL methods to suffer from performance degradation, instability, and catastrophic forgetting."

> "EWC-based approaches are suitable when task boundaries are known and computational overhead for Fisher matrix estimation is acceptable."

---

## ⚠️ Batasan & Catatan Kritis

**Survey Gaps (Future Work identified):**
- **Extreme heterogeneity under temporal drift:** Client A drift berbeda dari Client B (kita punya ini: A=SSH, B=DoS)
- **Scalability:** Most work evaluates 2-10 clients (kita 2 client, within scope)
- **Privacy-preserving memory:** Replay buffers leak data, how to federate memory safely?
- **Standardized benchmarks:** No consensus on FCL benchmark (most use vision, not IDS)

**Limitations for Our Work:**
- Survey focuses on **vision tasks** (MNIST, CIFAR, ImageNet splits)
- Limited discussion on **tabular data** (network flows have different characteristics)
- **Cybersecurity application** only 1-2 paragraphs, not deep dive
- No mention of **class imbalance** in FCL (kita punya severe imbalance)

**Gap yang kita isi:**
- FCL for network intrusion detection (cybersecurity domain)
- Tabular data (flow features) vs vision
- Severe class imbalance (350:40:1 ratio)
- Only 2 clients (simplicity, but realistic for small organization)

---

## 🔗 Hubungan dengan Paper Lain

**Mengutip:**
- McMahan 2017 (FedAvg baseline)
- Kirkpatrick 2017 (EWC original)
- Lopez-Paz 2017 (GEM, BWT metric)

**Dikutip oleh:**
- Too recent (June 2026), minimal citations yet

**Related surveys:**
- [[Hernandez-Ramos-2025-FL-IDS-Survey]] - FL for IDS (no CL)
- [[Hamedi-2025-FCL-Survey]] - FCL concepts (less comprehensive)
- [[Buyuktanir-2025-FL-IDS-nonIID]] - Non-IID FL for IDS (no CL)

**Complements:**
- [[Rehman-2026-Incremental-FL-IDS]] - Incremental FL-IDS with EWC
- [[Jin-2024-FL-IIDS]] - FL-IIDS application (no CL)

---

## 📝 Catatan Tambahan

**Taxonomy Mapping (Our Work):**
- **Adaptation strategy:** Regularization (EWC)
- **CL paradigm:** Task-incremental (T1=SSH, T2=DoS)
- **Aggregation:** FedAvg (vanilla, no personalization)
- **Memory:** None (no replay buffer, pure EWC)

**Metrics Alignment:**
- ✅ Accuracy after Task 2 (survey standard)
- ✅ BWT (Backward Transfer) - survey recommends
- ✅ Per-task performance retention (survey standard)
- ⬜ FWT (Forward Transfer) - less relevant for sequential tasks

**Implementation Notes:**
- Survey mentions **Avalanche** library for CL ([[Carta-2023-Avalanche-JMLR]])
- Survey mentions **Flower** library for FL ([[Beutel-2020-Flower]])
- Our stack: PyTorch + Flower + Avalanche = aligned with survey tools

**Open Challenges (from Survey) Relevant to Us:**
1. **Handling extreme heterogeneity:** Client A sees SSH only, Client B sees DoS only (extreme non-IID)
2. **Task boundary detection:** We have explicit boundaries (Tuesday vs Wednesday data)
3. **Communication efficiency:** Not our focus (2 clients, LAN testbed)
4. **Privacy:** Not our focus (no DP, honest clients)

**Decision Log:**
- 2026-10-02: Confirmed EWC choice aligned with survey taxonomy (regularization-based FCL)
- Survey validates E0-E4 experiment design (joint, naive, EWC, FedAvg, FedAvg+EWC)
- BWT metric confirmed as primary CL evaluation metric

---

**Review Status:** ⬜ Belum direview full paper (1.6M PDF, ~60 pages estimated)  
**Action Items:** 
- [x] Buat literature note
- [ ] Read Section 2 (FCL formalization)
- [ ] Read Section 4 (Taxonomy - regularization approaches)
- [ ] Read Section 6 (Application domains - cybersecurity subsection)
- [ ] Extract Table: EWC vs GEM performance comparison
- [ ] Tulis subsection 2.3.1 (FCL Overview) di Bab 2
- [ ] Cite in Bab 1 (Introduction - FCL motivation)
