import re
import logging

from locators.book_content_locator import BookContentLocator

logger = logging.getLogger('scraping.book_parser')


class Book:
    """
    A class to take in an HTML page and find properties of a selected item in it
    """

    RATING = {
        'One': 1,
        'Two': 2,
        'Three': 3,
        'Four': 4,
        'Five': 5
    }

    def __init__(self, parent):
        logger.debug(f'New book parser created from parent')
        self.parent = parent

    def __repr__(self):
        return f'<BOOK name: {self.name} \n price: {self.price} \n rating: {self.rating} star{"s" if self.rating > 1 else ""} \n availability: {self.is_available} \n details: http://books.toscrape.com/{self.details}> \n'

    @property
    def name(self):
        logger.debug('Finding book name')
        locator = BookContentLocator.NAME
        book_name = self.parent.select_one(locator)
        name = book_name.attrs['title']
        logger.debug(f'Found book name, `{name}`.')
        return name

    @property
    def price(self):
        logger.debug('Finding book price')
        # pattern = '[0-9]+\.[0-9]+'
        locator = BookContentLocator.PRICE
        book_price = self.parent.select_one(locator).string
        # price_str = re.findall(pattern, book_price)[0]
        # price_float = float(price_str)
        logger.debug(f'Found book price, `{book_price}`.')
        return book_price

    @property
    def rating(self):
        logger.debug('Finding book rating')
        locator = BookContentLocator.RATING
        book_rating = self.parent.select_one(locator)
        rating_class = book_rating.attrs['class']
        rating = filter(lambda x: x != 'star-rating', rating_class)
        rating_number = Book.RATING.get(next(rating))
        logger.debug(f'Found book rating, `{rating_number}`.')
        return rating_number

    @property
    def is_available(self):
        logger.debug('Checking book availability')
        locator = BookContentLocator.AVAILABLE
        book_availability = self.parent.select_one(locator).attrs['class']
        availability_gen = filter(
            lambda x: x != 'availability', book_availability)
        availability = next(availability_gen)
        logger.debug(f'Found book availability, `{availability}`.')
        return availability

    @property
    def details(self):
        logger.debug('Finding book details')
        locator = BookContentLocator.DETAILS_LINK
        book_details = self.parent.select_one(locator)
        details = book_details.attrs['href']
        logger.debug(f'Found book details, `{details}`.')
        return details
