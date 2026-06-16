"""
Test: Calculate pooled sample covariance determinant from TSV files
"""

import numpy as np
from determinant_pooled_sample_variance import PooledSampleCovariance

# Create calculator
calc = PooledSampleCovariance()

print("="*70)
print("POOLED SAMPLE COVARIANCE DETERMINANT - USING EXAM DATA")
print("="*70)

try:
    # Use compatible data files (all have 2 columns: V1, V2)
    calc.add_group_from_file("Data4a", "Data/Exam2026Data4a.tsv")
    calc.add_group_from_file("Data4b", "Data/Exam2026Data4b.tsv")
    calc.add_group_from_file("Data4c", "Data/Exam2026Data4c.tsv")
    
    # Print detailed summary
    calc.print_summary()
    
except FileNotFoundError as e:
    print(f"\nError: File not found - {e}")
    print("\nMake sure you have the correct file paths.")
    
except ValueError as e:
    print(f"\nError: {e}")
    print("\nThis often happens when files have different numbers of columns.")
    print("All groups must have the same number of variables!")

print("\n" + "="*70)
print("OTHER OPTIONS:")
print("="*70)
print("""
If you want to try different files:

Option 1: 3-variable data (only 1 file available)
  # Can't create pooled covariance with only 1 file

Option 2: 2-variable data (4 files available)
  calc.add_group_from_file("Group1", "Data/Exam2026Data4a.tsv")  # 225 rows
  calc.add_group_from_file("Group2", "Data/Exam2026Data4b.tsv")  # 300 rows
  calc.add_group_from_file("Group3", "Data/Exam2026Data4c.tsv")  # 400 rows
  calc.add_group_from_file("Group4", "Data/Exam2026Data4d.tsv")  # 600 rows
  
Option 3: Create your own groups
  import pandas as pd
  group1 = pd.read_csv('Data/Exam2026Data4a.tsv', sep='\\t').values
  group2 = pd.read_csv('Data/Exam2026Data4b.tsv', sep='\\t').values
  calc.add_group("Group1", group1)
  calc.add_group("Group2", group2)
  calc.print_summary()

FILE COMPATIBILITY SUMMARY:
- 1 column: Exam2026data3.tsv (can't use for pooled analysis)
- 2 columns: Exam2026Data4a/b/c/d.tsv ✓ (can use together)
- 3 columns: Exam2026data1.tsv (only 1 file)
- 4 columns: Exam2026data2.tsv (only 1 file)
""")

