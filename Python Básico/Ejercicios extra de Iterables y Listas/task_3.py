my_list = [9, 4, 7, 1, 5, -9, -10]

min_number =  my_list[0]

for index in range(0, len(my_list)):
    if my_list[index]< min_number:
        min_number = my_list[index]

print(f"El numero menor de la lista es  {min_number}")