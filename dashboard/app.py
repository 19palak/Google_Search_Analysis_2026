import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from pathlib import Path


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="Google Search Trends India 2026",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown(
    """
    <style>

    .main {
        background-color: #f8fafc;
    }

    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
    }

    .main-title {
        font-size: 42px;
        font-weight: 700;
        margin-bottom: 5px;
    }

    .subtitle {
        font-size: 18px;
        color: #64748b;
        margin-bottom: 30px;
    }

    .section-title {
        font-size: 28px;
        font-weight: 650;
        margin-top: 20px;
        margin-bottom: 15px;
    }

    .metric-card {
        background-color: white;
        padding: 20px;
        border-radius: 12px;
        border: 1px solid #e2e8f0;
        box-shadow: 0 2px 8px rgba(0,0,0,0.04);
    }

    .footer {
        text-align: center;
        color: #64748b;
        padding: 30px;
        font-size: 14px;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# ============================================================
# PROJECT PATHS
# ============================================================

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data" / "raw"


# ============================================================
# LOAD DATA
# ============================================================

@st.cache_data
def load_data():

    multi_df = pd.read_csv(
        DATA_DIR / "multi_keyword_india_2026.csv"
    )

    chatgpt_df = pd.read_csv(
        DATA_DIR / "chatgpt_india_2026.csv"
    )

    trending_df = pd.read_csv(
        DATA_DIR / "trending_now_india_2026.csv"
    )

    return multi_df, chatgpt_df, trending_df


multi_df, chatgpt_df, trending_df = load_data()


# ============================================================
# CLEAN MULTI-KEYWORD DATA
# ============================================================

multi_df = multi_df.rename(
    columns={
        "chatgpt": "ChatGPT",
        "ChatGPT": "ChatGPT",

        "google gemini": "Google Gemini",
        "Google Gemini": "Google Gemini",

        "claude": "Claude",
        "Claude": "Claude",

        "pyth": "Python",
        "python": "Python",
        "Python": "Python",

        "data science": "Data Science",
        "Data Science": "Data Science"
    }
)

multi_df["Time"] = pd.to_datetime(
    multi_df["Time"],
    errors="coerce"
)


# ============================================================
# CLEAN CHATGPT DATA
# ============================================================

chatgpt_df["Time"] = pd.to_datetime(
    chatgpt_df["Time"],
    errors="coerce"
)


# Automatically identify the ChatGPT search-interest column
chatgpt_columns = [
    col for col in chatgpt_df.columns
    if col != "Time"
]

if len(chatgpt_columns) == 0:

    st.error(
        "No search-interest column was found in chatgpt_india_2026.csv."
    )

    st.stop()


CHATGPT_COLUMN = chatgpt_columns[0]


# ============================================================
# CLEAN TRENDING NOW DATA
# ============================================================

trending_df["Started"] = pd.to_datetime(
    trending_df["Started"],
    errors="coerce"
)

trending_df["Ended"] = pd.to_datetime(
    trending_df["Ended"],
    errors="coerce"
)


# ============================================================
# SEARCH VOLUME CONVERSION
# ============================================================

def convert_search_volume(value):

    value = str(value).replace("+", "").strip()

    try:

        if value.endswith("K"):
            return float(value[:-1]) * 1_000

        elif value.endswith("M"):
            return float(value[:-1]) * 1_000_000

        elif value.endswith("B"):
            return float(value[:-1]) * 1_000_000_000

        else:
            return float(value)

    except:

        return np.nan


trending_df["Search Volume Numeric"] = (
    trending_df["Search volume"]
    .apply(convert_search_volume)
)


# ============================================================
# SIDEBAR
# ============================================================

st.sidebar.title("📊 Google Trends")

st.sidebar.markdown(
    "### India Search Trends — 2026"
)

page = st.sidebar.radio(
    "Navigate",
    [
        "🏠 Overview",
        "📈 Keyword Analysis",
        "🔥 Trending Now",
        "📊 Correlation Analysis",
        "📝 Key Findings"
    ]
)

st.sidebar.markdown("---")

st.sidebar.info(
    """
    **Dataset**

    Google Trends data for India.

    Historical period:
    January – September 2026

    Trending Now:
    Recent search activity snapshot.
    """
)


# ============================================================
# HEADER
# ============================================================

st.markdown(
    '<div class="main-title">📊 Google Search Trends Analysis</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">India — 2026 | Exploring AI, technology and search-interest patterns</div>',
    unsafe_allow_html=True
)


# ============================================================
# OVERVIEW
# ============================================================

if page == "🏠 Overview":

    st.markdown(
        '<div class="section-title">Overview</div>',
        unsafe_allow_html=True
    )

    chatgpt_values = pd.to_numeric(
        chatgpt_df[CHATGPT_COLUMN],
        errors="coerce"
    )

    average_interest = chatgpt_values.mean()
    peak_interest = chatgpt_values.max()
    lowest_interest = chatgpt_values.min()

    peak_index = chatgpt_values.idxmax()

    peak_date = chatgpt_df.loc[
        peak_index,
        "Time"
    ]

    # --------------------------------------------------------
    # KPI CARDS
    # --------------------------------------------------------

    col1, col2, col3, col4 = st.columns(4)

    col1.metric(
        "Average Search Interest",
        f"{average_interest:.2f}"
    )

    col2.metric(
        "Peak Search Interest",
        f"{peak_interest:.0f}"
    )

    col3.metric(
        "Lowest Search Interest",
        f"{lowest_interest:.0f}"
    )

    col4.metric(
        "Peak Date",
        peak_date.strftime("%d %b %Y")
    )

    st.markdown("---")

    # --------------------------------------------------------
    # DATASET SIZE
    # --------------------------------------------------------

    col1, col2 = st.columns(2)

    with col1:

        st.metric(
            "Historical Records",
            len(multi_df)
        )

    with col2:

        st.metric(
            "Trending Searches",
            len(trending_df)
        )

    st.markdown("---")

    # --------------------------------------------------------
    # CHATGPT TREND
    # --------------------------------------------------------

    st.markdown(
        "### 📈 ChatGPT Search Interest"
    )

    chart_df = chatgpt_df.set_index("Time")

    st.line_chart(
        chart_df[CHATGPT_COLUMN],
        height=400,
        width="stretch"
    )

    st.info(
        """
        Google Trends values are normalized relative search-interest
        values from 0 to 100. They should not be interpreted as exact
        search counts.
        """
    )


# ============================================================
# KEYWORD ANALYSIS
# ============================================================

elif page == "📈 Keyword Analysis":

    st.markdown(
        '<div class="section-title">Keyword Analysis</div>',
        unsafe_allow_html=True
    )

    keywords = [
        "ChatGPT",
        "Google Gemini",
        "Claude",
        "Python",
        "Data Science"
    ]

    selected_keyword = st.selectbox(
        "Select a keyword",
        keywords
    )

    # --------------------------------------------------------
    # SELECTED KEYWORD DATA
    # --------------------------------------------------------

    selected_values = pd.to_numeric(
        multi_df[selected_keyword],
        errors="coerce"
    )

    average_value = selected_values.mean()
    peak_value = selected_values.max()
    lowest_value = selected_values.min()

    peak_index = selected_values.idxmax()

    peak_date = multi_df.loc[
        peak_index,
        "Time"
    ]

    # --------------------------------------------------------
    # KPI
    # --------------------------------------------------------

    col1, col2, col3, col4 = st.columns(4)

    col1.metric(
        "Average Interest",
        f"{average_value:.2f}"
    )

    col2.metric(
        "Peak Interest",
        f"{peak_value:.0f}"
    )

    col3.metric(
        "Lowest Interest",
        f"{lowest_value:.0f}"
    )

    col4.metric(
        "Peak Date",
        peak_date.strftime("%d %b %Y")
    )

    st.markdown("---")

    # --------------------------------------------------------
    # SELECTED KEYWORD TREND
    # --------------------------------------------------------

    st.markdown(
        f"### 📈 {selected_keyword} Search Interest"
    )

    selected_chart = multi_df.set_index("Time")[
        [selected_keyword]
    ]

    st.line_chart(
        selected_chart,
        height=400,
        width="stretch"
    )

    st.markdown("---")

    # --------------------------------------------------------
    # ALL KEYWORDS
    # --------------------------------------------------------

    st.markdown(
        "### 🔎 Compare All Keywords"
    )

    comparison_columns = [
        "ChatGPT",
        "Google Gemini",
        "Claude",
        "Python",
        "Data Science"
    ]

    comparison_df = multi_df.set_index("Time")[
        comparison_columns
    ]

    st.line_chart(
        comparison_df,
        height=450,
        width="stretch"
    )

    st.markdown("---")

    # --------------------------------------------------------
    # AVERAGE SEARCH INTEREST
    # --------------------------------------------------------

    st.markdown(
        "### 📊 Average Search Interest"
    )

    averages = (
        multi_df[comparison_columns]
        .mean()
        .sort_values(ascending=False)
    )

    st.bar_chart(
        averages,
        height=400,
        width="stretch"
    )


# ============================================================
# TRENDING NOW
# ============================================================

elif page == "🔥 Trending Now":

    st.markdown(
        '<div class="section-title">🔥 Google Trending Now</div>',
        unsafe_allow_html=True
    )

    # --------------------------------------------------------
    # METRICS
    # --------------------------------------------------------

    total_trends = len(trending_df)

    active_trends = trending_df["Ended"].isna().sum()

    ended_trends = trending_df["Ended"].notna().sum()

    highest_volume = trending_df[
        "Search Volume Numeric"
    ].max()

    col1, col2, col3, col4 = st.columns(4)

    col1.metric(
        "Total Trends",
        total_trends
    )

    col2.metric(
        "Active Trends",
        active_trends
    )

    col3.metric(
        "Ended Trends",
        ended_trends
    )

    col4.metric(
        "Highest Search Volume",
        f"{highest_volume:,.0f}"
    )

    st.markdown("---")

    # --------------------------------------------------------
    # TOP 10
    # --------------------------------------------------------

    st.markdown(
        "### 🔥 Top 10 Trending Searches"
    )

    top10 = (
        trending_df
        .sort_values(
            "Search Volume Numeric",
            ascending=False
        )
        .head(10)
    )

    display_columns = [
        col
        for col in [
            "Trends",
            "Search volume",
            "Started",
            "Ended"
        ]
        if col in top10.columns
    ]

    st.dataframe(
        top10[display_columns],
        width="stretch",
        hide_index=True
    )

    st.markdown("---")

    # --------------------------------------------------------
    # SEARCH VOLUME CHART
    # --------------------------------------------------------

    st.markdown(
        "### 📊 Search Volume of Top Trends"
    )

    volume_chart = (
        top10[
            ["Trends", "Search Volume Numeric"]
        ]
        .set_index("Trends")
        .sort_values(
            "Search Volume Numeric"
        )
    )

    st.bar_chart(
        volume_chart,
        height=450,
        width="stretch"
    )

    st.markdown("---")

    # --------------------------------------------------------
    # ACTIVE VS ENDED
    # --------------------------------------------------------

    st.markdown(
        "### ⏱️ Active vs Ended Trends"
    )

    status_df = pd.DataFrame(
        {
            "Status": [
                "Active",
                "Ended"
            ],
            "Count": [
                active_trends,
                ended_trends
            ]
        }
    )

    status_chart = status_df.set_index(
        "Status"
    )

    st.bar_chart(
        status_chart,
        height=300,
        width="stretch"
    )


# ============================================================
# CORRELATION ANALYSIS
# ============================================================

elif page == "📊 Correlation Analysis":

    st.markdown(
        '<div class="section-title">📊 Correlation Analysis</div>',
        unsafe_allow_html=True
    )

    correlation_columns = [
        "ChatGPT",
        "Google Gemini",
        "Claude",
        "Python",
        "Data Science"
    ]

    correlation_df = multi_df[
        correlation_columns
    ].corr()

    # --------------------------------------------------------
    # HEATMAP
    # --------------------------------------------------------

    st.markdown(
        "### 🔥 Keyword Correlation Heatmap"
    )

    fig, ax = plt.subplots(
        figsize=(10, 7)
    )

    sns.heatmap(
        correlation_df,
        annot=True,
        fmt=".2f",
        cmap="coolwarm",
        center=0,
        ax=ax
    )

    ax.set_title(
        "Correlation Between Search Interests"
    )

    st.pyplot(
        fig,
        width="stretch"
    )

    plt.close(fig)

    st.markdown("---")

    # --------------------------------------------------------
    # CORRELATION TABLE
    # --------------------------------------------------------

    st.markdown(
        "### 📋 Correlation Table"
    )

    st.dataframe(
        correlation_df.round(2),
        width="stretch"
    )

    st.info(
        """
        Correlation measures the strength and direction of a linear
        relationship between variables. Correlation does not imply
        causation.
        """
    )


# ============================================================
# KEY FINDINGS
# ============================================================

elif page == "📝 Key Findings":

    st.markdown(
        '<div class="section-title">📝 Key Findings</div>',
        unsafe_allow_html=True
    )

    comparison_columns = [
        "ChatGPT",
        "Google Gemini",
        "Claude",
        "Python",
        "Data Science"
    ]

    averages = (
        multi_df[comparison_columns]
        .mean()
        .sort_values(ascending=False)
    )

    peak_keyword = averages.idxmax()

    # --------------------------------------------------------
    # FINDING 1
    # --------------------------------------------------------

    st.markdown("### 🔹 Keyword Comparison")

    st.write(
        f"""
        Among the selected keywords, **{peak_keyword}** recorded the
        highest average relative search interest during the analyzed
        period.
        """
    )

    # --------------------------------------------------------
    # FINDING 2
    # --------------------------------------------------------

    chatgpt_values = pd.to_numeric(
        chatgpt_df[CHATGPT_COLUMN],
        errors="coerce"
    )

    chatgpt_peak = chatgpt_values.max()

    chatgpt_peak_index = chatgpt_values.idxmax()

    chatgpt_peak_date = chatgpt_df.loc[
        chatgpt_peak_index,
        "Time"
    ]

    st.markdown("### 🔹 ChatGPT Peak")

    st.write(
        f"""
        ChatGPT reached a peak Google Trends search-interest value of
        **{chatgpt_peak:.0f}** on
        **{chatgpt_peak_date.strftime("%d %B %Y")}**.
        """
    )

    # --------------------------------------------------------
    # FINDING 3
    # --------------------------------------------------------

    claude_january = (
        multi_df.loc[
            multi_df["Time"].dt.month == 1,
            "Claude"
        ].mean()
    )

    claude_september = (
        multi_df.loc[
            multi_df["Time"].dt.month == 9,
            "Claude"
        ].mean()
    )

    st.markdown("### 🔹 Claude Search Interest")

    st.write(
        f"""
        Claude's average search interest increased from approximately
        **{claude_january:.2f}** in January to
        **{claude_september:.2f}** in September in the analyzed dataset.
        """
    )

    # --------------------------------------------------------
    # FINDING 4
    # --------------------------------------------------------

    st.markdown("### 🔹 Correlation")

    st.write(
        """
        The correlation analysis shows different relationships between
        the selected keywords. These relationships describe search
        patterns in the dataset and should not be interpreted as
        evidence of causation.
        """
    )

    # --------------------------------------------------------
    # IMPORTANT NOTE
    # --------------------------------------------------------

    st.warning(
        """
        Google Trends values are normalized relative search-interest
        values rather than exact search counts. Therefore, the results
        should be interpreted as relative search-interest patterns.
        """
    )


# ============================================================
# FOOTER
# ============================================================

st.markdown(
    """
    <div class="footer">
        Google Search Trends Analysis in India — 2026<br>
        Built with Python, Pandas, Matplotlib, Seaborn and Streamlit
    </div>
    """,
    unsafe_allow_html=True
)