# Service Project Database

A Python and SQLite application developed during a software and database internship with **FIUTS (Foundation for International Understanding Through Students)**.

The application provides a lightweight workflow for organizing service-project information, validating records, storing structured data in SQLite, and generating Salesforce-compatible CSV files.

## Overview

The Service Project Database was created to simplify the process of preparing service-project records for Salesforce.

Instead of manually creating individual Salesforce records, project information can be entered into a standardized Microsoft Excel spreadsheet.

A Python import script validates and processes the spreadsheet data before storing it in a relational SQLite database. Existing projects can be updated using a unique Project Code rather than duplicated.

The application can then generate a Salesforce-compatible CSV file that can be uploaded using Salesforce's Data Import Wizard.

## Features

- Import structured service-project data from Microsoft Excel
- Validate required spreadsheet columns and field values
- Store project information in a relational SQLite database
- Create related program and organization records automatically
- Insert new projects or update existing projects using a unique Project Code
- Reduce duplicate service-project records
- Store supporting-document references
- Export records to a Salesforce-compatible CSV file
- Support future reporting and data analysis
- Run locally without requiring a database server

## Technology Stack

- Python 3
- SQLite
- Microsoft Excel
- openpyxl
- Salesforce Data Import Wizard
- Git
- GitHub

## Application Workflow

```text
Microsoft Excel
        ↓
import_from_excel.py
        ↓
Data Validation
        ↓
SQLite Database
        ↓
export_for_salesforce.py
        ↓
Salesforce-Compatible CSV
        ↓
Salesforce Data Import Wizard
        ↓
Service Project Object
```

## Project Structure

```text
service-project-database/
│
├── database/
│   └── schema.sql
│
├── scripts/
│   ├── create_database.py
│   ├── add_sample_data.py
│   ├── import_from_excel.py
│   └── export_for_salesforce.py
│
├── .gitignore
├── README.md
└── requirements.txt
```

The `data/` and `exports/` directories are created or used locally during application operation and are excluded from source control when they contain operational data.

## Database Design

The SQLite database contains the following related entities:

- Programs
- Organizations
- Service Projects
- Project Results
- Supporting Documents

Service projects reference programs and organizations using foreign keys.

Each service project also has a unique **Project Code**, which is used to identify existing projects and prevent duplicate records.

Database constraints are used to help maintain valid data, including:

- Primary keys
- Foreign keys
- Unique constraints
- Non-negative participant counts
- Non-negative volunteer/service hours
- Cascading deletion for related project records

## Installation

Clone the repository:

```bash
git clone https://github.com/xniki22/service-project-database.git
```

Move into the project directory:

```bash
cd service-project-database
```

Create a Python virtual environment:

### Windows

```bash
python -m venv .venv
.venv\Scripts\activate
```

### macOS / Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install the required Python package:

```bash
pip install -r requirements.txt
```

## Create the Database

Run:

```bash
python scripts/create_database.py
```

This creates:

```text
data/service_projects.db
```

The database file is intentionally excluded from Git.

## Add Demonstration Data

Optional fictional sample data can be added with:

```bash
python scripts/add_sample_data.py
```

The sample records are demonstration data only and do not represent real FIUTS participants or production records.

## Excel Import

The Excel import script expects a local file at:

```text
data/service_projects_input.xlsx
```

The spreadsheet should contain the following columns:

```text
Visiting Program
Program Year
Project Code
Project Name
Project Date
Organization
Number of Participants
Number of Hours
Notes
Supporting Documents
```

Run the import with:

```bash
python scripts/import_from_excel.py
```

The importer validates required values and uses the Project Code to determine whether a service project should be inserted or updated.

## Salesforce Export

After records have been stored in SQLite, generate a Salesforce-compatible CSV with:

```bash
python scripts/export_for_salesforce.py
```

The generated file is written to:

```text
exports/service_projects.csv
```

Generated exports are intentionally excluded from Git because operational exports may contain organization-specific data.

## Salesforce Configuration

The workflow assumes a Salesforce custom object representing a **Service Project**.

The Salesforce **Project Code** field should be configured as:

- Unique
- External ID

Using a unique external identifier makes it possible to identify existing projects during future imports and helps prevent duplicate records.

The generated CSV includes fields such as:

```text
Project Name
Visiting Program
Project Code
Project Date
Number of Participants
Number of Hours
Notes
Supporting Documents
```

The exact Salesforce field mappings depend on the organization's Salesforce configuration.

## Data Privacy

This public repository contains application source code and fictional demonstration data only.

Production FIUTS data is not intended to be stored in this repository.

The following are excluded from source control:

- SQLite database files
- Excel input files
- Generated CSV exports
- Environment files
- Credentials and API secrets
- Production supporting-document links
- Participant or volunteer records

Operational data should remain in approved private storage locations and should never be committed to the public repository.

## Security

The application uses parameterized SQLite queries rather than constructing SQL statements directly from spreadsheet values.

Local database files, spreadsheets, environment files, and generated exports are excluded through `.gitignore`.

No Salesforce usernames, passwords, OAuth tokens, API keys, or other credentials are required by the source code in this repository.

## Portfolio Context

This project demonstrates practical experience with:

- Python application development
- Relational database design
- SQL
- Data validation
- Excel data processing
- Data transformation
- Database normalization
- Salesforce data preparation
- Duplicate prevention
- Import and export workflows
- Git and GitHub

## Author

**Nikitha Cano**

Computer Science student at Bellevue College  
Data Science concentration