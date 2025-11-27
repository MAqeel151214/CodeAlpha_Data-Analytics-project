import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from collections import Counter
import warnings


# Suppress warnings for cleaner output
warnings.filterwarnings('ignore')

# 1. LOAD DATA
df = pd.read_csv('books_ecommerce_data.csv')

# Set the visual style
sns.set_theme(style="whitegrid")

# --- FEATURE ENGINEERING (Creating new data) ---
# Create 'Title_Length': Count of characters in the title
df['Title_Length'] = df['Title'].apply(len)

# Create 'Price_Segment': Categorize prices
# We use quantiles to ensure groups are balanced (33% in each bucket)
labels = ['Budget', 'Mid-Range', 'Premium']
df['Price_Segment'] = pd.qcut(df['Price_GBP'], q=3, labels=labels)

# A. Univariate Analysis: Price Distribution
plt.figure(figsize=(10, 5))
sns.histplot(df['Price_GBP'], bins=20, kde=True, color='skyblue')
plt.title('Distribution of Book Prices (£)')
plt.xlabel('Price')
plt.show()

# B. Univariate Analysis: Rating Count
plt.figure(figsize=(8, 5))
sns.countplot(x='Rating', data=df, palette='viridis')
plt.title('Count of Books by Star Rating')
plt.show()

# C. Bivariate Analysis: Price vs. Rating
# QUESTION: Do higher-rated books cost more?
plt.figure(figsize=(10, 6))
sns.boxplot(x='Rating', y='Price_GBP', data=df, palette="coolwarm")
plt.title('Book Price Distribution by Star Rating')
plt.show()


print("-------------------------------------")
print(df[['Title', 'Price_GBP', 'Title_Length', 'Price_Segment']].head())


# --- 3. ADVANCED VISUALIZATIONS ---
sns.set_theme(style="whitegrid")

# A. VIOLIN PLOT: Price Density by Rating
# Why this is better than a boxplot: It shows the 'shape' of the data.
# Fat sections mean many books exist at that price point.
plt.figure(figsize=(10, 6))
sns.violinplot(x='Rating', y='Price_GBP', data=df, palette="muted", inner="quartile")
plt.title('Price Density Distribution by Star Rating', fontsize=14)
plt.xlabel('Star Rating')
plt.ylabel('Price (£)')
plt.show()

# B. JOINT PLOT: Title Length vs Price
# Why this matters: Checks if detailed titles imply higher costs.
# We use kind="hex" to handle overlapping points better than a scatter plot.
g = sns.jointplot(x='Title_Length', y='Price_GBP', data=df, kind="hex", color="#4CB391")
g.fig.suptitle('Relationship: Title Length vs Price', y=1.02)
plt.show()

# C. BAR CHART: Top 15 Most Common Words in Titles
# Text Mining: Breaking down titles into individual words
all_titles = " ".join(df['Title']).lower()
# Remove punctuation implies simple replacement
words = [word for word in all_titles.split() if len(word) > 3] # Ignore short words like 'the', 'of'
word_counts = Counter(words).most_common(15)

words_df = pd.DataFrame(word_counts, columns=['Word', 'Count'])

plt.figure(figsize=(12, 6))
sns.barplot(x='Count', y='Word', data=words_df, palette='magma')
plt.title('Top 15 Keywords in Book Titles', fontsize=14)
plt.show()

