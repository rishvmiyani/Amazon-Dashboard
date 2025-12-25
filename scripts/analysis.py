import pandas as pd
from pathlib import Path

# Base directory (Amazon-Dashboard)
BASE_DIR = Path(__file__).resolve().parent.parent

# Paths
CLEANED_DATA = BASE_DIR / "data" / "processed" / "cleaned_sales.csv"
PRODUCT_SALES_PATH = BASE_DIR / "data" / "processed" / "product_sales.csv"
FULFILLMENT_PATH = BASE_DIR / "data" / "processed" / "fulfillment_analysis.csv"
STATE_SALES_PATH = BASE_DIR / "data" / "processed" / "state_sales.csv"

# Load cleaned data
df = pd.read_csv(CLEANED_DATA)

# Sales overview
total_sales = df["Amount"].sum()
total_orders = df.shape[0]
avg_order_value = df["Amount"].mean()

print(f"Total Sales: {total_sales}")
print(f"Total Orders: {total_orders}")
print(f"Average Order Value: {avg_order_value}")

# Product analysis
product_sales = (
    df.groupby(["Category", "Size"])["Amount"]
    .sum()
    .reset_index()
)
product_sales.to_csv(PRODUCT_SALES_PATH, index=False)

# Fulfillment analysis
fulfillment_analysis = (
    df.groupby("Fulfilment")["Amount"]
    .agg(["sum", "count"])
    .reset_index()
)
fulfillment_analysis.to_csv(FULFILLMENT_PATH, index=False)

# Geographical analysis
state_sales = (
    df.groupby("ship-state")["Amount"]
    .sum()
    .sort_values(ascending=False)
    .reset_index()
)
state_sales.to_csv(STATE_SALES_PATH, index=False)

print("Analysis completed and saved successfully.")
