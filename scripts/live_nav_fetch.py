import requests
import pandas as pd
from pathlib import Path

# ==========================================
# Project Paths
# ==========================================

BASE_DIR = Path(__file__).resolve().parent.parent

RAW_PATH = BASE_DIR / "data" / "raw"
RAW_PATH.mkdir(parents=True, exist_ok=True)

# ==========================================
# Selected Mutual Funds
# ==========================================

funds = {
    "SBI Bluechip Fund": 119551,
    "ICICI Prudential Bluechip Fund": 120504,
    "Axis Bluechip Fund": 120503,
    "Nippon India Large Cap Fund": 118632,
    "HDFC Top 100 Fund": 125497
}

all_nav_data = []

print("\nFetching live NAV data...\n")

for fund_name, scheme_code in funds.items():

    url = f"https://api.mfapi.in/mf/{scheme_code}"

    try:

        response = requests.get(url)

        if response.status_code == 200:

            data = response.json()

            latest_nav = data["data"][0]

            all_nav_data.append({
                "scheme_code": scheme_code,
                "fund_name": fund_name,
                "date": latest_nav["date"],
                "nav": latest_nav["nav"]
            })

            print(f"✓ {fund_name}")

        else:

            print(f"✗ Failed: {fund_name}")

    except Exception as e:

        print(f"✗ Error: {fund_name}")
        print(e)

# ==========================================
# Save Results
# ==========================================

nav_df = pd.DataFrame(all_nav_data)

output_file = RAW_PATH / "live_nav_data.csv"

nav_df.to_csv(output_file, index=False)

print("\n====================================")
print("LIVE NAV FETCH COMPLETE")
print("====================================")

print(nav_df)

print(f"\nSaved to:\n{output_file}")