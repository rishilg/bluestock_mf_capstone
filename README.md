# Mutual Fund Analytics Dashboard

## Project Overview

This project analyzes mutual fund performance using data engineering, SQL analytics, portfolio optimization, risk analysis, and interactive Power BI dashboards.

The objective is to build a complete analytics pipeline that ingests mutual fund datasets, stores them in a relational database, performs advanced performance calculations, and visualizes insights through dashboards.

---

## Project Objectives

* Set up a complete Python analytics environment
* Ingest and clean 10 mutual fund datasets
* Build an ETL pipeline for automated processing
* Store cleaned data in SQLite
* Perform analytical SQL queries
* Fetch live NAV data using the mfapi.in API
* Calculate performance and risk metrics
* Perform portfolio optimization
* Build interactive Power BI dashboards
* Generate reports and business insights

---

## Technology Stack

* Python
* Pandas
* NumPy
* SQLite
* SQL
* Power BI
* Git
* VS Code

---

## Project Structure

```text
bluestock_mf_capstone/
│
├── data/
│   ├── raw/
│   ├── processed/
│   └── db/
│
├── scripts/
│   ├── data_ingestion.py
│   ├── etl_pipeline.py
│   ├── load_to_sqlite.py
│   ├── compute_metrics.py
│   ├── export_dashboard_data.py
│   ├── live_nav_fetch.py
│   └── test_queries.py
│
├── sql/
│   ├── schema.sql
│   └── queries.sql
│
├── reports/
│
├── dashboard/
│
└── Mutual_Fund_Analytics_Dashboard.pbix
```

---

## Datasets Used

The project uses 10 mutual fund datasets:

1. Fund Master
2. NAV History
3. AUM by Fund House
4. Monthly SIP Inflows
5. Category Inflows
6. Industry Folio Count
7. Scheme Performance
8. Investor Transactions
9. Portfolio Holdings
10. Benchmark Indices

---

## ETL Pipeline

1. Extract raw CSV datasets
2. Clean and validate records
3. Handle missing values
4. Standardize schemas
5. Generate processed datasets
6. Load data into SQLite database

---

## Data Quality Assessment

* All 10 datasets loaded successfully
* No duplicate records detected
* Missing values identified only in expected fields
* Dataset quality verified and approved for analysis

---

## Live NAV Integration

Live NAV data is fetched using the mfapi.in API for selected mutual fund schemes.

Output file:

```text
data/raw/live_nav_data.csv
```

---

## SQL Analytics

The project includes analytical SQL queries for:

* Fund counts
* AUM analysis
* Expense ratio analysis
* Sharpe ratio ranking
* Risk analysis
* Category distribution
* Alpha and Beta analysis
* Portfolio holdings analysis

---

## Performance Metrics

Calculated metrics include:

* Sharpe Ratio
* Sortino Ratio
* Alpha
* Beta
* Maximum Drawdown
* Annualized Standard Deviation
* 1-Year Returns
* 3-Year Returns
* 5-Year Returns

---

## Dashboard Pages

### Executive Overview

High-level business KPIs and fund distribution insights.

### Fund Performance Analysis

Performance comparison across mutual funds.

### Performance Filters & Deep Dive

Interactive filtering and fund-level exploration.

### Risk Analytics Insights

Volatility, drawdown, VaR, and risk-return analysis.

### Portfolio Optimization

Optimized portfolio allocation using risk-adjusted returns.

### Sector Analysis

Sector allocation and exposure breakdown.

---

## Key Findings

* Large-cap funds dominate the dataset.
* Banking and IT sectors have the highest exposure.
* Several funds demonstrate strong risk-adjusted returns.
* Portfolio optimization improves return-risk balance.
* Data quality is high and suitable for investment analysis.

---

## Author

Rishil Gopal

Mutual Fund Analytics Capstone Project
