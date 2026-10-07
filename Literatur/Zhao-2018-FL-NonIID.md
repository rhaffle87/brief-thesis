---
type: literatur
title: "Federated Learning with Non-IID Data"
authors: "Yue Zhao, Meng Li, Liangzhen Lai, Naveen Suda, Damon Civin, Vikas Chandra"
year: 2018
venue: "arXiv preprint"
doi: "10.48550/arXiv.1806.00582"
arxiv: "1806.00582"
pdf: "[[PDFs/Opsional/Zhao-2018-FL-NonIID.pdf]]"
dibaca_dari_pdf: ya
status: ✔ terverifikasi
tags:
  - literatur
  - federated-learning
  - non-iid
  - weight-divergence
  - earth-movers-distance
rm_supported: RM1
relevance: ⭐⭐⭐⭐⭐
prioritas: inti-terkait
---

# Zhao et al. (2018) - Federated Learning with Non-IID Data

## Metadata

**Penulis:** Yue Zhao, Meng Li, Liangzhen Lai, Naveen Suda, Damon Civin, Vikas Chandra  
**Institusi:** Arm Inc., San Jose, CA, USA  
**Tahun:** 2018  
**Venue:** arXiv:1806.00582  
**PDF Lokal:** [[PDFs/Opsional/Zhao-2018-FL-NonIID.pdf]]  
**Status Verifikasi:** ✔ Terverifikasi dari naskah PDF Arm Inc. (12 halaman)  
**Relevansi Scope:** ⭐⭐⭐⭐⭐ CRITICAL - Studi fundamental tentang Weight Divergence akibat Non-IID data pada FedAvg  

---

## 📌 3 Temuan Utama

1. **Teorema Divergensi Bobot (Weight Divergence):** Membuktikan secara analitis dan empiris bahwa derajat non-IID dapat diukur menggunakan Earth Mover's Distance (EMD) antara distribusi data klien dan distribusi populasi global. Nilai EMD yang tinggi memicu divergensi bobot $\|w_{FedAvg} - w_{Centralized}\|$.
2. **Degradasi Drastis Akurasi FedAvg:** Menunjukkan bahwa akurasi model FedAvg dapat merosot drastis (hingga penurunan 55% pada CNN/CIFAR-10) murni disebabkan oleh divergensi bobot lokal yang ditarik ke optimum lokal yang saling berjauhan sebelum diagregasi.
3. **Analisis Sensitivitas Komputasi Lokal ($E$):** Menemukan bahwa semakin banyak jumlah epoch lokal ($E$) yang dijalankan sebelum agregasi, divergensi bobot akan semakin parah jika data terdistribusi non-IID.

---

## 💡 Relevansi Terhadap Penelitian Ini

- **Pondasi Analisis RM1:** Menjadi rujukan teoretis sentral di Bab 2 dan Bab 4 untuk menerangkan mengapa akurasi model terdistribusi non-IID tertinggal dibandingkan model centralized/IID.
- **Rasionalisasi Pilihan Hyperparameter Epoch Lokal:** Memberikan dasar ilmiah dalam membatasi epoch lokal ($E$) pada simulasi federasi IDS agar divergensi bobot antar-klien tidak meledak.
