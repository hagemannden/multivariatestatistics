"""Check dimensions of all data files"""
import pandas as pd
import os

print("="*80)
print("DATA FILE DIMENSIONS CHECK")
print("="*80)

data_dir = "Data"
file_info = []

for filename in sorted(os.listdir(data_dir)):
    if filename.endswith('.tsv'):
        filepath = os.path.join(data_dir, filename)
        df = pd.read_csv(filepath, sep='\t')
        n_rows, n_cols = df.shape
        cols = list(df.columns)
        file_info.append((filename, n_rows, n_cols, cols))
        print(f"\n{filename}")
        print(f"  Shape: {n_rows} rows × {n_cols} columns")
        print(f"  Columns: {cols}")

# Group by number of columns
print("\n" + "="*80)
print("COMPATIBILITY GROUPS (same number of variables)")
print("="*80)

by_cols = {}
for filename, n_rows, n_cols, cols in file_info:
    if n_cols not in by_cols:
        by_cols[n_cols] = []
    by_cols[n_cols].append(filename)

for n_cols in sorted(by_cols.keys()):
    print(f"\n{n_cols} columns: {', '.join(by_cols[n_cols])}")

print("\n" + "="*80)
print("RECOMMENDATION")
print("="*80)

# Find the group with most files
if by_cols:
    best_group = max(by_cols.items(), key=lambda x: len(x[1]))
    n_cols, files = best_group
    if len(files) >= 2:
        print(f"\nFiles with {n_cols} columns (can be used together):")
        for f in files:
            print(f"  - {f}")
        print(f"\nTo use them, run:")
        print(f"  calc.add_group_from_file('Group1', 'Data/{files[0]}')")
        print(f"  calc.add_group_from_file('Group2', 'Data/{files[1]}')")
        if len(files) > 2:
            print(f"  calc.add_group_from_file('Group3', 'Data/{files[2]}')")
