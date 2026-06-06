from pathlib import Path
import sqlite3
import pandas as pd

# =====================================================
# DATABASE CONNECTION
# =====================================================

BASE_DIR = Path(__file__).resolve().parent.parent

DB_PATH = BASE_DIR / "data" / "db" / "bluestock_mf.db"

conn = sqlite3.connect(DB_PATH)

# =====================================================
# SQL QUERIES
# =====================================================

queries = {

    "Total Funds":
    """
    SELECT COUNT(*) AS total_funds
    FROM fund_master
    """,

    "Top 5 Funds By AUM":
    """
    SELECT
        scheme_name,
        aum_crore
    FROM scheme_performance
    ORDER BY aum_crore DESC
    LIMIT 5
    """,

    "Average Expense Ratio":
    """
    SELECT
        AVG(expense_ratio_pct) AS avg_expense_ratio
    FROM fund_master
    """,

    "Top 10 Funds By Sharpe Ratio":
    """
    SELECT
        scheme_name,
        sharpe_ratio
    FROM scheme_performance
    ORDER BY sharpe_ratio DESC
    LIMIT 10
    """,

    "Sector Wise Holdings":
    """
    SELECT
        sector,
        COUNT(*) AS holdings_count
    FROM portfolio_holdings
    GROUP BY sector
    ORDER BY holdings_count DESC
    """,

    "Average 3-Year Return":
    """
    SELECT
        AVG(return_3yr_pct) AS avg_return_3yr_pct
    FROM scheme_performance
    """,

    "Top 10 Funds By 3-Year Return":
    """
    SELECT
        scheme_name,
        return_3yr_pct
    FROM scheme_performance
    ORDER BY return_3yr_pct DESC
    LIMIT 10
    """,

    "Top 10 Highest Volatility Funds":
    """
    SELECT
        scheme_name,
        std_dev_ann_pct
    FROM scheme_performance
    ORDER BY std_dev_ann_pct DESC
    LIMIT 10
    """,

    "Category Distribution":
    """
    SELECT
        category,
        COUNT(*) AS fund_count
    FROM fund_master
    GROUP BY category
    ORDER BY fund_count DESC
    """,

    "Risk Grade Distribution":
    """
    SELECT
        risk_grade,
        COUNT(*) AS fund_count
    FROM scheme_performance
    GROUP BY risk_grade
    ORDER BY fund_count DESC
    """,

    "Top 10 Funds By Sortino Ratio":
    """
    SELECT
        scheme_name,
        sortino_ratio
    FROM scheme_performance
    ORDER BY sortino_ratio DESC
    LIMIT 10
    """,

    "Top 10 Funds By Alpha":
    """
    SELECT
        scheme_name,
        alpha
    FROM scheme_performance
    ORDER BY alpha DESC
    LIMIT 10
    """,

    "Top 10 Funds By Beta":
    """
    SELECT
        scheme_name,
        beta
    FROM scheme_performance
    ORDER BY beta DESC
    LIMIT 10
    """,

    "Top Rated Funds":
    """
    SELECT
        scheme_name,
        morningstar_rating
    FROM scheme_performance
    ORDER BY morningstar_rating DESC
    LIMIT 10
    """,

    "Highest Drawdown Funds":
    """
    SELECT
        scheme_name,
        max_drawdown_pct
    FROM scheme_performance
    ORDER BY max_drawdown_pct ASC
    LIMIT 10
    """
}

# =====================================================
# EXECUTE QUERIES
# =====================================================

for title, query in queries.items():

    print("\n" + "=" * 80)
    print(title)
    print("=" * 80)

    try:

        result = pd.read_sql_query(
            query,
            conn
        )

        print(result)

    except Exception as e:

        print(f"ERROR: {e}")

# =====================================================
# CLOSE CONNECTION
# =====================================================

conn.close()

print("\nAll queries executed.")