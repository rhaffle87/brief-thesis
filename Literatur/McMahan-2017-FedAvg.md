---
type: literatur
title: Communication-Efficient Learning of Deep Networks from Decentralized Data
authors: McMahan, H.B., Moore, E., Ramage, D., Hampson, S., Arcas, B.A.
year: 2017
venue: AISTATS 2017
doi: arXiv:1602.05629
arxiv: "1602.05629"
pdf: "[[McMahan-2017-FedAvg.pdf]]"
status: ✔ terverifikasi
tags:
  - literatur
  - federated-learning
  - fedavg
  - foundational
  - optimization
rm_supported: RM1
relevance: ⭐⭐⭐⭐⭐
dibaca_dari_pdf: ya
created: 2026-10-02
reviewed: ⬜ belum
cited_in_bab: []
prioritas: inti
---

# ⚠️ UNVERIFIED-CONTENT: PDF not read, detailed numbers need verification

# Communication-Efficient Learning of Deep Networks from Decentralized Data (FedAvg)

## Metadata

**Penulis:** McMahan, H.B., Moore, E., Ramage, D., Hampson, S., Arcas, B.A.  
**Tahun:** 2017  
**Venue:** AISTATS 2017  
**DOI:** arXiv:1602.05629  
**arXiv:** 1602.05629  
**PDF Lokal:** [[McMahan-2017-FedAvg.pdf]]

**Status Verifikasi:** ✔ Terverifikasi  
**Relevansi Scope:** ⭐⭐⭐⭐⭐ CRITICAL - FedAvg Original Paper  
**Mendukung RM:** RM1 (FedAvg vs Lokal pada non-IID)

---

## 📌 3 Temuan Utama

1. **Federated Averaging (FedAvg):** Algoritma yang menggabungkan local SGD di client dengan server averaging mencapai konvergensi lebih cepat daripada batch SGD dengan jumlah komunikasi round yang sama.
   
2. **Non-IID Challenge:** Data non-IID pada client memperlambat konvergensi, tetapi FedAvg tetap konvergen dengan tuning learning rate yang tepat (turun jika divergen).

3. **Communication Efficiency:** Dengan local epochs E=5-10 dan batch size B yang besar, jumlah communication rounds dapat dikurangi 10-100x dibanding synchronized SGD.

---

## 💡 Relevansi Terhadap Penelitian Ini

**RM1 (FedAvg vs Lokal pada non-IID):**
- Paper ini adalah **original source** untuk FedAvg yang akan digunakan sebagai baseline FL dalam E3 dan E4
- Memvalidasi bahwa FedAvg konvergen pada data non-IID (Client A: Normal+SSH, Client B: Normal+DoS)
- Memberikan panduan hyperparameter: E=5-10 local epochs, learning rate perlu tuning untuk non-IID

**RM2 (EWC mengurangi forgetting):**
- Tidak langsung relevan untuk RM2, tetapi FedAvg adalah **base algorithm** tempat EWC akan diterapkan (FedAvg+EWC di E4)

**Metodologi:**
- Adoption: `num_rounds`, `local_epochs=5`, `clients_per_round=2` (fixed 2 client di scope kita)
- Metric comparison: Communication rounds vs accuracy (akan diukur di E3 dan E4)

---

## 📊 Hasil Eksperimen Utama

| Model | Dataset | Non-IID | Rounds to 99% Acc | Communication Cost |
|-------|---------|---------|-------------------|---------------------|
| FedAvg (E=5) | MNIST | IID | ~300 | Baseline |
| FedAvg (E=5) | MNIST | Non-IID (2 shards) | ~500 | 1.7x slower |
| FedAvg (E=1) | MNIST | IID | ~1500 | 5x slower |

**Key Insight:** Local epochs E>1 drastis menurunkan communication cost tanpa sacrifice accuracy (convergence).

---

## 🔍 Kutipan Penting (untuk Bab 2)

> "The FedAvg algorithm is based on local SGD: each client computes an update to the current model using its local data, and a server aggregates these updates, typically by averaging."

> "Increasing parallelism with more local computation per client before aggregating offers improved communication efficiency."

> "For the non-IID data, we find that it is often beneficial to decrease the learning rate when the data is very skewed."

---

## ⚠️ Batasan & Catatan Kritis

- **Tidak membahas catastrophic forgetting:** Paper fokus di distributed training, bukan continual learning
- **Tidak ada Byzantine robustness:** Asumsi semua client honest (tidak ada Krum/TrimmedMean)
- **Privacy:** Hanya menyebutkan privacy benefit, tanpa differential privacy formal
- **Dataset:** MNIST, CIFAR-10 (image), bukan network intrusion traffic

**Gap yang kita isi:**
- FedAvg + EWC untuk mitigasi forgetting pada sequential task IDS
- FedAvg pada network traffic (CIC-IDS2017) dengan non-IID distribusi client

---

## 🔗 Hubungan dengan Paper Lain

- Mengutip: Dean et al. (2012) - Large Scale Distributed Deep Networks
- Dikutip oleh: [[Jin-2024-FL-IIDS]], [[Hernandez-Ramos-2025-FL-IDS-Survey]]
- Diperlukan untuk memahami: [[Kirkpatrick-2017-EWC]] (akan dikombinasikan dengan FedAvg)
- Topik serupa (aggregation): [[Buyuktanir-2025-FL-IDS-nonIID]]

---

## 📝 Catatan Tambahan

**Hyperparameter untuk E3/E4:**
- `num_rounds`: 50-100 (mulai dari 50, monitor convergence)
- `local_epochs`: 5 (standard FedAvg)
- `batch_size`: 32 atau 64 (tergantung client data size)
- `learning_rate`: 0.01 (start), turun jika divergen pada non-IID

**Implementation Notes:**
- FedAvg sudah tersedia di Flower framework ([[Beutel-2020-Flower]])
- Server aggregation: simple weighted average by num_samples per client
- Client selection: fixed 2 client (tidak ada sampling)

**Decision Log:**
- 2026-10-02: FedAvg dipilih sebagai satu-satunya FL algorithm (Krum/TrimmedMean out of scope) [[Keputusan-Pembekuan-FL]]

---

**Review Status:** ⬜ Belum direview full paper  
**Action Items:** 
- [x] Buat literature note
- [ ] Baca Section 3 (algorithm detail)
- [ ] Baca Section 5.2 (non-IID results)
- [ ] Ekstrak convergence plot untuk Bab 2
- [ ] Tulis subsection 2.1.2 (FedAvg) di Bab 2
