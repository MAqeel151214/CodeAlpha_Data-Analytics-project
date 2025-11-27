import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
import re # Import the re module for regular expressions

# --- CONFIGURATION ---
BASE_URL = "http://books.toscrape.com/catalogue/page-{}.html"
NUM_PAGES = 5  # Number of pages to scrape (there are 50 total on the site)
data = []

print(f"Starting scrape of first {NUM_PAGES} pages...")

# --- SCRAPING LOOP ---
for page_num in range(1, NUM_PAGES + 1):
    url = BASE_URL.format(page_num)
    response = requests.get(url)

    # Check if request was successful
    if response.status_code != 200:
        print(f"Failed to retrieve page {page_num}")
        continue

    # Parse HTML
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find all book containers (HTML tag: <article class="product_pod">)
    books = soup.find_all('article', class_='product_pod')

    for book in books:
        # 1. Extract Title
        # The title is in the <h3> tag, inside an <a> tag's 'title' attribute
        title_tag = book.find('h3').find('a')
        title = title_tag['title']

        # 2. Extract Price
        # Price is in a <p> tag with class "price_color"
        price_text = book.find('p', class_='price_color').text
        # Use regex to remove all non-digit and non-dot characters, then convert to float
        price = float(re.sub(r'[^\d.]', '', price_text))

        # 3. Extract Star Rating
        # Rating is a class name (e.g., "star-rating Three")
        rating_tag = book.find('p', class_='star-rating')
        # The second class name usually holds the number (e.g., ['star-rating', 'Three'])
        rating_class = rating_tag.get('class')[1]

        # Convert text rating to number
        rating_map = {'One': 1, 'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5}
        rating = rating_map.get(rating_class, 0)

        # 4. Extract Availability
        # Located in <p class="instock availability">
        availability_tag = book.find('p', class_='instock availability')
        availability = availability_tag.text.strip()

        # Append to our list
        data.append({
            'Title': title,
            'Price_GBP': price,
            'Rating': rating,
            'Availability': availability
        })

    print(f"Page {page_num} scraped successfully. ({len(books)} books found)")

    # Good practice: Sleep briefly to be polite to the server
    time.sleep(1)

# --- SAVE DATA ---
# Convert to DataFrame
df = pd.DataFrame(data) # Just creating new DF here

# Display first few rows to verify
print("\nScraping Complete! Preview of data:")
print(df.head())

# Save to CSV for your EDA project
df.to_csv('books_ecommerce_data.csv', index=False)
print("\nData saved to 'books_ecommerce_data.csv'")