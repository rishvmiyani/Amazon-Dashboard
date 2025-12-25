# Amazon Sales Analysis – Data Analytics Internship Project (Project ID: 78G0OL)

## 📌 Project Overview
This project analyzes Amazon India sales data to generate actionable business insights for sales optimization, inventory planning, and customer experience improvement. The analysis covers overall sales performance, product and size preferences, fulfillment methods (Amazon vs Merchant), and geographical distribution of orders across Indian states.

The project was completed as part of a Data Analyst internship task to:  
> “Analyze and provide insights on Amazon Sales Report and deliver a comprehensive report with visualizations and recommendations.”[file:2]

---

## 🧾 Objectives

1. **Sales Overview** – Understand total revenue, order volume, average order value, and returns.[data/processed/state_sales.csv]  
2. **Product Analysis** – Identify top-performing categories and sizes to guide inventory decisions.[data/processed/product_sales.csv]  
3. **Fulfillment Analysis** – Compare Amazon-fulfilled vs Merchant-fulfilled orders and their contribution to sales.[data/processed/fulfillment_analysis.csv]  
4. **Customer / Geography Analysis** – Study state-wise sales distribution to identify key markets and growth regions. 
5. **Business Insights & Recommendations** – Provide clear, actionable suggestions to improve sales, reduce returns, and optimize operations.

---

## 📂 Repository Structure

Amazon-Dashboard/
├── data/
│ ├── raw/
│ │ └── Amazon-Sale-Report.csv # Original dataset
│ └── processed/
│ ├── cleaned_sales.csv # Cleaned dataset
│ ├── product_sales.csv # Category & size level sales
│ ├── fulfillment_analysis.csv # Amazon vs Merchant metrics
│ └── state_sales.csv # State-wise revenue
├── notebooks/ # (optional) exploratory notebooks
├── scripts/
│ ├── clean_data.py # Data cleaning & preprocessing
│ ├── analysis.py # KPI & aggregation calculations
│ └── visualize.py # Chart generation scripts
├── reports/
│ ├── figures/
│ │ ├── product_sales.png # Sales by category & size
│ │ ├── fulfillment_analysis.png # Fulfillment method pie chart
│ │ └── state_sales.jpg # Sales by state bar chart
│ ├── project_report.md # Markdown report
│ └── Amazon_Sales_Analysis_Complete.pdf # Final PDF report (for submission)
├── docs/
│ └── README.md # This documentation
├── environment.yml # Conda environment (Python 3.12)
└── LICENSE # Project license

---

## 🧮 Data Source & Description

- **File:** `data/raw/Amazon-Sale-Report.csv`  
- **Rows:** 121,176 orders (after cleaning).
- **Key Fields:**
  - `Order ID`, `Date`, `Status` (Shipped, Cancelled, Returned, etc.)  
  - `Fulfilment` (Amazon / Merchant)  
  - `Sales Channel`, `ship-service-level`  
  - `Category` (T-shirt, Shirt, Blazer, Perfume, Wallet, etc.)  
  - `Size` (XS–6XL, Free)  
  - `Qty`, `Amount`, `Currency`  
  - Shipping city, state, postal code, country  
  - `B2B`, `fulfilled-by`, flags for new / pending

Pre-processing steps include handling missing values, filtering invalid records, and deriving metrics such as return rate and state-wise totals.

---

## ⚙️ Tech Stack

- **Language:** Python 3.12  
- **Libraries:**  
  - `pandas` – data cleaning & aggregation  
  - `matplotlib`, `seaborn` – visualizations  
  - `jupyter` – interactive analysis (if notebooks used)  
- **Environment:** Managed via `environment.yml` for reproducibility.

To create the environment:

conda env create -f environment.yml
conda activate amazon-dashboard


---

## ▶️ How to Run the Project

From the project root:

1. **Clean the raw data**

python scripts/clean_data.py

Outputs: `data/processed/cleaned_sales.csv`.

2. **Generate aggregations & KPIs**

python scripts/analysis.py

Outputs: `product_sales.csv`, `fulfillment_analysis.csv`, `state_sales.csv` in `data/processed/`.

3. **Create visualizations**

python scripts/visualize.py

Outputs charts in `reports/figures/`:
- `product_sales.png`
- `fulfillment_analysis.png`
- `state_sales.jpg`[file:34][file:35][file:36]

4. **View final report**

Open `reports/Amazon_Sales_Analysis_Complete.pdf` (or `project_report.md`) to see the complete narrative with charts and recommendations.[file:37]

---

## 📊 Key Results (Summary)

- **Total Sales:** ~₹7,85,90,170 (7.86 crore).[file:37]  
- **Total Orders:** 121,176.[file:37]  
- **Average Order Value:** ~₹648.56.[file:37]  
- **Return Rate:** 15.8% (19,146 returned orders).[file:37]  

- **Top Categories (by revenue):** Blazer, Perfume, Shirt, with T‑shirts overall leading by volume.[file:34][file:37]  
- **Top Sizes:** XXL, XL, and Free size products.[file:34][file:37]  

- **Fulfillment Split:** Amazon – 69.1%, Merchant – 30.9%.[file:35][file:37]  

- **Top 5 States by Sales:** Maharashtra, Karnataka, Telangana, Uttar Pradesh, Tamil Nadu.[file:36][file:37]

For the full detailed interpretation, see `reports/Amazon_Sales_Analysis_Complete.pdf`.[file:37]

---

## 💡 Business Insights (Highlights)

- Revenue is concentrated in fashion categories and larger sizes (XXL/XL), suggesting the need to prioritize inventory in these segments.[file:34][file:37]  
- High return rate indicates potential sizing or expectation mismatch; improving size charts and product details is critical.[file:37]  
- Amazon-fulfilled orders dominate, indicating trust in Amazon logistics; Merchant fulfillment performance should be aligned via clear SLAs.[file:35][file:2]  
- A handful of states drive most revenue, but there is a long tail of underpenetrated regions with growth potential.[file:36][file:2]

---

## 🚀 Future Work

- Build an interactive dashboard (Power BI / Tableau / Streamlit) on top of current aggregations.  
- Add customer‑level metrics if unique customer IDs become available (CLV, RFM analysis).  
- Automate pipeline using a scheduler (Airflow / Cron) for periodic refresh.  
- Add tests (unit tests for scripts) and CI workflow (GitHub Actions).[web:17][web:49]

---

## 👤 Author

- **Name:** Rishv (Data Analyst Intern)  
- **Role:** Data cleaning, analysis, visualization, documentation, and reporting.  

---

## 📄 License

This project is licensed under the **MIT License** – see the [LICENSE](../LICENSE) file for details.[web:40][web:55]
