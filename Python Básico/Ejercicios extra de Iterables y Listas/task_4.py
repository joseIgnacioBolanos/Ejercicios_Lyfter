my_numbers= int(input("Digite cuantos numross desea agregar a la lista "))
counter = 1
my_list=[]
my_list2=[]
while counter <= my_numbers:
    list_numbers = int(input("Digite el numero que desea agregar"))
    my_list.append(list_numbers)
    counter+=1

print(my_list)

total_sum=0
for index in range(0, len(my_list)):
    total_sum = total_sum + my_list[index]

average = total_sum / len(my_list)
print(f"El promeido de los numeros ingresados es de {average}")

for index1 in range(0, len(my_list)):
    if my_list[index1] > average:
        my_list2.append(my_list[index1])

print(my_list2)