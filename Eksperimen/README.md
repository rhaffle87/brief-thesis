# Folder Eksperimen

Direktori ini dialokasikan untuk menyimpan log eksekusi, rekaman metrik training, dan parameter per run eksperimen E0 s.d. E5 per seed (seed 42, 43, 44, 45, 46).

## Struktur Pengarsipan:
- `E0_Joint/`: Log baseline terpusat
- `E1_Local_Naive/`: Log sekuensial lokal tanpa CL
- `E2_Local_EWC/`: Log sekuensial lokal dengan EWC
- `E3_FedAvg_Naive/`: Log FL terdistribusi tanpa CL
- `E4_FedAvg_EWC/`: Log FL-CL usulan (FedAvg + EWC)
- `E5_Live_Traffic/`: (Opsional) Log uji inferensi testbed Proxmox

Template format log eksperimen mengacu pada [[Template-Log-Eksperimen]].
