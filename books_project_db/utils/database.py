import sqlite3

from typing import List, Dict, Union
from .database_conection import DatabaseConnection

Book = Dict[str, Union[str, int]]


def create_book_table() -> None:
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()

        cursor.execute(
            'CREATE TABLE IF NOT EXISTS books(name text primary key not null, author text not null, read integer)')


def insert_book(name: str, author: str) -> None:
    try:
        with DatabaseConnection('data.db') as connection:
            cursor = connection.cursor()
            cursor.execute('INSERT INTO books VALUES(?, ?, 0)', (name, author))

    except sqlite3.IntegrityError:
        print('Error: Name exists in collection')


def get_all_books() -> List[Book]:
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM books')

        books = [{'name': row[0], 'author': row[1], 'read': row[2]}
                 for row in cursor.fetchall()]

    return books


def mark_book_as_read(name: str) -> None:
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()

        cursor.execute(
            'UPDATE books SET read=1 WHERE name=? collate nocase', (name,))


def delete_book(name: List) -> None:
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()
        cursor.execute(
            'DELETE FROM books WHERE name=? collate nocase', (name, ))
