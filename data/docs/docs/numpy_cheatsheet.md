# 🔢 NumPy Quick Reference Cheatsheet

> A one-page reference for the most important NumPy functions.

---

## 📥 Import

```python
import numpy as np
```

---

## 🧱 Array Creation

```python
np.array([1, 2, 3])           # 1D array from list
np.array([[1,2],[3,4]])        # 2D array (matrix)
np.zeros([3, 4])               # 3×4 array of zeros
np.ones([3, 4])                # 3×4 array of ones
np.ones([3, 4]) * 9            # 3×4 array of nines
np.full((3, 3), 7)             # 3×3 array of sevens
np.eye(3)                      # 3×3 identity matrix
np.empty((2, 3))               # Uninitialized array (random junk)
```

---

## 🔢 Range Arrays

```python
np.arange(5)             # [0, 1, 2, 3, 4]        — stop EXCLUSIVE
np.arange(1, 11)         # [1, 2, 3, ..., 10]
np.arange(0, 10, 3)      # [0, 3, 6, 9]            — step=3
np.linspace(1, 10, 6)    # 6 values from 1 to 10   — stop INCLUSIVE
```

---

## 🎲 Random Arrays

```python
np.random.seed(42)           # Set seed for reproducibility
np.random.randn(3, 4)        # 3×4, random (normal dist, mean=0)
np.random.rand(3, 4)         # 3×4, random (uniform 0 to 1)
np.random.randint(0, 10, (3, 4))  # 3×4, random integers 0-9
```

---

## 📐 Array Properties

| Property | Meaning | Example output |
|----------|---------|---------------|
| `a.shape` | Dimensions as tuple | `(3, 4)` |
| `a.ndim` | Number of dimensions | `2` |
| `a.dtype` | Data type of elements | `float64` |
| `a.size` | Total number of elements | `12` |

```python
a = np.zeros([3, 4])
print(a.shape)   # (3, 4) — 3 rows, 4 columns
print(a.ndim)    # 2 — 2D array
print(a.dtype)   # float64
print(a.size)    # 12 — total elements
```

---

## ✂️ Slicing

```python
# 1D
a = np.array([10, 20, 30, 40, 50])
a[0]       # 10       — first element
a[-1]      # 50       — last element
a[1:4]     # [20,30,40] — index 1,2,3 (exclusive at 4)
a[:3]      # [10,20,30] — first 3
a[::2]     # [10,30,50] — every 2nd element

# 2D — array[row, column]
x = np.arange(1, 13).reshape(3, 4)
x[0, :]    # First row, all columns
x[:, 0]    # All rows, first column
x[1:3, 1:3]  # Rows 1-2, columns 1-2 (exclusive)
x[-1, -1]    # Last row, last column
```

---

## 🔄 Reshape

```python
a = np.arange(1, 13)       # [1, 2, 3, ..., 12]
a.reshape(3, 4)             # 3 rows × 4 columns
a.reshape(4, 3)             # 4 rows × 3 columns
a.reshape(2, 6)             # 2 rows × 6 columns
a.reshape(-1, 4)            # Auto rows, 4 columns (-1 = let NumPy figure it out)
a.flatten()                 # Any shape → 1D array
```

---

## ➕ Math Operations

```python
# Element-wise (same shape arrays)
a + b        # Add
a - b        # Subtract
a * b        # Multiply
a / b        # Divide
a ** 2       # Square every element
np.sqrt(a)   # Square root of every element

# Scalar operations
a + 5        # Add 5 to every element
a * 3        # Multiply every element by 3
```

---

## 📊 Aggregation (axis)

```python
# axis=0 → column-wise → 1 result per COLUMN
X.mean(axis=0)    # Average of each column
X.sum(axis=0)     # Sum of each column

# axis=1 → row-wise → 1 result per ROW
X.sum(axis=1)     # Sum of each row
X.mean(axis=1)    # Average of each row

# No axis → global (entire array)
X.sum()           # Grand total
X.max()           # Global maximum
X.min()           # Global minimum
X.mean()          # Global average
```

---

## 🎨 Visual Guide: axis=0 vs axis=1

```
Array shape: (4 rows × 3 columns)

       Col0  Col1  Col2
Row0 [ 10    20    30 ]  ──→ axis=1 (across each row)
Row1 [ 40    50    60 ]  ──→ axis=1
Row2 [ 70    80    90 ]  ──→ axis=1
Row3 [ 10    30    50 ]  ──→ axis=1
      ↓     ↓     ↓
    axis=0  axis=0  axis=0   (down each column)

X.mean(axis=0) → [32.5, 45.0, 57.5]  ← 3 values (one per column)
X.sum(axis=1)  → [60, 150, 240, 90]  ← 4 values (one per row)
```

---

## ⚠️ Common Mistakes

| Mistake | Fix |
|---------|-----|
| `np.zeros(3, 4)` → Error | Use `np.zeros((3, 4))` or `np.zeros([3, 4])` |
| Confusing `axis=0` and `axis=1` | axis=0 = down columns; axis=1 = across rows |
| Reshape fails | Check total elements: `old_shape product == new_shape product` |
| `a.shape()` → Error | `shape` is a property, not a function: `a.shape` |

---

## 💡 Tips

- Use `np.random.seed(42)` to make random results reproducible
- `reshape(-1, n)` lets NumPy calculate the number of rows automatically
- NumPy arrays must contain **one data type** — mixing causes automatic conversion
- **Vectorized operations** (no loops!) are what make NumPy fast — always prefer them over Python loops
