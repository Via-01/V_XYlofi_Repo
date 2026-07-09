"""
Shared visual theme for the Sales Forecasting dashboard.

Call `inject_css()` once near the top of every page, use `page_header()`
instead of st.title for a consistent branded header, and run every
Plotly figure through `style_fig()` so charts match the light off-white /
blue theme set in .streamlit/config.toml.
"""

import streamlit as st

# ---------------------------------------------------------------------------
# Palette — keep in sync with .streamlit/config.toml
# ---------------------------------------------------------------------------
BG = "#F5FEFD"  # app background (off-white, faint mint)
CARD_BG = "#FFFFFF"  # cards / secondary surfaces
CARD_BG_SOFT = "#F0F9F8"
BORDER = "#DCE7E5"
TEXT = "#0F172A"
MUTED_TEXT = "#5B6B79"
ACCENT = "#2563EB"  # primary blue
ACCENT_LIGHT = "#3B82F6"
ACCENT_CYAN = "#0891B2"  # secondary accent for sparks / highlights
SUCCESS = "#059669"
DANGER = "#DC2626"
WARNING = "#D97706"

COLOR_SEQUENCE = [
    "#0B3C8C",   # Navy
    "#1D4ED8",   # Blue 700
    "#2563EB",   # Blue 600
    "#3B82F6",   # Blue 500
    "#589DF1",   # Blue 400
    "#7BADE7",   # Blue 300
]

FONT_DISPLAY = "'Space Grotesk', 'Inter', sans-serif"
FONT_BODY = "'Inter', 'Segoe UI', sans-serif"
FONT_MONO = "'JetBrains Mono', 'SFMono-Regular', monospace"


def inject_css():
    """Call once near the top of every page."""
    st.markdown(
        f"""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@500;600;700&family=Inter:wght@400;500;600&family=JetBrains+Mono:wght@400;500;600&display=swap');

        html, body, [class*="css"] {{
            font-family: {FONT_BODY};
        }}

        h1 {{
            font-family: {FONT_DISPLAY};
            font-weight: 700 !important;
            letter-spacing: -0.02em;
        }}
        h2, h3 {{
            font-family: {FONT_DISPLAY};
            font-weight: 600 !important;
            letter-spacing: -0.01em;
            color: {TEXT};
        }}

        /* ---- Custom branded page header ---- */
        .dash-kicker {{
            font-family: {FONT_MONO};
            font-size: 0.72rem;
            font-weight: 500;
            letter-spacing: 0.18em;
            text-transform: uppercase;
            color: {ACCENT_CYAN};
            margin-bottom: 0.3rem;
        }}
        .dash-title-row {{
            display: flex;
            align-items: baseline;
            justify-content: space-between;
            flex-wrap: wrap;
            gap: 0.6rem;
        }}
        .dash-title {{
            font-family: {FONT_DISPLAY};
            font-size: 2.05rem;
            font-weight: 700;
            letter-spacing: -0.02em;
            color: {TEXT};
            margin: 0;
        }}
        .dash-subtitle {{
            font-family: {FONT_BODY};
            font-size: 0.95rem;
            color: {MUTED_TEXT};
            margin-top: 0.35rem;
            max-width: 62ch;
        }}
        .dash-badge {{
            font-family: {FONT_MONO};
            font-size: 0.72rem;
            color: {SUCCESS};
            background: rgba(5, 150, 105, 0.08);
            border: 1px solid rgba(5, 150, 105, 0.35);
            padding: 0.28rem 0.7rem;
            border-radius: 999px;
            white-space: nowrap;
        }}
        .dash-badge::before {{
            content: "●";
            margin-right: 0.4rem;
            color: {SUCCESS};
        }}
        .dash-rule {{
            height: 2px;
            border: none;
            margin: 1rem 0 1.6rem 0;
            background: linear-gradient(90deg, {ACCENT} 0%, {ACCENT_CYAN} 18%, {BORDER} 55%, transparent 100%);
            border-radius: 2px;
        }}

        /* ---- Section dividers used inline via st.markdown('---') ---- */
        hr {{
            border: none;
            height: 1px;
            background: linear-gradient(90deg, {BORDER} 0%, transparent 90%);
            margin: 1.5rem 0;
        }}

        /* ---- Metric cards ---- */
        div[data-testid="stMetric"] {{
            background: linear-gradient(160deg, {CARD_BG} 0%, {CARD_BG_SOFT} 100%);
            border: 1px solid {BORDER};
            border-left: 3px solid {ACCENT};
            border-radius: 12px;
            padding: 0.9rem 1.1rem;
            box-shadow: 0 2px 8px rgba(15, 23, 42, 0.05);
        }}
        div[data-testid="stMetric"] label {{
            font-family: {FONT_MONO};
            font-size: 0.7rem !important;
            letter-spacing: 0.08em;
            text-transform: uppercase;
            color: {MUTED_TEXT} !important;
        }}
        div[data-testid="stMetricValue"] {{
            font-family: {FONT_MONO};
            color: {ACCENT} !important;
            font-weight: 600 !important;
        }}

        /* ---- Bordered containers used as chart / content cards ---- */
        div[data-testid="stVerticalBlockBorderWrapper"] {{
            background: {CARD_BG};
            border: 1px solid {BORDER} !important;
            border-radius: 16px !important;
            padding: 0.4rem 0.2rem;
            box-shadow: 0 2px 12px rgba(15, 23, 42, 0.05);
        }}

        /* ---- Sidebar ---- */
        section[data-testid="stSidebar"] {{
            background: {CARD_BG_SOFT};
            border-right: 1px solid {BORDER};
        }}
        section[data-testid="stSidebar"] [data-testid="stMarkdownContainer"] p {{
            font-family: {FONT_MONO};
        }}

        /* ---- Inputs ---- */
        div[data-baseweb="select"] > div {{
            background-color: {CARD_BG} !important;
            border-radius: 10px !important;
            border-color: {BORDER} !important;
        }}
        div[data-testid="stSlider"] {{
            padding-top: 0.3rem;
        }}

        /* ---- Alerts ---- */
        div[data-testid="stAlert"] {{
            border-radius: 12px;
            border: 1px solid {BORDER};
        }}

        /* ---- Tables ---- */
        div[data-testid="stDataFrame"] {{
            border: 1px solid {BORDER};
            border-radius: 12px;
            overflow: hidden;
        }}

        /* ---- Expander ---- */
        details {{
            background: {CARD_BG};
            border: 1px solid {BORDER} !important;
            border-radius: 12px !important;
        }}
        summary {{
            font-family: {FONT_DISPLAY};
            font-weight: 600;
        }}

        /* ---- Scrollbar polish ---- */
        ::-webkit-scrollbar {{ width: 10px; height: 10px; }}
        ::-webkit-scrollbar-track {{ background: {BG}; }}
        ::-webkit-scrollbar-thumb {{ background: {BORDER}; border-radius: 8px; }}
        ::-webkit-scrollbar-thumb:hover {{ background: {ACCENT}; }}

        .block-container {{
            padding-top: 1rem;
            padding-bottom: 3rem;
        }}

        [data-testid="stHeader"]{{
            background: transparent;
        }}

        header{{
            background: transparent !important;
        }}
        </style>
        """,
        unsafe_allow_html=True,
    )


def page_header(
    kicker: str, title: str, subtitle: str = "", badge: str = "Data synced"
):
    """Branded header used at the top of every page in place of st.title()."""
    st.markdown(
        f"""
        <div class="dash-kicker">{kicker}</div>
        <div class="dash-title-row">
            <h1 class="dash-title">{title}</h1>
            <span class="dash-badge">{badge}</span>
        </div>
        {f'<div class="dash-subtitle">{subtitle}</div>' if subtitle else ''}
        <hr class="dash-rule" />
        """,
        unsafe_allow_html=True,
    )


def style_fig(fig, height=None, fill_line=False, title=None):
    """Apply the light/blue chart theme to any Plotly figure in place."""
    fig.update_layout(
        template="plotly_white",
        paper_bgcolor=CARD_BG,
        plot_bgcolor=CARD_BG,
        font=dict(color=TEXT, family="Inter, sans-serif"),
        title_font=dict(color=TEXT, size=17, family="Space Grotesk, sans-serif"),
        legend=dict(
            orientation="h",
            yanchor="top",
            y=-0.18,
            xanchor="center",
            x=0.5,
            bgcolor="rgba(0,0,0,0)",
            borderwidth=0,
            font=dict(size=12),
        ),
        margin=dict(t=75, l=20, r=20, b=70),
        colorway=COLOR_SEQUENCE,
        hoverlabel=dict(bgcolor=CARD_BG, font_color=TEXT, bordercolor=ACCENT),
        bargap=0.28,
    )
    if title:
        fig.update_layout(title=dict(text=title, x=0, xanchor="left"))
    fig.update_xaxes(
        gridcolor=BORDER, zerolinecolor=BORDER, showline=True, linecolor=BORDER
    )
    fig.update_yaxes(
        gridcolor=BORDER, zerolinecolor=BORDER, showline=True, linecolor=BORDER
    )
    if fill_line:
        fig.update_traces(
            selector=dict(type="scatter", mode="lines+markers"),
            line=dict(width=3),
            fill="tozeroy",
            fillcolor="rgba(37,99,235,0.10)",
        )
    if height:
        fig.update_layout(height=height)
    return fig
