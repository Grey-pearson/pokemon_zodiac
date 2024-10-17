# takes birth day and birth month, adds them
# multiplies num by 4
# searches csv for pokemon

birth_day = int(input('what day were you born on?: '))
age = int(input('whats your age?: '))

age_range = bool(input('if you want just your current age hit 0, if you want to know pokemon for 1-80 press 1'))
print(age_range)

def pokemon_number(birth_day, age):
    age_day = age + birth_day
    pokemon_number = age_day * 4
    return pokemon_number

pokemon = pokemon_number(birth_day, age)
print(pokemon)