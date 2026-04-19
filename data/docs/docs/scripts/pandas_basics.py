"""
=============================================================
 pandas_basics.py — Pandas Fundamentals
 Part of: Python-Data-Analysis-LabTasks
=============================================================
 Topics Covered:
   - Data Loading
   - Data Viewing
   - Data Selection (loc, iloc)
   - Data Summary
   - Missing Values
   - Index Operations
   - Value Functions & Boolean Filtering
=============================================================
"""

import pandas as pd
import numpy as np

# ─────────────────────────────────────────────
# SECTION 1: DATA LOADING
# ─────────────────────────────────────────────
print("=" * 55)
print("SECTION 1: DATA LOADING")
print("=" * 55)

# Load from a CSV file
df = pd.read_csv('../data/weather_sample.csv')
print("✅ CSV loaded successfully!")
print(f"   Shape: {df.shape[0]} rows × {df.shape[1]} columns\n")

# Create a DataFrame from a dictionary (no CSV needed)
weather_data = {
    'Day':         ['Mon',  'Tue', 'Wed', 'Thu', 'Fri'],
    'Temperature': [32,     28,   35,    36,    45],
    'Humidity':    [72,     54,   74,    61,    58],
    'Events':      ['Snow', None, None,  None, 'Rain']
}
sample_df = pd.DataFrame(weather_data)
print("Sample DataFrame created from dictionary:")
print(sample_df)


# ─────────────────────────────────────────────
# SECTION 2: DATA VIEWING
# ─────────────────────────────────────────────
print("\n" + "=" * 55)
print("SECTION 2: DATA VIEWING")
print("=" * 55)

# head() — First 5 rows
print("\n[head()] First 5 rows:")
print(df.head())

# tail() — Last 5 rows
print("\n[tail()] Last 5 rows:")
print(df.tail())

# columns — All column names
print("\n[columns] Column names:")
print(df.columns.tolist())

# index — Row labels
print("\n[index] Row index:")
print(df.index)

# shape — (rows, columns)
print(f"\n[shape] {df.shape[0]} rows × {df.shape[1]} columns")

# Select specific columns (use double brackets for multiple)
print("\n[Column Selection] Temperature, DewPoint, Humidity:")
print(df[['Temperature', 'DewPoint', 'Humidity']].head())


# ─────────────────────────────────────────────
# SECTION 3: DATA SELECTION — loc & iloc
# ─────────────────────────────────────────────
print("\n" + "=" * 55)
print("SECTION 3: DATA SELECTION")
print("=" * 55)

# loc — select by INDEX LABEL (INCLUSIVE both ends)
print("\n[loc[1:4]] Rows labeled 1 to 4 (inclusive):")
print(df.loc[1:4])

# iloc — select by POSITION NUMBER (EXCLUSIVE at end)
print("\n[iloc[1:5, 2:]] Rows 1-4, columns from index 2 onwards:")
print(df.iloc[1:5, 2:])


# ─────────────────────────────────────────────
# SECTION 4: DATA SUMMARY
# ─────────────────────────────────────────────
print("\n" + "=" * 55)
print("SECTION 4: DATA SUMMARY")
print("=" * 55)

# describe() — statistical summary of numeric columns
print("\n[describe()] Numeric summary:")
print(df.describe())

# describe(include='O') — summary of text/object columns
print("\n[describe(include='O')] Text column summary:")
print(df.describe(include='O'))

# unique() — all unique values in a column
print("\n[unique()] Unique weather events:")
print(df['Events'].unique())


# ─────────────────────────────────────────────
# SECTION 5: MISSING VALUES
# ─────────────────────────────────────────────
print("\n" + "=" * 55)
print("SECTION 5: MISSING VALUES")
print("=" * 55)

# isnull().sum() — count NaN per column
print("\n[isnull().sum()] Missing value count:")
print(df.isnull().sum())

total = df.isnull().sum().sum()
print(f"\nTotal missing cells: {total}")

# fillna() — fill NaN with a value (does NOT modify original without inplace=True)
df_filled = df.fillna(0)
print("\n[fillna(0)] After filling NaN with 0:")
print(df_filled.isnull().sum().sum(), "missing values remaining")

# replace() — replace a specific value with another
df_replaced = df.replace(0, np.nan)
print("\n[replace(0, np.nan)] Replaced all 0s with NaN")

# interpolate() — estimate missing values from neighbors
df_interp = df[['Temperature', 'DewPoint']].interpolate()
print("\n[interpolate()] After interpolation:")
print(df_interp.isnull().sum())


# ─────────────────────────────────────────────
# SECTION 6: INDEX OPERATIONS
# ─────────────────────────────────────────────
print("\n" + "=" * 55)
print("SECTION 6: INDEX OPERATIONS")
print("=" * 55)

# set_index() — use a column as the row index
df_indexed = df.set_index('EST')
print("\n[set_index('EST')] First 3 rows with date as index:")
print(df_indexed.head(3))

# Now select by date label using loc
print("\n[loc with date index] Rows from 1/1 to 1/3:")
print(df_indexed.loc['1/1/2017':'1/3/2017'])

# reset_index() — move index back into a column
df_reset = df_indexed.reset_index()
print("\n[reset_index()] Index is back to 0,1,2,3...:")
print(df_reset.head(3))


# ─────────────────────────────────────────────
# SECTION 7: VALUE FUNCTIONS & FILTERING
# ─────────────────────────────────────────────
print("\n" + "=" * 55)
print("SECTION 7: VALUE FUNCTIONS & BOOLEAN FILTERING")
print("=" * 55)

# Statistical value functions
print("\n[Value Functions] Temperature column:")
print(f"  Max:  {df['Temperature'].max()}")
print(f"  Min:  {df['Temperature'].min()}")
print(f"  Mean: {df['Temperature'].mean():.2f}")
print(f"  Std:  {df['Temperature'].std():.2f}")
print(f"  Sum:  {df['Temperature'].sum()}")

# Boolean filtering
print("\n[Boolean Filter] Rows where Temperature > 30:")
hot_days = df[df['Temperature'] > 30]
print(hot_days[['EST', 'Temperature']].head())

# Filter with multiple columns
print("\n[Multi-column Filter] EST, Temp, Visibility where Temp > 30:")
print(df[['EST', 'Temperature', 'VisibilityMiles']][df['Temperature'] > 30].head())

# Filter by text value
print("\n[Text Filter] Rainy days:")
rain_df = df[df['Events'] == 'Rain']
print(rain_df[['EST', 'Temperature', 'VisibilityMiles']])

print("\n✅ All Pandas examples completed!")
