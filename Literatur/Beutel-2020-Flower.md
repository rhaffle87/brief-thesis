---
type: literatur
title: "Flower: A Friendly Federated Learning Framework"
authors: "Daniel J. Beutel, Taner Topal, Akhil Mathur, Xinchi Qiu, Javier Fernandez-Marques, Yan Gao, Lorenzo Sani, Kwing Hei Li, Titouan Parcollet, Pedro Porto Buarque de Gusmao, Nicholas D. Lane"
year: 2020
venue: "arXiv preprint"
doi: "10.48550/arXiv.2007.14390"
arxiv: "2007.14390"
pdf: "[[PDFs/Beutel-2020-Flower.pdf]]"
dibaca_dari_pdf: ya
status: ✔ terverifikasi
tags:
  - literatur
  - federated-learning
  - flower
  - framework
  - edge-computing
rm_supported: RM1
relevance: ⭐⭐⭐⭐
prioritas: inti-terkait
---

# Beutel et al. (2020) - Flower: A Friendly Federated Learning Framework

## Metadata

**Penulis:** Daniel J. Beutel, Taner Topal, Akhil Mathur, Xinchi Qiu, Javier Fernandez-Marques, Yan Gao, Lorenzo Sani, Kwing Hei Li, Titouan Parcollet, Pedro Porto Buarque de Gusmao, Nicholas D. Lane  
**Institusi:** University of Cambridge, Adap, Samsung AI Center  
**Tahun:** 2020  
**Venue:** arXiv:2007.14390  
**PDF Lokal:** [[PDFs/Beutel-2020-Flower.pdf]]  
**Status Verifikasi:** ✔ Terverifikasi dari naskah PDF  
**Relevansi Scope:** ⭐⭐⭐⭐ HIGH - Framework FL utama yang mendasari orkestrasi federasi penelitian  

---

## 📌 3 Temuan Utama

1. **Desain Arsitektur Agnostik Framework:** Flower dirancang agar independen dari framework deep learning (mendukung PyTorch, TensorFlow, Jax, Hugging Face) dengan abstraksi komunikasi klien-server berbasis gRPC yang ringan dan modular.
2. **Skalabilitas dan Heterogenitas Perangkat:** Mampu menangani dari simulasi komputasi skala besar pada satu mesin (Virtual Client Engine) hingga penyebaran nyata pada perangkat edge bergerak (Android, Raspberry Pi) dengan konsumsi memori efisien.
3. **Dukungan Kustomisasi Algoritma Strategi Agregasi:** Menyediakan antarmuka kustom yang fleksibel untuk berbagai strategi federasi (FedAvg, FedProx, QFedAvg, Fault-Tolerant Aggregations) serta penanganan metrik evaluasi federasi yang terstandar.

---

## 💡 Relevansi Terhadap Penelitian Ini

- **Dasar Implementasi Testbed:** Flower menjadi library orkestrator yang digunakan dalam arsitektur eksperimen skripsi untuk menghubungkan client Proxmox/simulasi dengan federated server.
- **Kemudahan Integrasi Continual Learning:** Arsitektur modular Flower memungkinkan injeksi modul continual learning lokal (EWC, GEM, replay) di setiap local client tanpa merusak alur komunikasi federasi.
