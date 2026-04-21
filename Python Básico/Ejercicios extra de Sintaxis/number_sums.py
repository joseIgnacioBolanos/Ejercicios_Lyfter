entered_number = int(input("Ingrese un numero "))
counter = 1
total = 0
while counter <= entered_number:
    total = total + counter 
    counter = counter +1

print(f"El total de la suma de todos los numeros hasta el {entered_number} es de {total}")