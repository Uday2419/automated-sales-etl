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
    Load transformed data into PostgreSQL.
    """

    engine = create_database_connection()

    df.to_sql(
        table_name,
        engine,
        if_exists="replace",
        index=False
    )

    print(f"Successfully loaded {len(df)} records into '{table_name}'.")


if __name__ == "__main__":

    processed_file = "data/processed/clean_sales.csv"

    df = pd.read_csv(processed_file)

    load_data(df)