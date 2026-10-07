---
type: literatur
title: "Federated Learning for Intrusion Detection System: Concepts, Challenges and Future Directions"
authors: "Shaashwat Agrawal, Sagnik Sarkar, Ons Aouedi, Gokul Yenduri, Kandaraj Piamrat, Sweta Bhattacharya, Praveen Kumar Reddy Maddikunta, Thippa Reddy Gadekallu"
year: 2021
venue: "arXiv preprint"
doi: "10.48550/arXiv.2106.09527"
arxiv: "2106.09527"
pdf: "PDFs/Opsional/Agrawal-2021-FL-IDS-Survey.pdf"
dibaca_dari_pdf: ya
status: ✔ terverifikasi
tags:
  - literatur
  - federated-learning
  - ids
  - cybersecurity
  - privacy
rm_supported: RM1
relevance: ⭐⭐⭐
prioritas: opsional-pendukung
---

# Agrawal et al. (2021) - Federated Learning for Intrusion Detection System: Concepts, Challenges and Future Directions

## Metadata

**Penulis:** Shaashwat Agrawal, Sagnik Sarkar, Ons Aouedi, Gokul Yenduri, Kandaraj Piamrat, Sweta Bhattacharya, Praveen Kumar Reddy Maddikunta, Thippa Reddy Gadekallu  
**Institusi:** Vellore Institute of Technology (India), University of Nantes (France)  
**Tahun:** 2021  
**Venue:** arXiv preprint (`arXiv:2106.09527`)  
**PDF Lokal:** [Agrawal-2021-FL-IDS-Survey.pdf](PDFs/Opsional/Agrawal-2021-FL-IDS-Survey.pdf)  
**Status Verifikasi:** ✔ Terverifikasi dari naskah PDF  
**Relevansi Scope:** ⭐⭐⭐ MEDIUM - Survey komprehensif implementasi FL pada deteksi intrusi jaringan  

---

## 📌 3 Temuan Utama

1. **Arsitektur FL untuk Deteksi Intrusi Terdistribusi:** Paper menyajikan taksonomi lengkap bagaimana Federated Learning (FL) memecahkan masalah privasi pada IDS kolaboratif. Alih-alih mentransfer log lalu lintas mentah dari perimeter jaringan lokal ke server sentral, masing-masing client (node IDS lokal) hanya membagikan pembaruan bobot model gradien.
2. **Karakteristik Heterogenitas Data Jaringan (Non-IID):** Menggarisbawahi bahwa sifat alami lalu lintas jaringan antar-node sangat heterogen (non-IID) dan asinkron, yang menjadi sumber utama degradasi performa pada algoritma agregasi konvensional seperti FedAvg standar.
3. **Analisis Komparasi Dataset IDS:** Mereview penggunaan dataset populer dalam literatur FL-IDS (NSL-KDD, UNSW-NB15, CIC-IDS2017, CSE-CIC-IDS2018) dan menyoroti perlunya standardisasi pembersihan fitur serta penanganan ketidakseimbangan kelas (*class imbalance*).

---

## 💡 Relevansi Terhadap Penelitian Ini

- **Pondasi Teoretis FL-IDS:** Memberikan tinjauan fondasi yang kuat mengenai justifikasi penerapan FL pada domain IDS jaringan (Bab 2).
- **Pemetaan Arsitektur:** Memperkuat argumen bahwa pertukaran parameter model lokal lebih aman dan hemat bandwidth daripada agregasi data mentah terpusat.
- **Kontekstualisasi Non-IID:** Memperjelas tantangan non-IID data distribution yang dihadapi dalam pengujian skenario terdistribusi pada skripsi ini.
