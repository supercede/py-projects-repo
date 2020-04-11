"""
* A web scrapper that gets quotes from the homepage http://quotes.toscrape.com
* To use, create a python venv and install, using pip, bs4 and requests
* Run 'py app.py'
"""

import requests

from pages.quotes_page import QuotesPage

page_content = requests.get('http://quotes.toscrape.com').content

quotes_page = QuotesPage(page_content)

for quote in quotes_page.quotes:
    print(quote)
