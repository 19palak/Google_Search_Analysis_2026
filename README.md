# Google Search Trends Analysis in India - 2026

## 📌 Project Overview

This project analyzes Google search trends in India during 2026 using Python and Google Trends data.

The project examines search-interest patterns for selected technology and AI-related keywords and also analyzes Google's Trending Now data to identify recent trending searches.

The goal of this project is to demonstrate how Python can be used to clean, analyze, visualize, and interpret real-world search-trend data.

---

## 🎯 Objectives

The main objectives of this project are:

- Analyze Google search interest over time.
- Compare search interest across multiple technology-related keywords.
- Identify periods of high and low search interest.
- Analyze monthly and weekly changes in search interest.
- Calculate percentage changes between different periods.
- Analyze correlations between search-interest patterns.
- Examine currently trending searches in India.
- Analyze reported search-volume ranges and trend duration.
- Create meaningful visualizations using Python.

---

## 📊 Datasets

The project uses Google Trends data for India.

### 1. Historical Keyword Dataset

The historical analysis covers the following keywords:

- ChatGPT
- Google Gemini
- Claude
- Python
- Data Science

The historical dataset covers the period from **January 2026 to September 2026**.

Google Trends provides normalized relative search-interest values on a scale from 0 to 100. These values represent relative interest rather than exact numbers of searches.

### 2. Trending Now Dataset

A separate Google Trends Trending Now dataset was used to analyze recent trending searches in India.

This dataset includes information such as:

- Trending search
- Reported search volume
- Start time
- End time
- Trend status
- Related trend information

> **Note:** Trending Now represents a snapshot of recent search activity and can change frequently.

---

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Jupyter Notebook
- Google Trends

---

## 🔍 Analysis Performed

### Single-Keyword Analysis

The ChatGPT dataset was analyzed to determine:

- Average search interest
- Peak search interest
- Lowest search interest
- Top search periods
- Moving average
- Weekly changes
- Search-interest distribution

### Multi-Keyword Analysis

The following keywords were compared:

- ChatGPT
- Google Gemini
- Claude
- Python
- Data Science

The analysis includes:

- Average search interest
- Search-interest trends
- Peak values
- Weekly changes
- Monthly averages
- January-to-September percentage changes
- Correlation analysis
- Correlation heatmap

### Trending Now Analysis

The Trending Now dataset was analyzed using:

- Top trending searches
- Reported search-volume ranges
- Active vs ended trends
- Trend duration
- Longest-lasting trends

---

## 📈 Key Findings

### ChatGPT

ChatGPT recorded the highest relative search interest among the five selected keywords in the analyzed dataset.

Its monthly average increased from **70.25 in January** to **83.80 in August**, followed by a decrease to **78.00 in September**.

### Claude

Claude showed an increase in relative search interest during the analyzed period.

Its monthly average increased from **2.00 in January** to **13.25 in June and July**.

The January-to-September percentage change was **416.67%**. However, this percentage is strongly influenced by the low January baseline.

### Google Gemini

Google Gemini showed relatively stable search interest throughout the analyzed period, with moderate fluctuations between months.

### Python

Python search interest remained relatively stable, with moderate month-to-month fluctuations.

### Data Science

Data Science remained at a value of **1.00** throughout the available monthly data.

Because the value did not vary, correlation with the other keywords could not be calculated.

### Correlation

The correlation analysis showed different relationships between the selected keywords.

For example:

- ChatGPT and Claude: approximately **0.49**
- Claude and Python: approximately **-0.54**
- ChatGPT and Google Gemini: approximately **0.01**

Correlation measures how variables move together and does not establish causation.

---

## 📉 Visualizations

The project includes visualizations such as:

- Search-interest trend lines
- Average search-interest bar charts
- Peak search-interest comparison
- Monthly search-interest comparison
- Weekly change analysis
- Search-interest distribution
- Correlation heatmap
- Top Trending Now searches
- Active vs ended trends
- Trend-duration analysis

---

## 📁 Project Structure

```text
Google_Search_Analysis_2026/
│
├── data/
│   └── raw/
│       ├── chatgpt_india_2026.csv
│       ├── multi_keyword_india_2026.csv
│       └── trending_now_india_2026.csv
│
├── notebooks/
│   ├── google_search_analysis.ipynb
│   ├── multi_keyword_analysis.ipynb
│   └── trending_now_analysis.ipynb
│
├── requirements.txt
│
└── README.md

```
## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/19palak/Google_Search_Analysis_2026.git
```

Move into the project directory:

```bash
cd Google_Search_Analysis_2026
```

Install the required Python libraries:

```bash
pip install -r requirements.txt
```

---

## ▶️ How to Run

Start Jupyter Notebook:

```bash
jupyter notebook
```

Open the `notebooks` folder and run the notebooks in the following order:

1. `google_search_analysis.ipynb`
2. `multi_keyword_analysis.ipynb`
3. `trending_now_analysis.ipynb`

Run the cells in each notebook from top to bottom to reproduce the analysis and visualizations.

---

## ⚠️ Limitations

- Google Trends provides relative search-interest values rather than exact search counts.
- The historical dataset currently covers January to September 2026.
- The Trending Now dataset represents a snapshot of recent search activity.
- Trending searches can change frequently.
- Search interest does not necessarily represent actual product usage or user preference.
- Correlation does not imply causation.
- Google Trends values are normalized within their comparison context.
- The analysis is based on the selected keywords and datasets and may not represent all search behavior in India.

---

## 🚀 Future Scope

Possible future improvements include:

- Building an interactive Streamlit dashboard.
- Adding more technology and AI-related keywords.
- Performing regional analysis across Indian states.
- Analyzing search trends by category.
- Automating data collection where technically and reliably possible.
- Adding more historical datasets for year-to-year comparison.
- Applying machine learning techniques for trend forecasting.
- Adding interactive filters for keywords, dates, and regions.
- Creating automated reports from the analysis.

---

## 👩‍💻 Skills Demonstrated

This project demonstrates practical experience with:

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Data cleaning
- Exploratory Data Analysis (EDA)
- Statistical analysis
- Correlation analysis
- Time-series analysis
- Data visualization
- Data interpretation
- Jupyter Notebook
- Git and GitHub
- Working with real-world datasets

---

## 📌 Disclaimer

This project is intended for educational and portfolio purposes.

Google Trends data represents relative search interest and should not be interpreted as exact search volume, user preference, or actual product usage.

The results presented in this project are based on the selected datasets, keywords, time periods, and analysis methods used in the project.
