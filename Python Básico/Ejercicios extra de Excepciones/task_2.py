def convert_to_int(list_of_stings):
    my_numbers=0
    print('Resultado')
    for value in list_of_stings:
        try:
            my_numbers = int(value)
            print(f'{value} convertido a {my_numbers}')
        except ValueError:
            print(f'No se pudo convertir el elemento: {value}')



def main():
    my_list = ['4', 'hola', '10', '5.2']
    convert_to_int(my_list)

main()