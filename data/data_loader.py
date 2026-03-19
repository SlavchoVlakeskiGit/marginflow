from pathlib import Path

import pandas as pd


def load_orders(file_path: str | Path) -> pd.DataFrame:
    df = pd.read_csv(file_path, parse_dates=["order_date"])

    numeric_columns = [
        "units_sold",
        "unit_price",
        "discount_pct",
        "revenue",
        "cost",
        "profit",
    ]

    for column in numeric_columns:
        df[column] = pd.to_numeric(df[column], errors="coerce")

    df = df.dropna(subset=["order_date", "order_id", "product", "revenue", "profit"])
    df = df.sort_values("order_date").reset_index(drop=True)

    return df