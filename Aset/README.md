# Dokumentasi Inventaris Aset Visual & Model (`Aset/`)

**Lokasi Repositori:** `E:/Projects/thesis/Aset/`  
**Terakhir Diperbarui:** 2026-10-06  
**Status Audit:** ✅ Terorganisasi, Tervalidasi, & Bebas Redundansi  

---

## 📌 1. Gambaran Umum & Kebijakan Folder

Direktori `Aset/` berfungsi sebagai repositori penyimpanan tunggal untuk seluruh **aset visual non-generatif AI** (diagram arsitektur, skema metodologi, ilustrasi teoretis berdasar paper rujukan resmi, diagram evaluasi) serta **artefak model komputasi biner** (`.onnx`) yang disematkan dalam dokumen proposal, naskah skripsi, dan presentasi tugas akhir.

### ⚠️ Catatan Reorganisasi Berkas PDF
Sebelumnya, terdapat 3 berkas jurnal/survei ilmiah berformat PDF di folder ini yang diunduh saat proses ekstraksi diagram Continual Learning. Sesuai konvensi repositori dan standar pemisahan konten, berkas-berkas PDF tersebut telah **direlokasi ke folder literatur resmi**:
1. `delange2021_survey.pdf` ➡️ [DeLange-2021-CL-Survey.pdf](../Literatur/PDFs/Opsional/DeLange-2021-CL-Survey.pdf) ([DeLange-2021-CL-Survey](../Literatur/DeLange-2021-CL-Survey.md))
2. `vandeven2019_scenarios.pdf` ➡️ [VandeVen-2019-CL-Scenarios.pdf](../Literatur/PDFs/Opsional/VandeVen-2019-CL-Scenarios.pdf) ([VandeVen-2019-CL-Scenarios](../Literatur/VandeVen-2019-CL-Scenarios.md))
3. `wang2023_survey.pdf` ➡️ [Wang-2023-CL-Survey.pdf](../Literatur/PDFs/Opsional/Wang-2023-CL-Survey.pdf) ([Wang-2023-CL-Survey](../Literatur/Wang-2023-CL-Survey.md))

Dengan demikian, direktori `Aset/` saat ini murni memuat aset visual dan biner model komputasi.

---

## 📂 2. Katalog Lengkap Aset (16 Berkas)

### A. Diagram Arsitektur & Topologi Testbed
| Nama Berkas | Format & Ukuran | Resolusi | Deskripsi & Konten | Sumber / Rujukan |
|---|---|---|---|---|
| `arsitektur_testbed_fl_cl.png` | PNG (247,1 KB) | 2720 × 1920 | Arsitektur lengkap testbed FL-CL terdistribusi: PVE FL Server (FedAvg Aggregator), Client A (Node PVE-01, Task 1: Normal+SSH), Client B (Node PVE-02, Task 2: Normal+DoS), metrik evaluasi F1/BWT, dan Avalanche EWC. | Dibuat khusus untuk arsitektur tugas akhir ITS |
| `cicids2017_testbed_architecture_sharafaldin2018.png` | PNG (698,4 KB) | 2063 × 842 | Diagram topologi jaringan capture dataset CIC-IDS2017: Victim Network (Web, Management, Server) dan Attack Network terpisah. | Sharafaldin et al. (2018) [Sharafaldin-2018-CIC-IDS2017](../Literatur/Sharafaldin-2018-CIC-IDS2017.md) |
| `centralized_vs_fl_hernandezramos2025.png` | PNG (121,8 KB) | 1605 × 834 | Ilustrasi perbandingan komparatif model terpusat (Centralized) vs Federated Learning berbasis pertukaran bobot gradien tanpa memindahkan raw traffic. | Hernandez-Ramos et al. (2025, ACM CSUR) [Hernandez-Ramos-2025-FL-IDS-Survey](../Literatur/Hernandez-Ramos-2025-FL-IDS-Survey.md) |
| `federated_learning_architecture_web.png` | PNG (160,2 KB) | 1716 × 1196 | Siklus umum Federated Learning: global model initialization, local training pada edge clients, weight aggregation pada server, dan global distribution. | Konsep dasar Federated Learning |
| `federated_learning_fedavg_protocol.png` | PNG (136,1 KB) | 1716 × 1196 | Protokol detail langkah demi langkah algoritma Federated Averaging (FedAvg). | McMahan et al. (2017) [McMahan-2017-FedAvg](../Literatur/McMahan-2017-FedAvg.md) |

---

### B. Diagram Alur Metodologi & Tahapan Riset
| Nama Berkas | Format & Ukuran | Resolusi | Deskripsi & Konten | Sumber / Rujukan |
|---|---|---|---|---|
| `alur_metode_penelitian.png` | PNG (158,9 KB) | 2720 × 1000 | Diagram 6 tahapan riset: (1) Ekstraksi & Kurasi Data, (2) Partisi Skenario Non-IID & Class-IL, (3) Baseline E0-E2, (4) Inovasi E3 FL-CL, (5) Evaluasi Macro-F1 & BWT, (6) Sintesis Laporan Akhir. | Dibuat untuk Metodologi Penelitian TA |

---

### C. Diagram Teoretis Continual Learning & Regularisasi EWC
| Nama Berkas | Format & Ukuran | Resolusi | Deskripsi & Konten | Sumber / Rujukan |
|---|---|---|---|---|
| `continual_learning_taxonomy_delange2021.png` | PNG (159,6 KB) | 1076 × 626 | Taksonomi komprehensif Continual Learning ke dalam 3 cabang: Replay, Regularization-based (Prior/Data-focused), dan Parameter Allocation. | De Lange et al. (2021, IEEE TPAMI) [DeLange-2021-CL-Survey](../Literatur/DeLange-2021-CL-Survey.md) |
| `continual_learning_framework_wang2023.png` | PNG (286,3 KB) | 1064 × 787 | Kerangka arsitektur Continual Learning sistematis: computational flow antara memory buffer, parameter regularization, dan multi-objective trade-off. | Wang et al. (2023, IEEE TPAMI 2024) [Wang-2023-CL-Survey](../Literatur/Wang-2023-CL-Survey.md) |
| `ewc_parameter_space_kirkpatrick2017.png` | PNG (212,3 KB) | 1043 × 1063 | Visualisasi manifold lintasan parameter ruang bobot: penalti kuadratik EWC menjaga bobot tetap dalam batas performa Task A selagi mempelajari Task B, mencegah catastrophic forgetting. | Kirkpatrick et al. (2017, PNAS) [Kirkpatrick-2017-EWC](../Literatur/Kirkpatrick-2017-EWC.md) |

---

### D. Arsitektur Model Multilayer Perceptron (MLP) & Artefak Netron
| Nama Berkas | Format & Ukuran | Resolusi / Ukuran | Deskripsi & Konten | Sumber / Rujukan |
|---|---|---|---|---|
| `arsitektur_model_mlp.drawio` | XML / Draw.io | Diagram XML Interaktif | Diagram arsitektur MLP kompak 3 lapis (63 masukan, Linear 64, ReLU, Linear 32, ReLU, Linear 3 keluaran) berkapasitas 6.275 parameter. Dibuat via Draw.io MCP. | Rancangan Terkini Model TA |
| `arsitektur_model_mlp.svg` | SVG | Vektor Asli Skalabel | Ilustrasi vektor resolusi tinggi rancangan arsitektur layer-by-layer MLP 6.275 parameter dengan rincian parameter, memori ~25,1 KB, dan spesifikasi komputasi. | Aset Vektor Resmi TA |
| `mlp_architecture_diagram_web.png` | PNG (104,0 KB) | 986 × 1186 | Diagram detail layer-by-layer MLP IDS: Input 63 fitur -> Dense 128 (ReLU + Dropout 0.2) -> Dense 64 -> Dense 32 -> Output 3 kelas (Softmax/Logits). | Rancangan Model Task TA |
| `mlp_architecture_diagram_web.svg` | SVG (205,9 KB) | Vektor Asli | Berkas master format vektor skalabel untuk diagram layer-by-layer MLP IDS. | Vektor rancangan model TA |
| `netron_mlp_architecture.png` | PNG (21,4 KB) | 344 × 585 | Screenshot komputasi grafis resmi yang dirender langsung melalui Netron.app dari berkas `mlp_intrusion_model.onnx`. | Netron Visualizer |
| `mlp_intrusion_model.onnx` | ONNX (25,4 KB) | Biner Model | Model komputasi PyTorch serialisasi Open Neural Network Exchange (ONNX) untuk inspeksi arsitektur, parameter weights, tensor shape, dan op-types. | PyTorch Export ONNX |

---

### E. Metrik Evaluasi Klasifikasi & Deteksi Intrusi
| Nama Berkas | Format & Ukuran | Resolusi | Deskripsi & Konten | Sumber / Rujukan |
|---|---|---|---|---|
| `confusion_matrix_detailed_web.png` | PNG (65,4 KB) | 481 × 483 | Matriks kontingensi detail (True Positive, False Positive, True Negative, False Negative) beserta rumus turunan sensitivitas, spesifisitas, dan presisi. | Standar Metrik Evaluasi Klasifikasi |
| `precision_recall_diagram_walber2014.png` | PNG (196,9 KB) | 1834 × 3334 | Diagram himpunan Venn presisi, recall, akurasi, dan F1-score dengan skema warna definisi standar informasi temu balik. | Walber (2014), Wikimedia Commons (CC-BY-SA 4.0) |
| `precision_recall_diagram_walber2014.svg` | SVG (47,0 KB) | Vektor Asli | Master berkas vektor skalabel diagram presisi dan recall. | Walber (2014), CC-BY-SA 4.0 |

---

## 🔗 3. Referensi Integrasi dalam Naskah & Dokumen

Seluruh aset di atas telah dihubungkan langsung ke dalam dokumen perencanaan dan naskah:
- `Proposal/Briefing-Scope-TA.md` (bagian 1, 2, 3, 6, 8, dan 10)
- `README-Structure.md` (ikhtisar repositori)
- Naskah Bab 2 (Landasan Teori) dan Bab 3 (Metodologi Penelitian)
