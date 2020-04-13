# Web Scraping with Selenium

This is a variant of the quotes scraper project (in the previous folder) with a browser automation tool (Selenium).

A different webpage from the [quotes to scrape website](http://quotes.toscrape.com/search.aspx) which is usually generated with Javascript is scraped and Selenium is used to execute select and click actions to get quotes which is printed to the terminal.

To use this app on your local:

- Download [chromedriver](https://chromedriver.chromium.org/downloads) or any browser driver of your choice (Change Selenium configuration settings if you're using a different browser)
- Clone this project and go to the automation/quotes_scrapper folder
- Create a python virtual environment
- Install Selenium
- Run py app.py