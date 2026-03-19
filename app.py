from pathlib import Path

import streamlit as st

from src.data_loader import load_orders


DATA_PATH = Path("data/retail_orders.csv")


st.set_page_config(
    page_title="MarginFlow",
    page_icon="📊",
    layout="wide",
)


def get_data():
    return load_orders(DATA_PATH)


def main() -> None:
    st.title("MarginFlow")
    st.caption(
        "A small internal dashboard for reviewing revenue, profit, discount pressure, and customer mix."
    )

    if not DATA_PATH.exists():
        st.error("Dataset not found. Make sure data/retail_orders.csv exists.")
        st.stop()

    df = get_data()

    st.subheader("Dataset preview")
    st.write(f"Loaded {len(df)} rows")
    st.dataframe(df, use_container_width=True, hide_index=True)

    st.subheader("Planned dashboard sections")
    st.markdown(
        """
- Overview KPI cards
- Quick Takeaways
- Revenue and profit trends
- Top products by revenue and profit
- Customer breakdown
- Areas to Watch
"""
    )


if __name__ == "__main__":
    main()