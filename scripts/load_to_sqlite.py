from pathlib import Path
import pandas as pd
import sqlite3


BASE_DIR = Path(__file__).resolve().parent.parent

DB_PATH = BASE_DIR / "data" / "db" / "bluestock_mf.db"

PROCESSED_PATH = BASE_DIR / "data" / "processed"


def load_table(csv_name, table_name, conn):

    file_path = PROCESSED_PATH / csv_name

    df = pd.read_csv(file_path)

    df.to_sql(
        table_name,
        conn,
        if_exists="replace",
        index=False
    )

    print(
        f"{table_name}: {len(df)} rows loaded"
    )


def main():

    conn = sqlite3.connect(DB_PATH)

    load_table(
        "01_fund_master_clean.csv",
        "fund_master",
        conn
    )

    load_table(
        "02_nav_history_clean.csv",
        "nav_history",
        conn
    )

    load_table(
        "07_scheme_performance_clean.csv",
        "scheme_performance",
        conn
    )

    load_table(
        "09_portfolio_holdings_clean.csv",
        "portfolio_holdings",
        conn
    )

    load_table(
        "10_benchmark_indices_clean.csv",
        "benchmark_indices",
        conn
    )

    conn.close()

    print("\nDatabase load complete.")


if __name__ == "__main__":
    main()