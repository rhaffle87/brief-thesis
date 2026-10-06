---
type: eksperimen-log
experiment_id: {{EXP_ID}}
seed: {{SEED}}
date_run: {{DATE}}
status: planned / running / completed / failed
tags: [eksperimen, {{EXP_ID}}, seed-{{SEED}}]
---

# Eksperimen {{EXP_ID}} - Seed {{SEED}}

## Konfigurasi

**Eksperimen ID:** {{EXP_ID}}  
**Tipe:** {{EXP_TYPE}}  
**Seed:** {{SEED}}  
**Tanggal Run:** {{DATE}}  
**Commit Hash Repo:** {{COMMIT_HASH}}

### Hyperparameter

| Parameter | Nilai |
|-----------|-------|
| **Model** | MLP (64 → 32 → 3) |
| **Optimizer** | Adam |
| **Learning Rate** | {{LR}} |
| **Batch Size** | {{BATCH_SIZE}} |
| **Epochs (Local)** | {{LOCAL_EPOCHS}} |
| **FL Rounds** | {{FL_ROUNDS}} (jika FL) |
| **EWC Lambda** | {{EWC_LAMBDA}} (jika EWC) |

### Data Split

| Split | Client A | Client B | Total |
|-------|----------|----------|-------|
| **Train** | {{TRAIN_A}} samples | {{TRAIN_B}} samples | {{TRAIN_TOTAL}} |
| **Val** | {{VAL_A}} | {{VAL_B}} | {{VAL_TOTAL}} |
| **Test** | {{TEST_TOTAL}} (global) | | {{TEST_TOTAL}} |

**Distribusi Non-IID:**
- Client A: Normal + SSH-Patator
- Client B: Normal + DoS

**Urutan Task:**
- Task 1: Normal + SSH-Patator
- Task 2: Normal + DoS

---

## Hasil

### Metrik Utama (Test Set)

| Metrik | Task 1 | Task 2 (After) | Task 1 (Retained) |
|--------|--------|----------------|-------------------|
| **Macro-F1** | {{MACRO_F1_T1}} | {{MACRO_F1_T2}} | {{MACRO_F1_T1_AFTER}} |
| **Accuracy** | {{ACC_T1}} | {{ACC_T2}} | {{ACC_T1_AFTER}} |

### Per-Class Performance (Task 2)

| Kelas | Precision | Recall | F1-Score | Support |
|-------|-----------|--------|----------|---------|
| Normal | {{P_NORMAL}} | {{R_NORMAL}} | {{F1_NORMAL}} | {{N_NORMAL}} |
| SSH-Patator | {{P_SSH}} | {{R_SSH}} | {{F1_SSH}} | {{N_SSH}} |
| DoS | {{P_DOS}} | {{R_DOS}} | {{F1_DOS}} | {{N_DOS}} |

### Continual Learning Metrics

| Metrik | Nilai | Keterangan |
|--------|-------|------------|
| **BWT** | {{BWT}} | Backward Transfer |
| **SSH F1 Drop** | {{SSH_DROP}}% | T1 → T2 retention |

### System Metrics

| Metrik | Nilai |
|--------|-------|
| **Training Time** | {{TRAIN_TIME}} seconds |
| **Communication Rounds** | {{ROUNDS}} (jika FL) |
| **Payload Size** | {{PAYLOAD_KB}} KB (jika FL) |

---

## Lokasi File Output

**Path Repo:** `E:/Projects/fl-cl/experiments/{{EXP_ID}}/seed_{{SEED}}/`

| File | Path |
|------|------|
| Config YAML | `config.yaml` |
| Model Checkpoint | `model_final.pt` |
| Training Log | `train.log` |
| Metrics JSON | `metrics.json` |
| Confusion Matrix | `confusion_matrix_t2.png` |

---

## Observasi & Catatan

### Anomali

- [Catat anomali jika ada: divergence, NaN loss, dll]

### Convergence

- [Apakah konvergen? Berapa round/epoch?]

### Forgetting

- [Seberapa parah forgetting SSH setelah Task 2?]

---

## Perbandingan dengan Eksperimen Lain

| Eksperimen | Macro-F1 T2 | SSH F1 Retained | BWT | Catatan |
|------------|-------------|-----------------|-----|---------|
| E1 (Baseline) | {{E1_F1}} | {{E1_SSH}} | {{E1_BWT}} | Lokal naive |
| E2 (EWC) | {{E2_F1}} | {{E2_SSH}} | {{E2_BWT}} | Lokal EWC |
| **{{EXP_ID}}** | **{{MACRO_F1_T2}}** | **{{F1_SSH}}** | **{{BWT}}** | **Current** |

---

## Action Items

- [ ] Verify hasil dengan re-run 1 seed
- [ ] Update tabel agregat di [[Matriks-E0-E5]]
- [ ] Generate confusion matrix untuk Bab 4
- [ ] Tulis interpretasi untuk Bab 5

---

**Status:** {{STATUS}}  
**Link:** [[Matriks-E0-E5]]
