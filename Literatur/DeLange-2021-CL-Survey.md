---
type: literatur
title: "A Continual Learning Survey: Defying Forgetting in Classification Tasks"
authors: "Matthias De Lange, Rahaf Aljundi, Marc Masana, Sarah Parisot, Xu Jia, Ales Leonardis, Gregory Slabaugh, Tinne Tuytelaars"
year: 2021
venue: "IEEE Transactions on Pattern Analysis and Machine Intelligence (TPAMI)"
doi: "10.1109/TPAMI.2021.3057446"
arxiv: "1909.08383"
pdf: "[[PDFs/Opsional/DeLange-2021-CL-Survey.pdf]]"
dibaca_dari_pdf: ya
status: ✔ terverifikasi
tags:
  - literatur
  - continual-learning
  - catastrophic-forgetting
  - survey
  - regularization
rm_supported: RM2
relevance: ⭐⭐⭐⭐
prioritas: opsional-pendukung
---

# De Lange et al. (2021) - A Continual Learning Survey: Defying Forgetting in Classification Tasks

## Metadata

**Penulis:** Matthias De Lange, Rahaf Aljundi, Marc Masana, Sarah Parisot, Xu Jia, Ales Leonardis, Gregory Slabaugh, Tinne Tuytelaars  
**Institusi:** KU Leuven, Toyota Motor Europe, Queen Mary University of London  
**Tahun:** 2021  
**Venue:** IEEE Transactions on Pattern Analysis and Machine Intelligence (TPAMI), Vol. 44, No. 7  
**DOI:** 10.1109/TPAMI.2021.3057446  
**PDF Lokal:** [[PDFs/Opsional/DeLange-2021-CL-Survey.pdf]]  
**Status Verifikasi:** ✔ Terverifikasi dari naskah PDF IEEE TPAMI  
**Relevansi Scope:** ⭐⭐⭐⭐ HIGH - Survey definitif taksonomi continual learning dan penanganan catastrophic forgetting  

---

## 📌 3 Temuan Utama

1. **Taksonomi Metode Continual Learning:** Mengklasifikasikan pendekatan mitigasi forgetting ke dalam 3 paradigma utama:
   - *Regularization-based approaches* (misal: EWC, SI, MAS) yang membatasi pergeseran bobot kritis.
   - *Replay-based approaches* (misal: Experience Replay, GEM) yang menyimpan sebagian sampel masa lalu atau menggunakan generator data.
   - *Parameter-allocation/Architectural approaches* (misal: Progressive Networks, PackNet) yang mengalokasikan subnet khusus per task.
2. **Trade-off Stabilitas vs Plastisitas:** Menguraikan dilema komputasional fundamental di mana model harus cukup plastis untuk mempelajari representasi baru tetapi cukup stabil untuk tidak melupakan representasi lama.
3. **Analisis Komparasi Kebutuhan Memori:** Membandingkan efisiensi penyimpanan memori antara pendekatan regulasi (yang hanya memerlukan matriks fisher/pentingnya bobot) versus replay buffer (yang memerlukan kuota buffer sampel mentah).

---

## 💡 Relevansi Terhadap Penelitian Ini

- **Landasan Komparasi Algoritma CL:** Menjadi dasar teori perbandingan antara metode berbasis regulasi (EWC) dan replay (GEM/Experience Replay) pada arsitektur IDS terdistribusi (Bab 2).
- **Justifikasi Efisiensi Parameter:** Mendukung keputusan arsitektur model lokal di mana batasan kapasitas penyimpanan menjadi variabel pertimbangan penting.
