---
type: literatur
title: "Avalanche: An End-to-End Library for Continual Learning"
authors: "Antonio Carta, Lorenzo Pellegrini, Andrea Cossu, Hamed Hemati, Vincenzo Lomonaco"
year: 2023
venue: "Journal of Machine Learning Research (JMLR)"
doi: ""
arxiv: "2302.01766"
pdf: "PDFs/Opsional/Carta-2023-Avalanche-JMLR.pdf"
dibaca_dari_pdf: ya
status: ✔ terverifikasi
tags:
  - literatur
  - continual-learning
  - avalanche
  - framework
  - benchmark
rm_supported: RM2
relevance: ⭐⭐⭐⭐
prioritas: opsional-pendukung
---

# Carta et al. (2023) - Avalanche: An End-to-End Library for Continual Learning

## Metadata

**Penulis:** Antonio Carta, Lorenzo Pellegrini, Andrea Cossu, Hamed Hemati, Vincenzo Lomonaco  
**Institusi:** University of Pisa, ContinualAI Foundation, University of Zurich  
**Tahun:** 2023  
**Venue:** Journal of Machine Learning Research (JMLR), Vol. 24, pp. 1-6  
**PDF Lokal:** [Carta-2023-Avalanche-JMLR.pdf](PDFs/Opsional/Carta-2023-Avalanche-JMLR.pdf)  
**Status Verifikasi:** ✔ Terverifikasi dari naskah PDF JMLR  
**Relevansi Scope:** ⭐⭐⭐⭐ HIGH - Pustaka standar industri untuk desain arsitektur dan evaluasi Continual Learning  

---

## 📌 3 Temuan Utama

1. **Arsitektur Modular Continual Learning:** Avalanche mengorganisir pipeline CL ke dalam lima modul inti: *Benchmarks* (pembuatan skenario incremental stream), *Training* (strategi mitigasi forgetting), *Evaluation* (metrik terstandar), *Models* (arsitektur adaptif), dan *Logging*.
2. **Standardisasi Metrik BWT dan FWT:** Menyediakan implementasi terverifikasi untuk metrik evaluasi retensi: Backward Transfer (BWT), Forward Transfer (FWT), serta penelusuran kurva lupa (*forgetting curve*).
3. **Ekosistem dan Reproduksibilitas Riset:** Memfasilitasi benchmark multi-skenario (Class-Incremental, Task-Incremental, Domain-Incremental) yang terintegrasi penuh dengan PyTorch.

---

## 💡 Relevansi Terhadap Penelitian Ini

- **Standar Metrik Evaluasi Continual Learning:** Menjadi landasan formulasi matematis untuk pengukuran BWT dan forgetting rate pada evaluasi Task 1 (SSH Brute Force) dan Task 2 (DoS) di Bab 3 dan Bab 4.
- **Desain Skenario Inkremental:** Memberikan panduan baku dalam perancangan stream task inkremental IDS berbasis PyTorch.
