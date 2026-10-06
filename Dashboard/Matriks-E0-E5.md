# Matriks Eksperimen E0-E5

## 📊 Matriks Eksperimen

| Kode | FL | CL | Keterangan | Status | File Output |
|------|----|----|------------|--------|-------------|
| E0 | – | – | Joint/centralized (upper bound) | ⬜ TODO | - |
| E1 | Tidak | Naive | Lokal sekuensial tanpa CL | ⬜ TODO | - |
| E2 | Tidak | EWC | Lokal sekuensial dengan EWC | ⬜ TODO | - |
| E3 | FedAvg | Naive | Federated tanpa CL | ⬜ TODO | - |
| E4 | FedAvg | EWC | **FL-CL (Target Utama)** | ⬜ TODO | - |
| E5 | – | – | Validasi live traffic (OPSIONAL) | ⬜ SKIP | - |

**Target Seed:** 3-5 kali pengulangan per eksperimen  
**Metrik Utama:** Macro-F1, per-class recall/F1, BWT

**Perbandingan Inti:**
- E1 vs E2 → Efek EWC
- E1 vs E3 → Efek FL
- E3 vs E4 → Nilai tambah CL pada FL

---
