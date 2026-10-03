import pandas as pd


def test_sales_data_has_required_columns():

    df = pd.read_csv("data/processed/clean_sales.csv")

    required_columns = [
        "row_id",
        "order_id",
        "order_date",
        "ship_date",
        "customer_id",
        "product_id",
        "sales"
    ]

    for column in required_columns:
        assert column in df.columns


def test_row_id_is_unique():

    df = pd.read_csv("data/processed/clean_sales.csv")

    assert df["row_id"].is_unique


def test_sales_values_are_positive():

    df = pd.read_csv("data/processed/clean_sales.csv")

    assert (df["sales"] >= 0).all()