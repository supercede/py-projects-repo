import re
import logging
from bs4 import BeautifulSoup

from locators.book_page_locator import BooksPageLocator

from parsers.books_parser import Book

logger = logging.getLogger('scraping.books_page')


class BooksPage:
    def __init__(self, page):
        logger.debug('Parsing page content with beautiful soup')
        self.soup = BeautifulSoup(page, 'html.parser')

    @property
    def books(self):
        logger.debug(f'Finding all books using `{BooksPageLocator.BOOK}`.')
        locator = BooksPageLocator.BOOK
        books_collection = self.soup.select(locator)
        return [Book(el) for el in books_collection]

    @property
    def page_count(self):
        logger.debug(f'Finding number of pages available.')
        locator = BooksPageLocator.PAGER
        content = self.soup.select_one(locator).string
        logger.info(f'Found number of catalogue pages available: `{content}`.')
        pattern = 'Page [0-9]+ of ([0-9]+)'
        matcher = re.search(pattern, content)
        pages = int(matcher.group(1))
        logger.debug(f'Extracted number of pages as integer: `{pages}`.')
        return pages
