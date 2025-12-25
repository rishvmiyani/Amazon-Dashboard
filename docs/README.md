![Python](https://img.shields.io/badge/Python-3.12-blue.svg)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Cleaning%20%26%20Analysis-purple.svg)
![Matplotlib](https://img.shields.io/badge/Matplotlib-Visualization-orange.svg)
![Seaborn](https://img.shields.io/badge/Seaborn-Statistical%20Visualization-lightblue.svg)
![Data Analytics](https://img.shields.io/badge/Data%20Analytics-End--to--End%20Project-success.svg)
![Dataset Size](https://img.shields.io/badge/Dataset-120k%2B%20Rows-informational.svg)
![Business Insights](https://img.shields.io/badge/Business%20Insights-Actionable%20Recommendations-yellow.svg)
![Internship Project](https://img.shields.io/badge/Internship-Data%20Analyst%20Project-brightgreen.svg)
![Power BI Ready](https://img.shields.io/badge/Dashboard-Power%20BI%20%2F%20Tableau%20Ready-blueviolet.svg)
![MIT License](https://img.shields.io/badge/License-MIT-green.svg)
![Repo Size](https://img.shields.io/github/repo-size/rishvmiyani/Amazon-Dashboard)
![Last Commit](https://img.shields.io/github/last-commit/rishvmiyani/Amazon-Dashboard)

# Amazon Sales Analysis – Data Analytics Internship Project (Project ID: 78G0OL)

## 📌 Project Overview
This project analyzes Amazon India sales data to generate actionable business insights for sales optimization, inventory planning, and customer experience improvement. The analysis covers overall sales performance, product and size preferences, fulfillment methods (Amazon vs Merchant), and geographical distribution of orders across Indian states.

The project was completed as part of a Data Analyst internship task to:  
> “Analyze and provide insights on Amazon Sales Report and deliver a comprehensive report with visualizations and recommendations.”

---

## 🧾 Objectives

1. **Sales Overview** – Understand total revenue, order volume, average order value, and returns.  
   → [`data/processed/state_sales.csv`](data/processed/state_sales.csv)

2. **Product Analysis** – Identify top-performing categories and sizes to guide inventory decisions.  
   → [`data/processed/product_sales.csv`](data/processed/product_sales.csv)

3. **Fulfillment Analysis** – Compare Amazon-fulfilled vs Merchant-fulfilled orders and their contribution to sales.  
   → [`data/processed/fulfillment_analysis.csv`](data/processed/fulfillment_analysis.csv)

4. **Customer / Geography Analysis** – Study state-wise sales distribution to identify key markets and growth regions.

5. **Business Insights & Recommendations** – Provide clear, actionable suggestions to improve sales, reduce returns, and optimize operations.

---

## 📈 Dashboard Features
| Feature | Description |
|----------|-------------|
| **Sales Overview** | Displays total sales, profit, and quantity sold. |
| **Category Analysis** | Compares sales performance across product categories. |
| **Regional Insights** | Shows top-performing states and cities. |
| **Customer Segment Analysis** | Visualizes how different customer segments contribute to total revenue. |
| **Order Trends** | Tracks monthly and yearly sales performance. |
| **Profitability Metrics** | Highlights top 10 profitable products and least-performing items. |

---
## 🖼️ Dashboard Preview

### 🔹 Sales Overview Dashboard
<img width="1148" height="635" alt="Screenshot 211831" src="https://github.com/rishvmiyani/Amazon-Dashboard/blob/main/reports/figures/fulfillment_analysis.png" />


### 🔹 Product & Category Insights
<img width="1166" height="641" alt="Screenshot 211853" src="https://github.com/rishvmiyani/Amazon-Dashboard/blob/main/reports/figures/product_sales.png" />


### 🔹 Regional Analysis
<img width="1171" height="652" alt="Screenshot 211907" src="https://github.com/rishvmiyani/Amazon-Dashboard/blob/main/reports/figures/state_sales.png" />

---
## 📂 Repository Structure

Amazon-Dashboard/
├── data/
│ ├── raw/
│ │ └── Amazon-Sale-Report.csv
│ └── processed/
│ ├── cleaned_sales.csv
│ ├── product_sales.csv
│ ├── fulfillment_analysis.csv
│ └── state_sales.csv
├── notebooks/
├── scripts/
│ ├── clean_data.py
│ ├── analysis.py
│ └── visualize.py
├── reports/
│ ├── figures/
│ │ ├── product_sales.png
│ │ ├── fulfillment_analysis.png
│ │ └── state_sales.jpg
│ ├── project_report.md
│ └── Amazon_Sales_Analysis_Complete.pdf
├── docs/
│ └── README.md
├── environment.yml
└── LICENSE

---

## 🧮 Data Source & Description

- **File:** [`data/raw/Amazon-Sale-Report.csv`](data/raw/Amazon-Sale-Report.csv)
- **Rows:** 121,176 orders (after cleaning)

### Key Fields
- Order ID, Date, Status  
- Fulfilment (Amazon / Merchant)  
- Sales Channel, ship-service-level  
- Category (T-shirt, Shirt, Blazer, Perfume, Wallet, etc.)  
- Size (XS–6XL, Free)  
- Quantity, Amount, Currency  
- Shipping city, state, postal code, country  

Pre-processing includes handling missing values, filtering invalid records, and deriving metrics such as return rate and state-wise totals.

---

## ⚙️ Tech Stack

- **Power BI** – Dashboard creation and data visualization  
- **Microsoft Excel / CSV** – Dataset management  
- **Data Cleaning** – Power Query  
- **DAX (Data Analysis Expressions)** – Custom calculations and measures
- **Language:** Python 3.12
- **Libraries:**
  - pandas – data cleaning & aggregation
  - matplotlib, seaborn – visualizations
  - jupyter – exploratory analysis
- **Environment:** Managed via `environment.yml`

---


📊 Key Results (Summary)

-Total Sales: ~₹7.86 Crore
-Total Orders: 121,176
-Average Order Value: ~₹648.56
-Return Rate: 15.8%
-Top Categories: Blazer, Perfume, Shirt
-Top Sizes: XXL, XL, Free
-Fulfillment Split: Amazon – 69.1%, Merchant – 30.9%
-Top States: Maharashtra, Karnataka, Telangana, Uttar Pradesh, Tamil Nadu

---

## 💡 Key Insights
- Identified top-selling categories driving the majority of revenue.  
- Highlighted seasonal trends affecting order volumes.  
- Detected low-performing regions needing marketing focus.  
- Visualized customer segmentation to target specific demographics.

---

## 🚀 How to Use
1. Download the repository or clone it:
   ```bash
   git clone https://github.com/rishvmiyani/Amazon-Dashboard.git

---

💡 Business Insights

High revenue concentration in fashion categories and larger sizes indicates inventory prioritization opportunities.
Elevated return rate suggests sizing or expectation mismatch; improving size charts and descriptions can reduce returns.
Amazon-fulfilled orders dominate, reflecting customer trust in logistics.
Sales are concentrated in a few states, while several regions show untapped growth potential.

---

🚀 Future Enhancements

Build an interactive dashboard using Power BI, Tableau, or Streamlit.

Add customer-level analysis (CLV, RFM) if customer IDs are available.

Automate the pipeline using Airflow or Cron.

Add unit tests and CI/CD using GitHub Actions.


---

## 👤 Author

- **Name:** Rishv (Data Analyst Intern)  
- **Role:** Data cleaning, analysis, visualization, documentation, and reporting.  

---

## 📄 License

This project is licensed under the **MIT License** – see the [LICENSE](../LICENSE) file for details.
