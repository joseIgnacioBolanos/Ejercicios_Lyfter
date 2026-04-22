my_list = []
my_list2=[]
for index in range(5):
    my_list.append(input("Ingrese una palabra "))
print(my_list)


for index1 in range(0, len(my_list)):
    temp= my_list[index1]
    if len(temp) > 4:
        my_list2.append(temp)

print(my_list2)