import requests

from pages.quotes_page import QuotesPage

page_content = requests.get('http://quotes.toscrape.com').content

quotes_page = QuotesPage(page_content)

for quote in quotes_page.quotes:
    print(quote)
