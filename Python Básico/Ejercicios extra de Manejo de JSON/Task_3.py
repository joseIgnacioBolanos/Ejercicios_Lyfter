import json

def reading_json_and_get_pokemon(my_json):
    with open(my_json) as file:
        my_pokemon=json.load(file)

        for pokemon in my_pokemon:
            print(f"Nombre: {pokemon['name']['english']}")
            print(f"HP: {pokemon['base']['HP']}")
            print(f"Ataque: {pokemon['base']['Attack']}")
            print(f"Defensa: {pokemon['base']['Defense']}")
            print(f"Sp. Ataque: {pokemon['base']['Sp. Attack']}")
            print(f"Sp. Defensa: {pokemon['base']['Sp. Defense']}")
            print(f"Speed: {pokemon['base']['Speed']}")
            print('\n')


def main():
    my_json= "pokemon.JSON"
    reading_json_and_get_pokemon(my_json)


if __name__ == "__main__":
      main()

