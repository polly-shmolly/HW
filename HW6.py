import json
import csv

data = [
    {
        "name": "John Smith",
        "birthday": "02.10.1990",
        "height": 175,
        "weight": 76.5,
        "car": True,
        "languages": ["C++", "Python"]
    },
    {
        "name": "Alexey Alexeev",
        "birthday": "05.06.1986",
        "height": 197,
        "weight": 101.2,
        "car": False,
        "languages": ["Pascal", "Delphi"]
    },
    {
        "name": "Maria Ivanova",
        "birthday": "28.08.1998",
        "height": 165,
        "weight": 56.1,
        "car": True,
        "languages": ["C#", "C++", "C"]
    }
]

# add data in json
def add_data(data):
    with open('data.json', 'w') as f:
        json.dump(data, f, indent=4)

# from json to csv
def json_to_csv():
    json_data = []
    with open('data.json', 'r') as f:
        json_data = json.load(f)
    with open('data.csv', 'w') as f:
        writer = csv.writer(f, delimiter=',')
        writer.writerow(json_data)

# add new person in data, file json
def add_new_data(data, answer):
    new_data = {
        "name": "",
        "birthday": "",
        "height": None,
        "weight": None,
        "car": None,
        "languages": []
    }
    new_data['name'] = input('Enter name: ')
    new_data['birthday'] = input('Enter Bday: ')
    new_data['height'] = int(input('Enter height: '))
    new_data['weight'] = int(input('Enter weight: '))
    new_data['car'] = bool(input('Enter do person has car (True/False): '))
    amount = int(input('Enter how many languages knows person: '))
    for i in range(amount):
        lang = input('Enter language: ')
        new_data['languages'].append(lang)
    data.append(new_data)
    add_data(data)
    if answer == 4:
        json_to_csv()


# give information after entering name
def name_info(name):
    with open('data.json', 'r') as f:
        lst = json.load(f)
    for i in lst:
        if i['name'] == name:
            for key, value in i.items():
                print(key, value)


# language filter
def lang_filter(language):
    with open('data.json', 'r') as f:
        lst = json.load(f)
    for i in lst:
        for j in i['languages']:
            if j == language:
                print(f'List of employees who use {language=}: ', i['name'])

# height filter
def height_filter(year):
    with open('data.json', 'r') as f:
        lst = json.load(f)
    amount = 0
    temp = 0
    for i in lst:
        year_birth1 = i['birthday']
        a = year_birth1.split('.')
        y = int(a[2])
        if y > year:
            temp += i['height']
            amount += 1
    result = temp / amount
    return result

answer = 0
while answer != 8:
    print('\n1 add data in json\n2 from json to csv\n3 add new person in data, file json')
    print('4 add new person in data, file csv\n5 give information after entering name')
    print('6 language filter\n7 height filter\n8 Exit')
    answer = int(input('\nSelect function to execute: '))
    if answer == 1:
        add_data(data)
    if answer == 2:
        json_to_csv()
    if answer == 3:
        add_new_data(data, 3)
    if answer == 4:
        add_new_data(data, 4)
    if answer == 5:
        name = input('Enter name: ')
        print(name_info(name))
    if answer == 6:
        lang = input('Enter language: ')
        lang_filter(lang)
    if answer == 7:
        year = int(input('Enter year: '))
        print(height_filter(year))

