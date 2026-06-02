from pathlib import Path
import pandas as pd

# Project paths
BASE_DIR = Path(__file__).resolve().parent.parent
RAW_DATA_PATH = BASE_DIR / "data" / "raw"

print("=" * 80)
print("DATA INGESTION REPORT")
print("=" * 80)

# Find all CSV files
csv_files = list(RAW_DATA_PATH.glob("*.csv"))

print(f"\nFound {len(csv_files)} CSV files.\n")

for file in csv_files:

    print("\n" + "=" * 80)
    print(f"FILE: {file.name}")
    print("=" * 80)

    try:

        df = pd.read_csv(file)

        print("\nShape:")
        print(df.shape)

        print("\nData Types:")
        print(df.dtypes)

        print("\nFirst 5 Rows:")
        print(df.head())

    except Exception as e:
        print(f"Error reading {file.name}")
        print(e)