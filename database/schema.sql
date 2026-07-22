PRAGMA foreign_keys = ON;

CREATE TABLE IF NOT EXISTS programs (
    program_id INTEGER PRIMARY KEY AUTOINCREMENT,
    program_code TEXT NOT NULL UNIQUE,
    program_name TEXT NOT NULL,
    program_year INTEGER,
    program_type TEXT,
    notes TEXT
);

CREATE TABLE IF NOT EXISTS organizations (
    organization_id INTEGER PRIMARY KEY AUTOINCREMENT,
    organization_name TEXT NOT NULL UNIQUE,
    location TEXT,
    website TEXT,
    salesforce_account_id TEXT
);

CREATE TABLE IF NOT EXISTS service_projects (
    project_id INTEGER PRIMARY KEY AUTOINCREMENT,
    project_code TEXT NOT NULL UNIQUE,
    program_id INTEGER NOT NULL,
    organization_id INTEGER,
    project_date TEXT,
    participant_count INTEGER,
    hours_per_participant REAL,
    notes TEXT,
    salesforce_record_id TEXT,
    sync_status TEXT NOT NULL DEFAULT 'Not Synced',

    FOREIGN KEY (program_id)
        REFERENCES programs(program_id),

    FOREIGN KEY (organization_id)
        REFERENCES organizations(organization_id),

    CHECK (participant_count IS NULL OR participant_count >= 0),
    CHECK (
        hours_per_participant IS NULL
        OR hours_per_participant >= 0
    )
);

CREATE TABLE IF NOT EXISTS project_results (
    result_id INTEGER PRIMARY KEY AUTOINCREMENT,
    project_id INTEGER NOT NULL,
    result_type TEXT NOT NULL,
    quantity REAL,
    unit TEXT,
    outcome_description TEXT,

    FOREIGN KEY (project_id)
        REFERENCES service_projects(project_id)
        ON DELETE CASCADE,

    CHECK (quantity IS NULL OR quantity >= 0)
);

CREATE TABLE IF NOT EXISTS supporting_documents (
    document_id INTEGER PRIMARY KEY AUTOINCREMENT,
    project_id INTEGER NOT NULL,
    document_name TEXT NOT NULL,
    document_type TEXT,
    box_url TEXT,
    description TEXT,

    FOREIGN KEY (project_id)
        REFERENCES service_projects(project_id)
        ON DELETE CASCADE
);