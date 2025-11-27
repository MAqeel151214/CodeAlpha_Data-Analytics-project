
import pandas as pd
from collections import Counter

# 1. LOAD RAW DATA
df = pd.read_csv('books_ecommerce_data.csv')

# --- PREP: Add Contextual Features ---
# We calculate the "Average Market Price" to help us segment the data
avg_market_price = df['Price_GBP'].mean()
df['Price_Versus_Avg'] = df['Price_GBP'] - avg_market_price

# ==========================================
# CUSTOM DATASET 1: The "High-Value" Catalog
# Use Case: For the Sales Team to focus on high-margin items.
# ==========================================
# Logic: Filter for books priced above the 75th percentile (Top 25% most expensive)
price_threshold = df['Price_GBP'].quantile(0.75)
high_value_df = df[df['Price_GBP'] >= price_threshold].sort_values(by='Price_GBP', ascending=False)

# Save
high_value_df.to_csv('dataset_1_vip_catalog.csv', index=False)
print(f"✅ Created 'dataset_1_vip_catalog.csv' with {len(high_value_df)} items.")


# ==========================================
# CUSTOM DATASET 2: The "Audit" List (Risk Analysis)
# Use Case: For the Quality Control team.
# ==========================================
# Logic: Identify "Risky" products -> High Price but Low Rating (1 or 2 stars).
# Customers hate paying a lot for bad products; these cause returns.
audit_df = df[(df['Price_GBP'] > avg_market_price) & (df['Rating'] <= 2)]

# Save
audit_df.to_csv('dataset_2_risk_audit.csv', index=False)
print(f"✅ Created 'dataset_2_risk_audit.csv' with {len(audit_df)} risky items.")


# ==========================================
# CUSTOM DATASET 3: Pricing Strategy Summary
# Use Case: For the Management Dashboard (High-level view).
# ==========================================
# Logic: We don't want individual books; we want Averages grouped by Rating.
summary_df = df.groupby('Rating').agg({
    'Price_GBP': ['mean', 'min', 'max', 'count'],
    'Title': 'count' # Total inventory count per rating
})

# Flatten the multi-level column names for easier reading in Excel
summary_df.columns = ['Avg_Price', 'Min_Price', 'Max_Price', 'Price_Count', 'Inventory_Count']
summary_df = summary_df.reset_index()

# Save
summary_df.to_csv('dataset_3_pricing_summary.csv', index=False)
print(f"✅ Created 'dataset_3_pricing_summary.csv'.")


# ==========================================
# CUSTOM DATASET 4: Marketing Keyword Analysis
# Use Case: For the SEO/Marketing team to find trending keywords.
# ==========================================
# Logic: Break titles into words to see what topics are trending.

# 1. Combine all titles into one string and lower case them
all_text = " ".join(df['Title']).lower()

# 2. Simple tokenizer (remove non-alphabet characters)
words = [word.strip(".,!?:;()[]") for word in all_text.split()]

# 3. Filter out common "stop words" (boring words)
stop_words = {'the', 'a', 'an', 'of', 'and', 'in', 'to', 'for', 'with', 'on', 'at', 'by', 'from'}
filtered_words = [w for w in words if w not in stop_words and len(w) > 3]

# 4. Count frequencies
word_counts = Counter(filtered_words)
marketing_df = pd.DataFrame(word_counts.most_common(50), columns=['Keyword', 'Frequency'])

# Save
marketing_df.to_csv('dataset_4_marketing_keywords.csv', index=False)
print(f"✅ Created 'dataset_4_marketing_keywords.csv' with top 50 keywords.")

print("\nAll custom datasets are ready for analysis!")