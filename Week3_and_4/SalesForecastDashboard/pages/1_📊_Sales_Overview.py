import streamlit as st
import pandas as pd  # noqa: F401
import plotly.express as px

from utils import load_data, yearly_sales, monthly_sales
from theme import inject_css, style_fig, page_header

# Configure the page.
st.set_page_config(
    page_title="Sales Overview",
    page_icon="📊",
    layout="wide"
)

inject_css()

# Load the dataset.
df = load_data()

page_header(
    kicker="Page 1 · Overview",
    title="📊 Sales Overview Dashboard",
    subtitle="Explore sales performance using interactive charts and filters.",
)

# ===========================
# KPI SECTION
# ===========================

total_sales = df["Sales"].sum()
total_orders = len(df)
average_order = df["Sales"].mean()
years = df["Year"].nunique()

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Total Sales", f"${total_sales:,.2f}")

with col2:
    st.metric("Orders", f"{total_orders:,}")

with col3:
    st.metric("Average Order Value", f"${average_order:,.2f}")

with col4:
    st.metric("Years Covered", years)

st.write("")

# ===========================
# TOTAL SALES BY YEAR
# ===========================

with st.container(border=True):

    st.subheader("Total Sales by Year")

    year_df = yearly_sales(df)

    fig = px.bar(
        year_df,
        x="Year",
        y="Sales",
        text_auto=".2s",
        color="Sales",
        color_continuous_scale=[ "#93C5FD", "#60A5FA", "#3B82F6", "#2563EB","#1D4ED8","#0B3C8C",]
    )

    fig.update_layout(
        xaxis_title="Year",
        yaxis_title="Sales ($)",
        coloraxis_showscale=False
    )
    fig.update_traces(marker_line_width=0)
    style_fig(fig, height=380, title="Total Sales by Year")

    st.plotly_chart(fig, use_container_width=True)

st.write("")

# ===========================
# MONTHLY SALES TREND
# ===========================

with st.container(border=True):

    st.subheader("Monthly Sales Trend")

    month_df = monthly_sales(df)

    line_fig = px.line(
        month_df,
        x="Order Date",
        y="Sales",
        markers=True
    )

    line_fig.update_layout(
        xaxis_title="Month",
        yaxis_title="Sales ($)"
    )
    style_fig(line_fig, height=380, fill_line=True, title="Monthly Sales Trend (All Regions & Categories)")

    st.plotly_chart(line_fig, use_container_width=True)

st.write("")

# ===========================
# INTERACTIVE FILTERS
# ===========================

with st.container(border=True):

    st.subheader("Sales by Region and Category")

    left, right = st.columns(2)

    with left:

        selected_region = st.multiselect(
            "Select Region(s)",
            sorted(df["Region"].unique()),
            default=sorted(df["Region"].unique())
        )

    with right:

        selected_category = st.multiselect(
            "Select Category",
            sorted(df["Category"].unique()),
            default=sorted(df["Category"].unique())
        )

    filtered = df[
        (df["Region"].isin(selected_region))
        &
        (df["Category"].isin(selected_category))
    ]

    summary = (
        filtered.groupby(["Region", "Category"])["Sales"]
        .sum()
        .reset_index()
    )

    filtered_fig = px.bar(
    summary,
    x="Region",
    y="Sales",
    color="Category",
    barmode="group",
    text_auto=".2s",
    color_discrete_map={
        "Furniture": "#062F72",         # Dark Navy
        "Office Supplies": "#1A52C9",   # Medium Blue
        "Technology": "#5392DF",        # Light Blue
    },
)

    filtered_fig.update_layout(
        xaxis_title="Region",
        yaxis_title="Sales ($)",
        legend_title_text="Category"
    )
    filtered_fig.update_traces(marker_line_width=0)
    style_fig(filtered_fig, height=400, title="Sales by Region, Split by Category")

    st.plotly_chart(filtered_fig, use_container_width=True)

    with st.expander("View filtered data"):

        st.dataframe(
            filtered[
                [
                    "Order Date",
                    "Region",
                    "Category",
                    "Sub-Category",
                    "Sales"
                ]
            ],
            use_container_width=True,
            hide_index=True,
        )

st.caption("Interactive Sales Overview Dashboard")
