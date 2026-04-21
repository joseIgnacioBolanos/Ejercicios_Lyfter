seconds = int(input("Ingrese una cantidad de segudos "))
if seconds > 600:
    print("Mayor")
elif seconds < 600:
    missing_seconds = 600 - seconds
    print(f"Falta {missing_seconds}  para llegar a 10 minutos ")
else:
    print("Igual ")