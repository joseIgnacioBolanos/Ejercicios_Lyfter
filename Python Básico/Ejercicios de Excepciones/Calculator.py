def sum(actual_number, user_number):
    sum_result=0
    sum_result= actual_number + user_number
    print(f'El resultado de la suma de {actual_number} mas {user_number} es de {sum_result}')
    return sum_result
    

def division(actual_number, user_number):
    division_result = 0
    try:
        division_result= actual_number / user_number
        print(f'El resultado de la division de {actual_number} entre {user_number} es de {division_result}')
        return division_result
    except ZeroDivisionError as e:
        print(f"Error [ZeroDivisionError]: Intentaste dividir {actual_number} entre 0. Detalles: {e}")
        return actual_number
    

def multiply(actual_number, user_number):
    multiplication_result = 0
    multiplication_result = actual_number * user_number
    print(f'El resultado de la multiplicacion  de {actual_number} por {user_number} es de {multiplication_result}')
    return multiplication_result
    

def subtract(actual_number, user_number):
    subtract_result= 0 
    subtract_result = actual_number - user_number
    print(f'El resultado de la resta de {actual_number} menos {user_number} es de {subtract_result}')
    return subtract_result
    

def asking_user_number():
    cont= True
    while cont:
        try:
            user_name= int(input('Digite un numero'))
            return user_name
        except ValueError:
            print('Valor ingresado no válido')
    

def menu():
    cont=True
    actual_number = 4
    while cont:
        try:
            user_option= int(input('Digite: \n1. Para Suma\n2. Para Resta \n3. Para Multiplicar\n4. Para Division\n5. Para Borrar Resultado\n'))
            if user_option == 1:
                actual_number= sum(actual_number, asking_user_number() )
            elif user_option == 2:
                actual_number=subtract(actual_number, asking_user_number() )
            elif user_option == 3:
                actual_number=multiply(actual_number, asking_user_number() )
            elif user_option== 4:
                actual_number=division(actual_number, asking_user_number() )
            elif user_option==5:
                actual_number =0
            else:
               print("Ingrese una opcion valida!")
        except ValueError as ex:
            print("Opcion Invalida!")
            

def main():   
    menu()


main()


