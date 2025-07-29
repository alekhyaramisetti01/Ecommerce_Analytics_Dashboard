
# 🛒 E-commerce Analytics Dashboard

A comprehensive end-to-end data analytics project designed to extract actionable business insights from raw e-commerce transaction data. This project covers the complete analytics workflow — from data ingestion and transformation to KPI calculation and dashboard visualization — using industry-standard tools.

---

## 📊 Project Overview

This project simulates a real-world e-commerce business scenario, focusing on analyzing sales performance, customer demand, cancellation rates, and supply-chain efficiency using cleaned transaction data from multiple sources.

📥 The raw dataset was originally downloaded from **Kaggle**, then transformed and structured for analysis using Python and SQL.

---

## 📁 Folder Structure

```
Ecommerce_Analytics_Dashboard/
│
├── data/
│   ├── raw/                # Original input datasets (CSV)
│   ├── processed/          # Cleaned CSVs used for loading into PostgreSQL
│   └── exports/            # Exported KPI CSVs used in Tableau
│
├── scripts/                # Python scripts for data cleaning, pivoting, and automation
│
├── sql/
│   ├── create/             # CREATE TABLE scripts
│   ├── load/               # Data loading scripts using COPY
│   └── kpis/               # SQL scripts for KPI calculation
│
├── dashboards/
│   └── ecommerce_dashboard_final.pdf    # Exported Tableau dashboard (PDF format)
│
└── README.md               # Project documentation
```

---

## 🛠️ Tools & Technologies

| Tool/Technology  | Purpose                            |
|------------------|-------------------------------------|
| **Python (Pandas)**     | Data cleaning, transformation, exporting KPIs |
| **PostgreSQL**          | Data storage and complex SQL queries |
| **Tableau Public**      | Interactive dashboard visualization |
| **SQL**                 | KPI generation and aggregation |
| **VS Code**             | Development environment |

---

## 🧹 Data Cleaning

Raw sales data was cleaned using Python scripts:
- Removed nulls and unnecessary columns
- Standardized inconsistent date formats
- Fixed invalid column names
- Exported cleaned data to `/data/processed/` for further use

A dynamic script was also used to **auto-generate `CREATE TABLE` statements** from cleaned CSVs, handling edge cases like:
- Hyphens and spaces in column names
- Data type inference
- Safe SQL-compliant schema creation

---

## 🗃️ Database & ETL Process

- PostgreSQL used as the backend database
- SQL scripts auto-generated from Python
- Data loaded using `\COPY` statements from processed CSVs
- Clean separation between `sql/create/`, `sql/load/`, and `sql/kpis/`

---

## 📈 Key KPIs Implemented

| KPI Name                  | Description                                                                 |
|---------------------------|-----------------------------------------------------------------------------|
| 📉 **Monthly Revenue**          | Tracks monthly business revenue trends using line charts                    |
| ❌ **Cancellation Rate by Category** | Highlights product categories with the highest return rates              |
| 🏆 **Top Products by Revenue**     | Lists the top 10 revenue-generating products (domestic + international) |
| 🎯 **Stock vs Orders (Bullet Chart)** | Custom bullet chart visualizing over-demanded or understocked SKUs      |

---
## 📌 Dashboard Snapshot

Explore the full Power BI dashboard for the Bank Marketing Campaign Analysis:

🔗 [Click here to view the published report](https://public.tableau.com/views/ecommerce_analytics_dashboard/Dashboard1?:language=en-US&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link)


![Dashboard Screenshot](dashboard1.png)

---

## 🧠 What I Learned

- Building an end-to-end data pipeline using Python, SQL, and Tableau
- Automating schema generation and KPI exports using dynamic scripts
- Designing executive-level dashboards using real business insights
- Presenting supply vs. demand imbalances visually using bullet and dot plots

---

## 🚀 How to Reproduce

1. Clone the repo
2. Add raw datasets to `data/raw/`
3. Run Python cleaning scripts in `scripts/`
4. Use SQL scripts in `sql/create/` and `sql/load/` to prepare PostgreSQL
5. Run `export_kpis_to_csv.py` to generate KPI data
6. Import CSVs in Tableau and build the dashboard using saved sheets

---

## 🧩 Dashboard Highlights

- **Tableau Public** with interactive sheets
- Exported KPIs visualized through:
  - Line charts
  - Dot plots
  - Grouped bars
  - Bullet graphs
- Clean labels, color-coded metrics, and category filters

---

## 📬 Contact

Author: **Alekhya Ramisetti**  
📧 Email: ar89z@umsystem.edu 
🔗 LinkedIn: https://www.linkedin.com/in/alekhyaramisetti/

---
