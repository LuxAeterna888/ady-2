import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

DATA_PATH = "C:/Users/minh6/Học/Kỳ 4/ADY201m/cardio_train.csv"

if not Path(DATA_PATH).exists():
    raise FileNotFoundError(
        "File not found"
    )

df_raw = pd.read_csv(DATA_PATH, sep=';')

# Fallback in case a copied version uses commas.
if df_raw.shape[1] == 1:
    df_raw = pd.read_csv(DATA_PATH)

# Standardize column names
df_raw.columns = df_raw.columns.str.strip().str.lower()

print(f"Raw dataset shape: {df_raw.shape[0]:,} rows, {df_raw.shape[1]} columns")
print("\nColumns:")
print(df_raw.columns.tolist())

print("\nFirst 5 rows:")


print("\nLast 5 rows:")


print("\nDataset information:")
df_raw.info()

print("\nBasic statistics:")
