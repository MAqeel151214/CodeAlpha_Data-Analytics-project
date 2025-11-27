```markdown
# 🕸️ Module 1: Web Scraping

## 🎯 Objective
To build an automated script that navigates through multiple pages of an e-commerce website to harvest product data for analysis.

## ⚙️ How it Works
The script `book_scraper.py` performs the following steps:
1.  **HTTP Request:** Sends `GET` requests to `http://books.toscrape.com`.
2.  **HTML Parsing:** Uses `BeautifulSoup` to locate specific HTML tags (`<article>`, `<h3>`, `<p class="price_color">`).
3.  **Pagination:** Loops through 50 pages of the catalogue automatically.
4.  **Data Cleaning (On-the-fly):**
    *   Removes currency symbols (£).
    *   Converts text ratings ("Three") to integers (3).
    *   Strips whitespace from text fields.

## 📄 Output
The script generates `books_ecommerce_data.csv` containing:
*   `Title`: Name of the book.
*   `Price_GBP`: Price in numeric format.
*   `Rating`: Star rating (1-5).
*   `Availability`: Stock status.

## 💻 Code Snippet
```python
# Example of extraction logic
price_text = book.find('p', class_='price_color').text
price = float(re.sub(r'[^\d.]', '', price_text))
```
