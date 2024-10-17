# takes birth day and birth month, adds them
# multiplies num by 4
# searches csv for pokemon

birth_day = int(input('what day were you born on?: '))
age = int(input('whats your age?: '))

def pokemon_number(birth_day, age):
    age_day = age + birth_day
    pokemon_number = age_day * 4
    return pokemon_number

def full_age_range(birth_day, age):
    for 

age_range = int(input('if you want just your current age hit 0, if you want to know pokemon for 1-80 press 1: '))

match age_range:
    case 1:
        full_age_range(birth_day, age)
    case _:
        pokemon_number(birth_day, age)
    

print(age_range)
print(full_age_range)

