import pandas as pd
import plotly.express as px


def revenue_over_time_chart(df: pd.DataFrame):
    daily = (
        df.groupby("order_date", as_index=False)["revenue"]
        .sum()
        .sort_values("order_date")
    )

    fig = px.line(
        daily,
        x="order_date",
        y="revenue",
        title="Revenue Over Time",
        markers=True,
    )

    fig.update_layout(
        margin=dict(l=20, r=20, t=50, b=20),
        xaxis_title="Date",
        yaxis_title="Revenue",
    )

    return fig


def profit_over_time_chart(df: pd.DataFrame):
    daily = (
        df.groupby("order_date", as_index=False)["profit"]
        .sum()
        .sort_values("order_date")
    )

    fig = px.line(
        daily,
        x="order_date",
        y="profit",
        title="Profit Over Time",
        markers=True,
    )

    fig.update_layout(
        margin=dict(l=20, r=20, t=50, b=20),
        xaxis_title="Date",
        yaxis_title="Profit",
    )

    return fig


def top_products_revenue_chart(df: pd.DataFrame):
    product_df = (
        df.groupby("product", as_index=False)["revenue"]
        .sum()
        .sort_values("revenue", ascending=False)
        .head(8)
    )

    fig = px.bar(
        product_df,
        x="revenue",
        y="product",
        orientation="h",
        title="Top Products by Revenue",
    )

    fig.update_layout(
        margin=dict(l=20, r=20, t=50, b=20),
        xaxis_title="Revenue",
        yaxis_title="Product",
        yaxis=dict(categoryorder="total ascending"),
    )

    return fig


def top_products_profit_chart(df: pd.DataFrame):
    product_df = (
        df.groupby("product", as_index=False)["profit"]
        .sum()
        .sort_values("profit", ascending=False)
        .head(8)
    )

    fig = px.bar(
        product_df,
        x="profit",
        y="product",
        orientation="h",
        title="Top Products by Profit",
    )

    fig.update_layout(
        margin=dict(l=20, r=20, t=50, b=20),
        xaxis_title="Profit",
        yaxis_title="Product",
        yaxis=dict(categoryorder="total ascending"),
    )

    return fig


def customer_type_revenue_chart(customer_df: pd.DataFrame):
    fig = px.bar(
        customer_df,
        x="customer_type",
        y="revenue",
        title="Revenue by Customer Type",
    )

    fig.update_layout(
        margin=dict(l=20, r=20, t=50, b=20),
        xaxis_title="Customer Type",
        yaxis_title="Revenue",
        showlegend=False,
    )

    return fig