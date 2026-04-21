my_list= []

go = True

while go:
    temp = input("Digite el numero para gregar a la lista. Sino desea continuar ingrese la palabra Salir ")
    if temp == "Salir" or temp == "salir":
        go=False
    else:
        number_to_add= int(temp)
        my_list.append(number_to_add)
    

my_number = int(input("Digite el numero que desee buscar en la lista "))


counter= 0
for index in range(0, len(my_list))    :
    if my_list[index]== my_number:
        counter+=1


print(f"El cantidade de veces que el {my_number} aparece es de: {counter} ")