# 🐼 Pandas Quick Reference Cheatsheet

> A one-page reference for the most important Pandas functions.

---

## 📥 Loading Data

```python
import pandas as pd

df = pd.read_csv('file.csv')           # Load from CSV
df = pd.read_excel('file.xlsx')        # Load from Excel
df = pd.DataFrame({'col': [1, 2, 3]}) # Create from dictionary
```

---

## 👀 Viewing Data

| Code | What it does |
|------|--------------|
| `df.head()` | First 5 rows |
| `df.head(n)` | First n rows |
| `df.tail()` | Last 5 rows |
| `df.columns` | All column names |
| `df.index` | Row labels |
| `df.shape` | (rows, columns) tuple |
| `df.info()` | Data types + non-null counts |
| `df.dtypes` | Data type of each column |

---

## 🎯 Selecting Data

```python
df['col']                    # One column → Series
df[['col1', 'col2']]         # Multiple columns → DataFrame
df.loc[1:4]                  # Rows by label (INCLUSIVE)
df.loc['a':'d', 'col']       # Row label range + column name
df.iloc[0:5, 0:3]            # By position (EXCLUSIVE at end)
df.iloc[0]                   # First row
df.iloc[:, 0]                # First column (all rows)
```

---

## 📊 Summarizing Data

```python
df.describe()                # Stats for numeric columns
df.describe(include='O')     # Stats for text columns
df['col'].unique()           # All unique values
df['col'].value_counts()     # Count of each unique value
df['col'].nunique()          # Number of unique values
```

---

## 🔍 Filtering Rows (Boolean Masking)

```python
df[df['col'] > 30]                     # Simple condition
df[df['col'] == 'Rain']                # Text match
df[(df['A'] > 10) & (df['B'] < 50)]   # AND condition
df[(df['A'] > 10) | (df['B'] < 50)]   # OR condition
df[df['col'].isin(['Rain', 'Snow'])]   # Multiple values
```

---

## 🔧 Missing Values (NaN)

```python
df.isnull()                  # True/False table
df.isnull().sum()            # Count NaN per column
df.isnull().sum().sum()      # Total NaN count

df.fillna(0)                 # Replace NaN with 0 (new df)
df.fillna(0, inplace=True)   # Replace NaN — modifies ORIGINAL
df.fillna(df.mean())         # Fill with column means
df.dropna()                  # Remove rows with any NaN
df.dropna(subset=['col'])    # Remove rows where 'col' is NaN
df.interpolate()             # Estimate NaN from neighbors
df.replace(0, np.nan)        # Replace specific value with NaN
```

---

## 📐 Index Operations

```python
df.set_index('col')           # Use a column as row index
df.reset_index()              # Move index back to a column
df.set_index('col', inplace=True)   # Modify original
```

---

## 📈 Value / Aggregation Functions

```python
df['col'].max()       # Maximum value
df['col'].min()       # Minimum value
df['col'].mean()      # Average
df['col'].median()    # Median
df['col'].std()       # Standard deviation
df['col'].sum()       # Sum
df['col'].count()     # Non-null count
df['col'].cumsum()    # Running total
```

---

## 🔠 Column Operations

```python
df.rename(columns={'old': 'new'})    # Rename specific columns
df.columns = ['a', 'b', 'c']         # Replace ALL column names
df.drop('col', axis=1)               # Remove a column
df.drop(['c1', 'c2'], axis=1)        # Remove multiple columns
df['new'] = df['a'] + df['b']        # Create new column
```

---

## ⚠️ Common Mistakes

| Mistake | Why it's wrong | Fix |
|---------|---------------|-----|
| `df.fillna(0)` and expecting original to change | Returns new df | Use `inplace=True` or reassign |
| `df.shape()` | shape is a **property**, not a function | Use `df.shape` |
| `df['col1', 'col2']` | Single bracket for multiple columns | Use `df[['col1', 'col2']]` |
| `df.loc[0:5]` vs `df.iloc[0:5]` | `loc` is INCLUSIVE at end, `iloc` is EXCLUSIVE | Know which one you need |

---

## 💡 Tips

- **Always** explore your data with `df.info()` and `df.describe()` first
- **Check missing values** with `df.isnull().sum()` before any analysis
- **Use `.copy()`** when you want to modify data without affecting the original: `df2 = df.copy()`
- **`loc` = labels, `iloc` = integers** — remember by the 'i' in iloc = integer
