from selenium import webdriver
from pages.quotes_page import QuotesPage, InvalidTagForAuthorError

try:

    # Method 1, get inputs, then fire browser driver

    author = input('Who would you like to get quotes from? ')
    tag = input('Enter your tag: ')

    chrome = webdriver.Chrome(
        executable_path='/Users/newbu/Desktop/chromedriver/chromedriver.exe')

    chrome.get('http://quotes.toscrape.com/search.aspx')

    quotes_page = QuotesPage(chrome)

    # Method 2 - Fire browser driver, then get input (with tags options)

    # author = input('Who would you like to get quotes from? ')
    # quotes_page.select_author(author)
    # tags = quotes_page.get_available_tags()
    # print('Please select one of the following tags [{}]'.format(' | '.join(tags)))
    # tag = input('Enter your tag: ')

    print(quotes_page.search_for_quotes(author, tag))
except InvalidTagForAuthorError as e:
    print(e)
except Exception as e:
    print(e)
    print('An unknown error occured. Please try again')
