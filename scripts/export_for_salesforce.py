from pathlib import Path
import csv
import sqlite3


# Locate the main project directory.
BASE_DIR = Path(__file__).resolve().parent.parent

# Input SQLite database.
DATABASE_PATH = BASE_DIR / "data" / "service_projects.db"

# Output directory and CSV file.
EXPORT_DIRECTORY = BASE_DIR / "exports"
EXPORT_PATH = EXPORT_DIRECTORY / "service_projects.csv"


def export_service_projects() -> None:
    """Export service-project data from SQLite to a Salesforce-ready CSV."""

    if not DATABASE_PATH.exists():
        print(f"Database was not found: {DATABASE_PATH}")
        return

    # Create the exports folder if it does not already exist.
    EXPORT_DIRECTORY.mkdir(parents=True, exist_ok=True)

    try:
        with sqlite3.connect(DATABASE_PATH) as connection:
            connection.row_factory = sqlite3.Row
            cursor = connection.cursor()

            cursor.execute(
                """
                SELECT
                    sp.project_name,
                    sp.project_code,

                    CASE
                        WHEN p.program_year IS NOT NULL
                        THEN p.program_name || ' ' || p.program_year
                        ELSE p.program_name
                    END AS visiting_program,

                    sp.project_date,
                    sp.participant_count,
                    sp.hours_per_participant,
                    sp.notes,

                    GROUP_CONCAT(
                        sd.box_url,
                        ' | '
                    ) AS supporting_documents

                FROM service_projects AS sp

                INNER JOIN programs AS p
                    ON sp.program_id = p.program_id

                LEFT JOIN supporting_documents AS sd
                    ON sp.project_id = sd.project_id

                GROUP BY
                    sp.project_id,
                    sp.project_name,
                    sp.project_code,
                    p.program_name,
                    p.program_year,
                    sp.project_date,
                    sp.participant_count,
                    sp.hours_per_participant,
                    sp.notes

                ORDER BY
                    sp.project_date,
                    sp.project_name;
                """
            )

            records = cursor.fetchall()

        if not records:
            print("No service-project records were found to export.")
            return

        fieldnames = [
            "Project Name",
            "Visiting Program",
            "Project Code",
            "Project Date",
            "Number of Participants",
            "Number of Hours",
            "Notes",
            "Supporting Documents",
        ]

        with EXPORT_PATH.open(
            mode="w",
            newline="",
            encoding="utf-8-sig",
        ) as csv_file:
            writer = csv.DictWriter(
                csv_file,
                fieldnames=fieldnames,
            )

            writer.writeheader()

            for record in records:
                writer.writerow(
                    {
                        "Project Name": record["project_name"],
                        "Visiting Program": record["visiting_program"],
                        "Project Code": record["project_code"],
                        "Project Date": record["project_date"] or "",
                        "Number of Participants":
                            record["participant_count"]
                            if record["participant_count"] is not None
                            else "",
                        "Number of Hours":
                            record["hours_per_participant"]
                            if record["hours_per_participant"] is not None
                            else "",
                        "Notes": record["notes"] or "",
                        "Supporting Documents":
                            record["supporting_documents"] or "",
                    }
                )

        print("Salesforce CSV export completed successfully.")
        print(f"Exported {len(records)} project record(s).")
        print(f"CSV location: {EXPORT_PATH}")

    except sqlite3.Error as error:
        print(f"Database error: {error}")

    except OSError as error:
        print(f"File error: {error}")


if __name__ == "__main__":
    export_service_projects()