import os

import pandas as pd
from dotenv import load_dotenv
from sqlalchemy import create_engine


load_dotenv()


def create_database_connection():
    """
    Create a connection to PostgreSQL.
    """

    host = os.getenv("DB_HOST")
    port = os.getenv("DB_PORT")
    database = os.getenv("DB_NAME")
    username = os.getenv("DB_USER")
    password = os.getenv("DB_PASSWORD")

    connection_string = (
        f"postgresql+psycopg2://{username}:{password}"
        f"@{host}:{port}/{database}"
    )

    engine = create_engine(connection_string)

    return engine


def load_data(df, table_name="sales"):
    """
    Load transformed data into PostgreSQL using incremental loading.
    """

    # Convert date columns
    date_columns = ["order_date", "ship_date"]

    for column in date_columns:
        df[column] = pd.to_datetime(df[column], errors="coerce")

    engine = create_database_connection()

    temp_table = f"{table_name}_temp"

    with engine.begin() as connection:

        # Load data into temporary staging table
        df.to_sql(
            temp_table,
            connection,
            if_exists="replace",
            index=False
        )

        # Insert only new records
        result = connection.exec_driver_sql(f"""
            INSERT INTO {table_name}
            SELECT *
            FROM {temp_table} AS temp
            WHERE NOT EXISTS (
                SELECT 1
                FROM {table_name} AS main
                WHERE main.row_id = temp.row_id
            );
        """)

        inserted_rows = result.rowcount
        skipped_rows = len(df) - inserted_rows

        # Remove temporary table
        connection.exec_driver_sql(
            f"DROP TABLE IF EXISTS {temp_table};"
        )

    print("ETL completed successfully.")
    print(f"Total records processed: {len(df)}")
    print(f"New records inserted: {inserted_rows}")
    print(f"Existing records skipped: {skipped_rows}")


if __name__ == "__main__":

    processed_file = "data/processed/clean_sales.csv"

    df = pd.read_csv(processed_file)

    load_data(df)