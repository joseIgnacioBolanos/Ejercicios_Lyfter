my_list=[]
my_list2=[]
for index in range(10):
    temp = int(input("Digite un numero "))
    my_list.append(temp)

print(my_list)



while len(my_list)!= 0:
    index1=0
    temp=0
    higher_number = my_list[0]

    while index1<= len(my_list)-1:
        if(my_list[index1]> higher_number):
            higher_number = my_list[index1]
            temp= index1
            index1+=1
        else:
            index1+=1
    my_list2.append(higher_number)
    my_list.pop(temp)
print(my_list2)

