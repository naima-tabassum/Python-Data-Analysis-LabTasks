# 🐍 Python Data Analysis — Lab Tasks

> **A beginner-friendly, hands-on guide to Pandas & NumPy — the two most important Python libraries for Data Analysis.**

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python)](https://www.python.org/)
[![Pandas](https://img.shields.io/badge/Pandas-2.x-green?logo=pandas)](https://pandas.pydata.org/)
[![NumPy](https://img.shields.io/badge/NumPy-1.x-orange?logo=numpy)](https://numpy.org/)
[![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-orange?logo=jupyter)](https://jupyter.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

---

## 📌 About This Repository

This repository is a **structured learning resource** built from weekly lab task notes. It is designed for **absolute beginners** who want to learn data analysis using Python.

Whether you are a university student, a self-learner, or someone switching to data science — this repo will help you understand **Pandas** and **NumPy** step by step, with clear explanations and real code examples.

---

## 🎯 What You Will Learn

By the end of this lab series, you will be able to:

- ✅ Load and explore datasets using **Pandas**
- ✅ View, select, and filter data easily
- ✅ Handle **missing values** (NaN) like a professional
- ✅ Summarize and describe data statistically
- ✅ Create and manipulate **NumPy arrays**
- ✅ Perform math operations on arrays efficiently
- ✅ Slice and reshape arrays for data science use cases
- ✅ Understand the difference between **axis=0** and **axis=1**

---

## 📚 Topics Covered

### 🐼 Pandas
| # | Topic | Description |
|---|-------|-------------|
| 1 | Data Loading | Read CSV files, create DataFrames |
| 2 | Data Viewing | `head()`, `tail()`, `shape`, `columns`, `index` |
| 3 | Selection | `loc[]`, `iloc[]`, column selection |
| 4 | Data Summary | `describe()`, `unique()` |
| 5 | Missing Values | `isnull()`, `fillna()`, `replace()`, `interpolate()` |
| 6 | Index Operations | `set_index()`, `reset_index()` |
| 7 | Value Functions | `max()`, `min()`, `mean()`, `std()`, `sum()` |
| 8 | Boolean Filtering | Filter rows based on conditions |

### 🔢 NumPy
| # | Topic | Description |
|---|-------|-------------|
| 1 | Array Creation | `np.array()`, `np.zeros()`, `np.ones()` |
| 2 | Array Properties | `shape`, `ndim`, `dtype` |
| 3 | Range Arrays | `np.arange()`, `np.linspace()`, `np.full()` |
| 4 | Random Arrays | `np.random.randn()` |
| 5 | Reshape | `.reshape()` |
| 6 | Array Slicing | `array[row, col]` indexing |
| 7 | Axis Operations | `axis=0` vs `axis=1` |

---

## 📁 Repository Structure

```
Python-Data-Analysis-LabTasks/
│
├── 📄 README.md                    ← You are here
│
├── 📓 notebooks/
│   └── lab_task_1.ipynb            ← Full Jupyter Notebook with all examples
│
├── 🐍 scripts/
│   ├── pandas_basics.py            ← Clean Python script: Pandas functions
│   └── numpy_basics.py             ← Clean Python script: NumPy functions
│
├── 📊 data/
│   └── weather_sample.csv          ← Sample weather dataset for practice
│
└── 📖 docs/
    ├── pandas_cheatsheet.md        ← Quick reference for Pandas
    └── numpy_cheatsheet.md         ← Quick reference for NumPy
```

---

## 🚀 Getting Started

### Step 1: Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/Python-Data-Analysis-LabTasks.git
cd Python-Data-Analysis-LabTasks
```

### Step 2: Install Required Libraries

```bash
pip install pandas numpy jupyter
```

### Step 3: Launch Jupyter Notebook

```bash
jupyter notebook notebooks/lab_task_1.ipynb
```

Or run the scripts directly:

```bash
python scripts/pandas_basics.py
python scripts/numpy_basics.py
```

---

## 💡 Quick Code Examples

### Load a CSV File with Pandas

```python
import pandas as pd

df = pd.read_csv('data/weather_sample.csv')
df.head()  # Show first 5 rows
```

### Filter Rows Based on a Condition

```python
# Show all rows where Temperature is greater than 30
df[df['Temperature'] > 30]
```

### Create a NumPy Array

```python
import numpy as np

a = np.array([1, 2, 3, 4])
print(a * 2)  # Output: [2 4 6 8]
```

### Reshape an Array

```python
np.arange(1, 13).reshape(3, 4)
# Creates a 3-row, 4-column array from numbers 1 to 12
```

---

## ⚠️ Common Mistakes to Avoid

| Mistake | Fix |
|--------|-----|
| `df.fillna(1)` doesn't change the original | Use `df.fillna(1, inplace=True)` |
| Confusing `loc` and `iloc` | `loc` uses labels, `iloc` uses position numbers |
| Thinking `shape` is a function | It's a property — use `df.shape` not `df.shape()` |
| Forgetting `import numpy as np` | Always import at the top of your file |
| Mixing up `axis=0` and `axis=1` | axis=0 = column-wise, axis=1 = row-wise |

---

## 🏋️ Mini Practice Tasks

Try these yourself after going through the notebook:

1. Load `weather_sample.csv` and print only the first 3 rows.
2. Find the **maximum** and **minimum** temperature.
3. Count how many rows have **missing values**.
4. Fill all missing values with the **mean** of that column.
5. Create a NumPy array of numbers from 1 to 20, then reshape it into a 4×5 matrix.
6. Filter all rows where `Events == 'Rain'` and display only the `Date` and `Temperature` columns.

---

## 🛠️ Requirements

```
python >= 3.8
pandas >= 1.3
numpy >= 1.21
jupyter >= 1.0
```

---

## 📖 Additional Resources

- [Pandas Official Documentation](https://pandas.pydata.org/docs/)
- [NumPy Official Documentation](https://numpy.org/doc/)
- [Jupyter Notebook Guide](https://jupyter-notebook.readthedocs.io/)

---

## 🤝 Contributing

Found a bug or want to add more examples? Feel free to:

1. Fork this repository
2. Create a new branch: `git checkout -b feature/add-new-example`
3. Commit your changes: `git commit -m "Add new example for groupby"`
4. Push and open a Pull Request

---

## 📄 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

---

<div align="center">

**Made with ❤️ for beginner data analysts**

*If this helped you, please give it a ⭐ on GitHub!*

</div>
