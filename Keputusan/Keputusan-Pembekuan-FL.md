# Keputusan Pembekuan Algoritma Federated Learning

**Status:** **RESMI DISETUJUI PEMBIMBING — TERKUNCI (READY FOR PREPROCESSING)**  
**Tanggal:** 2026-10-06  

## Ketetapan Scope
- Algoritma Federated Learning yang digunakan **hanya FedAvg (McMahan et al., 2017)**.
- Jumlah client dibekukan pada **2 client** (Client A dan Client B) dengan karakteristik distribusi non-IID terisolasi (Client A: Normal + SSH; Client B: Normal + DoS).
- **Protokol Staging Testbed:** Realisasi lokal terlebih dahulu (Local First via Docker Compose / isolated Python environment), kemudian dilanjutkan simulasi server klaster Proxmox VE.
- **Injeksi Trafik:** Ditiadakan resmi oleh dosen pembimbing. Seluruh pengujian menggunakan data tabular batch offline CIC-IDS2017.
- Algoritma agregasi lanjutan (FedProx, Scaffold, Krum, TrimmedMean, DP) berada **di luar scope** penelitian.
