# AlphaCare Insurance Analytics

## Overview
This repository contains **insurance risk analytics** using real policyholder data.  
The goal is to analyze claims, premiums, and loss ratios to generate insights for **policy optimization**.  

**Tasks included:**
- **Task 1:** Exploratory Data Analysis (EDA)  
- **Task 2:** Loss Ratio Analysis by Province  

---

## Dataset
`MachineLearningRating_v3.csv` contains:

| Column                 | Description                    |
|------------------------|--------------------------------|
| `PolicyID`             | Unique policy ID               |
| `Gender`               | Policyholder gender            |
| `Province`             | Province of policyholder       |
| `TotalClaims`          | Total claims made              |
| `TotalPremium`         | Total premium paid             |
| `CustomValueEstimate`  | Estimated custom value         |

---

## Task 1 – Exploratory Data Analysis (EDA)

**Steps:**
- Inspect dataset structure, missing values, basic statistics  
- Visualize distributions: `TotalClaims`, `TotalPremium`  
- Count plots: `Gender`, `Province`  
- Analyze relationships & outliers: scatter plots & boxplots  
- Compute `LossRatio` for further analysis  

**Example Visualizations:**  
- Histogram of TotalClaims  
- Histogram of TotalPremium  
- Gender & Province counts  
- Scatter plot: TotalPremium vs TotalClaims  
- LossRatio boxplot by Province  

---

## Task 2 – Loss Ratio Analysis

**Steps:**
1. Compute loss ratio:  

df['LossRatio'] = df['TotalClaims'] / df['TotalPremium']
Aggregate by province:

loss_ratio = df.groupby('Province')['LossRatio'].mean()
loss_ratio.to_csv('../reports/loss_ratio_by_province.csv')


Helps identify high-risk provinces for better decision-making.

How to Run

Clone the repository:

git clone <your-repo-url>
cd AlphaCare-Insurance-week-3


Create environment and install dependencies:

conda create -n acis-env python=3.11.9 -y
conda activate acis-env
pip install -r requirements.txt


Open notebook:

jupyter notebook

Folder Structure
AlphaCare-Insurance-week-3/
│
├─ data/processed/        # CSV files
├─ notebooks/             # EDA & analysis notebooks
├─ reports/               # Output CSVs
├─ README.md              # Project overview
├─ requirements.txt       # Dependencies

# 🧪 Task 3 — Hypothesis Testing & Statistical Analysis

### 🎯 Goal

Determine statistically significant factors that influence claim probability, severity, and loss ratios.

---

### ✅ Implemented Steps

1. Formulated hypotheses on risk factors:

   * Age groups & claim frequency
   * Vehicle type & claim severity
   * Security features (alarm/immobilizer) & claim reduction

2. Conducted statistical tests:

   * Chi-square tests for categorical variables
   * T-tests / ANOVA for numeric features across groups

3. Summarized results and effect sizes

---

### 🔍 Key Findings
* Certain age groups and citizenship categories have higher claim probabilities
* Vehicles with alarm/immobilizer devices show significantly lower claims
* Cresta zones show geographic variation in claims and risk

---

# 🤖 Task 4 — Predictive Modeling & Insights

### 🎯 Goal

Build models to predict the probability of claims and identify high-impact risk factors.

---

### ✅ Models & Techniques

* Logistic Regression
* Random Forest Classifier
* Feature importance analysis
* Cross-validation to evaluate performance

---

### 🔍 Key Insights

* Age, vehicle type, and security features are top predictors
* Loss ratios and premiums can be adjusted dynamically based on risk
* Model outputs inform both marketing segmentation and pricing strategy

---

## 📈 Actionable Recommendations

1. Targeted Marketing

   * Promote policies to low-risk demographics and regions
   * Upsell security devices to mitigate risk

2. Dynamic Pricing Strategy

   * Adjust premiums based on predictive risk factors
   * Incorporate vehicle features, model year, and security status

3. Cross-Selling Opportunities

   * Offer tracking devices or alarms to high-risk segments

---

## ⚠️ Limitations & Future Work

* Non-numeric columns required encoding → some nuance lost
* External factors like economic conditions or seasonal effects not included
* Rare events may reduce model accuracy

Future Work:

* Time-series analysis for seasonal trends
* Advanced machine learning models (XGBoost, Gradient Boosting)
* Integrate external datasets (traffic, weather, economy)

---

# 📝 Task Status

| Task                              | Status       | Description                         |
| --------------------------------- | ------------ | ----------------------------------- |
| Task 1.2 – EDA & Statistics   | ✔️ Completed | Full EDA + insights + plots         |
| Task 2 – DVC & Pipeline Setup | ✔️ Completed | Reproducible data tracking          |
| Task 3 – Hypothesis Testing   | ✔️ Completed | Statistical analysis of risk        |
| Task 4 – Predictive Modeling  | ✔️ Completed | Claim prediction & feature 
