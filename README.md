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
```python
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
