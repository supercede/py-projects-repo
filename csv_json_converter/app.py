'''
* App to convert file from csv to json file
* file is imported from file.csv and saved to file.json
'''

import csv
import json

with open('file.csv', 'r') as file:
    csv_file = file.readlines()
    csv_body = [line.strip() for line in csv_file[1:]]

csv_list = []
for prop in csv_body:
    [name, age, univerity, degree] = prop.split(',')
    prop_dict = {
        'name': name,
        'age': age,
        'university': univerity,
        'degree': degree
    }
    csv_list.append(prop_dict)

with open('file.json', 'w') as json_file:
    json.dump(csv_list, json_file, indent=4)
