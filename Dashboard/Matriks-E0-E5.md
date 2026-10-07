# Matriks Eksperimen E0-E5

## 📊 Matriks Eksperimen Resmi (Scope Terkunci)

| Kode | FL | CL | Keterangan | Status | File Output |
|------|----|----|------------|--------|-------------|
| **E0** | – | – | Joint/centralized (upper bound benchmark, 5 seeds) | ⬜ TODO | `Hasil/E0_centralized_results.json` |
| **E1** | Tidak | Naive | Lokal sekuensial Task 1 $\to$ Task 2 tanpa CL | ⬜ TODO | `Hasil/E1_local_naive_results.json` |
| **E2** | Tidak | EWC | Lokal sekuensial dengan penalti Fisher ($\lambda$ balanced) | ⬜ TODO | `Hasil/E2_local_ewc_results.json` |
| **E3** | FedAvg | Naive | Federated 2-client non-IID tanpa CL | ⬜ TODO | `Hasil/E3_fedavg_naive_results.json` |
| **E4** | FedAvg | EWC | **Metode Usulan (FL-CL): FedAvg + EWC** | ⬜ TODO | `Hasil/E4_fedavg_ewc_results.json` |
| **E5** | – | – | Injeksi Live Traffic Testbed | ❌ DIELIMINASI | Ditiadakan resmi oleh pembimbing |

**Target Seed:** 5 kali pengulangan per eksperimen (Seed: 42, 43, 44, 45, 46)  
**Metrik Evaluasi Utama (Deteksi ML):** Macro-F1, per-class Recall & Precision, Backward Transfer (BWT)  
**Metrik Profiling Komputasi & Instance (Ref. Skripsi Hafizh, 2024):**  
- **Inference Latency per Flow ($\mu\text{s}$):** Mengukur kecepatan prediksi per flow untuk validasi *near real-time*.  
- **Memory Footprint (RAM / Storage):** Membuktikan efisiensi EWC ($\approx$ puluhan KB untuk bobot $\theta^*$ dan Fisher $F_i$) vs Experience Replay (puluhan/ratusan MB buffer data mentah).  
- **CPU Training Duration:** Waktu latih lokal per round untuk mengukur overhead komputasi penalti kuadratik EWC.  
- **Communication Overhead FL:** Ukuran payload parameter model (KB per round) yang dipertukarkan antara client dan server Flower ($2 \times \text{Size}(\theta) \times R$).  
*(Catatan: Parameter QoS jaringan fisik seperti jitter, bandwidth link, dan packet loss resmi ditiadakan karena E5 dieliminasi).*  
**Loss Function:** Weighted Cross-Entropy Loss (Penyeimbangan frekuensi kelas + Gradient Clipping norm 1.0)  
**Staging:** Local Workstation First $\to$ Proxmox VE Server Simulation

**Perbandingan Inti:**
- **E1 vs E2:** Mengukur dampak EWC dalam meredam *catastrophic forgetting* pada pelatihan lokal.
- **E1 vs E3:** Mengukur dampak kolaborasi Federated Learning pada data terdistribusi non-IID.
- **E3 vs E4:** Mengukur nilai tambah integrasi Continual Learning (EWC) pada arsitektur Federated Learning.
- **E4 vs E0:** Mengukur seberapa dekat performa FL-CL terhadap batas atas ideal (*Centralized Joint Training*).

---
