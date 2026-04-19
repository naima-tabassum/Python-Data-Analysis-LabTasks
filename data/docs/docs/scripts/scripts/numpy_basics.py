"""
=============================================================
 numpy_basics.py — NumPy Fundamentals
 Part of: Python-Data-Analysis-LabTasks
=============================================================
 Topics Covered:
   - Array Creation (1D, 2D)
   - Array Properties (shape, ndim, dtype)
   - Range Arrays (arange, linspace, full)
   - Random Arrays
   - Reshape
   - Array Slicing
   - Axis Operations (axis=0 vs axis=1)
=============================================================
"""

import numpy as np

# ─────────────────────────────────────────────
# SECTION 1: ARRAY CREATION
# ─────────────────────────────────────────────
print("=" * 55)
print("SECTION 1: ARRAY CREATION")
print("=" * 55)

# 1D Array — like a flat list of numbers
a = np.array([1, 2, 3, 4])
print(f"\n[1D Array] a = {a}")

# The power of NumPy: math applies to ALL elements instantly!
print(f"  a * 2  = {a * 2}")   # [2 4 6 8]
print(f"  a + 10 = {a + 10}")  # [11 12 13 14]
print(f"  a ** 2 = {a ** 2}")  # [1 4 9 16]

# 2D Array — like a table (rows × columns)
b = np.array([
    [1, 2],   # Row 0
    [3, 4],   # Row 1
    [5, 6]    # Row 2
])
print(f"\n[2D Array] b =")
print(b)

# All-zeros array
c = np.zeros([3, 4])  # 3 rows, 4 columns
print(f"\n[np.zeros([3,4])]")
print(c)

# All-ones array
ones = np.ones([3, 4])
print(f"\n[np.ones([3,4])]")
print(ones)

# All-nines (multiply ones by any number)
nines = np.ones([3, 4]) * 9
print(f"\n[np.ones([3,4]) * 9]")
print(nines)

# Fill with a specific value directly
sevens = np.full((3, 3), 7)
print(f"\n[np.full((3,3), 7)]")
print(sevens)

# Random array (values from normal distribution: mean=0, std=1)
np.random.seed(42)  # Seed for reproducibility — same result every run
X = np.random.randn(4, 3)
print(f"\n[np.random.randn(4,3)] Random 4×3 array:")
print(X.round(3))


# ─────────────────────────────────────────────
# SECTION 2: ARRAY PROPERTIES
# ─────────────────────────────────────────────
print("\n" + "=" * 55)
print("SECTION 2: ARRAY PROPERTIES")
print("=" * 55)

print(f"\n  a.shape = {a.shape}")   # (4,)   — 1D with 4 elements
print(f"  b.shape = {b.shape}")   # (3, 2) — 3 rows, 2 columns
print(f"  c.shape = {c.shape}")   # (3, 4) — 3 rows, 4 columns

print(f"\n  a.ndim  = {a.ndim}")   # 1 — one dimension
print(f"  b.ndim  = {b.ndim}")   # 2 — two dimensions
print(f"  c.ndim  = {c.ndim}")   # 2 — two dimensions

print(f"\n  a.dtype = {a.dtype}")  # int64  — integers
print(f"  c.dtype = {c.dtype}")  # float64 — decimals (zeros are floats)


# ─────────────────────────────────────────────
# SECTION 3: RANGE & SPECIAL ARRAYS
# ─────────────────────────────────────────────
print("\n" + "=" * 55)
print("SECTION 3: RANGE & SPECIAL ARRAYS")
print("=" * 55)

# np.arange(start, stop, step) — stop is EXCLUSIVE
print("\n[np.arange(start, stop, step)]")
print(f"  arange(0, 10, 3) = {np.arange(0, 10, 3)}")   # [0 3 6 9]
print(f"  arange(5)        = {np.arange(5)}")           # [0 1 2 3 4]
print(f"  arange(1, 11)    = {np.arange(1, 11)}")       # [1 2 3...10]

# np.linspace(start, stop, num) — stop is INCLUSIVE
print("\n[np.linspace(start, stop, num)]")
print(f"  linspace(1, 10, 6) = {np.linspace(1, 10, 6)}")
# [1.0, 2.8, 4.6, 6.4, 8.2, 10.0] — 6 evenly spaced values


# ─────────────────────────────────────────────
# SECTION 4: RESHAPE
# ─────────────────────────────────────────────
print("\n" + "=" * 55)
print("SECTION 4: RESHAPE")
print("=" * 55)

# reshape() — rearrange elements into a new shape
# Total elements must remain the same!
arr_12 = np.arange(1, 13)
print(f"\nOriginal (12 elements): {arr_12}")

reshaped_3x4 = arr_12.reshape(3, 4)
print("\nReshaped to (3, 4):")
print(reshaped_3x4)

reshaped_4x3 = arr_12.reshape(4, 3)
print("\nReshaped to (4, 3):")
print(reshaped_4x3)

reshaped_2x6 = arr_12.reshape(2, 6)
print("\nReshaped to (2, 6):")
print(reshaped_2x6)


# ─────────────────────────────────────────────
# SECTION 5: ARRAY SLICING
# ─────────────────────────────────────────────
print("\n" + "=" * 55)
print("SECTION 5: ARRAY SLICING")
print("=" * 55)
print("Syntax: array[row_start:row_end, col_start:col_end]")
print("         End index is EXCLUSIVE (not included)")

x = np.array([
    [1,  2,  3,  55, 56, 57],   # Row 0
    [4,  5,  6,  66, 67, 68],   # Row 1
    [7,  8,  9,  99, 96, 97],   # Row 2
    [33, 44, 50, 23, 45, 23]    # Row 3
])

print("\nFull array:")
print(x)

# Select specific rows and columns
print("\nx[1:3, 1:3] → rows 1,2 and columns 1,2:")
print(x[1:3, 1:3])
#   Row 1, Col 1 = 5  |  Row 1, Col 2 = 6
#   Row 2, Col 1 = 8  |  Row 2, Col 2 = 9

print("\nx[0, :]    → first row, all columns:")
print(x[0, :])

print("\nx[:, 0]    → all rows, first column:")
print(x[:, 0])

print("\nx[-1, :]   → last row (using negative index):")
print(x[-1, :])

print("\nx[2:, 4:]  → last 2 rows, last 2 columns (bottom-right corner):")
print(x[2:, 4:])


# ─────────────────────────────────────────────
# SECTION 6: AXIS OPERATIONS
# ─────────────────────────────────────────────
print("\n" + "=" * 55)
print("SECTION 6: AXIS OPERATIONS")
print("=" * 55)
print("""
  axis=0 → Operate DOWN each column  (collapse rows)    → 1 result per COLUMN
  axis=1 → Operate ACROSS each row   (collapse columns) → 1 result per ROW
  
  In data science terms:
    rows    = samples (observations)
    columns = features (variables)
""")

X = np.array([
    [10, 20, 30],   # Sample 1
    [40, 50, 60],   # Sample 2
    [70, 80, 90],   # Sample 3
    [10, 30, 50],   # Sample 4
])
print(f"X shape: {X.shape}  (4 samples × 3 features)\n")
print(X)

# axis=0: column-wise — average of each feature
col_mean = X.mean(axis=0)
print(f"\n[axis=0] Mean of each COLUMN (feature average): {col_mean}")
print("   → 1 result per column: 3 values total")

# axis=1: row-wise — sum of each sample
row_sum = X.sum(axis=1)
print(f"\n[axis=1] Sum of each ROW (sample total): {row_sum}")
print("   → 1 result per row: 4 values total")

# No axis: global operation
print(f"\n[No axis] Global sum:  {X.sum()}")
print(f"[No axis] Global mean: {X.mean():.2f}")
print(f"[No axis] Global max:  {X.max()}")
print(f"[No axis] Global min:  {X.min()}")

print("\n✅ All NumPy examples completed!")
