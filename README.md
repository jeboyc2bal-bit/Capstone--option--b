# Logistics, Delivery & Returns Insights (Capstone Option B)

**Student:** Benjedick Christian T. Cristobal | **Course:** Python Programming Data Analyst Professional Certificate, B04

## Business question
How well are we delivering, and what causes returns?

## Executive summary
- 7 retail tables (customers, products, orders, order items, payments, shipments, returns) were loaded, cleaned and documented in Python.
- Cleaning: removed duplicate customers, orders and order items, standardised categories and gender labels, converted mixed dates and currency text, and flagged or removed orphan keys.
- 77.9% of shipments were delivered, 18.0% are still in transit, 3.1% were returned to sender and 1.1% were lost.
- The average delivery lead time is 4.0 days (range 1-7) and is nearly identical across all 5 couriers.
- J&T has the highest lost rate (1.25%) and returned-to-sender rate (3.58%).
- The overall return rate is 8.0% (1,200 of 15,000 orders).
- About 70% of returns come from controllable causes: defective, missing parts, wrong item, damaged item and late delivery.
- Return rates are slightly higher for NinjaVan, J&T and Home & Kitchen, but the gaps are small.
- Data quality issue: many non-delivered shipments carry a delivered date, and many "In Transit" statuses look outdated.
- Recommendation 1: add quality and packing checks to reduce controllable returns.
- Recommendation 2: review J&T performance and require shipment status and delivery date to be updated together.

The full text is in [Executive_Summary.txt](Executive_Summary.txt), and a one-page version is in [INSIGHTS_SUMMARY.md](INSIGHTS_SUMMARY.md).

## What is in this repository

| Path | Description |
|------|-------------|
| `notebooks/capstone_option_b.ipynb` | The full analysis: loading, cleaning, cleaning log, metrics and charts |
| `data/raw/` | The 7 original synthetic CSV files (unchanged) |
| `data/cleaned/` | `cleaned_customers.csv`, `cleaned_products.csv` and the other cleaned tables, plus `cleaning_log.csv` |
| `charts/` | The 5 exported PNG charts |
| `app/dashboard.py` | The Streamlit dashboard, with a courier filter |
| `screenshots/` | Notebook and dashboard screenshots |
| `Executive_Summary.txt` | Executive summary (8-15 bullet lines) |
| `INSIGHTS_SUMMARY.md` | One-page insights summary |
| `requirements.txt` | Python packages needed to run the project |

## Charts

1. `charts/1_lead_time_distribution.png` - delivery lead time distribution
2. `charts/2_courier_comparison.png` - average lead time by courier
3. `charts/3_return_reasons.png` - top return reasons
4. `charts/4_return_rate_by_category.png` - return rate by product category
5. `charts/5_shipment_status.png` - shipment status breakdown

## How to run it yourself

1. Install the packages:
   ```
   pip install -r requirements.txt
   ```
2. Open the notebook and choose Kernel > Restart & Run All:
   ```
   jupyter notebook
   ```
   Then open `notebooks/capstone_option_b.ipynb`. Running it recreates the files in `data/cleaned/` and `charts/`.
3. Start the dashboard from the project folder:
   ```
   streamlit run app/dashboard.py
   ```

## Method in brief

- **Cleaning:** duplicates were defined by ID (same `customer_id` or `order_id` means the same record). Mixed date formats and currency text were converted. Blank values were filled, flagged or left blank depending on the column, and every decision is recorded in `data/cleaned/cleaning_log.csv`.
- **Lead time:** `delivered_date` minus `ship_date`, counted only for shipments with status Delivered, because some non-delivered shipments contain a delivered date.
- **Return rate:** unique returned orders divided by total orders.
- **Return rate by category:** an order counts once for each category it contains.

## Notes

- The data is synthetic and was created for training, so findings are indications and not proof.
- Many differences between couriers and categories are small and may be partly chance.
