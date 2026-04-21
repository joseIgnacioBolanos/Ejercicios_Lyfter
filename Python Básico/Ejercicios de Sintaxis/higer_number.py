num1 = int(input("Digite un numero "))
higher_number  = num1

counter=1

while counter<=2:
    num2 = int(input("Digite un  numero "))
    if num2>higher_number:
        higher_number = num2
        counter = counter +1
    else:
        counter=counter+ 1
else:
    print(f"El numero mayor es {higher_number}")