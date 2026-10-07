---
type: literatur
title: "GFCL: A GRU-based Federated Continual Learning Framework against Data Poisoning Attacks"
authors: "Nadeem Talpur, Matthew N. Dailey, S. M. Ahsan Kazmi, et al."
year: 2022
venue: "IEEE Internet of Things Journal"
doi: "10.1109/JIOT.2022.3217436"
arxiv: ""
pdf: "PDFs/Opsional/Talpur-2022-GFCL.pdf"
dibaca_dari_pdf: ya
status: ✔ terverifikasi
tags:
  - literatur
  - federated-continual-learning
  - gru
  - intrusion-detection
  - data-poisoning
rm_supported: Both
relevance: ⭐⭐⭐⭐
prioritas: opsional-pendukung
---

# Talpur et al. (2022) - GFCL: A GRU-based Federated Continual Learning Framework

## Metadata

**Penulis:** Nadeem Talpur, Matthew N. Dailey, S. M. Ahsan Kazmi, et al.  
**Institusi:** Asian Institute of Technology, Thailand  
**Tahun:** 2022  
**Venue:** IEEE Internet of Things Journal  
**DOI:** 10.1109/JIOT.2022.3217436  
**PDF Lokal:** [Talpur-2022-GFCL.pdf](PDFs/Opsional/Talpur-2022-GFCL.pdf)  
**Status Verifikasi:** ✔ Terverifikasi dari naskah PDF IEEE JIOT  
**Relevansi Scope:** ⭐⭐⭐⭐ HIGH - Salah satu studi pionir yang menggabungkan Federated Learning dan Continual Learning untuk deteksi anomali jaringan IoT  

---

## 📌 3 Temuan Utama

1. **Framework FCL Berbasis Recurrent Architecture (GRU):** Memadukan Gated Recurrent Units (GRU) dalam kerangka kerja Federated Continual Learning untuk menangani data deret waktu jaringan serta mencegah forgetting.
2. **Mekanisme Replay Inkremental:** Menerapkan strategi penyimpanan memori selektif (selective sample replay) di tingkat lokal untuk mempertahankan performa deteksi terhadap kelas-kelas anomali lawas.
3. **Ketahanan Terhadap Poisoning:** Menguji ketahanan skema gabungan federasi dan continual learning terhadap serangan keracunan data terkoordinasi pada node IoT.

---

## 💡 Relevansi Terhadap Penelitian Ini

- **Bukti Empiris Sinergi FL + CL:** Membuktikan secara nyata pada domain keamanan jaringan bahwa federasi dan continual learning dapat diintegrasikan secara efektif (Bab 2).
- **Perbandingan Arsitektur:** Memberikan konteks pembanding arsitektur (GRU vs MLP/Feedforward) dalam trade-off latensi komputasi dan retensi memori pada node IDS terdistribusi.
