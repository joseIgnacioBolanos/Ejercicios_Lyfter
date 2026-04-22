entred_number = int(input("Digite un numero del 1 al 10 "))
counter = 1

for i in range(12):
    total= entred_number * counter
    print(f"{entred_number} X {counter} = {total}" )
    counter = counter +1