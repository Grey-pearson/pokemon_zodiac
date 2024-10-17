# takes birth day and birth month, adds them
# multiplies num by 4
# searches csv for pokemon

birth_day = int(input('what day were you born on?: '))
birth_month = int(input('what month (number) where you born in?: '))

def pokemon_number(birth_day, birth_month):
    birth_number = birth_month + birth_day
    pokemon_number = birth_number * 4
    return pokemon_number

pokemon = pokemon_number(birth_day, birth_month)
print(pokemon)