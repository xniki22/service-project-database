from pathlib import Path
import sqlite3


BASE_DIR = Path(__file__).resolve().parent.parent
DATABASE_PATH = BASE_DIR / "data" / "service_projects.db"


def add_sample_data() -> None:
    try:
        with sqlite3.connect(DATABASE_PATH) as connection:
            connection.execute("PRAGMA foreign_keys = ON;")

            cursor = connection.cursor()

            cursor.executemany(

    """
    INSERT INTO programs (
        program_code,
        program_name,
        program_year,
        program_type,
        notes
    )
    VALUES (?, ?, ?, ?, ?)
    """,
    [
        ("SUSI-SUMMER-2025", "SUSI Summer", 2025, "Visiting Program", None),
        ("KANDA-2025", "Kanda University", 2025, "Visiting Program", None),
        ("KOISHIKAWA-2025", "Koishikawa High School", 2025, "Visiting Program", None),
        ("SUSI-WINTER-2026", "SUSI Winter", 2026, "Visiting Program", None),
        ("EHIME-2026", "Ehime", 2026, "Visiting Program", None),
        ("YLAI-2026", "YLAI", 2026, "Visiting Program", None),
    ],
)
            

            cursor.executemany(
                """
                INSERT INTO organizations (organization_name)
                VALUES (?)
                """,
                [
                    ("Northwest Harvest",),
                    ("Food Lifeline",),
                    ("Sample Community Organization",),
                ],
            )

            connection.commit()

        print("Sample data added successfully.")

    except sqlite3.IntegrityError:
        print("Sample data may already exist in the database.")

    except sqlite3.Error as error:
        print(f"Database error: {error}")


if __name__ == "__main__":
    add_sample_data()