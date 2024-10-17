# takes birth day and birth month, adds them
# multiplies num by 4
# searches csv for pokemon

birth_day = int(input('what day were you born on?: '))
age = int(input('whats your age?: '))

def pokemon_number(birth_day, age):
    birth_number = age + birth_day
    pokemon_number = birth_number * 4
    return pokemon_number

pokemon = pokemon_number(birth_day, age)
print(pokemon)