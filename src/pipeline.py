from extract import extract_data
from transform import transform_data
from load import load_data


RAW_FILE = "data/raw/sales.csv"


def run_pipeline():

    print("=" * 50)
    print("STARTING SALES ETL PIPELINE")
    print("=" * 50)

    # 1. Extract
    print("\n[1] Extracting data...")
    df = extract_data(RAW_FILE)

    # 2. Transform
    print("\n[2] Transforming data...")
    df = transform_data(df)

    # 3. Load
    print("\n[3] Loading data into PostgreSQL...")
    load_data(df)

    print("\n" + "=" * 50)
    print("ETL PIPELINE COMPLETED SUCCESSFULLY")
    print("=" * 50)


if __name__ == "__main__":
    run_pipeline()