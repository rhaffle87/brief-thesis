---
type: literatur
title: "Federated Optimization in Heterogeneous Networks (FedProx)"
authors: "Tian Li, Anit Kumar Sahu, Manzil Zaheer, Maziar Sanjabi, Ameet Talwalkar, Virginia Smith"
year: 2020
venue: "Proceedings of Machine Learning and Systems (MLSys)"
doi: "10.48550/arXiv.1812.06127"
arxiv: "1812.06127"
pdf: "PDFs/Opsional/Li-2020-FedProx.pdf"
dibaca_dari_pdf: ya
status: ✔ terverifikasi
tags:
  - literatur
  - federated-learning
  - fedprox
  - optimization
  - non-iid
rm_supported: RM1
relevance: ⭐⭐⭐⭐
prioritas: opsional-pendukung
---

# Li et al. (2020) - Federated Optimization in Heterogeneous Networks (FedProx)

## Metadata

**Penulis:** Tian Li, Anit Kumar Sahu, Manzil Zaheer, Maziar Sanjabi, Ameet Talwalkar, Virginia Smith  
**Institusi:** Carnegie Mellon University, Google  
**Tahun:** 2020  
**Venue:** MLSys 2020 (arXiv:1812.06127)  
**PDF Lokal:** [Li-2020-FedProx.pdf](PDFs/Opsional/Li-2020-FedProx.pdf)  
**Status Verifikasi:** ✔ Terverifikasi dari naskah PDF MLSys (22 halaman)  
**Relevansi Scope:** ⭐⭐⭐⭐ HIGH - Algoritma optimasi federasi standar untuk menangani heterogenitas data dan sistem  

---

## 📌 3 Temuan Utama

1. **Formulasi Istilah Proksimal (Proximal Term):** Menambahkan regularisasi proksimal $\frac{\mu}{2} \|w - w^t\|^2$ ke dalam fungsi objektif loss lokal klien, yang membatasi agar pembaruan model lokal tidak menyimpang terlalu jauh dari model global $w^t$.
2. **Jaminan Konvergensi Teoretis:** Memberikan bukti konvergensi analitis untuk data non-IID dan kondisi perangkat komputasi yang tidak homogen (stragglers/variabel jumlah epoch lokal).
3. **Stabilitas Pelatihan di Bawah Heterogenitas:** Menunjukkan bahwa penambahan suku proksimal mencegah osilasi bobot dan distorsi agregasi yang umum terjadi pada FedAvg murni saat dihadapkan pada non-IID ekstrem.

---

## 💡 Relevansi Terhadap Penelitian Ini

- **Baseline Pembanding Alternatif:** Menjadi acuan teoritis penting dalam memahami penanganan non-IID pada FL terdistribusi (Bab 2).
- **Inspirasi Mekanisme Penstabil Bobot:** Konsep pengekangan deviasi bobot proksimal memiliki analogi konseptual dengan regulasi EWC pada continual learning, memperkuat pemahaman integrasi FCL.
