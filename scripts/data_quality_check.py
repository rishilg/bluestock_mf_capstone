from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).resolve().parent.parent
RAW_DATA_PATH = BASE_DIR / "data" / "raw"

csv_files = list(RAW_DATA_PATH.glob("*.csv"))

for file in csv_files:

    print("\n" + "="*80)
    print(f"DATA QUALITY REPORT: {file.name}")
    print("="*80)

    try:

        df = pd.read_csv(file)

        print("\nShape:")
        print(df.shape)

        print("\nMissing Values:")
        print(df.isnull().sum())

        print("\nDuplicate Rows:")
        print(df.duplicated().sum())

        print("\nColumns:")
        print(df.columns.tolist())

    except Exception as e:
        print(f"Error: {e}")