import pandas as pd
import plotly.express as px
import streamlit as st


st.set_page_config(page_title="Logistics, Delivery & Returns", layout="wide")

BLUE = "#2563eb"
LIGHT_BLUE = "#93C5fd"
GREY = "#94a3b8"

def style_chart(fig, title, x_title, y_title):
    fig.update_layout(
        title=dict(text=title, font=dict(size=18), x=0, xanchor="left"),
        xaxis_title=x_title,
        yaxis_title=y_title,
        template="plotly_dark",
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font=dict(size=13),
        margin=dict(l=10, r=10, t=60, b=10),
        height=380,
        showlegend=False,
    )
    fig.update_xaxes(showgrid=False, linecolor=GREY)
    fig.update_yaxes(gridcolor="rgba(148, 163,184,0.2)", zeroline=False)
    return fig

shipment = pd.read_csv("C:/Users/Erkai/capstone-option-b/data/cleaned/cleaned_shipments.csv")
returns = pd.read_csv("C:/Users/Erkai/capstone-option-b/data/cleaned/cleaned_returns.csv")
items = pd.read_csv("C:/Users/Erkai/capstone-option-b/data/cleaned/cleaned_order_items.csv")
products = pd.read_csv("C:/Users/Erkai/capstone-option-b/data/cleaned/cleaned_products.csv")

st.title("Logistics, Delivery & Returns Dashboard")
st.caption("How well are we delivering, and what causes returns?")

st.sidebar.header("Filters")

couriers = sorted(shipment["courier"].unique())
chosen = st.sidebar.multiselect("Courier", couriers, default= couriers)

shipment_f = shipment[shipment["courier"].isin(chosen)]
order_ids = shipment_f["order_id"]
returns_f = returns[returns["order_id"].isin(order_ids)]

total_orders = shipment_f["order_id"].nunique()
pct_delivered = (shipment_f["shipment_status"] == "Delivered").mean() * 100
pct_lost = (shipment_f["shipment_status"] == "Lost").mean() * 100
avg_lead = shipment_f["lead_time_valid"].mean()
return_rate = returns_f["order_id"].nunique() / total_orders * 100

k1, k2, k3, k4, k5 = st.columns(5)
k1.metric("Orders shipped", f"{total_orders:,}")
k2.metric("% Delivered", f"{pct_delivered:.1f}%")
k3.metric("% Lost", f"{pct_lost:.1f}%")
k4.metric("Avg lead time", f"{avg_lead:.2f} days")
k5.metric("Return rate", f"{return_rate:.1f}%")

col1, col2 = st.columns(2)
lead = shipment_f.dropna(subset=["lead_time_valid"])

fig1 = px.box(lead, x="courier", y="lead_time_valid", color_discrete_sequence=[BLUE])
style_chart(fig1,  "Delivery time range by courier", "Courier", "Delivery time (days)")
col1.plotly_chart(fig1, width="stretch")

by_courier = (
        shipment_f.groupby("courier")["lead_time_valid"].mean().round(2).reset_index()
        .sort_values("lead_time_valid")
)
colors = [BLUE if i == 0 else LIGHT_BLUE for i in range(len(by_courier))]
fig2 = px.bar(by_courier, x="courier", y="lead_time_valid", text_auto=".2f")
fig2.update_traces(marker_color=colors, textposition="outside",
                    hovertemplate="%{x}: %{y:.2f} days<extra></extra>")
fig2.update_yaxes(range=[0, by_courier["lead_time_valid"].max() * 1.2])
style_chart(fig2, "Average delivery time by courier", "Courier", "Average delivery time (days)")
col2.plotly_chart(fig2, width="stretch")              

col3, col4 = st.columns(2)
reasons = returns_f["reason"].value_counts().reset_index()
reasons.columns = ["reason", "returns"]
fig3 = px.bar(reasons, x="returns", y="reason", orientation="h",
title="Top return reasons")
fig3.update_layout(yaxis={"categoryorder": "total ascending"})
col3.plotly_chart(fig3, width="stretch")
category = items.merge(products[["product_id", "category"]], on="product_id")
category = category[["order_id", "category"]].drop_duplicates()
category = category[category["order_id"].isin(order_ids)]
category["returned"] = category["order_id"].isin(returns_f["order_id"])
category_rate = (category.groupby("category")["returned"].mean() * 100).round(2).reset_index()
fig4 = px.bar(category_rate, x="returned", y="category", orientation="h",
title="Return rate by category (%)")
fig4.update_layout(yaxis={"categoryorder": "total ascending"})
col4.plotly_chart(fig4, width="stretch")


status = shipment_f["shipment_status"].value_counts().reset_index()
status.columns = ["status", "shipments"]
fig5 = px.pie(status, names="status", values="shipments",
title="Shipment status breakdown", hole=0.4)
st.plotly_chart(fig5, width="stretch")

st.subheader("Courier summary")
summary = (
    shipment_f.groupby("courier")
    .agg(
        Shipments=("order_id", "count"),
        Avg_days=("lead_time_valid", "mean"),
        Median_days=("lead_time_valid", "median"),
        Fastest=("lead_time_valid", "min"),
        Slowest=("lead_time_valid", "max"),
        Pct_lost=("shipment_status", lambda s: (s == "Lost").mean() * 100),
        )
        .round(2)
        .reset_index()
        .rename(columns={"courier": "Courier", "Avg_days": "Avg days",
                         "Median_days": "Median days", "Pct_lost": "% Lost"})
)
st.dataframe(summary,  width="stretch", hide_index=True)
