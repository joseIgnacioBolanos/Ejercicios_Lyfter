my_list=[]

for index in range(10):
   

    temp = int(input("Digite un numero ")) 
    my_list.append(temp)
    if index == 0:
        higher_number = temp
    else:
        if temp> higher_number:
            higher_number = temp
    
print(f"{my_list}. El numero mayor es {higher_number}")




