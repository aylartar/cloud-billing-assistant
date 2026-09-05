# Cloud Billing Assistant

## Overview
A Python project to analyze FOCUS-compliant cloud billing data, inspect dataset quality, and prepare data structures for cloud cost engineering.

## Project Structure
```text
cloud-billing-assistant/
├── data/
│   ├── billing_sample.csv
│   ├── billing_full.json
│   └── billing_summary.json
├── src/
│   └── data_loader.py
├── .env
├── .gitignore
├── requirements.txt
└── README.md
└── week2_analysis.ipynb 
```

## Weekly Progress

### Week 1: Python + Git Foundations
- Set up the local project structure and Git repository.
- Created virtual environment and managed configurations using `.env`.
- Handled CSV data loading and converted raw billing data into full JSON format and summary JSON reports.

### Week 2: Data Basics with NumPy and Pandas
- **1. Data Loading & Initial Inspection:** Loaded the FOCUS billing dataset using pandas and inspected its overall structure, dimensions, and schema (`df.info()`, `df.describe()`).
- **2. Missing Values Analysis:** Evaluated missing data across dataset columns and generated bar plots to visualize missingness patterns.
- **3. Cost Aggregation & Analysis:** Summarized billing data by cloud services and commitment discount statuses to understand main cost drivers.
- **4. Exploratory Data Visualizations:** Created multiple analytical charts (including provider distribution donut charts and missing data plots) to thoroughly explore and understand the dataset
- **Note:** Kept the raw dataset as-is for initial inspection; full missing value handling and data cleaning are planned for **Week 3**.