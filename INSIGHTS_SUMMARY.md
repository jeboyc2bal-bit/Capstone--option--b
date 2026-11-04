# One-Page Insights Summary: Logistics, Delivery & Returns (Option B)

**Student:** Benjedick Christian T. Cristobal | **Course:** Python Programming Data Analyst, B04

## Business question
How well are we delivering, and what causes returns?

## Headline numbers

| Metric | Result |
|---|---|
| Orders analysed (after removing 75 duplicates) | 15,000 |
| Shipments delivered / in transit / returned to sender / lost | 77.9% / 18.0% / 3.1% / 1.1% |
| Average delivery lead time (Delivered shipments only) | 4.0 days (range 1-7) |
| Overall return rate | 8.0% (1,200 of 15,000 orders) |

## Top insights

1. **Delivery speed is consistent but not fast.** Delivered orders take 4.0 days on average, and all five couriers are within 0.06 days of each other, so speed does not separate them.
2. **18% of shipments are still "In Transit".** 2,468 of these 2,694 shipped before December 2025, which suggests statuses are not being updated rather than parcels actually on the road.
3. **J&T has the weakest delivery record.** It has the highest lost rate (1.25%), the highest returned-to-sender rate (3.58%) and the lowest delivered rate (76.6%). NinjaVan has the lowest lost rate (0.84%).
4. **About 70% of returns are controllable.** Defective, Missing Parts, Wrong Item, Damaged Item and Late Delivery account for 844 of 1,200 returns. Only Changed Mind and Size Issue (30%) are customer preference.
5. **Return rates differ only slightly.** NinjaVan (8.8%), J&T (8.6%) and GrabExpress (8.4%) are higher than LBC (7.1%) and 2GO (7.0%). Home & Kitchen (8.7%) is higher than Groceries (7.5%). These gaps are small and may be partly chance.
6. **Data quality is a finding too.** 3,149 non-delivered shipments carry a delivered date, 558 "Delivered" shipments have no date, and only 40 of 1,200 returned orders have the order status "Returned".

## Recommendations

1. **Reduce controllable returns.** Add pick-and-pack verification and a quick quality check on the products that appear most often in Defective, Missing Parts, Wrong Item and Damaged Item returns. Track the controllable-return share monthly, with a target such as a 20% reduction.
2. **Review courier performance and fix tracking data.** Hold a service review with J&T on lost and returned-to-sender shipments, and compare NinjaVan and J&T return rates with LBC and 2GO. Require shipment status and delivery date to be updated together, so "In Transit" and "Delivered" can be trusted.

## Method and limits
Data from 7 CSV files were cleaned in Python (duplicates removed, mixed dates and currency text converted, categories standardised, orphan keys flagged or removed; see `data/cleaned/cleaning_log.csv`). Lead time = delivered_date minus ship_date, counted only for shipments with status Delivered. Return rate = unique returned orders divided by total orders. The data are synthetic and many differences are small, so findings are indications, not proof.

**Full analysis:** `notebooks/capstone_option_b.ipynb` | **Dashboard:** `app/dashboard.py`
