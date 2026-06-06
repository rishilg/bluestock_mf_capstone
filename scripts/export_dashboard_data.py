from pathlib import Path
import pandas as pd

# ======================================
# PATHS
# ======================================

BASE_DIR = Path(__file__).resolve().parent.parent

PROCESSED_PATH = BASE_DIR / "data" / "processed"

EXPORT_PATH = (
    BASE_DIR
    / "dashboard"
    / "dashboard_exports"
)

EXPORT_PATH.mkdir(
    parents=True,
    exist_ok=True
)

# ======================================
# LOAD DATA
# ======================================

fund_master = pd.read_csv(
    PROCESSED_PATH / "01_fund_master_clean.csv"
)

performance_metrics = pd.read_csv(
    PROCESSED_PATH / "performance_metrics.csv"
)

portfolio_holdings = pd.read_csv(
    PROCESSED_PATH / "09_portfolio_holdings_clean.csv"
)

# ======================================
# EXECUTIVE OVERVIEW
# ======================================

fund_master.to_csv(
    EXPORT_PATH / "executive_overview.csv",
    index=False
)

# ======================================
# PERFORMANCE DASHBOARD
# ======================================

performance_dashboard = performance_metrics.merge(
    fund_master[
        ["amfi_code", "sub_category"]
    ],
    on="amfi_code",
    how="left"
)

performance_dashboard.rename(
    columns={
        "fund_house_x": "fund_house"
    },
    inplace=True
)

performance_dashboard.to_csv(
    EXPORT_PATH / "performance_dashboard.csv",
    index=False
)

# ======================================
# RISK DASHBOARD
# ======================================

risk_dashboard = performance_dashboard[
    [
        "amfi_code",
        "scheme_name",
        "fund_house",
        "sub_category",
        "volatility_pct",
        "max_drawdown_pct",
        "var_95_pct",
        "sharpe_ratio"
    ]
]

risk_dashboard.to_csv(
    EXPORT_PATH / "risk_dashboard.csv",
    index=False
)

# ======================================
# SECTOR DASHBOARD
# ======================================

sector_dashboard = (
    portfolio_holdings
    .groupby(
        "sector",
        as_index=False
    )["weight_pct"]
    .sum()
)

sector_dashboard.to_csv(
    EXPORT_PATH / "sector_dashboard.csv",
    index=False
)

# ======================================
# PORTFOLIO OPTIMIZATION
# ======================================

portfolio_optimization = pd.DataFrame({
    "Fund": [
        "SBI Bluechip",
        "SBI Small Cap",
        "ICICI Midcap",
        "Kotak Flexicap",
        "Mirae Tax Saver"
    ],
    "Weight (%)": [
        28.04,
        10.25,
        17.00,
        25.82,
        18.89
    ]
})

portfolio_optimization.to_csv(
    EXPORT_PATH / "portfolio_optimization.csv",
    index=False
)

# ======================================
# SUMMARY
# ======================================

print("\nDashboard Export Complete\n")

for file in EXPORT_PATH.glob("*.csv"):
    print(file.name)