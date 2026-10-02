import sys
from pathlib import Path

import pandas as pd

sys.path.append(str(Path(__file__).resolve().parents[1] / "src"))

from extract import extract_data
from transform import transform_data


RAW_FILE = "data/raw/sales.csv"


def get_transformed_data():
    df = extract_data(RAW_FILE)
    return transform_data(df)


def test_required_columns_exist():
    df = get_transformed_data()

    required_columns = [
        "row_id",
        "order_id",
        "order_date",
        "ship_date",
        "customer_id",
        "customer_name",
        "sales",
        "category",
        "region",
    ]

    for column in required_columns:
        assert column in df.columns


def test_order_id_not_null():
    df = get_transformed_data()

    assert df["order_id"].notna().all()


def test_sales_is_numeric():
    df = get_transformed_data()

    assert pd.api.types.is_numeric_dtype(df["sales"])


def test_sales_not_negative():
    df = get_transformed_data()

    assert (df["sales"] >= 0).all()


def test_order_dates_are_valid():
    df = get_transformed_data()

    assert df["order_date"].notna().all()


def test_no_duplicate_rows():
    df = get_transformed_data()

    assert not df.duplicated().any()