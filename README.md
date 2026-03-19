# MarginFlow

![MarginFlow dashboard overview](assets/preview.png)

MarginFlow is an internal retail reporting dashboard for reviewing revenue quality, profit margin, discount pressure, and customer mix.

The project is intentionally small and focused. The goal was to build a clear reporting dashboard with useful summaries and a simple interface, without adding unnecessary complexity.

---

## Highlights

- Tracks revenue, profit, margin, and discount pressure in one compact dashboard
- Uses rule-based takeaways to surface what stands out in the filtered data
- Built as a practical internal analytics tool with Streamlit, Pandas, and Plotly

---

## What this dashboard helps answer

- Is revenue growing faster than profit?
- Are discounts helping sales volume but reducing margin quality?
- Which products generate strong revenue but weak profit?
- Are returning customers contributing more value than new customers?
- Which categories, regions, or channels need attention?

---

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

### Business Insights
- Quick Takeaways (rule-based insights)
- Low margin products  
- High discount impact products  
- Category performance  
- Region performance  

---

## Dashboard Views

![MarginFlow business analysis view](assets/analysis-view.png)

---

## Tech Stack

- Python  
- Streamlit  
- Pandas  
- Plotly  

---

## Project Structure

```
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

---

## How to Run

```bash
git clone https://github.com/SlavchoVlakeskiGit/marginflow.git
cd marginflow
pip install -r requirements.txt
py -m streamlit run app.py
```

---

## Dataset

The project uses a synthetic retail dataset with fields such as:

- order_date  
- order_id  
- product  
- category  
- region  
- sales_channel  
- units_sold  
- unit_price  
- discount_pct  
- revenue  
- cost  
- profit  
- customer_type  

The dataset is designed to be simple but realistic enough for meaningful analysis.

---

## Project notes

- Uses a synthetic retail dataset included in the repository for easy local setup
- Quick Takeaways are rule-based reporting insights, not machine learning
- The dashboard focuses on a compact internal reporting workflow rather than full BI platform features

---

## Future improvements

- CSV upload support  
- Export filtered results  
- Period-over-period comparison  
- Improved table styling  

---

## Example takeaways

Depending on the selected filters, the dashboard can surface observations such as:

- Revenue is increasing faster than profit, suggesting margin compression
- High-discount products are generating volume but underperforming on profit
- Returning customers have a higher average order value than new customers
- One region is contributing strong revenue with below-average margin

---

## Author

Built as a portfolio project to demonstrate practical analytics dashboard development with Python.
