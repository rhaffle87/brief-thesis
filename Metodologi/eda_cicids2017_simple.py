#!/usr/bin/env python3
"""
Exploratory Data Analysis for CIC-IDS2017 Dataset (stdlib only)
Checks: label distribution, column issues, basic stats
"""

import csv
from collections import Counter, defaultdict
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
    
    # Quick scan
    print("Analyzing...")
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        reader = csv.DictReader(f)
        
        # Strip column names
        fieldnames = [col.strip() for col in reader.fieldnames]
        
        # Find label column
        label_col = 'Label' if 'Label' in fieldnames else None
        if not label_col and ' Label' in reader.fieldnames:
            label_col = ' Label'
            print(f"  ⚠️ Label column has leading space")
        
        if not label_col:
            print(f"  ❌ No Label column found!")
            print(f"  Available columns (first 10): {fieldnames[:10]}")
            continue
        
        # Scan sample for labels
        label_counts = Counter()
        row_count = 0
        sample_size = 10000
        
        for row in reader:
            if row_count >= sample_size:
                break
            label_counts[row[label_col].strip()] += 1
            row_count += 1
    
    # Count total rows
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        total_rows = sum(1 for _ in f) - 1
    
    print(f"  Total rows: {total_rows:,}")
    print(f"  Total columns: {len(fieldnames)}")
    
    print(f"\n📊 Label Distribution (sample {sample_size}):")
    for label, count in label_counts.most_common():
        pct = (count / sample_size) * 100
        print(f"    {label}: {count:,} ({pct:.1f}%)")
    
    # Check for duplicate column names
    col_counts = Counter(fieldnames)
    dup_cols = [col for col, cnt in col_counts.items() if cnt > 1]
    if dup_cols:
        print(f"\n [!] Duplicate column names: {dup_cols}")
    
    eda_results.append({
        'file': filename,
        'total_rows': total_rows,
        'columns': len(fieldnames),
        'labels': dict(label_counts),
        'duplicate_cols': dup_cols,
        'fieldnames': fieldnames
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

# Check for problematic labels
print("\n [!] Labels to handle:")
tuesday_labels = eda_results[1]['labels'].keys()
wednesday_labels = eda_results[2]['labels'].keys()

if 'SSH-Patator' in tuesday_labels and 'FTP-Patator' in tuesday_labels:
    print("  Tuesday: Has both SSH-Patator and FTP-Patator (exclude FTP)")
if 'Heartbleed' in wednesday_labels:
    print("  Wednesday: Has Heartbleed (exclude, only 11 samples)")

print("\n✅ EDA complete.")
print("\nWriting detailed report to Metodologi/EDA-CIC-IDS2017.md...")
