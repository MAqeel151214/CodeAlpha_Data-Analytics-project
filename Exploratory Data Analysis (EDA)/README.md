```markdown
# 🔍 Module 2: Exploratory Data Analysis (EDA)

## 🎯 Objective
To "interrogate" the raw data, identify quality issues, and uncover initial patterns before deep visualization.

## 🧹 Data Cleaning & Preparation
*   **Missing Values:** Checked for nulls (Dataset was clean).
*   **Data Types:** Converted Price to `float64` and Rating to `int64`.
*   **Feature Engineering:**
    *   Created `Title_Length`: To analyze if title complexity affects price.
    *   Created `Price_Segment`: Categorized books into 'Budget', 'Mid-Range', and 'Premium' using quartiles.

## 📊 Statistical Insights
1.  **Pricing Distribution:** The mean price is approx £35, with a standard deviation indicating a wide spread.
2.  **Rating Distribution:** Ratings are fairly balanced, though 1-star ratings are slightly less common.
3.  **Correlation Analysis:** A Pearson Correlation matrix revealed a near-zero correlation between `Price` and `Rating`, suggesting that higher cost does not guarantee higher user satisfaction.

## 📝 Custom Datasets Created
The EDA script creates specialized CSVs for different business stakeholders:
*   `dataset_1_vip_catalog.csv`: High-margin items for the Sales team.
*   `dataset_2_risk_audit.csv`: Low-rated but expensive items for Quality Control.
```
