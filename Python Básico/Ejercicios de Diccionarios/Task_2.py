
keys = ['first_name', 'last_name', 'role']
values = [ 'Ignacio' , 'Bolanos','Admin' ]

user_date={}

for key in range(0,len(keys)):
    user_date[keys[key]] = values[key]


print(user_date)