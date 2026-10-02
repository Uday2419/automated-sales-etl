from extract import extract_data
from transform import transform_data


RAW_FILE = "data/raw/sales.csv"
PROCESSED_FILE = "data/processed/clean_sales.csv"


def process_data():

    # Extract
    df = extract_data(RAW_FILE)

    # Transform
    df = transform_data(df)

    # Save processed data
    df.to_csv(
        PROCESSED_FILE,
        index=False
    )

    print(f"Processed data saved to: {PROCESSED_FILE}")
    print(f"Final records: {len(df)}")


if __name__ == "__main__":
    process_data()