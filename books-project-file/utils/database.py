from helpers import save_book_file, display_results


def addBooks(books):
    book = {}
    name = input('Book Title: ')
    author = input('Book Author: ')

    book['name'] = name.lower()
    book['author'] = author.lower()
    book['read'] = False

    books.append(book)
    save_book_file(books)
    print('Book added')


def list_books(book_list):
    if len(book_list) == 0:
        print('There are no books in your collection')
    display_results(book_list)


def search_books(books):
    property = input("Search book by name or author? (Choose one)\n")
    while(property not in ['name', 'author']):
        property = input(
            "You made a wrong selection, you can only search by 'name', or 'author'\n")

    value = input(f"Which {property} would you like to search for: \n")
    search_results = [
        book for book in books if value.lower() in book[property]]
    print()
    if(len(search_results) == 0):
        print("Oops 😞, We couldn't find your book, Please try another search")
    else:
        print('Search Results:')
        display_results(search_results)


def delete_book(book_list):
    name = input('Enter name of book to delete: ')
    while not name:
        name = input('Invalid input, Enter name of book to delete: ')
    updated_list = list(filter(lambda x: x['name'] != name.lower(), book_list))
    if len(book_list) > len(updated_list):
        print(f'{name.title()} deleted from collection')
        save_book_file(updated_list)
        book_list = updated_list
    else:
        print(f'{name.title()} not found')
    return book_list


def mark_read(book_list):
    name = input('Enter name of book to mark as read: ')
    read_book = ''
    for book in book_list:
        if book['name'] == name.lower():
            read_book = book
            print(
                f"Another one to your collection! You have now read {book['name'].title()}.")
            book['read'] = True
            save_book_file(book_list)
    if not read_book:
        print(f'{name.title()} not found in collection')
    return book_list
