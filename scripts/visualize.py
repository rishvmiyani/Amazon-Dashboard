import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# Base directory
BASE_DIR = Path(__file__).resolve().parent.parent

# Input paths
PRODUCT_SALES = BASE_DIR / "data" / "processed" / "product_sales.csv"
FULFILLMENT = BASE_DIR / "data" / "processed" / "fulfillment_analysis.csv"
STATE_SALES = BASE_DIR / "data" / "processed" / "state_sales.csv"

# Output directory
FIGURES_DIR = BASE_DIR / "reports" / "figures"
FIGURES_DIR.mkdir(parents=True, exist_ok=True)

# Load data
product_sales = pd.read_csv(PRODUCT_SALES)
fulfillment_analysis = pd.read_csv(FULFILLMENT)
state_sales = pd.read_csv(STATE_SALES)

# -----------------------------
# Product sales bar chart
# -----------------------------
plt.figure(figsize=(10, 6))
for size in product_sales["Size"].unique():
    subset = product_sales[product_sales["Size"] == size]
    plt.bar(subset["Category"], subset["Amount"], label=size)

plt.title("Sales by Category and Size")
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()
plt.savefig(FIGURES_DIR / "product_sales.png")
plt.close()

# -----------------------------
# Fulfillment pie chart
# -----------------------------
plt.figure(figsize=(8, 8))
plt.pie(
    fulfillment_analysis["sum"],
    labels=fulfillment_analysis["Fulfilment"],
    autopct="%1.1f%%"
)
plt.title("Sales by Fulfillment Method")
plt.savefig(FIGURES_DIR / "fulfillment_analysis.png")
plt.close()

# -----------------------------
# State sales bar chart
# -----------------------------
plt.figure(figsize=(12, 6))
plt.bar(state_sales["ship-state"], state_sales["Amount"])
plt.title("Sales by State")
plt.xticks(rotation=90)
plt.tight_layout()
plt.savefig(FIGURES_DIR / "state_sales.png")
plt.close()

print("Visualizations saved successfully.")
