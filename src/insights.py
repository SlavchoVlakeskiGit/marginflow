import pandas as pd


def low_margin_products(df: pd.DataFrame) -> pd.DataFrame:
    product_df = (
        df.groupby("product", as_index=False)
        .agg(
            revenue=("revenue", "sum"),
            profit=("profit", "sum"),
        )
    )

    product_df["profit_margin_pct"] = (
        (product_df["profit"] / product_df["revenue"]) * 100
    ).round(1)

    product_df = product_df.sort_values("profit_margin_pct", ascending=True).head(5)
    product_df["revenue"] = product_df["revenue"].round(2)
    product_df["profit"] = product_df["profit"].round(2)

    return product_df


def discount_impact_products(df: pd.DataFrame) -> pd.DataFrame:
    discount_df = (
        df.groupby("product", as_index=False)
        .agg(
            average_discount_pct=("discount_pct", "mean"),
            revenue=("revenue", "sum"),
            profit=("profit", "sum"),
        )
    )

    discount_df["profit_margin_pct"] = (
        (discount_df["profit"] / discount_df["revenue"]) * 100
    ).round(1)

    discount_df["average_discount_pct"] = (
        discount_df["average_discount_pct"] * 100
    ).round(1)

    discount_df = discount_df.sort_values(
        ["average_discount_pct", "profit_margin_pct"],
        ascending=[False, True],
    ).head(5)

    discount_df["revenue"] = discount_df["revenue"].round(2)
    discount_df["profit"] = discount_df["profit"].round(2)

    return discount_df


def category_performance(df: pd.DataFrame) -> pd.DataFrame:
    category_df = (
        df.groupby("category", as_index=False)
        .agg(
            revenue=("revenue", "sum"),
            profit=("profit", "sum"),
        )
    )

    category_df["profit_margin_pct"] = (
        (category_df["profit"] / category_df["revenue"]) * 100
    ).round(1)

    category_df = category_df.sort_values("profit", ascending=True)
    category_df["revenue"] = category_df["revenue"].round(2)
    category_df["profit"] = category_df["profit"].round(2)

    return category_df


def region_performance(df: pd.DataFrame) -> pd.DataFrame:
    region_df = (
        df.groupby("region", as_index=False)
        .agg(
            revenue=("revenue", "sum"),
            profit=("profit", "sum"),
        )
    )

    region_df["profit_margin_pct"] = (
        (region_df["profit"] / region_df["revenue"]) * 100
    ).round(1)

    region_df = region_df.sort_values("profit", ascending=True)
    region_df["revenue"] = region_df["revenue"].round(2)
    region_df["profit"] = region_df["profit"].round(2)

    return region_df


def build_quick_takeaways(df: pd.DataFrame) -> list[str]:
    takeaways: list[str] = []

    daily = (
        df.groupby("order_date", as_index=False)
        .agg(
            revenue=("revenue", "sum"),
            profit=("profit", "sum"),
        )
        .sort_values("order_date")
    )

    if len(daily) >= 2:
        first_half = daily.iloc[: len(daily) // 2]
        second_half = daily.iloc[len(daily) // 2 :]

        first_revenue = first_half["revenue"].sum()
        second_revenue = second_half["revenue"].sum()

        first_profit = first_half["profit"].sum()
        second_profit = second_half["profit"].sum()

        first_margin = (first_profit / first_revenue * 100) if first_revenue else 0
        second_margin = (second_profit / second_revenue * 100) if second_revenue else 0

        if second_revenue > first_revenue and second_margin < first_margin:
            takeaways.append(
                "Revenue is improving across the period, but profit margin is getting tighter."
            )

    customer_df = (
        df.groupby("customer_type", as_index=False)
        .agg(
            revenue=("revenue", "sum"),
            orders=("order_id", "nunique"),
        )
    )

    if {"New", "Returning"}.issubset(set(customer_df["customer_type"])):
        new_row = customer_df[customer_df["customer_type"] == "New"].iloc[0]
        returning_row = customer_df[customer_df["customer_type"] == "Returning"].iloc[0]

        new_aov = new_row["revenue"] / new_row["orders"] if new_row["orders"] else 0
        returning_aov = (
            returning_row["revenue"] / returning_row["orders"]
            if returning_row["orders"]
            else 0
        )

        if returning_aov > new_aov:
            takeaways.append(
                "Returning customers have a higher average order value than new customers."
            )

    product_discount_df = (
        df.groupby("product", as_index=False)
        .agg(
            average_discount_pct=("discount_pct", "mean"),
            revenue=("revenue", "sum"),
            profit=("profit", "sum"),
        )
    )

    product_discount_df["profit_margin_pct"] = (
        (product_discount_df["profit"] / product_discount_df["revenue"]) * 100
    )

    high_discount_low_margin = product_discount_df[
        (product_discount_df["average_discount_pct"] >= 0.15)
        & (product_discount_df["profit_margin_pct"] < 25)
    ]

    if not high_discount_low_margin.empty:
        takeaways.append(
            "Some discount-heavy products are bringing in sales while weakening profitability."
        )

    region_df = (
        df.groupby("region", as_index=False)
        .agg(
            revenue=("revenue", "sum"),
            profit=("profit", "sum"),
        )
    )

    region_df["profit_margin_pct"] = (
        (region_df["profit"] / region_df["revenue"]) * 100
    )

    overall_margin = (df["profit"].sum() / df["revenue"].sum() * 100) if df["revenue"].sum() else 0
    weak_regions = region_df[region_df["profit_margin_pct"] < overall_margin - 5]

    if not weak_regions.empty:
        weakest_region = weak_regions.sort_values("profit_margin_pct").iloc[0]["region"]
        takeaways.append(
            f"{weakest_region} is underperforming compared with the overall margin level."
        )

    if not takeaways:
        takeaways.append("Revenue and profit look fairly balanced for the current filter selection.")
        takeaways.append("No major outlier stands out immediately from the selected slice of data.")

    return takeaways[:4]