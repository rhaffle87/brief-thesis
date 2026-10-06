# Keputusan Pembekuan Algoritma Continual Learning

**Status:** **RESMI DISETUJUI PEMBIMBING — TERKUNCI (READY FOR PREPROCESSING)**  
**Tanggal:** 2026-10-06  

## Ketetapan Scope
- Algoritma Continual Learning yang digunakan **hanya EWC (Elastic Weight Consolidation) vs Naive Fine-tuning**.
- Metode CL lain (GEM, A-GEM, Experience Replay, LwF, PackNet) berada **di luar scope** penelitian (out of scope) demi kepatuhan regulasi privasi FL dan efisiensi node sensor.
- Pembuktian mitigasi catastrophic forgetting difokuskan pada perbandingan E1 (Naive) vs E2 (EWC) pada skenario lokal, dan E3 vs E4 pada skenario federated.
- **Prinsip Keseimbangan Bobot:** Parameter penalti Fisher EWC ($\lambda$) dituning sistematis pada rentang logaritmik $\lambda \in [10^1, 10^2, 10^3, 10^4, 10^5]$ untuk mencapai keseimbangan optimal antara stabilitas retensi memori (Recall Task 1 / SSH) dan plastisitas pembelajaran (Recall Task 2 / DoS).
