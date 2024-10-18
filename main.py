# takes birth day and age, adds them
# multiplies num by 4
# searches csv for pokemon

import csv

fields = []
rows = []

with open('Pokemon.csv', mode='r') as file:
    csv_reader = csv.DictReader(file)
    data_list = []
    for row in csv_reader:
        data_list.append(row)

# for data in data_list:
#     print(data)

# print(data_list[0]['Name'])

birth_day = int(input('what day were you born on?: '))

def pokemon_number(birth_day, age):
    age_day = age + birth_day
    pokemon_number = age_day * 4
    print(f"Your pokemon is {data_list[pokemon_number-1]['Name']} and the type is {data_list[pokemon_number-1]['Type']}")

def full_age_range(birth_day):
    for i in range(80):
        age_day = (i + 1) + birth_day
        pokemon_number = age_day * 4
        print(f"Age {i+1}, pokemon is {data_list[pokemon_number-1]['Name']}, type is {data_list[pokemon_number-1]['Type']} INT {data_list[pokemon_number-1]['ID']}")


age_range = int(input('if you want just your current age hit 0, if you want to know pokemon for 1-80 press 1: '))

match age_range:
    case 1:
        full_age_range(birth_day)
    case _:
        age = int(input('whats your age?: '))
        pokemon_number(birth_day, age)

