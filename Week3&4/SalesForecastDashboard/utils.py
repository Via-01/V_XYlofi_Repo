import streamlit as st
import pandas as pd


def get_season(month):
    if month in [12, 1, 2]:
        return "Winter"
    elif month in [3, 4, 5]:
        return "Spring"
    elif month in [6, 7, 8]:
        return "Summer"
    else:
        return "Autumn"


@st.cache_data(show_spinner="Loading and preparing sales data...")
def load_data():

    df = pd.read_csv("dashboard_data/train.csv")

    # The source file stores dates as DD/MM/YYYY (e.g. "08/11/2017" = 8 Nov
    # 2017). read_csv's parse_dates can silently leave these as plain
    # strings instead of raising when the format is ambiguous, so dates are
    # parsed explicitly here with dayfirst=True — matching the notebook.
    df["Order Date"] = pd.to_datetime(df["Order Date"], dayfirst=True)
    df["Ship Date"] = pd.to_datetime(df["Ship Date"], dayfirst=True)

    # Missing postal code fix
    df.loc[
        (df["City"] == "Burlington") &
        (df["State"] == "Vermont"),
        "Postal Code"
    ] = 5401

    df["Postal Code"] = df["Postal Code"].astype(int)

    df["Year"] = df["Order Date"].dt.year
    df["Month"] = df["Order Date"].dt.month_name()
    df["Month Number"] = df["Order Date"].dt.month
    df["Quarter"] = df["Order Date"].dt.quarter
    df["Season"] = df["Month Number"].apply(get_season)

    return df


def yearly_sales(df):

    return (
        df.groupby("Year")["Sales"]
        .sum()
        .reset_index()
    )


def monthly_sales(df):

    return (
        df.groupby(pd.Grouper(
            key="Order Date",
            freq="ME"
        ))["Sales"]
        .sum()
        .reset_index()
    )


def weekly_sales(df):

    return (
        df.groupby(pd.Grouper(
            key="Order Date",
            freq="W"
        ))["Sales"]
        .sum()
        .reset_index()
    )


# ---------------------------------------------------------------------------
# Precomputed results exported from the Colab notebook (see
# export_dashboard_data.py). These live in dashboard_data/ at the project
# root and are read directly instead of retraining models in the app.
# ---------------------------------------------------------------------------

DASHBOARD_DATA_DIR = "dashboard_data"


def _require_precomputed(filename):
    import os
    path = os.path.join(DASHBOARD_DATA_DIR, filename)
    if not os.path.exists(path):
        st.error(
            f"Missing `{path}`. Run the export cell at the end of the "
            f"analysis notebook and place the resulting `{DASHBOARD_DATA_DIR}/` "
            f"folder next to `train.csv` in this project."
        )
        st.stop()
    return path


@st.cache_data(show_spinner="Loading model comparison...")
def load_model_comparison():
    path = _require_precomputed("model_comparison.csv")
    return pd.read_csv(path)


@st.cache_data(show_spinner="Loading segment forecasts...")
def load_segment_forecasts():
    path = _require_precomputed("segment_forecasts.csv")
    df = pd.read_csv(path, parse_dates=["Date"])
    return df


@st.cache_data(show_spinner="Loading anomaly report...")
def load_weekly_anomalies():
    path = _require_precomputed("weekly_anomalies.csv")
    df = pd.read_csv(path, parse_dates=["Week"])
    df["Isolation"] = df["Isolation"].astype(bool)
    return df


@st.cache_data(show_spinner="Loading demand clusters...")
def load_demand_clusters():
    path = _require_precomputed("demand_clusters.csv")
    return pd.read_csv(path)