import pandas as pd
from pathlib import Path

# Base directory (Amazon-Dashboard)
BASE_DIR = Path(__file__).resolve().parent.parent

# Paths
RAW_DATA = BASE_DIR / "data" / "raw" / "Amazon-Sale-Report.csv"
PROCESSED_DATA = BASE_DIR / "data" / "processed" / "cleaned_sales.csv"

# Load raw data
df = pd.read_csv(RAW_DATA)

# Clean data
df.dropna(subset=["Amount", "Category"], inplace=True)

# Save cleaned data
df.to_csv(PROCESSED_DATA, index=False)

print("Data cleaned and saved successfully.")
