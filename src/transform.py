import pandas as pd


def transform_data(df):
    """
    Clean and transform raw sales data.
    """

    df = df.copy()

    # 1. Clean column names
    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
        .str.replace(" ", "_")
        .str.replace("-", "_")
        .str.replace("&", "and")
    )

    # 2. Remove duplicate rows
    before_duplicates = len(df)

    df = df.drop_duplicates()

    duplicates_removed = before_duplicates - len(df)

    # 3. Convert order date to datetime
    df["order_date"] = pd.to_datetime(
        df["order_date"],
        dayfirst=True,
        errors="coerce"
    )

    # 4. Convert ship date to datetime
    df["ship_date"] = pd.to_datetime(
        df["ship_date"],
        dayfirst=True,
        errors="coerce"
    )

    # 5. Clean sales column
    df["sales"] = (
        df["sales"]
        .astype(str)
        .str.replace("$", "", regex=False)
        .str.replace(",", "", regex=False)
        .str.strip()
    )

    df["sales"] = pd.to_numeric(
        df["sales"],
        errors="coerce"
    )

    # 6. Remove records with invalid sales
    df = df.dropna(subset=["sales"])

    # 7. Handle missing values
    df["postal_code"] = df["postal_code"].fillna(0)

    # 8. Create useful date columns
    df["order_year"] = df["order_date"].dt.year
    df["order_month"] = df["order_date"].dt.month
    df["order_month_name"] = df["order_date"].dt.month_name()

    # 9. Calculate shipping days
    df["shipping_days"] = (
        df["ship_date"] - df["order_date"]
    ).dt.days

    print(f"Duplicates removed: {duplicates_removed}")
    print(f"Records after transformation: {len(df)}")

    return df


if __name__ == "__main__":

    from extract import extract_data

    input_file = "data/raw/sales.csv"

    df = extract_data(input_file)

    transformed_df = transform_data(df)

    print("\nTransformed columns:")
    print(transformed_df.columns.tolist())

    print("\nData types:")
    print(transformed_df.dtypes)

    print("\nFirst 5 transformed records:")
    print(transformed_df.head())