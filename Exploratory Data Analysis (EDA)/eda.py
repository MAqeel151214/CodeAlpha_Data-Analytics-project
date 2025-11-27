import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# --- 1. LOAD THE DATA ---
print("--- LOADING DATA ---")
df = pd.read_csv('books_ecommerce_data.csv')

# Check the first few rows and data types
print(df.head())
print("\nData Info:")
print(df.info())

# --- 2. DATA CLEANING & STRUCTURE ---
print("\n--- CLEANING & STRUCTURE ---")

# Check for missing values
print(f"Missing Values:\n{df.isnull().sum()}")

# Check unique values in 'Availability' to see if it's useful
# (On the catalogue page, this might all be 'In stock', which isn't very useful for analysis)
print(f"\nUnique Availability statuses: {df['Availability'].unique()}")

# Statistical Summary of Price
print("\nPrice Statistics:")
print(df['Price_GBP'].describe())

# --- FEATURE ENGINEERING (Creating new data) ---
# Create 'Title_Length': Count of characters in the title
df['Title_Length'] = df['Title'].apply(len)

# Create 'Price_Segment': Categorize prices
# We use quantiles to ensure groups are balanced (33% in each bucket)
labels = ['Budget', 'Mid-Range', 'Premium']
df['Price_Segment'] = pd.qcut(df['Price_GBP'], q=3, labels=labels)

print("\n---  ANALYSIS  ---")

# --- 3. ANSWERING QUESTIONS ---
print("\n--- INSIGHTS ---")

# Q1: What is the most expensive book scraped?
most_expensive = df.loc[df['Price_GBP'].idxmax()]
print(f"Most Expensive Book: {most_expensive['Title']} (£{most_expensive['Price_GBP']})")

# Q2: What is the cheapest book scraped?
cheapest = df.loc[df['Price_GBP'].idxmin()]
print(f"Cheapest Book: {cheapest['Title']} (£{cheapest['Price_GBP']})")

# Q3: Average price of a 5-star book vs a 1-star book
avg_price_by_rating = df.groupby('Rating')['Price_GBP'].mean()
print("\nAverage Price by Rating:")
print(avg_price_by_rating)


# --- 4. ADVANCED STATISTICAL INSIGHTS ---
print("\n--- ADVANCED ANALYTICS ---")

# Insight 1: Correlation Matrix
# Does Title Length correlate with Price or Rating?
correlation = df[['Price_GBP', 'Rating', 'Title_Length']].corr()
print("\n1. Correlation Matrix:")
print(correlation)
print("(Note: Values near 0 mean no relationship. Values near 1 or -1 mean strong relationship.)")

# Insight 2: Pricing Strategy (Cumulative Distribution)
# What price point covers 80% of our inventory?
sorted_prices = df['Price_GBP'].sort_values()
cumulative_percent = sorted_prices.rank(pct=True)
# Find the price where cumulative percentage crosses 0.80 (80%)
price_at_80_percentile = sorted_prices[cumulative_percent >= 0.80].iloc[0]

print(f"\n2. Pareto/Pricing Insight:")
print(f"80% of the books are priced below £{price_at_80_percentile:.2f}")

# Insight 3: Segment Analysis
# What is the average rating for Premium vs Budget books?
segment_stats = df.groupby('Price_Segment')['Rating'].mean()
print("\n3. Average Rating by Price Segment:")
print(segment_stats)