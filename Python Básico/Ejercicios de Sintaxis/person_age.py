name = input("Digite su nombre ")
last_name = input("Digite su Apellido ")
age =  int(input("Digite su edad "))

if age <= 2:
    print ("Eres un Bebé ")
elif age <= 11:
    print ("Eres un Niño ")
elif age <= 12:
    print ("Eres un Preadolescente ")
elif  age <= 17:
    print ("Eres un Adolescente ")
elif age <= 35:
    print ("Eres un Adulto Joven ")
elif age<= 59:
    print ("Eres un Adulto ")
else:
    print ("Eres un Adulto Mayor ")



