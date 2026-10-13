---
type: literatur
title: "Mitigating Catastrophic Forgetting in Continual Learning Using the Gradient-Based Approach: A Literature Review"
authors: "Haitham Ghallab, Mona Nasr, Hanan Fahmy"
year: 2025
venue: "International Journal of Advanced Computer Science and Applications (IJACSA)"
volume: 16
issue: 4
pages: "120-130"
doi: "10.14569/IJACSA.2025.0160414"
pdf: "PDFs/Ghallab-2025-Continual-Learning-Gradient-Survey.pdf"
dibaca_dari_pdf: ya
status: ✔ terverifikasi
tags:
  - literatur
  - continual-learning
  - catastrophic-forgetting
  - taxonomy
  - regularization-based
  - gradient-based
  - replay-based
  - ewc
rm_supported: RM2
relevance: ⭐⭐⭐⭐⭐
prioritas: inti-terkait
---

# Ghallab et al. (2025) - Mitigating Catastrophic Forgetting in Continual Learning Using the Gradient-Based Approach: A Literature Review

## Metadata

**Penulis:** Haitham Ghallab, Mona Nasr, Hanan Fahmy  
**Institusi:** Department of Information Systems, Faculty of Computers and Artificial Intelligence, Helwan University, Cairo, Egypt  
**Tahun:** 2025 (Mei 2025)  
**Publikasi:** *International Journal of Advanced Computer Science and Applications (IJACSA)*, Vol. 16, No. 4, pp. 120–130  
**DOI:** [10.14569/IJACSA.2025.0160414](https://doi.org/10.14569/IJACSA.2025.0160414)  
**PDF Lokal:** [Ghallab-2025-Continual-Learning-Gradient-Survey.pdf](PDFs/Ghallab-2025-Continual-Learning-Gradient-Survey.pdf)  
**Status Verifikasi:** ✔ Terverifikasi langsung dari dokumen PDF asli  
**Relevansi Scope:** ⭐⭐⭐⭐⭐ CRITICAL - Sumber primer taksonomi komprehensif pendekatan mitigasi *catastrophic forgetting* pada *Continual Learning* (Gambar 2.3)  

---

## 📌 Temuan Utama & Taksonomi (Figure 4)

1. **Taksonomi Pendekatan Mitigasi Catastrophic Forgetting:**
   Paper mengklasifikasikan pendekatan mitigasi kelupaan katastropik ke dalam kategori metodologis utama:
   - **Regularization-Based Approach:** Menggunakan suku penalti pada fungsi kerugian untuk membatasi pergeseran bobot penting tanpa menyimpan sampel mentah masa lalu (contoh: EWC, SI, MAS).
   - **Knowledge Distillation-Based Approach:** Mentransfer representasi luaran atau fitur model terdahulu ke model baru (contoh: LwF).
   - **Bayesian-Based Approach:** Memodelkan ketidakpastian posterior parameter model secara probabilistik (contoh: VCL).
   - **Gradient-Based Approach:** Memproyeksikan vektor pembaruan gradien ke ruang bagian ortogonal agar tidak mengganggu gradien tugas masa lalu (contoh: GEM, A-GEM, OGD).
   - **Architecture-Based Approach:** Mengalokasikan kapasitas jaringan, sub-jaringan, atau neuron modular baru untuk setiap tugas yang dipelajari (contoh: PNN, DEN).
   - **Replay-Based Approach:** Menyimpan atau membangkitkan kembali sampel data masa lalu untuk dilatihkan bersama (*Experience Replay* / *Generative Replay*).
   - **Hybrid Methods:** Menggabungkan dua atau lebih strategi di atas untuk mengatasi kelemahan masing-masing metode (contoh: iCaRL).

2. **Dilema Stabilitas vs Plastisitas (*Stability-Plasticity Dilemma*):**
   Menganalisis keseimbangan krusial antara mempertahankan representasi pengetahuan lampau (*stability*) dan mengakuisisi distribusi pengetahuan baru (*plasticity*).

3. **Komparasi Efisiensi Sumber Daya:**
   Mengevaluasi trade-off komputasi, jejak memori (*memory footprint*), dan privasi antar-metode, menegaskan efisiensi pendekatan regularisasi berbasis bobot dalam skenario dengan batasan memori ketat.

---

## 💡 Relevansi Terhadap Penelitian Ini

- **Sumber Primer Gambar 2.3:** Menjadi rujukan ilmiah langsung bagi diagram taksonomi mitigasi *catastrophic forgetting* pada Sub-bab 2.5.3 dan Gambar 2.3 di Bab 2 Tinjauan Pustaka.
- **Justifikasi Pemilihan EWC:** Memperkuat argumen pemilihan metode *Elastic Weight Consolidation* (EWC) sebagai varian *regularization-based* yang tidak memerlukan *buffer* penyimpanan data mentah, menjamin privasi transmisi pada arsitektur *Federated Learning*.
