"""
Calculate sample variance for TSV data files.
"""

import pandas as pd
import numpy as np

# ============ EDIT THIS LINE TO CHANGE THE FILE ============
DATA_FILE = "Data/Exam2026data3.tsv"
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
        print(f"{'Overall (all data combined):':<25} {df.values.flatten().var(ddof=1):>14.6f}\n")
        
        return variances
        
    except FileNotFoundError:
        print(f"Error: File not found - {filepath}")
        sys.exit(1)
    except Exception as e:
        print(f"Error reading file: {e}")
        sys.exit(1)


if __name__ == "__main__":
    calculate_variance(DATA_FILE)
