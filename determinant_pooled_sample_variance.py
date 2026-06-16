"""
Determinant of Pooled Sample Covariance Matrix

In multivariate analysis (e.g., discriminant analysis), when you have multiple groups,
you calculate a pooled sample covariance matrix from all groups combined.

Formula:
  S_p = Σ(n_i - 1)S_i / Σ(n_i - p)
  
Where:
  - n_i = sample size of group i
  - S_i = sample covariance matrix of group i
  - p = number of variables
  - k = number of groups
  - Denominator = n1 + n2 + ... + nk - k (total n minus number of groups)
"""

import numpy as np
import pandas as pd
from typing import List, Tuple, Dict

class PooledSampleCovariance:
    """Calculate determinant of pooled sample covariance matrix."""
    
    def __init__(self):
        self.groups = {}
        self.group_cov_matrices = {}
        self.pooled_cov = None
        self.determinant = None
    
    def add_group(self, group_name: str, data: np.ndarray):
        """
        Add a group's data.
        
        Args:
            group_name: Name of the group
            data: numpy array of shape (n_i, p) where n_i is sample size, p is variables
        """
        if data.ndim != 2:
            raise ValueError("Data must be 2D array (n_samples, n_features)")
        
        self.groups[group_name] = data
        
        # Calculate sample covariance for this group
        cov_matrix = np.cov(data.T, ddof=1)  # ddof=1 for sample covariance
        self.group_cov_matrices[group_name] = cov_matrix
    
    def add_group_from_file(self, group_name: str, filepath: str):
        """Load group data from TSV file."""
        data = pd.read_csv(filepath, sep='\t').values
        self.add_group(group_name, data)
    
    def calculate_pooled_covariance(self):
        """Calculate the pooled sample covariance matrix."""
        if len(self.groups) == 0:
            raise ValueError("No groups added. Use add_group() first.")
        
        n_groups = len(self.groups)
        
        # Get number of variables from first group
        first_group_data = list(self.groups.values())[0]
        n_vars = first_group_data.shape[1]
        
        # Initialize weighted sum
        weighted_sum = np.zeros((n_vars, n_vars))
        total_n = 0
        
        # Calculate weighted sum of covariance matrices
        group_info = []
        
        for group_name, data in self.groups.items():
            n_i = data.shape[0]  # Sample size of group i
            total_n += n_i
            
            cov_i = self.group_cov_matrices[group_name]
            weight = (n_i - 1)
            
            weighted_sum += weight * cov_i
            
            group_info.append({
                'group': group_name,
                'n_i': n_i,
                'weight': weight,
                'cov_matrix': cov_i
            })
        
        # Denominator: total_n - n_groups
        denominator = total_n - n_groups
        
        # Calculate pooled covariance
        self.pooled_cov = weighted_sum / denominator
        
        return self.pooled_cov, group_info, denominator, total_n
    
    def calculate_determinant(self):
        """Calculate determinant of pooled covariance matrix."""
        if self.pooled_cov is None:
            self.calculate_pooled_covariance()
        
        self.determinant = np.linalg.det(self.pooled_cov)
        return self.determinant
    
    def print_summary(self):
        """Print comprehensive summary of calculations."""
        if self.pooled_cov is None:
            pooled_cov, group_info, denominator, total_n = self.calculate_pooled_covariance()
        else:
            group_info = []
            total_n = sum([data.shape[0] for data in self.groups.values()])
            denominator = total_n - len(self.groups)
            for group_name, data in self.groups.items():
                group_info.append({
                    'group': group_name,
                    'n_i': data.shape[0],
                    'weight': data.shape[0] - 1,
                    'cov_matrix': self.group_cov_matrices[group_name]
                })
        
        if self.determinant is None:
            self.calculate_determinant()
        
        print("\n" + "="*70)
        print("POOLED SAMPLE COVARIANCE MATRIX - DETERMINANT CALCULATION")
        print("="*70)
        
        print(f"\nNumber of Groups (k): {len(self.groups)}")
        print(f"Total Sample Size (N): {total_n}")
        print(f"Number of Variables (p): {self.pooled_cov.shape[0]}")
        
        print("\n" + "-"*70)
        print("GROUP INFORMATION")
        print("-"*70)
        
        for info in group_info:
            print(f"\n{info['group']}:")
            print(f"  Sample Size (n_i): {info['n_i']}")
            print(f"  Weight (n_i - 1): {info['weight']}")
            print(f"  Sample Covariance Matrix S_{info['group'].lower()}:")
            print(info['cov_matrix'])
        
        print("\n" + "-"*70)
        print("POOLED COVARIANCE CALCULATION")
        print("-"*70)
        
        print(f"\nFormula: S_p = Σ(n_i - 1)S_i / (N - k)")
        print(f"         S_p = Σ(n_i - 1)S_i / ({total_n} - {len(self.groups)})")
        print(f"         S_p = Σ(n_i - 1)S_i / {denominator}")
        
        print(f"\nPooled Sample Covariance Matrix S_p:")
        print(self.pooled_cov)
        
        print("\n" + "-"*70)
        print("DETERMINANT CALCULATION")
        print("-"*70)
        
        print(f"\ndet(S_p) = {self.determinant:.6f}")
        print(f"det(S_p) rounded to 3 decimals = {self.determinant:.3f}")
        
        if self.determinant > 0:
            print(f"\n✓ The pooled covariance matrix is positive definite")
            print(f"  (det > 0 is expected for a valid covariance matrix)")
        elif self.determinant < 0:
            print(f"\n✗ WARNING: The determinant is negative")
            print(f"  (This shouldn't happen for a valid covariance matrix)")
        else:
            print(f"\n⚠ WARNING: The determinant is zero")
            print(f"  (The matrix is singular - not invertible)")
        
        print("\n" + "="*70)
    
    def print_step_by_step(self):
        """Print detailed step-by-step calculation."""
        if self.pooled_cov is None:
            self.calculate_pooled_covariance()
        if self.determinant is None:
            self.calculate_determinant()
        
        print("\n" + "="*70)
        print("STEP-BY-STEP CALCULATION")
        print("="*70)
        
        print("\nStep 1: Calculate sample covariance matrix for each group")
        print("-" * 70)
        for group_name, data in self.groups.items():
            n_i = data.shape[0]
            print(f"\nGroup: {group_name} (n = {n_i})")
            print(f"Data shape: {data.shape}")
            print(f"First few rows:\n{data[:3]}")
        
        print("\n\nStep 2: Calculate weighted sum")
        print("-" * 70)
        total_n = sum([data.shape[0] for data in self.groups.values()])
        weighted_sum = None
        
        for group_name, data in self.groups.items():
            n_i = data.shape[0]
            weight = n_i - 1
            cov_i = self.group_cov_matrices[group_name]
            
            if weighted_sum is None:
                weighted_sum = weight * cov_i
            else:
                weighted_sum += weight * cov_i
            
            print(f"\nGroup {group_name}: ({weight}) × S_{group_name}")
        
        print(f"\nSum: {weighted_sum}")
        
        print("\n\nStep 3: Divide by (N - k)")
        print("-" * 70)
        n_groups = len(self.groups)
        denominator = total_n - n_groups
        print(f"N - k = {total_n} - {n_groups} = {denominator}")
        print(f"\nS_p = Weighted Sum / {denominator}")
        print(self.pooled_cov)
        
        print("\n\nStep 4: Calculate determinant")
        print("-" * 70)
        print(f"det(S_p) = {self.determinant:.6f}")


def main():
    """Main function with example."""
    
    print("\n" + "="*70)
    print("POOLED SAMPLE COVARIANCE DETERMINANT CALCULATOR")
    print("="*70)
    
    # Example: Create sample data
    print("\nUsing example data with compatible dimensions...\n")
    
    # Create example data with same number of variables
    np.random.seed(42)
    
    # Group 1: 20 observations, 3 variables
    group1_data = np.random.multivariate_normal(
        mean=[0, 0, 0],
        cov=[[1.0, 0.2, 0.1],
             [0.2, 1.5, 0.3],
             [0.1, 0.3, 1.2]],
        size=20
    )
    
    # Group 2: 25 observations, 3 variables
    group2_data = np.random.multivariate_normal(
        mean=[1, 1, 1],
        cov=[[1.2, 0.15, 0.2],
             [0.15, 1.3, 0.25],
             [0.2, 0.25, 1.4]],
        size=25
    )
    
    # Group 3: 18 observations, 3 variables
    group3_data = np.random.multivariate_normal(
        mean=[-1, 0.5, -0.5],
        cov=[[0.9, 0.1, 0.05],
             [0.1, 1.1, 0.2],
             [0.05, 0.2, 1.0]],
        size=18
    )
    
    calc = PooledSampleCovariance()
    calc.add_group("Group1", group1_data)
    calc.add_group("Group2", group2_data)
    calc.add_group("Group3", group3_data)
    
    calc.print_summary()
    
    print("\n" + "="*70)
    print("ALTERNATIVE: Load from TSV files")
    print("="*70)
    print("""
To use your own data files:

    calc = PooledSampleCovariance()
    calc.add_group_from_file("Group1", "Data/Exam2026data1.tsv")
    calc.add_group_from_file("Group2", "Data/Exam2026data3.tsv")
    calc.add_group_from_file("Group3", "Data/Exam2026data4a.tsv")
    
NOTE: All files must have the same number of columns (variables)!
    """)


if __name__ == "__main__":
    main()
