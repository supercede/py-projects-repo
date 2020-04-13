import logging
from app import books

logger = logging.getLogger('scraping.menu')


def get_top_books():
    logger.debug('Finding top books...')
    top_books = sorted(books, key=lambda x: x.rating, reverse=True)[:10]
    [print(book) for book in top_books]


def get_cheapest_books():
    logger.debug('Finding cheapest books...')
    cheapest_books = sorted(books, key=lambda x: x.price)[:10]
    [print(book) for book in cheapest_books]


def get_all_books():
    [print(book) for book in books]


next_book = (book for book in books)


def get_next_book():
    logger.debug('Getting next book from all books generator...')
    print(next(next_book))


command_str = '''Hi, welcome to to Activa Books. Please make a choice:
    'b' to view top-rated books
    'c' to view cheapest books
    'n' to get next available book in the catalogue
    'q' to quit: \n
    '''

user_choices = {
    'b': get_top_books,
    'c': get_cheapest_books,
    'n': get_next_book
}


def menu():
    user_input = input(command_str)

    while user_input != 'q':
        if user_input in ['a', 'b', 'c', 'n']:
            user_choices[user_input]()
        else:
            print('Invalid Command')
        user_input = input(command_str)
    logger.debug('Terminating program...')


menu()
