import json

def reading_json_file(my_json):
   
    with open(my_json) as file:
        my_pokemon=json.load(file)

    return my_pokemon
    

def grouping_pokemon_by_type(pokemon_list):
    pokemon_types=[]
    for pokemon in pokemon_list:
        if pokemon['type'][0] in pokemon_types:
            continue
        else:
            pokemon_types.append(pokemon['type'][0])
        
    return(pokemon_types)

def getting_average_of_types(my_pokemon_types, my_pokemon):
    type_average=[]
    for types in my_pokemon_types:
        pokemon_counter=0
        type_counter=0
        for pokemon in  my_pokemon: 
            if pokemon['type'][0]== types:
                pokemon_counter+=1
                type_counter+= pokemon['level']
        
        if pokemon_counter > 0:
            type_average.append(type_counter/pokemon_counter)
        else: 
            type_average.append(0)
            
    for index in range(0, len(my_pokemon_types)):
        print(f"Tipo: {my_pokemon_types[index]} -> Promedio de nivel: {type_average[index]}")

        

def main():
    my_json= "pokemon.JSON"
  
    full_list_of_pokemon=reading_json_file(my_json)
    types=grouping_pokemon_by_type(full_list_of_pokemon)
    getting_average_of_types(types, full_list_of_pokemon )




if __name__ == "__main__":
      main()

