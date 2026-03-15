from __future__ import annotations

import argparse
import sqlite3
from pathlib import Path

import pandas as pd


STARTER_TABLES = [
    "patients",
    "encounters",
    "conditions",
    "medications",
    "observations",
]


def parse_args() -> argparse.Namespace:
    script_dir = Path(__file__).resolve().parent
    default_csv_dir = script_dir / "csv"
    default_db_path = script_dir / "synthea_starter.db"

    parser = argparse.ArgumentParser(
        description="Import starter Synthea CSV files into a local SQLite database."
    )
    parser.add_argument(
        "--csv-dir",
        type=Path,
        default=default_csv_dir,
        help="Directory containing extracted Synthea CSV files.",
    )
    parser.add_argument(
        "--db",
        type=Path,
        default=default_db_path,
        help="Output SQLite database path.",
    )
    return parser.parse_args()


def load_csv(csv_path: Path) -> pd.DataFrame:
    return pd.read_csv(csv_path, dtype=str, keep_default_na=False)


def create_indexes(conn: sqlite3.Connection) -> None:
    index_statements = [
        "CREATE INDEX IF NOT EXISTS idx_patients_id ON patients(Id)",
        "CREATE INDEX IF NOT EXISTS idx_encounters_id ON encounters(Id)",
        "CREATE INDEX IF NOT EXISTS idx_encounters_patient ON encounters(PATIENT)",
        "CREATE INDEX IF NOT EXISTS idx_conditions_patient ON conditions(PATIENT)",
        "CREATE INDEX IF NOT EXISTS idx_conditions_encounter ON conditions(ENCOUNTER)",
        "CREATE INDEX IF NOT EXISTS idx_medications_patient ON medications(PATIENT)",
        "CREATE INDEX IF NOT EXISTS idx_medications_encounter ON medications(ENCOUNTER)",
        "CREATE INDEX IF NOT EXISTS idx_observations_patient ON observations(PATIENT)",
        "CREATE INDEX IF NOT EXISTS idx_observations_encounter ON observations(ENCOUNTER)",
    ]
    for statement in index_statements:
        conn.execute(statement)


def main() -> None:
    args = parse_args()
    csv_dir = args.csv_dir.resolve()
    db_path = args.db.resolve()

    if not csv_dir.exists():
        raise SystemExit(f"CSV directory not found: {csv_dir}")

    with sqlite3.connect(db_path) as conn:
        for table_name in STARTER_TABLES:
            csv_path = csv_dir / f"{table_name}.csv"
            if not csv_path.exists():
                raise SystemExit(f"Missing expected CSV file: {csv_path}")

            df = load_csv(csv_path)
            df.to_sql(table_name, conn, if_exists="replace", index=False)
            print(f"- {table_name}: {len(df)} rows")

        create_indexes(conn)

    print(f"Created SQLite database: {db_path}")


if __name__ == "__main__":
    main()
