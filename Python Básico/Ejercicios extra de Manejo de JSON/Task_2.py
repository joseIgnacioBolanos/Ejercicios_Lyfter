import json 

def reading_json_and_get_pokemon(json_file):
    with open(json_file) as file:
        my_pokemon= json.load(file)
        pokemon_found=[]
        user_pokemon= input("Ingrese el tipo de pokemon que desea buscar(agua,electrico,fuego etc: " )
        user_pokemon_clean= user_pokemon.lower().strip()

        for pokemon in my_pokemon:

            for pokemon_type in range(0,len(pokemon['type'])):

                pokemon_lower= (pokemon['type'][pokemon_type]).lower()

                if pokemon_lower== user_pokemon_clean:

                    pokemon_found.append(pokemon['name']['english'])

        if pokemon_found:

            print('Los pokemon que existen de ese tipo son: ')
            for my_pokemon in pokemon_found:

                print(my_pokemon)
        else:
            print(f'No existen pokemon del tipo {user_pokemon}')

def main():
    my_json= "pokemon.JSON"
    reading_json_and_get_pokemon(my_json)

if __name__ == "__main__":
      main()

