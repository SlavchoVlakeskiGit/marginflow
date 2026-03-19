import pandas as pd


def calculate_profit_margin(df: pd.DataFrame) -> float:
    revenue = df["revenue"].sum()
    if revenue == 0:
        return 0.0
    return (df["profit"].sum() / revenue) * 100


def calculate_kpis(df: pd.DataFrame) -> dict:
    total_revenue = df["revenue"].sum()
    total_profit = df["profit"].sum()
    order_count = df["order_id"].nunique()

    average_order_value = total_revenue / order_count if order_count else 0.0
    profit_margin_pct = calculate_profit_margin(df)
    average_discount_pct = df["discount_pct"].mean() * 100 if not df.empty else 0.0

    return {
        "total_revenue": total_revenue,
        "total_profit": total_profit,
        "average_order_value": average_order_value,
        "profit_margin_pct": profit_margin_pct,
        "average_discount_pct": average_discount_pct,
    }


def customer_breakdown(df: pd.DataFrame) -> pd.DataFrame:
    customer_df = (
        df.groupby("customer_type", as_index=False)
        .agg(
            orders=("order_id", "nunique"),
            revenue=("revenue", "sum"),
            profit=("profit", "sum"),
        )
        .sort_values("revenue", ascending=False)
    )

    customer_df["average_order_value"] = (
        customer_df["revenue"] / customer_df["orders"]
    ).round(2)

    customer_df["profit_margin_pct"] = (
        (customer_df["profit"] / customer_df["revenue"]) * 100
    ).round(1)

    customer_df["revenue"] = customer_df["revenue"].round(2)
    customer_df["profit"] = customer_df["profit"].round(2)

    return customer_df