"""
• Books project that allows users manage their books collection using sqlite3
• Users add new books to the collection which are saved to a sqlite3 database;
• Users can view all the books in their collection;
• Users can find mark a book as read and delete a book;
• To use this app, Install Python 3 (If you don't have already), open the containing project folder, and type 'py app.py' on your terminal
"""

from utils import database


USER_CHOICE = """
Enter:
- 'a' to add a new book
- 'l' to list all books
- 'r' to mark a book as read
- 'd' to delete a book
- 'q' to quit

Your choice: """


def menu():
    database.create_book_table()
    user_input = input(USER_CHOICE)
    while user_input != 'q':
        if user_input == 'a':
            prompt_add_book()
        elif user_input == 'l':
            list_books()
        elif user_input == 'r':
            prompt_read_book()
        elif user_input == 'd':
            prompt_delete_book()

        user_input = input(USER_CHOICE)


def prompt_add_book():
    name = input('Enter the new book name: ')
    author = input('Enter the new book author: ')

    database.insert_book(name, author)


def list_books():
    for book in database.get_all_books():
        # book[3] will be a falsy value (0) if not read
        read = 'YES' if book['read'] else 'NO'
        print(f"{book['name']} by {book['author']} — Read: {read}")


def prompt_read_book():
    name = input('Enter the name of the book you just finished reading: ')

    database.mark_book_as_read(name)


def prompt_delete_book():
    name = input('Enter the name of the book you wish to delete: ')

    database.delete_book(name)


menu()
