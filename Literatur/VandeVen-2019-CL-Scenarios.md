---
type: literatur
title: "Three Scenarios for Continual Learning"
authors: "Gido M. van de Ven, Andreas S. Tolias"
year: 2019
venue: "arXiv preprint / Nature Communications"
doi: "10.48550/arXiv.1904.07734"
arxiv: "1904.07734"
pdf: "[[PDFs/Opsional/VandeVen-2019-CL-Scenarios.pdf]]"
dibaca_dari_pdf: ya
status: ✔ terverifikasi
tags:
  - literatur
  - continual-learning
  - class-incremental
  - task-incremental
  - domain-incremental
rm_supported: RM2
relevance: ⭐⭐⭐⭐⭐
prioritas: inti-terkait
---

# van de Ven & Tolias (2019) - Three Scenarios for Continual Learning

## Metadata

**Penulis:** Gido M. van de Ven, Andreas S. Tolias  
**Institusi:** Baylor College of Medicine, Houston, TX, USA  
**Tahun:** 2019  
**Venue:** arXiv:1904.07734 / Nature Communications  
**PDF Lokal:** [[PDFs/Opsional/VandeVen-2019-CL-Scenarios.pdf]]  
**Status Verifikasi:** ✔ Terverifikasi dari naskah PDF  
**Relevansi Scope:** ⭐⭐⭐⭐⭐ CRITICAL - Kerangka konseptual seminal yang mendefinisikan 3 skenario Continual Learning  

---

## 📌 3 Temuan Utama

1. **Tiga Skenario Utama Continual Learning:**
   - **Task-Incremental Learning (Task-IL):** Model diberikan Task-ID saat inferensi (kepala output terpisah untuk tiap task; skenario paling mudah).
   - **Domain-Incremental Learning (Domain-IL):** Struktur task berubah (distribusi input bergeser), tetapi output classes sama dan Task-ID tidak diketahui saat pengujian.
   - **Class-Incremental Learning (Class-IL):** Model harus mendiskriminasikan semua kelas dari semua task tanpa Task-ID (kepala output tunggal bersama; skenario paling sulit dan realistis).
2. **Kesenjangan Performa Antar Skenario:** Metode yang berhasil dengan baik di Task-IL (seperti EWC sederhana) sering kali gagal total di Class-IL karena masalah ambiguitas prediksi antar-task (*task-recency bias*).
3. **Urgensi Penentuan Skenario yang Jelas:** Menekankan bahwa klaim performa continual learning tidak bermakna tanpa menyebutkan secara eksplisit skenario mana yang sedang diuji.

---

## 💡 Relevansi Terhadap Penelitian Ini

- **Klasifikasi Skenario Skripsi (Class-IL):** Menjadi rujukan teoritis mutlak di Bab 1 dan Bab 3 yang menegaskan bahwa eksperimen Task 1 (SSH Brute Force) dan Task 2 (DoS) berada dalam skenario **Class-Incremental Learning (Class-IL)** tanpa Task-ID saat inferensi.
- **Justifikasi Analisis Catastrophic Forgetting:** Memperjelas mengapa penambahan kelas serangan baru pada node IDS menantang kestabilan klasifikasi model global.
