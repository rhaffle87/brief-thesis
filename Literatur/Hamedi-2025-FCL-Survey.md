---
type: literatur
title: "Federated continual learning: Concepts, challenges, and solutions"
authors: "Parisa Hamedi, Roozbeh Razavi-Far, Ehsan Hallaji"
year: 2025
venue: "Neurocomputing, Vol. 629, 2025, 130844"
doi: "10.1016/j.neucom.2025.130844"
arxiv: "2502.07059"
pdf: "PDFs/Hamedi-2025-FCL-Survey.pdf"
dibaca_dari_pdf: ya
status: ✔ terverifikasi
tags:
  - literatur
  - federated-learning
  - continual-learning
  - federated-continual-learning
  - survey
rm_supported: Both
relevance: ⭐⭐⭐⭐⭐
prioritas: inti-terkait
---

# Hamedi et al. (2025) - Federated Continual Learning: Concepts, Challenges, and Solutions

## Metadata

**Penulis:** Parisa Hamedi, Roozbeh Razavi-Far, Ehsan Hallaji  
**Institusi:** University of Windsor, Windsor, ON, Canada  
**Tahun:** 2025  
**Venue:** Neurocomputing, Vol. 629, 130844 (Elsevier) / arXiv:2502.07059  
**DOI:** 10.1016/j.neucom.2025.130844  
**PDF Lokal:** [Hamedi-2025-FCL-Survey.pdf](PDFs/Hamedi-2025-FCL-Survey.pdf)  
**Status Verifikasi:** ✔ Terverifikasi dari Crossref REST API & ScienceDirect  
**Relevansi Scope:** ⭐⭐⭐⭐⭐ CRITICAL - Survey komprehensif yang membedah irisan Federated Learning dan Continual Learning  

---

## 📌 3 Temuan Utama

1. **Definisi Formal Federated Continual Learning (FCL):** Merumuskan FCL sebagai integrasi dua dimensi tantangan: dimensi spasial (distribusi heterogen antar-klien secara terdistribusi) dan dimensi temporal (aliran task berurutan yang memicu forgetting).
2. **Kategori Lupa Ganda (Dual Forgetting):** Mengidentifikasi bahwa sistem FCL menghadapi dua jenis degradasi memori secara simultan: *Local Forgetting* (klien melupakan task lama saat belajar task baru) dan *Global Forgetting* (server melakukan agregasi rata-rata yang merusak parameter terpesialisasi tiap klien).
3. **Taksonomi Solusi FCL:** Mengelompokkan solusi ke dalam pendekatan berbasis regulasi terfederasi (Federated EWC), rehearsal terfederasi (buffer replay lokal/global), dan arsitektur model adaptif (modular neural network).

---

## 💡 Relevansi Terhadap Penelitian Ini

- **Pilar Utama Kerangka FCL Skripsi:** Menjadi landasan konseptual paling tepat yang menjelaskan sinergi antara FL dan CL dalam skripsi ini (Bab 2).
- **Rujukan Penjelasan Dual Forgetting:** Digunakan untuk menjelaskan fenomena penurunan akurasi pada pengujian model IDS saat berpindah dari Task 1 ke Task 2 di bawah skenario non-IID.
