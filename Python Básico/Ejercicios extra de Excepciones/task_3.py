def convert_to_float(list_of_stings):
    sum_of_floats=0
    for value in list_of_stings:
        try:
            sum_of_floats += float(value)
            print(f"{value} sumado correctamente")
        except ValueError:
            print(f'Elemento inválido: {value}')

    print(f'Total de la suma:  {sum_of_floats}')

def main():
    my_list = ['10', 'manzana', '5.5', '3', 'n/a']
    convert_to_float(my_list)

main()