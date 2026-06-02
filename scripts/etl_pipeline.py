from pathlib import Path
import pandas as pd


# ==========================
# PATHS
# ==========================

BASE_DIR = Path(__file__).resolve().parent.parent

RAW_DATA_PATH = BASE_DIR / "data" / "raw"
PROCESSED_DATA_PATH = BASE_DIR / "data" / "processed"

PROCESSED_DATA_PATH.mkdir(exist_ok=True)


# ==========================
# TRANSFORMATIONS
# ==========================

def transform_dataframe(df, filename):

    # Remove duplicates
    df = df.drop_duplicates()

    # -------------------------
    # fund_master
    # -------------------------
    if "fund_master" in filename.lower():

        if "launch_date" in df.columns:
            df["launch_date"] = pd.to_datetime(
                df["launch_date"],
                errors="coerce"
            )

    # -------------------------
    # nav_history
    # -------------------------
    elif "nav_history" in filename.lower():

        if "date" in df.columns:
            df["date"] = pd.to_datetime(
                df["date"],
                errors="coerce"
            )

            df = df.sort_values(
                ["amfi_code", "date"]
            )

    # -------------------------
    # benchmark_indices
    # -------------------------
    elif "benchmark_indices" in filename.lower():

        if "date" in df.columns:
            df["date"] = pd.to_datetime(
                df["date"],
                errors="coerce"
            )

            df = df.sort_values(
                ["index_name", "date"]
            )

    return df


# ==========================
# ETL PROCESS
# ==========================

def run_etl():

    csv_files = list(
        RAW_DATA_PATH.glob("*.csv")
    )

    print("\nStarting ETL Pipeline...\n")

    for file in csv_files:

        try:

            print(f"Processing: {file.name}")

            df = pd.read_csv(file)

            original_rows = len(df)

            df = transform_dataframe(
                df,
                file.name
            )

            cleaned_rows = len(df)

            output_name = (
                file.stem + "_clean.csv"
            )

            output_path = (
                PROCESSED_DATA_PATH /
                output_name
            )

            df.to_csv(
                output_path,
                index=False
            )

            print(
                f"Saved: {output_name}"
            )

            print(
                f"Rows: {original_rows} -> {cleaned_rows}"
            )

            print("-" * 50)

        except Exception as e:

            print(
                f"Error processing {file.name}"
            )

            print(e)

    print("\nETL Complete.")


# ==========================
# MAIN
# ==========================

if __name__ == "__main__":
    run_etl()