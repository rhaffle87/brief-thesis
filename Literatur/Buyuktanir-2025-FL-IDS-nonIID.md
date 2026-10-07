---
type: literatur
title: "Federated learning in intrusion detection: advancements, applications, and future directions"
authors: "Busra Buyuktanir, Sahsene Altinkaya, Gozde Karatas Baydogmus, Kazim Yildiz"
year: 2025
venue: "Artificial Intelligence Review (Springer)"
doi: "10.1007/s10462-025-11231-6"
arxiv: ""
pdf: "PDFs/Buyuktanir-2025-FL-IDS.pdf"
dibaca_dari_pdf: ya
status: ✔ terverifikasi
tags:
  - literatur
  - federated-learning
  - ids
  - non-iid
  - concept-drift
rm_supported: Both
relevance: ⭐⭐⭐⭐⭐
prioritas: inti-terkait
---

# Buyuktanir et al. (2025) - Federated Learning in Intrusion Detection: Advancements, Applications, and Future Directions

## Metadata

**Penulis:** Busra Buyuktanir, Sahsene Altinkaya, Gozde Karatas Baydogmus, Kazim Yildiz  
**Institusi:** Marmara University, Istanbul Technical University (Turkey)  
**Tahun:** 2025 (Published August 2025)  
**Venue:** Artificial Intelligence Review (Springer)  
**DOI:** 10.1007/s10462-025-11231-6  
**PDF Lokal:** [Buyuktanir-2025-FL-IDS.pdf](PDFs/Buyuktanir-2025-FL-IDS.pdf)  
**Status Verifikasi:** ✔ Terverifikasi dari naskah PDF Springer  
**Relevansi Scope:** ⭐⭐⭐⭐⭐ CRITICAL - Survey komprehensif terkini (2025) fokus pada FL-IDS, non-IID data, dan dinamika serangan baru  

---

## 📌 3 Temuan Utama

1. **Pemetaan Kesenjangan Riset FL-IDS:** Menunjukkan bahwa sebagian besar riset FL-IDS masih mengasumsikan distribusi data IID yang statis, sementara dunia nyata ditandai oleh non-IID ekstrem, pergeseran lalu lintas (*traffic drift*), dan kemunculan pola serangan zero-day/inkremental.
2. **Kelemahan FedAvg Konvensional:** FedAvg mengalami penurunan akurasi signifikan (drastic accuracy drop) saat diterapkan pada lingkungan jaringan di mana tiap entitas/cabang menghadapi jenis serangan yang tidak seimbang (skewed label distribution).
3. **Pentingnya Integrasi Adaptasi Berkelanjutan:** Paper merekomendasikan eksplorasi mekanisme adaptif seperti federated continual learning untuk mencegah degradasi performa model deteksi lama saat menghadapi gelombang serangan baru.

---

## 💡 Relevansi Terhadap Penelitian Ini

- **State-of-the-Art Review (2025):** Menjadi rujukan mutakhir Bab 1 dan Bab 2 yang memvalidasi bahwa kombinasi FL dan pembelajaran inkremental/continual adalah kebutuhan terdepan dalam domain cybersecurity.
- **Justifikasi Masalah Non-IID:** Memperkuat justifikasi perumusan masalah (RM1 dan RM2) bahwa pengujian model IDS harus mempertimbangkan kondisi non-IID dan retensi memori terhadap kelas serangan sebelumnya.
