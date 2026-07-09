import streamlit as st

from theme import inject_css, page_header

st.set_page_config(
    page_title="Superstore Sales Forecasting Dashboard",
    page_icon="📊",
    layout="wide"
)

inject_css()

page_header(
    kicker="Superstore Analytics · Internship Project",
    title="📊 Sales Forecasting & Demand Intelligence",
    subtitle=(
        "An end-to-end analytics workflow — forecasting, anomaly detection, "
        "and demand segmentation built on four years of Superstore sales data."
    ),
)

st.markdown(
    "Use the navigation menu on the left to explore each page of the dashboard."
)

st.write("")

nav1, nav2, nav3, nav4 = st.columns(4)

nav_cards = [
    (nav1, "📈", "Sales Overview", "Revenue by year, monthly trend, region & category filters."),
    (nav2, "🔮", "Forecast Explorer", "3-month XGBoost forecasts by category or region."),
    (nav3, "⚠️", "Anomaly Report", "Unusual sales weeks flagged by Isolation Forest."),
    (nav4, "📦", "Demand Segments", "K-Means clusters with recommended stocking strategy."),
]

for col, icon, title, desc in nav_cards:
    with col:
        with st.container(border=True):
            st.markdown(f"#### {icon} {title}")
            st.caption(desc)

st.write("")
st.write("")

col1, col2 = st.columns(2)

with col1:
    with st.container(border=True):
        st.markdown("##### ✔ Tasks Completed")
        st.markdown(
            "Data Exploration · Time Series Analysis · Forecasting · "
            "Segment Forecasting · Anomaly Detection · Product Clustering"
        )

with col2:
    with st.container(border=True):
        st.markdown("##### ⚙ Models Used")
        st.markdown(
            "SARIMA · Facebook Prophet · XGBoost · Isolation Forest · K-Means Clustering"
        )

st.write("")

st.caption(
    "Developed using Streamlit · XGBoost · Prophet · Scikit-Learn · Statsmodels"
)
