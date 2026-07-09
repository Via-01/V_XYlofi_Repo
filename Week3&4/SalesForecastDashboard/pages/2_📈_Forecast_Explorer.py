import streamlit as st
import pandas as pd
import plotly.graph_objects as go

from utils import load_data
from theme import inject_css, style_fig, page_header

# Configure the page.
st.set_page_config(
    page_title="Forecast Explorer",
    page_icon="📈",
    layout="wide"
)

inject_css()

page_header(
    kicker="Page 2 · Forecasting",
    title="📈 Forecast Explorer",
    subtitle="Three-month sales forecasts, precomputed in the analysis notebook using the best-performing XGBoost model.",
)

df = load_data()

# ==========================================================
# LOAD PRECOMPUTED FORECASTS (from the Colab notebook)
# ==========================================================


@st.cache_data(show_spinner="Loading precomputed forecasts...")
def load_forecast_data():
    forecasts = pd.read_csv("dashboard_data/segment_forecasts.csv", parse_dates=["Date"])
    comparison = pd.read_csv("dashboard_data/model_comparison.csv")
    return forecasts, comparison


segment_forecasts, comparison_df = load_forecast_data()

available_segments = segment_forecasts["Segment"].unique()

category_options = sorted(
    c for c in df["Category"].unique() if c in available_segments
)
region_options = sorted(
    r for r in df["Region"].unique() if r in available_segments
)

# ==========================================================
# INPUTS
# ==========================================================

with st.container(border=True):

    in1, in2, in3 = st.columns(3)

    with in1:
        forecast_type = st.selectbox(
            "Forecast By",
            ["Category", "Region"]
        )

    options = category_options if forecast_type == "Category" else region_options

    with in2:
        selection = st.selectbox(
            f"Select {forecast_type}",
            options
        )

    with in3:
        forecast_horizon = st.slider(
            "Forecast Horizon (Months)",
            min_value=1,
            max_value=3,
            value=3
        )

    if forecast_type == "Region" and len(region_options) < df["Region"].nunique():
        st.caption(
            "Note: precomputed forecasts are only available for the regions and "
            "categories generated in Task 4 of the notebook (West, East, and all "
            "three product categories)."
        )

st.write("")

# ==========================================================
# HISTORICAL SALES (computed live — cheap, needs to stay filterable)
# ==========================================================

if forecast_type == "Category":
    data = df[df["Category"] == selection]
else:
    data = df[df["Region"] == selection]

monthly = (
    data.groupby("Order Date")["Sales"]
    .sum()
    .resample("ME")
    .sum()
    .to_frame(name="Sales")
)

segment_data = (
    segment_forecasts[segment_forecasts["Segment"] == selection]
    .sort_values("Date")
    .head(forecast_horizon)
)

future_dates = list(segment_data["Date"])
predictions = list(segment_data["Forecast"])

# ==========================================================
# PLOT
# ==========================================================

with st.container(border=True):

    fig = go.Figure()

    # Shade the forecast horizon so it reads as "projected" at a glance
    if future_dates:
        fig.add_vrect(
            x0=monthly.index[-1],
            x1=future_dates[-1],
            fillcolor="rgba(29,78,216,0.12)",
            opacity=0.06,
            line_width=0,
        )

    fig.add_trace(
        go.Scatter(
            x=monthly.index,
            y=monthly["Sales"],
            mode="lines+markers",
            name="Historical Sales",
            line=dict(color="#2563EB", width=3),
            marker=dict(size=6),
        )
    )

    if future_dates:
        # Connect the last historical point to the forecast so the line is continuous
        bridge_x = [monthly.index[-1]] + future_dates
        bridge_y = [monthly["Sales"].iloc[-1]] + predictions

        fig.add_trace(
            go.Scatter(
                x=bridge_x,
                y=bridge_y,
                mode="lines+markers",
                name="Forecast (XGBoost)",
                line=dict(color="#0B3C8C", width=4, dash="dash"),
                marker=dict(size=8, symbol="diamond"),
            )
        )

    fig.update_layout(
        xaxis_title="Month",
        yaxis_title="Sales ($)",
        legend_title_text="",
    )

    style_fig(fig, height=460, title=f"{selection} — Historical Sales vs. {forecast_horizon}-Month Forecast")

    st.plotly_chart(fig, use_container_width=True)

st.write("")

fcol, mcol = st.columns([1.3, 1])

with fcol:
    with st.container(border=True):

        st.subheader("Forecast Output")

        forecast_df = pd.DataFrame({
            "Forecast Month": [d.strftime("%b %Y") for d in future_dates],
            "Predicted Sales": [f"${p:,.2f}" for p in predictions],
        })

        st.dataframe(
            forecast_df,
            use_container_width=True,
            hide_index=True,
        )

with mcol:
    with st.container(border=True):

        st.subheader("Model Performance")

        best_row = comparison_df.loc[comparison_df["MAE"].idxmin()]

        st.metric("Best Model", best_row["Model"])

        m1, m2 = st.columns(2)
        with m1:
            st.metric("MAE", f"{best_row['MAE']:,.2f}")
        with m2:
            st.metric("RMSE", f"{best_row['RMSE']:,.2f}")

        with st.expander("Compare all models"):
            st.dataframe(
                comparison_df[["Model", "MAE", "RMSE", "MAPE (%)"]],
                use_container_width=True,
                hide_index=True,
            )

        st.info(
            f"{best_row['Model']} achieved the lowest error among all evaluated "
            "forecasting models and was selected for production forecasting.",
            icon="✅",
        )
