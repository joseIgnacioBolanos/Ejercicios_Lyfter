def check_if_name_is_valid(user_name):
    if user_name.isdigit():
        raise ValueError('El nombre no puede ser un número')
   

def check_if_age_is_valid(user_age):
    try:
        number_int = int(user_age)
    except ValueError:
        raise ValueError("Ingrese una edad valida!")
    
    if number_int < 1 or number_int >100:
            raise ValueError('Número no valido')
        
def main():
    try:
        my_name = input('Digite su nombre ')
        check_if_name_is_valid(my_name)
        my_age = input('Digite su edad ')
        check_if_age_is_valid(my_age)
        print(f'Hola {my_name}, su edad es {my_age}')
    except ValueError as ex:
        print(ex)

main()