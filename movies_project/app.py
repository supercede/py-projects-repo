"""
• Movie project that allows users manage their movie collecton
• Users add new movies to the collection which are saved to a movies.json file;
• Users can view all the movies in their collection by following the commands;
• Users can find any particular movie by any of its attributes
• To use this app, Install Python 3 (If you don't have already), open the containing project folder, and type 'py app.py' on your terminal
"""

import json
import os

movies = []


def create_movie_file():
    global movies
    check_file = os.path.exists('movies.json')
    if check_file:
        with open('movies.json') as movies_file:
            movies = json.load(movies_file)
    else:
        save_movie_file([])


def save_movie_file(content):
    with open('movies.json', 'w', encoding='utf-8') as movies_file:
        json.dump(content, movies_file, ensure_ascii=False, indent=4)


def check_valid_year(year):
    while not year.isdigit():
        year = input('Please enter a valid year: ')
    return year


def create_movie():
    movie = {}
    print('Add a movie')
    name = input('Movie Title: ')
    year = input('Movie year: ')
    check_valid_year(year)
    director = input(
        'Movie Director(s) (IMPORTANT: separate multiple directors with a comma AND space): ')

    movie['name'] = name.lower()
    movie['year'] = year.lower()
    movie['director'] = [dir.lower() for dir in director.split(', ')]
    movies.append(movie)
    save_movie_file(movies)
    print()
    print(f"{name} added successfully")
    print()
    controller()


def view_movies():
    if len(movies) == 0:
        print('There is no movie in your collection\n')
    else:
        [print(movie) for movie in movies]
        print()
    controller()


def search_movies():
    property = input("Search movie by year, director or name? (Choose one)\n")
    while(property not in ['name', 'director', 'year']):
        property = input(
            "You made a wrong selection, you can only search by 'name', 'director' or 'year'\n")

    value = input(f"Which {property} would you like to search for: \n")
    search_results = [
        movie for movie in movies if value.lower() in movie[property]]

    print()
    if(len(search_results) == 0):
        print("Oops 😞, We couldn't find your movie, Please try another search")
    else:
        [print(result) for result in search_results]

    controller()


def controller():
    command_str = "Enter 'a' to add a movie\n 'l' to see your movies\n 's' to search movies\n 'q' to close the program \n"
    command = input(command_str)

    while (command not in ['a', 'l', 's', 'q']):
        command = input(f"Invalid selection. {command_str}")

    if command == 'a':
        create_movie()
    elif command == 'l':
        view_movies()
    elif command == 's':
        search_movies()
    elif command == 'q':
        quit()


create_movie_file()
controller()
