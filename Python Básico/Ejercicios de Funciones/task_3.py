def sum_list_numbers(my_list):
    total = 0
    for number in my_list:
        total+=  number

    return print(f'El resultado de la suma de los numeros es  {total}')


def main():
    my_list_number=[4, 6, 2, 29] 
    sum_list_numbers(my_list_number)

main()