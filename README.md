# Service Project Database

A Python and SQLite application developed for **FIUTS (Foundation for International Understanding Through Students)** to manage volunteer service project data and prepare it for import into Salesforce.

## Overview

The Service Project Database provides a simple workflow for organizing service project information before importing it into Salesforce.

Instead of manually creating Salesforce records, staff members enter project information into a standardized Microsoft Excel spreadsheet. Python scripts then import the data into a SQLite database, validate the records, and generate a Salesforce-compatible CSV file for upload using Salesforce's Data Import Wizard.

The application improves data consistency, reduces manual data entry, and provides a centralized database for managing service projects.

---

## Features

- Import service project data from Microsoft Excel
- Store project information in a SQLite relational database
- Automatically update existing projects using Project Code
- Export validated records to a Salesforce-compatible CSV
- Reduce duplicate records using a unique Project Code
- Support future reporting and data analysis
- Lightweight database requiring no database server

---

## Technology Stack

- Python 3
- SQLite
- Microsoft Excel
- openpyxl
- Git & GitHub
- Salesforce Data Import Wizard

---

## Workflow

```
Microsoft Excel
        ↓
import_from_excel.py
        ↓
SQLite Database
        ↓
export_for_salesforce.py
        ↓
Salesforce CSV
        ↓
Salesforce Data Import Wizard
        ↓
Service Project Object
```


## Salesforce Configuration

The project assumes a custom Salesforce object named **Service Project** with fields corresponding to the exported CSV.

The **Project Code** field should be configured as:

- Unique
- External ID

This allows Salesforce to update existing records instead of creating duplicates during future imports.

---

## Documentation

Additional project documentation includes:

- User Guide
- Administrator Guide
- Salesforce Setup Guide

These documents describe installation, maintenance, troubleshooting, and Salesforce configuration in greater detail.

---

