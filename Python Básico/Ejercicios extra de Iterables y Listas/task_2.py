my_list = [3, 6, 1, 2, 4, -9]

counter=0
for index in range(0, len(my_list)):
    if my_list[index]<=0:
        counter+=1

if counter >= 1:
    print("Hay al menos un número negativo o cero")
else:
    print("Todos son positivos")