from pathlib import Path
import sqlite3


BASE_DIR = Path(__file__).resolve().parent.parent
DATABASE_PATH = BASE_DIR / "data" / "service_projects.db"


def add_sample_data() -> None:
    try:
        with sqlite3.connect(DATABASE_PATH) as connection:
            connection.execute("PRAGMA foreign_keys = ON;")
            cursor = connection.cursor()

            # Add sample programs
            cursor.executemany(
                """
                INSERT INTO programs (
                    program_name,
                    program_year,
                    notes
                )
                VALUES (?, ?, ?)
                """,
                [
                    (
                        "SUSI Summer",
                        2025,
                        "Sample program for testing",
                    ),
                    (
                        "Kanda University",
                        2025,
                        "Sample program for testing",
                    ),
                    (
                        "Koishikawa High School",
                        2025,
                        "Sample program for testing",
                    ),
                    (
                        "SUSI Winter",
                        2026,
                        "Sample program for testing",
                    ),
                    (
                        "Ehime",
                        2026,
                        "Sample program for testing",
                    ),
                    (
                        "YLAI",
                        2026,
                        "Sample program for testing",
                    ),
                ],
            )

            # Add sample organizations
            cursor.executemany(
                """
                INSERT INTO organizations (
                    organization_name,
                    location
                )
                VALUES (?, ?)
                """,
                [
                    ("Northwest Harvest", "Seattle, WA"),
                    ("Food Lifeline", "Seattle, WA"),
                    (
                        "Sample Community Organization",
                        "Seattle, WA",
                    ),
                ],
            )

            # Find the IDs needed for the service project
            cursor.execute(
                """
                SELECT program_id
                FROM programs
                WHERE program_name = ?
                  AND program_year = ?
                """,
                ("SUSI Summer", 2025),
            )

            program_row = cursor.fetchone()

            cursor.execute(
                """
                SELECT organization_id
                FROM organizations
                WHERE organization_name = ?
                """,
                ("Food Lifeline",),
            )

            organization_row = cursor.fetchone()

            if program_row is None or organization_row is None:
                raise ValueError(
                    "Could not find the sample program or organization."
                )

            program_id = program_row[0]
            organization_id = organization_row[0]

            # Add one sample service project
            cursor.execute(
                 """
                 INSERT INTO service_projects (
                 project_code,
                 project_name,
                 program_id,
                 organization_id,
                 project_date,
                 participant_count,
                 hours_per_participant,
                 notes,
                 sync_status
                 )
                 VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
                 """,
                 (
                     "SP-SUSI-SUMMER-2025-001",
                     "Food Packaging Project",
                     program_id,
                     organization_id,
                     "2025-07-15",
                     20,
                     3.0,
                     "Sample project for Salesforce import testing",
                     "Not Synced",
                     ),
                )

            project_id = cursor.lastrowid

            # Add a sample supporting document
            cursor.execute(
                """
                INSERT INTO supporting_documents (
                    project_id,
                    document_name,
                    document_type,
                    box_url,
                    description
                )
                VALUES (?, ?, ?, ?, ?)
                """,
                (
                    project_id,
                    "Sample Project Documents",
                    "Box Folder",
                    "https://example.com/sample-documents",
                    "Placeholder link for testing",
                ),
            )

            connection.commit()

        print("Sample data added successfully.")

    except sqlite3.IntegrityError as error:
        print(f"Sample data may already exist: {error}")

    except (sqlite3.Error, ValueError) as error:
        print(f"Database error: {error}")


if __name__ == "__main__":
    add_sample_data()