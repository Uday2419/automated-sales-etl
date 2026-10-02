import pandas as pd
from pathlib import Path


def extract_data(file_path):
    """
    Extract sales data from the raw CSV file.
    """

    file_path = Path(file_path)

    if not file_path.exists():
        raise FileNotFoundError(f"File not found: {file_path}")

    df = pd.read_csv(
        file_path,
        sep=";",
        encoding="cp1252"
    )

    print(f"Successfully extracted {len(df)} records.")
    print(f"Columns: {len(df.columns)}")

    return df


if __name__ == "__main__":

    file_path = "data/raw/sales.csv"

    df = extract_data(file_path)

    print("\nDataset shape:")
    print(df.shape)

    print("\nColumns:")
    print(df.columns.tolist())

    print("\nFirst 5 records:")
    print(df.head())