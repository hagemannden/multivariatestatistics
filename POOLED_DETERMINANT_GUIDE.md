# Pooled Sample Covariance Determinant Calculator

## 📋 Summary

The `determinant_pooled_sample_variance.py` file calculates the **determinant of the pooled sample covariance matrix** for multivariate data with multiple groups.

## 🎯 Quick Start

### Run with Example Data
```bash
python determinant_pooled_sample_variance.py
```

### Run with Your Exam Data
```bash
python test_pooled_determinant.py
```

### Check Data File Compatibility
```bash
python check_data_dimensions.py
```

## 📐 Formula

For k groups with sample sizes n₁, n₂, ..., nₖ:

```
S_p = Σ(nᵢ - 1)Sᵢ / (N - k)
```

Where:
- **Sᵢ** = sample covariance matrix of group i
- **nᵢ** = sample size of group i
- **N** = total sample size (n₁ + n₂ + ... + nₖ)
- **k** = number of groups
- **S_p** = pooled sample covariance matrix

Then calculate: **det(S_p)**

## 💻 Usage Examples

### Example 1: Use Your Exam Data
```python
from determinant_pooled_sample_variance import PooledSampleCovariance

calc = PooledSampleCovariance()

# Load 3 groups (all must have same number of columns!)
calc.add_group_from_file("Group1", "Data/Exam2026Data4a.tsv")
calc.add_group_from_file("Group2", "Data/Exam2026Data4b.tsv")
calc.add_group_from_file("Group3", "Data/Exam2026Data4c.tsv")

# Calculate and display results
calc.print_summary()
```

### Example 2: Use NumPy Arrays
```python
import numpy as np
from determinant_pooled_sample_variance import PooledSampleCovariance

calc = PooledSampleCovariance()

# Create your data
group1 = np.array([[1, 2], [3, 4], [5, 6]])
group2 = np.array([[2, 3], [4, 5], [6, 7]])

# Add groups
calc.add_group("Group1", group1)
calc.add_group("Group2", group2)

# Get results
calc.calculate_pooled_covariance()
det = calc.calculate_determinant()
print(f"Determinant: {det:.3f}")
```

### Example 3: Get Just the Determinant
```python
calc = PooledSampleCovariance()
calc.add_group_from_file("G1", "Data/file1.tsv")
calc.add_group_from_file("G2", "Data/file2.tsv")

det = calc.calculate_determinant()
print(f"det(S_p) = {det:.6f}")
```

## 📊 Your Data Files

| File | Variables | Rows | Compatible With |
|------|-----------|------|-----------------|
| Exam2026data1.tsv | 3 (X1, X2, X3) | 200 | ❌ Only one file |
| Exam2026data2.tsv | 4 (V1-V4) | 250 | ❌ Only one file |
| Exam2026data3.tsv | 1 (V1) | 500 | ❌ Only one file |
| **Exam2026Data4a.tsv** | **2 (V1, V2)** | **225** | ✓ 4a, 4b, 4c, 4d |
| **Exam2026Data4b.tsv** | **2 (V1, V2)** | **300** | ✓ 4a, 4b, 4c, 4d |
| **Exam2026Data4c.tsv** | **2 (V1, V2)** | **400** | ✓ 4a, 4b, 4c, 4d |
| **Exam2026Data4d.tsv** | **2 (V1, V2)** | **600** | ✓ 4a, 4b, 4c, 4d |

**✓ Best option: Use Data4a, Data4b, Data4c, Data4d together** (all have 2 columns)

## 📈 Output Example

```
======================================================================
POOLED SAMPLE COVARIANCE MATRIX - DETERMINANT CALCULATION
======================================================================

Number of Groups (k): 3
Total Sample Size (N): 925
Number of Variables (p): 2

GROUP INFORMATION
─────────────────────────────────────────────────────────────────────
Data4a: n_i = 225, weight = 224
  Covariance: [[ 4.66  14.15]
               [14.15  76.44]]

Data4b: n_i = 300, weight = 299
  Covariance: [[ 4.54  12.26]
               [12.26  69.25]]

Data4c: n_i = 400, weight = 399
  Covariance: [[ 3.52   8.62]
               [ 8.62  56.14]]

POOLED COVARIANCE CALCULATION
─────────────────────────────────────────────────────────────────────
S_p = Σ(n_i - 1)S_i / (N - k)
    = Σ(n_i - 1)S_i / (925 - 3)
    = Σ(n_i - 1)S_i / 922

S_p = [[ 4.13  11.15]
       [11.15  65.32]]

DETERMINANT CALCULATION
─────────────────────────────────────────────────────────────────────
det(S_p) = 145.421334
det(S_p) rounded to 3 decimals = 145.421

✓ Positive definite (det > 0 is expected for valid covariance)
```

## 🔧 Methods

### Create Calculator
```python
calc = PooledSampleCovariance()
```

### Add Data
```python
calc.add_group(name, data_array)              # From NumPy array
calc.add_group_from_file(name, filepath)      # From TSV file
```

### Calculate
```python
pooled_cov, info, denom, total_n = calc.calculate_pooled_covariance()
det = calc.calculate_determinant()
```

### Display Results
```python
calc.print_summary()              # Full summary with all details
calc.print_step_by_step()         # Detailed step-by-step calculation
```

## ✅ Result from Your Data

Using Exam2026Data4a, 4b, 4c:
- **Number of Groups**: 3
- **Total Sample Size**: 925
- **Variables**: 2
- **Determinant**: **145.421**

## 📝 Notes

- All groups must have the **same number of variables (columns)**
- Each group needs at least 2 observations
- The pooled matrix is used in discriminant analysis and MANOVA
- Positive determinant indicates the matrix is positive definite (good!)
- Zero determinant indicates singular matrix (data may be collinear)
