"""
• A webscraper app that gets weather forecast from https://forecast.weather.gov
• Weather info is compiled into a dataframe and saved as a csv file using the pandas module
• To use this app
    * Install Python 3 (If you don't have already), create a python virtual environment, 
    * Install pandas, requests and BeautifulSoup modules
    * Run the program by typing 'py weather-scraper.py' in your terminal
"""

import pandas as pd
import requests
from bs4 import BeautifulSoup

page = requests.get(
    'https://forecast.weather.gov/MapClick.php?lat=18.4594&lon=-66.1935#.XnjYeYhKiCg')
soup = BeautifulSoup(page.content, 'html.parser')

div_container = soup.find(id="seven-day-forecast-body")
items = div_container.find_all(class_="tombstone-container")

period_names = [item.find(class_='period-name').get_text() for item in items]
descriptions = [item.find(class_='short-desc').get_text() for item in items]
temperatures = [item.find(class_='temp').get_text() for item in items]

# print()
# print(period_names)
# print(descriptions)
# print(temperatures)

weather_stuff = pd.DataFrame(
    {
        'period': period_names,
        'short_descriptions': descriptions,
        'temperatures': temperatures,
    }
)

print(weather_stuff)
weather_stuff.to_csv('weather.csv')
