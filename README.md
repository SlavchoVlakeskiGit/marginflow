# MarginFlow

MarginFlow is a  internal-style dashboard for looking at retail performance with a focus on revenue quality, margin pressure, discount impact, and customer mix.

## What this dashboard helps answer

- Is revenue growing faster than profit?
- Are discounts helping sales volume but weakening margin quality?
- Which products bring in revenue but underperform on profit?
- Are returning customers contributing more value than new customers?
- Which categories, regions, or channels need attention?

## Features

### Overview KPIs
- Total Revenue
- Total Profit
- Average Order Value
- Profit Margin %
- Average Discount %

### Filters
- Date range
- Region
- Category
- Sales channel

### Visuals
- Revenue over time
- Profit over time
- Top products by revenue
- Top products by profit
- Revenue by customer type

### Business insights
- Quick Takeaways (rule-based insights)
- Low margin products
- High discount impact products
- Category performance
- Region performance

## Tech stack

- Python
- Streamlit
- Pandas
- Plotly

## Project structure

```text
marginflow/
├── app.py
├── requirements.txt
├── README.md
├── data/
│   └── retail_orders.csv
├── src/
│   ├── __init__.py
│   ├── data_loader.py
│   ├── metrics.py
│   ├── insights.py
│   └── charts.py
└── assets/
    ├── preview.png
    └── analysis-view.png
```

## Run locally

```bash
git clone https://github.com/SlavchoVlakeskiGit/marginflow.git
cd marginflow
pip install -r requirements.txt
py -m streamlit run app.py
```

## Dataset

The project uses a synthetic retail dataset included in the repo at `data/retail_orders.csv`.

Fields include:
- order date
- product
- category
- region
- sales channel
- units sold
- revenue
- cost
- profit
- customer type

## Possible next improvements

- CSV upload support
- export filtered results
- period-over-period comparison
- improved table styling
