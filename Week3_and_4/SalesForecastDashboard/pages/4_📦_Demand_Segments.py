import streamlit as st
import pandas as pd
import plotly.express as px

from theme import inject_css, style_fig, page_header
from utils import load_demand_clusters

# Configure the page.
st.set_page_config(
    page_title="Product Demand Segments",
    page_icon="📦",
    layout="wide"
)

inject_css()

page_header(
    kicker="Page 4 · Segmentation",
    title="📦 Product Demand Segmentation",
    subtitle="Sub-category clusters, precomputed in the notebook using K-Means on standardized demand features.",
)

# ==========================================================
# LOAD PRECOMPUTED CLUSTERS (from the Colab notebook)
# ==========================================================

cluster_df = load_demand_clusters()

# ==========================================================
# CLUSTER PLOT (PCA-reduced)
# ==========================================================

fig = px.scatter(
    cluster_df,
    x="PC1",
    y="PC2",
    color="Demand Segment",
    color_discrete_map={
        "Premium High-Value Products": "#1C2F4D",
        "High Volume, Stable Demand": "#3976F8",
        "Growing Demand": "#8DBCF5",
        "Low Volume, Stable Demand": "#4A678B",
    },
    hover_name="Sub-Category",
    text="Sub-Category",
)

fig.update_traces(
    textposition="top center",
    marker=dict(size=11, line=dict(width=1, color="#FFFFFF")),
)
fig.update_layout(
    xaxis_title="Principal Component 1",
    yaxis_title="Principal Component 2",
    legend_title_text="Demand Segment",
     xaxis=dict(
        range=[cluster_df["PC1"].min() - 0.6,
               cluster_df["PC1"].max() + 0.6]
    ),

    yaxis=dict(
        range=[cluster_df["PC2"].min() - 0.6,
               cluster_df["PC2"].max() + 0.6]
    ),
)
style_fig(fig, height=560, title="Sub-Category Clusters (PCA-Reduced Feature Space)")

with st.container(border=True):
    st.plotly_chart(
        fig,
        use_container_width=True
    )

st.write("")

# ==========================================================
# CLUSTER TABLE
# ==========================================================

st.subheader("Demand Segments")

display = cluster_df[
    [
        "Sub-Category",
        "Demand Segment",
        "Total Sales",
        "Growth Rate",
        "Volatility",
        "Average Order Value"
    ]
].sort_values("Demand Segment")

with st.container(border=True):
    st.dataframe(
        display,
        use_container_width=True,
        hide_index=True,
    )

st.write("")

# ==========================================================
# STOCKING STRATEGY
# ==========================================================

st.subheader("Recommended Stocking Strategy")

strategies = pd.DataFrame({
    "Demand Segment": [
        "Premium High-Value Products",
        "High Volume, Stable Demand",
        "Low Volume, Stable Demand",
        "Growing Demand"
    ],
    "Recommended Strategy": [
        "Maintain moderate inventory and closely monitor demand to minimize holding costs while ensuring product availability.",
        "Maintain higher inventory levels with frequent replenishment to prevent stock-outs.",
        "Use routine replenishment with steady inventory levels due to predictable demand.",
        "Gradually increase inventory while monitoring demand growth to avoid shortages."
    ]
})

with st.container(border=True):
    st.dataframe(
        strategies,
        use_container_width=True,
        hide_index=True,
    )

st.write("")

st.success(
    "K-Means clustering provides actionable demand segments that support inventory planning and stock optimization."
)
