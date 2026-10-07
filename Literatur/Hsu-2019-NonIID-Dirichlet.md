---
type: literatur
title: "Measuring the Effects of Non-Identical Data Distribution for Federated Visual Classification"
authors: "Tzu-Ming Harry Hsu, Hang Qi, Matthew Brown"
year: 2019
venue: "arXiv preprint"
doi: "10.48550/arXiv.1909.06335"
arxiv: "1909.06335"
pdf: "PDFs/Opsional/Hsu-2019-NonIID-Visual-FL.pdf"
dibaca_dari_pdf: ya
status: ✔ terverifikasi
tags:
  - literatur
  - federated-learning
  - non-iid
  - dirichlet-distribution
  - label-skew
rm_supported: RM1
relevance: ⭐⭐⭐⭐
prioritas: opsional-pendukung
---

# Hsu et al. (2019) - Measuring the Effects of Non-Identical Data Distribution for Federated Visual Classification

## Metadata

**Penulis:** Tzu-Ming Harry Hsu, Hang Qi, Matthew Brown  
**Institusi:** Carnegie Mellon University, Google  
**Tahun:** 2019  
**Venue:** arXiv:1909.06335  
**PDF Lokal:** [Hsu-2019-NonIID-Visual-FL.pdf](PDFs/Opsional/Hsu-2019-NonIID-Visual-FL.pdf)  
**Status Verifikasi:** ✔ Terverifikasi dari naskah PDF  
**Relevansi Scope:** ⭐⭐⭐⭐ HIGH - Makalah seminal yang memperkenalkan partisi Non-IID berbasis Distribusi Dirichlet $\mathrm{Dir}(lpha)$  

---

## 📌 3 Temuan Utama

1. **Pemodelan Formal Non-IID dengan Dirichlet $\mathrm{Dir}(lpha)$:** Memperkenalkan metode kuantitatif terstandar untuk mempartisi data antar-klien federasi menggunakan distribusi Dirichlet dengan parameter konsentrasi $lpha$. Nilai $lpha$ yang kecil ($lpha 	o 0$) menciptakan non-IID ekstrem (label skew), sedangkan $lpha 	o \infty$ mendekati kondisi IID seragam.
2. **Korelasi Penurunan Akurasi terhadap Derajat Non-IID:** Membuktikan secara empiris bahwa penurunan performa FedAvg berbanding lurus dengan tingkat ketimpangan distribusi data ($lpha$ kecil memicu diversitas gradien yang saling bertolak belakang antar-klien).
3. **Pengaruh Heterogenitas pada Kecepatan Konvergensi:** Mengungkapkan bahwa client-drift akibat non-IID memperlambat konvergensi dan membutuhkan strategi optimasi lokal yang lebih teratur.

---

## 💡 Relevansi Terhadap Penelitian Ini

- **Metode Pembagian Data Non-IID:** Menjadi dasar matematis pembagian data antar node klien pada simulasi federasi di skripsi ini (Bab 3), di mana parameter $lpha$ digunakan untuk mengontrol derajat non-IID label skew.
- **Rujukan Analisis Komparasi IID vs Non-IID:** Memberikan justifikasi teoretis untuk pengujian performa FedAvg di bawah kondisi heterogenitas distribusi lalu lintas IDS.
