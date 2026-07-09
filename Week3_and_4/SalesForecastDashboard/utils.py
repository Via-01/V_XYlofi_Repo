from pathlib import Path

import pandas as pd
import streamlit as st

# ============================================================================
# Base project paths
# ============================================================================

BASE_DIR = Path(__file__).resolve().parent
DASHBOARD_DATA_DIR = BASE_DIR / "dashboard_data"


# ============================================================================
# Helper functions
# ============================================================================

def get_season(month):
    if month in [12, 1, 2]:
        return "Winter"
    elif month in [3, 4, 5]:
        return "Spring"
    elif month in [6, 7, 8]:
        return "Summer"
    else:
        return "Autumn"


# ============================================================================
# Main dataset
# ============================================================================

@st.cache_data(show_spinner="Loading and preparing sales data...")
def load_data():

    csv_path = BASE_DIR / "train.csv"

    if not csv_path.exists():
        st.error(f"Dataset not found:\n{csv_path}")
        st.stop()

    df = pd.read_csv(csv_path)

    # The source file stores dates as DD/MM/YYYY
    df["Order Date"] = pd.to_datetime(
        df["Order Date"],
        dayfirst=True
    )

    df["Ship Date"] = pd.to_datetime(
        df["Ship Date"],
        dayfirst=True
    )

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


# ============================================================================
# Aggregation helpers
# ============================================================================

def yearly_sales(df):

    return (
        df.groupby("Year")["Sales"]
        .sum()
        .reset_index()
    )


def monthly_sales(df):

    return (
        df.groupby(
            pd.Grouper(
                key="Order Date",
                freq="ME"
            )
        )["Sales"]
        .sum()
        .reset_index()
    )


def weekly_sales(df):

    return (
        df.groupby(
            pd.Grouper(
                key="Order Date",
                freq="W"
            )
        )["Sales"]
        .sum()
        .reset_index()
    )


# ============================================================================
# Dashboard CSV loaders
# ============================================================================

def _require_precomputed(filename):

    path = DASHBOARD_DATA_DIR / filename

    if not path.exists():
        st.error(
            f"Missing file:\n\n{path}\n\n"
            "Please ensure the dashboard_data folder is included "
            "with the deployed application."
        )
        st.stop()

    return path


@st.cache_data(show_spinner="Loading model comparison...")
def load_model_comparison():
    return pd.read_csv(
        _require_precomputed("model_comparison.csv")
    )


@st.cache_data(show_spinner="Loading segment forecasts...")
def load_segment_forecasts():

    return pd.read_csv(
        _require_precomputed("segment_forecasts.csv"),
        parse_dates=["Date"]
    )


@st.cache_data(show_spinner="Loading anomaly report...")
def load_weekly_anomalies():

    df = pd.read_csv(
        _require_precomputed("weekly_anomalies.csv"),
        parse_dates=["Week"]
    )

    df["Isolation"] = df["Isolation"].astype(bool)

    return df


@st.cache_data(show_spinner="Loading demand clusters...")
def load_demand_clusters():

    return pd.read_csv(
        _require_precomputed("demand_clusters.csv")
    )
