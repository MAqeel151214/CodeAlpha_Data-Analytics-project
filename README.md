# CodeAlpha_Data-Analytics-project


# 📚 E-Commerce Data Analytics Pipeline

## 📖 Project Overview
This project simulates a real-world E-commerce data pipeline. The goal is to extract competitive intelligence from an online bookstore, analyze pricing strategies, and visualize market trends.

The project is divided into three core phases:
1.  **Data Extraction:** Scraping product data from a public sandbox website.
2.  **Exploratory Data Analysis (EDA):** Cleaning, structuring, and finding statistical patterns.
3.  **Visual Analytics:** Creating advanced dashboards to drive business insights.

## 🛠️ Tech Stack
*   **Python 3.9+**
*   **Web Scraping:** `BeautifulSoup4`, `Requests`
*   **Data Manipulation:** `Pandas`, `NumPy`
*   **Visualization:** `Matplotlib`, `Seaborn`

## 🚀 How to Run
1.  **Clone the repository:**
    ```bash
    git clone https://github.com/YOUR_USERNAME/Ecommerce-Data-Science-Project.git
    ```
2.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
3.  **Run the scripts in order:**
    *   Run `scraping/book_scraper.py` to generate the raw data.
    *   Run `eda/exploratory_analysis.py` to clean and analyze.
    *   Run `visualization/advanced_visuals.py` to see the charts.

## 📂 Project Structure
*   `/scraping`: Scripts to extract data from `books.toscrape.com`.
*   `/eda`: Scripts for statistical summary, cleaning, and feature engineering.
*   `/visualization`: Advanced plotting and dashboarding scripts.
*   `/data`: Contains the generated CSV datasets.

## 💡 Key Findings
*   Pricing is largely independent of customer rating (0.02 correlation).
*   There is no "Premium" pricing strategy for longer, more complex titles.
*   The inventory is evenly distributed across budget and premium segments.

---
*Disclaimer: This project uses `books.toscrape.com`, a safe sandbox created specifically for scraping practice.*
```
