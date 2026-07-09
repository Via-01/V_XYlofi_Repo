import streamlit as st
import pandas as pd
import plotly.graph_objects as go

from theme import inject_css, style_fig, page_header, ACCENT, DANGER
from utils import load_weekly_anomalies

# Configure the page.
st.set_page_config(
    page_title="Anomaly Report",
    page_icon="⚠️",
    layout="wide"
)

inject_css()

page_header(
    kicker="Page 3 · Anomaly Detection",
    title="⚠️ Weekly Sales Anomaly Report",
    subtitle="Unusual sales weeks flagged in the notebook using Isolation Forest anomaly detection.",
)

# ==========================================================
# LOAD PRECOMPUTED ANOMALIES (from the Colab notebook)
# ==========================================================


weekly_sales = load_weekly_anomalies()
weekly_sales = weekly_sales.set_index("Week")

anomalies = weekly_sales[weekly_sales["Isolation"]]

# ==========================================================
# KPI CARDS
# ==========================================================

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Total Weeks", len(weekly_sales))

with col2:
    st.metric("Detected Anomalies", len(anomalies))

with col3:
    st.metric("Anomaly Rate", f"{len(anomalies) / len(weekly_sales):.1%}")

st.write("")

# ==========================================================
# ANOMALY CHART
# ==========================================================

with st.container(border=True):

    fig = go.Figure()

    fig.add_trace(
        go.Scatter(
            x=weekly_sales.index,
            y=weekly_sales["Sales"],
            mode="lines",
            name="Weekly Sales",
            line=dict(color=ACCENT, width=2),
        )
    )

    fig.add_trace(
        go.Scatter(
            x=anomalies.index,
            y=anomalies["Sales"],
            mode="markers",
            marker=dict(
                size=11,
                color=DANGER,
                symbol="diamond",
                line=dict(width=2, color="#FFFFFF"),
            ),
            name="Anomaly",
        )
    )

    fig.update_layout(
        xaxis_title="Week",
        yaxis_title="Sales ($)",
        legend_title_text="",
    )

    style_fig(fig, height=460, title="Weekly Sales with Isolation Forest Anomalies Highlighted")

    st.plotly_chart(fig, use_container_width=True)

st.write("")

tcol, icol = st.columns([1.3, 1])

with tcol:
    with st.container(border=True):

        st.subheader("Detected Anomalies")

        table = anomalies.reset_index()

        table["Week"] = table["Week"].dt.strftime("%Y-%m-%d")

        table = table.rename(columns={"Sales": "Weekly Sales"})[["Week", "Weekly Sales"]]

        table["Weekly Sales"] = table["Weekly Sales"].map(lambda v: f"${v:,.2f}")

        st.dataframe(
            table,
            use_container_width=True,
            hide_index=True,
        )

with icol:
    with st.container(border=True):

        st.subheader("Business Interpretation")

        st.markdown(
            """
- **High** anomalies often align with promotional campaigns,
  festive periods, or seasonal demand spikes.
- **Low** anomalies may signal inventory shortages,
  operational disruptions, or reduced demand.
- Isolation Forest learns the overall structure of the sales
  distribution, so it flags both unusually high and unusually
  low weeks.
"""
        )

st.caption("Isolation Forest Anomaly Detection")
