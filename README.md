# XYlofy AI — Data Analytics Internship

**Data Analytics Track**
**Intern:** Vaishnavi Bhan
**GitHub:** [Via-01](https://github.com/Via-01)

This repository contains all the work completed by **Vaishnavi Bhan** during a **4-week AI & Data Science micro-internship with XYlofy AI**. The internship was structured as a progressive skill build — starting with a foundational regression task, stepping up to a full classification problem with business interpretation, and culminating in a combined Weeks 3–4 capstone: an end-to-end sales forecasting and demand analytics system shipped as a live dashboard.

---

## 📋 Internship Overview

| Item                | Details                                              |
| ------------------- | ----------------------------------------------------- |
| Organization        | XYlofy AI                                              |
| Duration            | 4 Weeks                                                |
| Track               | Data Analytics                                         |
| Structure           | Week 1 → Week 2 → Weeks 3 & 4 (combined capstone)      |
| Weeks Completed     | **4 / 4**                                              |
| Repository Name     | `V_XYlofi_Repo`                                        |
| Submission Format   | One repository containing all weekly deliverables      |

---

## 📁 Repository Structure

```
V_XYlofi_Repo/
│
├── Week1/
│   ├── XYlofy_Vaishnavi_W1_analysis.ipynb
│   ├── XYlofy_vaishnavi_W1_summary.pdf
│   ├── Housing.csv
│   ├── HousePricePrediction_Vaishnavi_Bhan.zip
│   └── charts/
│       ├── chart1_histogram.png
│       ├── chart2_Correlation_Heatmap.png
│       └── chart3_scatter_plot_grid.png
│
├── Week2/
│   ├── XYlofy_Vaishnavi_W2_analysis.ipynb
│   ├── XYlofy_Vaishnavi_W2_summary.pdf
│   ├── WA_Fn-UseC_-HR-Employee-Attrition.csv
│   ├── EmployeeAttrition_Vaishnavi_Bhan.zip
│   └── charts/
│       ├── c1.png ... c5.png
│       └── c_eda0.png ... c_eda2.png
│
├── Week3_and_4/
│   ├── XYlofy_Vaishnavi_W3&4_analysis.ipynb
│   ├── XYlofy_Vaishnavi_W3&4_summary.pdf
│   ├── SalesForecasting_Vaishnavi_Bhan.zip
│   ├── train.csv
│   ├── vgsales.csv
│   ├── charts/
│   │   ├── ACF.png / PACF.png
│   │   ├── Prophet_forecast_plot.png
│   │   ├── SARIMA_actual_vs_forecast.png
│   │   ├── xgboost_actual_vs_forecast.png
│   │   ├── t5_isolation_forest_anomalies.png
│   │   ├── t5_zscore_anomalies.png
│   │   ├── t6_clustering.png
│   │   └── ...
│   └── SalesForecastDashboard/
│       ├── app.py
│       ├── theme.py
│       ├── utils.py
│       ├── requirements.txt
│       ├── dashboard_data/
│       └── pages/
│           ├── 1_📊_Sales_Overview.py
│           ├── 2_📈_Forecast_Explorer.py
│           ├── 3_⚠️_Anomaly_Report.py
│           └── 4_📦_Demand_Segments.py
│
└── README.md                          ← You are here
```

---

## 🧪 Weekly Deliverables

### Week 1 — House Price Prediction

**Objective:** Analyze housing data and build regression models to predict house prices from structural and location attributes.

- Dataset: 545 records, 13 attributes (numerical + categorical)
- Preprocessing: duplicate removal, One-Hot Encoding of categorical features
- EDA: price distribution histogram, correlation heatmap — area and bathrooms showed the strongest positive correlation with price
- Models: Linear Regression, Random Forest Regressor
- Result: Linear Regression outperformed Random Forest on every metric (MAE 779,346 · RMSE 1,061,503 · R² 0.673), indicating a largely linear relationship between features and price

📂 [View Week 1 Folder](https://github.com/Via-01/V_XYlofi_Repo/tree/main/Week1)

---

### Week 2 — Employee Attrition Analysis

**Objective:** Identify patterns behind employee attrition and build a model to help HR proactively flag at-risk employees.

- Dataset: 1,470 employees · overall attrition rate 16.12%
- Key findings: Sales had the highest departmental attrition (20.63%), Sales Representatives the highest by role (39.76%); employees in their first two years were disproportionately likely to leave
- Models: three classifiers evaluated; **Logistic Regression selected** over a higher-accuracy alternative because it identified far more of the employees who actually left — prioritizing business-relevant recall over raw accuracy
- Insight: overtime, frequent travel, and specific job roles were stronger attrition predictors than salary alone
- Delivered as an **executive summary** with concrete HR retention recommendations, not just a notebook

📂 [View Week 2 Folder](https://github.com/Via-01/V_XYlofi_Repo/tree/main/Week2)

---

### Weeks 3 & 4 — Superstore Sales Forecasting & Demand Analytics (Capstone)

**Objective:** Bring together forecasting, anomaly detection, and segmentation skills from Weeks 1–2 into a single end-to-end analytics system supporting inventory and demand planning.

- Dataset: 4 years of Superstore sales data
- **Forecasting:** SARIMA, Facebook Prophet, and XGBoost compared — XGBoost achieved the lowest error (MAPE 14.48%, RMSE ≈ 18,337) and was selected for the 3-month forecast
- **Insights:** Technology category and the West region show the strongest projected growth; clear year-end seasonality (Nov–Dec) confirmed via time-series decomposition
- **Anomaly detection:** two independent methods — Isolation Forest (11 anomalous weeks) and rolling Z-score (6 anomalous weeks) — flagged events including a March 2015 sales spike and the Nov–Dec 2018 holiday surge
- **Demand segmentation:** K-Means clustering grouped product sub-categories into 4 actionable tiers (Premium High-Value, High Volume/Stable, Low Volume/Stable, Growing Demand)
- **Deployed as a live, multi-page Streamlit dashboard** — Sales Overview, Forecast Explorer, Anomaly Report, and Demand Segments — turning the analysis into an interactive tool rather than a static report
- Delivered as a formal **Executive Business Report** with numbered, actionable business recommendations

📂 [View Week 3 & 4 Folder](https://github.com/Via-01/V_XYlofi_Repo/tree/main/Week3_and_4)
🚀 [Live Dashboard](https://vaishnavi-xylofi-w34.streamlit.app/)

---

## 🛠️ Technology Stack

| Category            | Tools / Libraries                                  |
| -------------------- | --------------------------------------------------- |
| Language              | Python                                              |
| Data Manipulation     | pandas, NumPy                                       |
| Visualization         | Matplotlib, Plotly                                  |
| Machine Learning       | scikit-learn, XGBoost                              |
| Time Series Forecasting | statsmodels (SARIMA), Prophet                    |
| Dashboard / Deployment | Streamlit                                          |
| Environment            | Jupyter Notebook / Google Colab                    |

---

## 🚀 How to Explore This Repository

1. **Clone the repository**

```
git clone https://github.com/Via-01/V_XYlofi_Repo.git
cd V_XYlofi_Repo
```

2. **Navigate into any week's folder**

```
cd Week1
```

3. **Install dependencies** (example for the notebooks)

```
pip install pandas numpy matplotlib scikit-learn statsmodels prophet xgboost notebook
```

4. **Launch Jupyter Notebook**

```
jupyter notebook
```

5. **To run the Week 3 & 4 capstone dashboard locally:**

```
cd Week3_and_4/SalesForecastDashboard
pip install -r requirements.txt
streamlit run app.py
```

Or skip local setup entirely and use the **[live hosted dashboard →](https://vaishnavi-xylofi-w34.streamlit.app/)**

Each week's folder contains a detailed executive-summary PDF alongside the analysis notebook, with findings, metrics, and recommendations.

---

## ✅ Completion Status

| Week | Focus                                   | Status      |
| ---- | ----------------------------------------- | ----------- |
| 1    | House Price Prediction (Regression)       | ✅ Completed |
| 2    | Employee Attrition Analysis (Classification) | ✅ Completed |
| 3 & 4 | Sales Forecasting & Demand Analytics (Capstone) | ✅ Completed |

**All 4 weeks successfully completed**, culminating in a deployed capstone dashboard.

---

## 📜 Certificate of Completion

[📄 View Certificate (PDF)](VaishnaviBhan-CompletionCertificate.pdf)

Issued by XYlofy AI on 30th June 2026, confirming successful completion of the 4-Week AI & Data Science Internship (15 June – 15 July 2026).

---

## 👩‍💻 Author

**Vaishnavi Bhan**
B.Tech CSE Graduate | BS Data Science Undergraduate

- GitHub: [Via-01](https://github.com/Via-01)
- Portfolio: [vaishnavi-portfolio-vert-one.vercel.app](https://vaishnavi-portfolio-vert-one.vercel.app/)

---

## 📄 License & Disclaimer

This repository was created solely for educational and evaluation purposes as part of the **XYlofy AI Internship Program**.

All datasets used are publicly available and belong to their respective owners. They are used here strictly for academic and learning purposes.

---

**Thank you for reviewing my work!**
Feel free to explore the individual week folders for detailed notebooks, executive reports, and the live dashboard.