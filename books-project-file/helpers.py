import json
import os


def create_books_file():
    global books
    check_file = os.path.exists('books.json')
    if check_file:
        with open('books.json') as books_file:
            books = json.load(books_file)
            return books
    else:
        save_book_file([])


def save_book_file(content):
    with open('books.json', 'w', encoding='utf-8') as books_file:
        json.dump(content, books_file, ensure_ascii=False, indent=4)


def display_results(results):
    [print(f"{result['name'].title()} by {result['author'].title()} - { '(read)' if result['read'] else '(unread)' }")
     for result in results]
