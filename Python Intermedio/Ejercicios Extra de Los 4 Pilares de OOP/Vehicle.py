class Vehicle:
    def __init__(self, brand, year):
        self._brand = brand
        self._year = year

    def get_info(self):
        return f"Marca: {self._brand},\nAño: {self._year}"
    
class Car(Vehicle):
    def __init__(self, doors, brand, year):
        self.doors = doors
        super().__init__(brand, year)


    def get_info(self):
        return f"Carro:\nMarca: {self._brand}\nNumero de Puertas: {self.doors}\nAño: {self._year}\n"
    


class Motorcycle(Vehicle):
    def  __init__(self, motorcycle_type, brand, year):
        super().__init__(brand, year)
        self.motorcycle_type = motorcycle_type

    def get_info(self):
        return f"Moto:\nMarca: {self._brand}\nTipo {self.motorcycle_type}\nAño {self._year}"


car = Car(4, 'Toyota', '2026')
print(car.get_info())

motorcycle = Motorcycle('Automatic', 'Toyota', '2026')
print(motorcycle.get_info())

        