from pathlib import Path
import sqlite3
import pandas as pd

BASE_DIR = Path(__file__).resolve().parent.parent

DB_PATH = BASE_DIR / "data" / "db" / "bluestock_mf.db"


conn = sqlite3.connect(DB_PATH)

queries = {

    "Total Funds":
    """
    SELECT COUNT(*) AS total_funds
    FROM fund_master
    """,

    "Top 5 Funds By AUM":
    """
    SELECT scheme_name, aum_crore
    FROM scheme_performance
    ORDER BY aum_crore DESC
    LIMIT 5
    """,

    "Average Expense Ratio":
    """
    SELECT AVG(expense_ratio_pct) AS avg_expense_ratio
    FROM fund_master
    """,

    "Top Sharpe Ratio":
    """
    SELECT scheme_name, sharpe_ratio
    FROM scheme_performance
    ORDER BY sharpe_ratio DESC
    LIMIT 10
    """
}

for title, query in queries.items():

    print("\n" + "=" * 80)
    print(title)
    print("=" * 80)

    result = pd.read_sql_query(
        query,
        conn
    )

    print(result)

conn.close()