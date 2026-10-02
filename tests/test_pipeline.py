import sys
from pathlib import Path

import pandas as pd

sys.path.append(str(Path(__file__).resolve().parents[1] / "src"))

from extract import extract_data
from transform import transform_data


RAW_FILE = "data/raw/sales.csv"


def get_data():
    df = extract_data(RAW_FILE)
    return transform_data(df)


def test_sales_not_null():
    df = get_data()

    assert df["sales"].notna().all()


def test_order_id_not_null():
    df = get_data()

    assert df["order_id"].notna().all()


def test_customer_id_not_null():
    df = get_data()

    assert df["customer_id"].notna().all()


def test_sales_positive():
    df = get_data()

    assert (df["sales"] >= 0).all()


def test_shipping_days_valid():
    df = get_data()

    assert (df["shipping_days"] >= 0).all()


def test_order_date_before_ship_date():
    df = get_data()

    assert (df["ship_date"] >= df["order_date"]).all()


def test_no_duplicate_rows():
    df = get_data()

    assert not df.duplicated().any()