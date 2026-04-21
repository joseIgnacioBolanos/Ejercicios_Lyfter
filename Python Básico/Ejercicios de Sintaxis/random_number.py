import random 

secret_number = random.randint(1, 10)

user_number = int(input("Adivina el numero secreto del 1 al 10 "))

while user_number != secret_number:
    user_number = int(input("Intenta de nuevo! Adivina el numero secreto "))

    if user_number == secret_number:
        break

print("Lo Adivinaste")
