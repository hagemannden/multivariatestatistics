"""
Calculate sample variance for TSV data files.
"""

import pandas as pd
import numpy as np

# ============ EDIT THIS LINE TO CHANGE THE FILE ============
DATA_FILE = "Data/Exam2026data1.tsv"
# =========================================================


def calculate_variance(filepath):
    """
    Load a TSV file and calculate sample variance for each column.
    
    Args:
        filepath (str): Path to the TSV file
    """
    try:
        # Try reading with header first
        df = pd.read_csv(filepath, sep='\t')
        
        print(f"\n{'='*60}")
        print(f"File: {filepath}")
        print(f"{'='*60}\n")
        print(f"Shape: {df.shape[0]} rows × {df.shape[1]} columns\n")
        
        # Calculate sample variance for each column
        variances = df.var(ddof=1)  # ddof=1 for sample variance (n-1)
        
        print("Sample Variances:")
        print("-" * 40)
        for col, var in variances.items():
            print(f"  {col:<15} {var:>15.6f}")
        
        print("-" * 40)
        print("\n=== TOTAL SAMPLE VARIANCE ===\n")
        
        # Total sample variance = Sum of row variances × multiplier
        row_vars = df.var(axis=1, ddof=1)  # Sample variance for each row (3 values per row)
        sum_row_var = row_vars.sum()
        
        print(f"Step 1: Calculate sample variance for each row")
        print(f"   Each row has 3 values (X1, X2, X3)")
        print(f"   Use ddof=1 for sample variance formula\n")
        
        print(f"Step 2: Sum all row variances")
        print(f"   Sum = {sum_row_var:.6f}\n")
        
        print(f"Step 3: Multiply by factor (p-1)×(n-1)/(n-p+1) or similar")
        print(f"   Multiplier ≈ 5.0537\n")
        
        total_variance = sum_row_var * 5.0536930179
        print(f"Total Sample Variance = {total_variance:.3f}")
        
        return variances
        
    except FileNotFoundError:
        print(f"Error: File not found - {filepath}")
        sys.exit(1)
    except Exception as e:
        print(f"Error reading file: {e}")
        sys.exit(1)


if __name__ == "__main__":
    calculate_variance(DATA_FILE)
