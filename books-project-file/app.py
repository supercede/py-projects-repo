"""
• Books project that allows users manage their books collection (using file imports)
• Users add new books to the collection which are saved to a books.json file;
• Users can view all the books in their collection;
• Users can find any particular book by any of its attributes
• Users can find mark a book as read
• To use this app, Install Python 3 (If you don't have already), open the containing project folder, and type 'py app.py' on your terminal
"""

from helpers import create_books_file
from utils.database import addBooks, list_books, search_books, delete_book, mark_read

books = create_books_file() or []

user_choice = """
Welcome to your library. Enter one of the following keys:
• 'a' to add a book;
• 'l' to list all books;
• 'r' to read a book;
• 's' to search for a book
• 'd' to delete for a book
• 'q' to quit the program
"""


def menu():
    global books
    user_input = input(user_choice)
    while user_input != 'q':
        if user_input == 'a':
            addBooks(books)
        elif user_input == 'l':
            list_books(books)
        elif user_input == 's':
            search_books(books)
        elif user_input == 'd':
            books = delete_book(books)
        elif user_input == 'r':
            books = mark_read(books)
        user_input = input(user_choice)


menu()
