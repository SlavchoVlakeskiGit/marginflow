# MarginFlow

MarginFlow is a small internal-style dashboard for looking at retail performance with a focus on revenue quality, margin pressure, discount impact, and customer mix.

I mainly wanted this project to feel more like a practical business tool than a typical dashboard demo.

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

## Why I built it

I wanted one project in the portfolio that sits between data work and a simple business-facing UI. A lot of dashboards look polished but do not really say much, so I tried to make this one more readable and a bit closer to something an internal team might actually use.

I ended up reworking the charts a couple of times to keep them readable instead of just adding more of them.

The synthetic dataset ended up being useful here because it let me shape the metrics around realistic sales questions without making local setup annoying.

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

## Notes

Quick Takeaways are rule-based, not machine learning. I kept that part simple on purpose because I wanted the dashboard to explain the data clearly rather than pretend to be smarter than it is.

## Possible next improvements

- CSV upload support
- export filtered results
- period-over-period comparison
- improved table styling
