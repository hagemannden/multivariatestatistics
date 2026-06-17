import pandas as pd
import numpy as np
import sys

# ============ EDIT THIS LINE TO CHANGE THE FILE ============
DATA_FILE = "Data/Exam2026data1.tsv"
# =========================================================


def calculate_variance(filepath):
    """
    Indlæser en TSV-fil og beregner stikprøvevarians (sample variance)
    for hver søjle samt den totale stikprøvevarians for hele datasættet.
    
    Args:
        filepath (str): Stien til TSV-filen
    """
    try:
        # Indlæser TSV-filen
        df = pd.read_csv(filepath, sep='\t')
        
        print(f"\n{'='*60}")
        print(f"Fil: {filepath}")
        print(f"{'='*60}\n")
        print(f"Dimensioner: {df.shape[0]} rækker × {df.shape[1]} søjler\n")
        
        # 1. Beregn sample varians for hver søjle (ddof=1 sikrer n-1 i nævneren)
        column_variances = df.var(ddof=1)
        
        print("Sample Varians for hver søjle:")
        print("-" * 40)
        for col, var in column_variances.items():
            print(f"  {col:<15} {var:>15.6f}")
        print("-" * 40)
        
        print("\n=== TOTAL SAMPLE VARIANS FOR HELE DATASÆTTET ===")
        
        # Mulighed 1: Summen af alle søjlevarianser (bruges typisk i multivariat statistik / PCA)
        total_var_sum = column_variances.sum()
        print(f"Metode 1 (Summen af alle søjlevarianser):     {total_var_sum:.6f}")
        
        # Mulighed 2: Variansen udregnet på tværs af absolut alle tal i datasættet på én gang
        all_values = df.to_numpy().flatten()
        total_var_all_data = np.var(all_values, ddof=1)
        print(f"Metode 2 (Variansen af alle datapunkter puljet): {total_var_all_data:.6f}")
        print("=" * 60)
        
        return column_variances
        
    except FileNotFoundError:
        print(f"Fejl: Filen blev ikke fundet - {filepath}")
        sys.exit(1)
    except Exception as e:
        print(f"Fejl ved læsning af filen: {e}")
        sys.exit(1)


if __name__ == "__main__":
    calculate_variance(DATA_FILE)