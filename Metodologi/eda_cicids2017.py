#!/usr/bin/env python3
"""
Exploratory Data Analysis for CIC-IDS2017 Dataset
Checks: label distribution, NaN/Inf values, duplicates, column issues
"""

import pandas as pd
import numpy as np
import sys

datasets_path = "E:/Projects/thesis/Datasets/CIC-IDS2017"
files = [
    "Monday-WorkingHours.pcap_ISCX.csv",
    "Tuesday-WorkingHours.pcap_ISCX.csv",
    "Wednesday-workingHours.pcap_ISCX.csv"
]

print("="*80)
print("EXPLORATORY DATA ANALYSIS - CIC-IDS2017")
print("="*80)

eda_results = []

for filename in files:
    print(f"\n{'='*80}")
    print(f"File: {filename}")
    print("="*80)
    
    filepath = f"{datasets_path}/{filename}"
    
    # Read sample for quick analysis
    print("Loading sample (10,000 rows)...")
    df_sample = pd.read_csv(filepath, encoding='utf-8', low_memory=False, nrows=10000)
    
    # Strip column names
    df_sample.columns = df_sample.columns.str.strip()
    
    # Get total row count (efficient)
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        total_rows = sum(1 for _ in f) - 1  # Exclude header
    
    print(f"  Total rows: {total_rows:,}")
    print(f"  Total columns: {len(df_sample.columns)}")
    
    # Check label column
    if 'Label' in df_sample.columns:
        label_col = 'Label'
    elif ' Label' in df_sample.columns:
        label_col = ' Label'
        print(f"  ⚠️ Label column has leading space: '{label_col}'")
    else:
        print(f"  ❌ Label column not found!")
        continue
    
    # Label distribution (sample)
    print(f"\n📊 Label Distribution (sample 10K):")
    label_counts = df_sample[label_col].value_counts()
    for label, count in label_counts.items():
        pct = (count / len(df_sample)) * 100
        print(f"    {label}: {count:,} ({pct:.1f}%)")
    
    # NaN/Inf check
    numeric_cols = df_sample.select_dtypes(include=[np.number]).columns
    print(f"\n⚠️ Numeric columns: {len(numeric_cols)}")
    
    nan_counts = df_sample[numeric_cols].isna().sum()
    problematic_nan = nan_counts[nan_counts > 0].sort_values(ascending=False)
    
    if len(problematic_nan) > 0:
        print(f"\n  Columns with NaN (top 10):")
        for col, count in problematic_nan.head(10).items():
            pct = (count / len(df_sample)) * 100
            print(f"    {col}: {count:,} ({pct:.1f}%)")
    
    # Check for Inf
    inf_check = []
    for col in numeric_cols[:20]:  # Sample 20 columns for speed
        inf_count = np.isinf(df_sample[col]).sum()
        if inf_count > 0:
            inf_check.append((col, inf_count))
    
    if inf_check:
        print(f"\n  Columns with Infinity values (sample):")
        for col, count in inf_check[:10]:
            print(f"    {col}: {count:,}")
    
    # Duplicate rows
    dup_rows = df_sample.duplicated().sum()
    print(f"\n📊 Duplicate rows (sample): {dup_rows:,}")
    
    # Duplicate columns
    from collections import Counter
    col_counts = Counter(df_sample.columns)
    dup_cols = [col for col, cnt in col_counts.items() if cnt > 1]
    if dup_cols:
        print(f"\n⚠️ Duplicate column names: {dup_cols}")
    
    eda_results.append({
        'file': filename,
        'total_rows': total_rows,
        'columns': len(df_sample.columns),
        'labels': label_counts.to_dict(),
        'nan_cols': len(problematic_nan),
        'duplicate_rows': dup_rows,
        'duplicate_cols': dup_cols
    })

print("\n" + "="*80)
print("SUMMARY - ALL FILES")
print("="*80)

total_rows_all = sum(r['total_rows'] for r in eda_results)
print(f"\n📊 Total dataset: {total_rows_all:,} rows across 3 files")

print("\n📋 Unique labels across all files:")
all_labels = set()
for r in eda_results:
    all_labels.update(r['labels'].keys())
print(f"  Total unique labels: {len(all_labels)}")
for label in sorted(all_labels):
    print(f"    - {label}")

print("\n✅ EDA complete. See Metodologi/EDA-CIC-IDS2017.md for full report.")
