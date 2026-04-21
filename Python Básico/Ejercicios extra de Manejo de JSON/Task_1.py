import json

def read_json_file(json_file):
    with open(json_file) as file:
        pokemon_list= json.load(file)

        for pokemon in pokemon_list:
            print(f"Nombre: {pokemon['name'].get('english')}")
            print(f"Nivel: {pokemon['level']}")
            print(f"Tipo: {pokemon['type'][0]}")
            print(f"Base: HP:{pokemon['base'].get('HP')}, Attack:{pokemon['base'].get('Attack')}, Defensa:{pokemon['base'].get('Defense')}, SP. Ataque:{pokemon['base'].get('Sp. Attack')}, Sp. Defense: {pokemon['base'].get('Sp. Defense')}, Speed: {pokemon['base'].get('Speed')} ")
            print('\n')

def main():
    my_json= "pokemon.JSON"
    read_json_file(my_json)



if __name__ == "__main__":
      main()
