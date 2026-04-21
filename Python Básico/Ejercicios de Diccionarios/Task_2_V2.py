
user_attributes = ['first_name', 'last_name', 'role']
user_values = [ 'Ignacio' , 'Bolanos','Admin' ]

result_dict={}

for key in range(0,len(user_attributes)):
    result_dict[user_attributes[key]] = user_values[key]


print(result_dict)