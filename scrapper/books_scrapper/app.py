import logging
import requests

from pages.book_page import BooksPage

# logs are generated in a logs.txt file, although most of them are debugs logs and not printed.
# To see debug logs as well, change level in basicConfig below to logging.DEBUG

logging.basicConfig(format='%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s',
                    datefmt='%d-%m-%Y %H:%M:%S', level=logging.INFO, filename='logs.txt')

logger = logging.getLogger('scraping')

logger.info('Loading books list')

books_page_content = requests.get(
    'http://books.toscrape.com', timeout=20).content

page = BooksPage(books_page_content)

books = page.books

# There are 50 pages and 1000 books in total, change page.page_count to between 1 and 50 in case of slow response (>120 seconds)
for page_num in range(1, page.page_count):
    url = f'http://books.toscrape.com/catalogue/page-{page_num + 1}.html'
    books_page_content = requests.get(url).content
    logger.debug('Creating BooksPage from page content')
    page = BooksPage(books_page_content)
    books.extend(page.books)
