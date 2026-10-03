# Automated Sales ETL Pipeline

An automated ETL pipeline that extracts sales data from CSV files, transforms and cleans the data using Python and Pandas, and loads it into PostgreSQL.

The project also includes automated data quality testing and CI/CD using GitHub Actions and Render.

## Architecture

```text
Sales CSV
    ↓
Extract
    ↓
Transform
    ↓
Clean Sales Data
    ↓
Data Quality Tests
    ↓
Staging Table
    ↓
Incremental Load
    ↓
PostgreSQL


CI/CD Architecture: 

Developer Push
      ↓
GitHub
      ↓
CI Pipeline
      ↓
pytest
      ↓
16 Tests
      ↓
CD Pipeline
      ↓
Render


Daily Scheduled ETL:


Daily Schedule
      ↓
GitHub Actions
      ↓
Python ETL
      ↓
PostgreSQL


Technologies Used
Python
Pandas
PostgreSQL
SQLAlchemy
Psycopg2
Python-dotenv
Pytest
Git
GitHub
GitHub Actions
Render
ETL Process
1. Extract

Sales data is read from the CSV file:

data/processed/clean_sales.csv

2. Transform

The pipeline performs data processing such as:

Date conversion
Data cleaning
Feature preparation
Validation
Duplicate checking
3. Load

The transformed data is loaded into PostgreSQL.

A temporary staging table is created before inserting data into the main sales table.

4. Incremental Loading

The pipeline checks row_id before inserting records.

Existing records are skipped and only new records are inserted.

This prevents duplicate records during repeated ETL executions.

Data Quality Tests

The project uses Pytest to validate the dataset.

Tests include:

Required columns exist
row_id values are unique
Sales values are non-negative
Transformation functions work correctly
Pipeline functionality works correctly

Current test result:

16 passed
Automation

GitHub Actions is used for automation.

CI Pipeline

Runs when code is pushed to the main branch.

It:

Installs dependencies
Runs automated tests
Verifies the pipeline
Scheduled ETL

The ETL workflow runs automatically on a daily schedule.

It connects securely to PostgreSQL using GitHub Secrets.

CD Pipeline

After successful testing, the deployment workflow triggers the Render deployment.

Database

The project uses PostgreSQL hosted on Render.

The main table is:

sales

The table contains approximately 9,800 sales records.

row_id is used as the primary key for duplicate prevention.

Environment Variables

Database credentials are stored securely as environment variables:

DB_HOST
DB_PORT
DB_NAME
DB_USER
DB_PASSWORD

Sensitive credentials are not stored directly in the source code.

Project Structure
automated-sales-etl/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── src/
│   ├── extract.py
│   ├── transform.py
│   └── load.py
│
├── tests/
│   ├── test_etl.py
│   ├── test_pipeline.py
│   └── test_transform.py
│
├── .github/
│   └── workflows/
│       ├── ci.yml
│       ├── cd.yml
│       └── etl.yml
│
├── requirements.txt
├── .gitignore
└── README.md
How to Run Locally

Create and activate a virtual environment:

python -m venv venv

Install dependencies:

pip install -r requirements.txt

Create a .env file containing the PostgreSQL connection details.

Run the ETL:

python src/load.py

Run tests:

pytest
Example ETL Output
ETL completed successfully.
Total records processed: 9800
New records inserted: 0
Existing records skipped: 9800
Key Features
Automated ETL pipeline
PostgreSQL data warehouse
Incremental data loading
Duplicate prevention
Data quality testing
GitHub Actions CI/CD
Scheduled ETL execution
Secure database credentials
Cloud deployment using Render
Future Improvements
Add a real-time or API-based data source
Add data validation with Great Expectations
Add logging and monitoring
Add an analytics dashboard using Power BI
Add email/Slack notifications for pipeline failures
Add Docker support

