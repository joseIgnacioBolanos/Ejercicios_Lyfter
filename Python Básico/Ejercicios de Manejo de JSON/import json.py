import json

def open_json_file(my_json_file):
    with open(my_json_file) as file:
        pokemon_list = json.load(file)

    for pokemon in pokemon_list:
        print(pokemon)
    
    return pokemon_list


def create_pokemon(my_pokemon_list ):
    my_new_pokemon={}
    name={}
    name['english']=validating_string_input('Digite el nombre del pokemon: ')
    my_new_pokemon['name']= name
    my_new_pokemon['level']= validating_int_input(('Digite el nivel: '))
    my_types=[]
    pokemon_types=validating_string_input('Digite su tipo: ')
    my_types.append(pokemon_types)
    my_new_pokemon['type']= my_types
    base={}
    base['HP']=validating_int_input(('Digite el HP del pokemon nuevo: '))
    base['Attack']= validating_int_input(('Digite el ataque del pokemon nuevo: '))
    base['Defense']= validating_int_input(('Digite la defensa del pokemon nuevo: '))
    base['Sp. Attack']=validating_int_input(('Digite el SP. Ataque del pokemon nuevo: '))
    base['Sp. Defense']= validating_int_input(('Digite el SP. Defense del pokemon nuevo: '))
    base['Speed']= validating_int_input(('Digite el Speed del pokemon nuevo: '))
    my_new_pokemon['base']=base

    my_pokemon_list.append(my_new_pokemon)

    for i in my_pokemon_list:
        print(i)
    
    return  my_pokemon_list


def validating_int_input(message):
    while True:
        user_input=input(message)
        try:
            user_input_int= int(user_input)
            return user_input_int
        except ValueError:
            print('Valor ingresado es Invalido')


def validating_string_input(message):
    while True:
        user_input=input(message).strip()
        if user_input.isalpha():
            user_input_capitalized = user_input.capitalize()
            return user_input_capitalized
        else:
            print("Valor ingresado no es Valido")

def rewrite_json_file(my_pokemons):
    with open("pokemon.json", 'w', encoding='utf-8')as file:
        json.dump( my_pokemons, file, indent=4)


def main():
   full_pokemon_list= open_json_file("pokemon.JSON")
   my_pokemon= create_pokemon(full_pokemon_list)
   rewrite_json_file(my_pokemon)



if __name__ == "__main__":
      main()

