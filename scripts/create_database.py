from pathlib import Path
import sqlite3


BASE_DIR = Path(__file__).resolve().parent.parent
DATABASE_PATH = BASE_DIR / "data" / "service_projects.db"
SCHEMA_PATH = BASE_DIR / "database" / "schema.sql"


def create_database() -> None:
    DATABASE_PATH.parent.mkdir(parents=True, exist_ok=True)

    try:
        schema = SCHEMA_PATH.read_text(encoding="utf-8")

        with sqlite3.connect(DATABASE_PATH) as connection:
            connection.execute("PRAGMA foreign_keys = ON;")
            connection.executescript(schema)
            connection.commit()

        print(f"Database created successfully: {DATABASE_PATH}")

    except FileNotFoundError:
        print(f"Schema file not found: {SCHEMA_PATH}")

    except sqlite3.Error as error:
        print(f"Database error: {error}")


if __name__ == "__main__":
    create_database()