from pathlib import Path

import streamlit as st

from src.charts import (
    customer_type_revenue_chart,
    profit_over_time_chart,
    revenue_over_time_chart,
    top_products_profit_chart,
    top_products_revenue_chart,
)
from src.data_loader import load_orders
from src.insights import (
    build_quick_takeaways,
    category_performance,
    discount_impact_products,
    low_margin_products,
    region_performance,
)
from src.metrics import calculate_kpis, customer_breakdown


DATA_PATH = Path("data/retail_orders.csv")


st.set_page_config(
    page_title="MarginFlow",
    page_icon="📊",
    layout="wide",
)


def get_data():
    return load_orders(DATA_PATH)


def format_currency_columns(df, columns):
    formatted_df = df.copy()
    for column in columns:
        if column in formatted_df.columns:
            formatted_df[column] = formatted_df[column].map(lambda x: f"€{x:,.2f}")
    return formatted_df


def format_percent_columns(df, columns):
    formatted_df = df.copy()
    for column in columns:
        if column in formatted_df.columns:
            formatted_df[column] = formatted_df[column].map(lambda x: f"{x:.1f}%")
    return formatted_df


def main() -> None:
    st.title("MarginFlow")
    st.caption(
        "A small internal dashboard for reviewing revenue, profit, discount pressure, and customer mix."
    )

    if not DATA_PATH.exists():
        st.error("Dataset not found. Make sure data/retail_orders.csv exists.")
        st.stop()

    df = get_data()

    st.sidebar.header("Filters")

    min_date = df["order_date"].min().date()
    max_date = df["order_date"].max().date()

    date_range = st.sidebar.date_input(
        "Date range",
        value=(min_date, max_date),
        min_value=min_date,
        max_value=max_date,
    )

    selected_regions = st.sidebar.multiselect(
        "Region",
        options=sorted(df["region"].unique()),
        default=sorted(df["region"].unique()),
    )

    selected_categories = st.sidebar.multiselect(
        "Category",
        options=sorted(df["category"].unique()),
        default=sorted(df["category"].unique()),
    )

    selected_channels = st.sidebar.multiselect(
        "Sales channel",
        options=sorted(df["sales_channel"].unique()),
        default=sorted(df["sales_channel"].unique()),
    )

    filtered_df = df.copy()

    if isinstance(date_range, tuple) and len(date_range) == 2:
        start_date, end_date = date_range
        filtered_df = filtered_df[
            filtered_df["order_date"].dt.date.between(start_date, end_date)
        ]

    filtered_df = filtered_df[
        filtered_df["region"].isin(selected_regions)
        & filtered_df["category"].isin(selected_categories)
        & filtered_df["sales_channel"].isin(selected_channels)
    ]

    if filtered_df.empty:
        st.warning("No data matches the selected filters.")
        st.stop()

    kpis = calculate_kpis(filtered_df)

    st.subheader("Overview")
    kpi_col1, kpi_col2, kpi_col3, kpi_col4, kpi_col5 = st.columns(5)

    kpi_col1.metric("Total Revenue", f"€{kpis['total_revenue']:,.2f}")
    kpi_col2.metric("Total Profit", f"€{kpis['total_profit']:,.2f}")
    kpi_col3.metric("Average Order Value", f"€{kpis['average_order_value']:,.2f}")
    kpi_col4.metric("Profit Margin", f"{kpis['profit_margin_pct']:.1f}%")
    kpi_col5.metric("Average Discount", f"{kpis['average_discount_pct']:.1f}%")

    st.subheader("Quick Takeaways")
    takeaways = build_quick_takeaways(filtered_df)

    takeaway_col1, takeaway_col2 = st.columns(2)
    takeaway_columns = [takeaway_col1, takeaway_col2]

    for index, takeaway in enumerate(takeaways):
        with takeaway_columns[index % 2]:
            st.info(takeaway)

    st.subheader("Performance Trends")
    trend_col1, trend_col2 = st.columns(2)

    with trend_col1:
        st.plotly_chart(
            revenue_over_time_chart(filtered_df),
            use_container_width=True,
        )

    with trend_col2:
        st.plotly_chart(
            profit_over_time_chart(filtered_df),
            use_container_width=True,
        )

    st.subheader("Top Products")
    product_col1, product_col2 = st.columns(2)

    with product_col1:
        st.plotly_chart(
            top_products_revenue_chart(filtered_df),
            use_container_width=True,
        )

    with product_col2:
        st.plotly_chart(
            top_products_profit_chart(filtered_df),
            use_container_width=True,
        )

    st.subheader("Customer Breakdown")
    customer_stats = customer_breakdown(filtered_df)

    customer_col1, customer_col2 = st.columns([1.2, 1])

    with customer_col1:
        customer_display = format_currency_columns(
            customer_stats,
            ["revenue", "profit", "average_order_value"],
        )
        customer_display = format_percent_columns(
            customer_display,
            ["profit_margin_pct"],
        )
        st.dataframe(customer_display, use_container_width=True, hide_index=True)

    with customer_col2:
        st.plotly_chart(
            customer_type_revenue_chart(customer_stats),
            use_container_width=True,
        )

    st.subheader("Areas to Watch")
    attention_col1, attention_col2 = st.columns(2)

    with attention_col1:
        st.markdown("**Low Margin Products**")
        low_margin_display = format_currency_columns(
            low_margin_products(filtered_df),
            ["revenue", "profit"],
        )
        low_margin_display = format_percent_columns(
            low_margin_display,
            ["profit_margin_pct"],
        )
        st.dataframe(low_margin_display, use_container_width=True, hide_index=True)

        st.markdown("**High Discount Impact**")
        discount_display = format_currency_columns(
            discount_impact_products(filtered_df),
            ["revenue", "profit"],
        )
        discount_display = format_percent_columns(
            discount_display,
            ["average_discount_pct", "profit_margin_pct"],
        )
        st.dataframe(discount_display, use_container_width=True, hide_index=True)

    with attention_col2:
        st.markdown("**Category Performance**")
        category_display = format_currency_columns(
            category_performance(filtered_df),
            ["revenue", "profit"],
        )
        category_display = format_percent_columns(
            category_display,
            ["profit_margin_pct"],
        )
        st.dataframe(category_display, use_container_width=True, hide_index=True)

        st.markdown("**Region Performance**")
        region_display = format_currency_columns(
            region_performance(filtered_df),
            ["revenue", "profit"],
        )
        region_display = format_percent_columns(
            region_display,
            ["profit_margin_pct"],
        )
        st.dataframe(region_display, use_container_width=True, hide_index=True)

    with st.expander("Preview filtered data"):
        st.dataframe(filtered_df, use_container_width=True, hide_index=True)


if __name__ == "__main__":
    main()