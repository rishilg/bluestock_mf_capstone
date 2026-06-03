from pathlib import Path
import sqlite3


BASE_DIR = Path(__file__).resolve().parent.parent

DB_PATH = BASE_DIR / "data" / "db" / "bluestock_mf.db"

SCHEMA_PATH = BASE_DIR / "sql" / "schema.sql"


def create_database():

    print("Creating database...")

    conn = sqlite3.connect(DB_PATH)

    cursor = conn.cursor()

    with open(SCHEMA_PATH, "r") as file:
        schema_sql = file.read()

    cursor.executescript(schema_sql)

    conn.commit()

    conn.close()

    print("Database created successfully.")


if __name__ == "__main__":
    create_database()