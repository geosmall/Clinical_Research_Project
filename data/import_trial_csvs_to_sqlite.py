from __future__ import annotations

import argparse
import csv
import sqlite3
from pathlib import Path


TABLE_FILES = {
    "sites": "sites.csv",
    "subjects": "subjects.csv",
    "visits": "visits.csv",
    "adverse_events": "adverse_events.csv",
    "protocol_deviations": "protocol_deviations.csv",
}

INDEX_STATEMENTS = {
    "sites": [
        "CREATE INDEX IF NOT EXISTS idx_sites_site_id ON sites(site_id)",
    ],
    "subjects": [
        "CREATE INDEX IF NOT EXISTS idx_subjects_subject_id ON subjects(subject_id)",
        "CREATE INDEX IF NOT EXISTS idx_subjects_site_id ON subjects(site_id)",
    ],
    "visits": [
        "CREATE INDEX IF NOT EXISTS idx_visits_visit_id ON visits(visit_id)",
        "CREATE INDEX IF NOT EXISTS idx_visits_subject_id ON visits(subject_id)",
        "CREATE INDEX IF NOT EXISTS idx_visits_site_id ON visits(site_id)",
    ],
    "adverse_events": [
        "CREATE INDEX IF NOT EXISTS idx_adverse_events_ae_id ON adverse_events(ae_id)",
        "CREATE INDEX IF NOT EXISTS idx_adverse_events_subject_id ON adverse_events(subject_id)",
        "CREATE INDEX IF NOT EXISTS idx_adverse_events_site_id ON adverse_events(site_id)",
    ],
    "protocol_deviations": [
        "CREATE INDEX IF NOT EXISTS idx_protocol_deviations_deviation_id ON protocol_deviations(deviation_id)",
        "CREATE INDEX IF NOT EXISTS idx_protocol_deviations_subject_id ON protocol_deviations(subject_id)",
        "CREATE INDEX IF NOT EXISTS idx_protocol_deviations_site_id ON protocol_deviations(site_id)",
    ],
}


def parse_args() -> argparse.Namespace:
    script_dir = Path(__file__).resolve().parent
    default_db_path = script_dir / "trial_workbench.db"
    default_csv_dir = script_dir / "csv"

    parser = argparse.ArgumentParser(
        description="Load the repo's synthetic clinical trial CSVs into a SQLite database."
    )
    parser.add_argument(
        "--db",
        type=Path,
        default=default_db_path,
        help="Path to the SQLite database file to create or update.",
    )
    parser.add_argument(
        "--data-dir",
        type=Path,
        default=default_csv_dir,
        help="Directory containing the input CSV files.",
    )
    return parser.parse_args()


def quote_identifier(name: str) -> str:
    return '"' + name.replace('"', '""') + '"'


def load_table(connection: sqlite3.Connection, table_name: str, csv_path: Path) -> int:
    with csv_path.open("r", encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        if reader.fieldnames is None:
            raise SystemExit(f"No header row found in {csv_path}")

        columns = reader.fieldnames
        quoted_columns = ", ".join(quote_identifier(column) for column in columns)
        create_columns = ", ".join(f"{quote_identifier(column)} TEXT" for column in columns)
        placeholders = ", ".join("?" for _ in columns)

        connection.execute(f"DROP TABLE IF EXISTS {quote_identifier(table_name)}")
        connection.execute(
            f"CREATE TABLE {quote_identifier(table_name)} ({create_columns})"
        )

        rows = [tuple(row.get(column, "") for column in columns) for row in reader]
        if rows:
            connection.executemany(
                f"INSERT INTO {quote_identifier(table_name)} ({quoted_columns}) VALUES ({placeholders})",
                rows,
            )

    for statement in INDEX_STATEMENTS.get(table_name, []):
        connection.execute(statement)
    return len(rows)


def main() -> None:
    args = parse_args()
    data_dir = args.data_dir.resolve()
    db_path = args.db.resolve()

    missing = [filename for filename in TABLE_FILES.values() if not (data_dir / filename).exists()]
    if missing:
        missing_list = ", ".join(missing)
        raise SystemExit(f"Missing required CSV files in {data_dir}: {missing_list}")

    db_path.parent.mkdir(parents=True, exist_ok=True)

    with sqlite3.connect(db_path) as connection:
        summary: list[tuple[str, int]] = []
        for table_name, filename in TABLE_FILES.items():
            row_count = load_table(connection, table_name, data_dir / filename)
            summary.append((table_name, row_count))
        connection.commit()

    print(f"Created SQLite database: {db_path}")
    for table_name, row_count in summary:
        print(f"- {table_name}: {row_count} rows")


if __name__ == "__main__":
    main()
