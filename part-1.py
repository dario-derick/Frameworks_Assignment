import pandas as pd

# Load the CSV
try:
    df = pd.read_csv('metadata.csv')
except FileNotFoundError:
    print("File not found. Make sure metadata.csv is in your working directory.")
    exit()

# Examine first few rows
print(df.head())

# DataFrame dimensions
print("Shape:", df.shape)

# Column data types
print(df.dtypes)

# Check missing values
print(df.isnull().sum())

# Basic statistics for numerical columns
print(df.describe())
