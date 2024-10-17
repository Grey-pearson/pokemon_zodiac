# takes birth day and age, adds them
# multiplies num by 4
# searches csv for pokemon

import csv

fields = []
rows = []

birth_day = int(input('what day were you born on?: '))

def pokemon_number(birth_day, age):
    age_day = age + birth_day
    pokemon_number = age_day * 4
    return pokemon_number

def full_age_range(birth_day):
    for i in range(80):
        print(f"{i+1}. {pokemon_number(birth_day, i+1)}")


age_range = int(input('if you want just your current age hit 0, if you want to know pokemon for 1-80 press 1: '))

match age_range:
    case 1:
        full_age_range(birth_day)
    case _:
        age = int(input('whats your age?: '))
        print(pokemon_number(birth_day, age))
    

print(f"result of 1 or 0 disition: {age_range}")

