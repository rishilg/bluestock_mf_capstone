from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).resolve().parent.parent
RAW_DATA_PATH = BASE_DIR / "data" / "raw"

csv_files = list(RAW_DATA_PATH.glob("*.csv"))

for file in csv_files:

    print("\n" + "="*80)
    print(file.name)
    print("="*80)

    df = pd.read_csv(file)

    for col in df.columns:
        print(col)