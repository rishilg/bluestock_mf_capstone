from pathlib import Path
import pandas as pd
import numpy as np

# ==================================================
# PATHS
# ==================================================

BASE_DIR = Path(__file__).resolve().parent.parent

PROCESSED_PATH = BASE_DIR / "data" / "processed"

OUTPUT_FILE = PROCESSED_PATH / "performance_metrics.csv"

# ==================================================
# LOAD DATA
# ==================================================

nav_history = pd.read_csv(
    PROCESSED_PATH / "02_nav_history_clean.csv"
)

fund_master = pd.read_csv(
    PROCESSED_PATH / "01_fund_master_clean.csv"
)

nav_history["date"] = pd.to_datetime(
    nav_history["date"]
)

# ==================================================
# CONFIGURATION
# ==================================================

RISK_FREE_RATE = 0.05

results = []

# ==================================================
# METRIC CALCULATION
# ==================================================

for amfi_code in nav_history["amfi_code"].unique():

    try:

        # ------------------------------------------
        # Filter Fund
        # ------------------------------------------

        fund = nav_history[
            nav_history["amfi_code"] == amfi_code
        ].copy()

        fund = fund.sort_values("date")

        # ------------------------------------------
        # Daily Returns
        # ------------------------------------------

        fund["daily_return"] = (
            fund["nav"].pct_change()
        )

        fund = fund.dropna()

        if len(fund) < 50:
            continue

        # ------------------------------------------
        # Fund Metadata
        # ------------------------------------------

        meta = fund_master[
            fund_master["amfi_code"] == amfi_code
        ].iloc[0]

        scheme_name = meta["scheme_name"]
        fund_house = meta["fund_house"]
        category = meta["sub_category"]

        # ------------------------------------------
        # CAGR
        # ------------------------------------------

        n_days = len(fund)

        begin_nav = fund["nav"].iloc[0]
        end_nav = fund["nav"].iloc[-1]

        cagr = (
            (end_nav / begin_nav)
            ** (252 / n_days)
        ) - 1

        # ------------------------------------------
        # Volatility
        # ------------------------------------------

        volatility = (
            fund["daily_return"].std()
            * np.sqrt(252)
        )

        # ------------------------------------------
        # Sharpe Ratio
        # ------------------------------------------

        if volatility != 0:

            sharpe = (
                (cagr - RISK_FREE_RATE)
                / volatility
            )

        else:

            sharpe = np.nan

        # ------------------------------------------
        # Maximum Drawdown
        # ------------------------------------------

        rolling_max = (
            fund["nav"]
            .cummax()
        )

        drawdown = (
            fund["nav"]
            - rolling_max
        ) / rolling_max

        max_drawdown = (
            drawdown.min()
        )

        # ------------------------------------------
        # VaR (95%)
        # ------------------------------------------

        var_95 = np.percentile(
            fund["daily_return"],
            5
        )

        # ------------------------------------------
        # Save Results
        # ------------------------------------------

        results.append({

            "amfi_code": amfi_code,

            "scheme_name": scheme_name,

            "fund_house": fund_house,

            "category": category,

            "trading_days": n_days,

            "cagr_pct": round(
                cagr * 100,
                2
            ),

            "volatility_pct": round(
                volatility * 100,
                2
            ),

            "sharpe_ratio": round(
                sharpe,
                2
            ),

            "max_drawdown_pct": round(
                max_drawdown * 100,
                2
            ),

            "var_95_pct": round(
                var_95 * 100,
                2
            )

        })

    except Exception as e:

        print(
            f"Error processing {amfi_code}: {e}"
        )

# ==================================================
# CREATE DATAFRAME
# ==================================================

metrics_df = pd.DataFrame(
    results
)

# ==================================================
# SORT BY CAGR
# ==================================================

metrics_df = metrics_df.sort_values(
    "cagr_pct",
    ascending=False
)

# ==================================================
# SAVE OUTPUT
# ==================================================

metrics_df.to_csv(
    OUTPUT_FILE,
    index=False
)

# ==================================================
# SUMMARY
# ==================================================

print("\n" + "=" * 60)
print("PERFORMANCE METRICS GENERATED")
print("=" * 60)

print(
    f"\nFunds Processed: {len(metrics_df)}"
)

print(
    f"\nOutput Saved To:\n{OUTPUT_FILE}"
)

print("\nTop 5 Funds By CAGR:\n")

print(
    metrics_df[
        [
            "scheme_name",
            "category",
            "cagr_pct",
            "sharpe_ratio"
        ]
    ].head()
)