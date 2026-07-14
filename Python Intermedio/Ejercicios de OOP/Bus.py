from Person import Person
class Bus:
    def __init__(self, max_passengers):
        self.max_passengers = max_passengers
        self.passengers = []

    def add_passengers(self, my_person):
        if my_person in self.passengers:
            print('f{my_person} ya existe')
        else:
            if len(self.passengers) < self.max_passengers:
                self.passengers.append(my_person)
            else:
                print("El bus está lleno.")
           
    def remove_passengers(self, p_name):
        if self.passengers:
                found=False
                for person in self.passengers:
                    passenger_name= person.name.lower().strip()
                    if passenger_name == p_name:
                        self.passengers.remove(person)
                        found=True
                if found:
                    print('Pasajero eliminado')
                else:
                    print(f'EL pasajero {p_name} no existe')
        else:
            print('No existen Pasajeros')



my_bus= Bus(3)
continue_adding=True
while continue_adding:
    passenger_name= input('Digite el nombre del Pasajero a agregar').lower().strip()
    my_bus.add_passengers(my_person=Person(passenger_name))
    while True:
        user_answer= input("Digite\n1.Para Continuar agregando\n2.Si no desea agregar mas pasajeros")
        if user_answer == '1':
            break
        elif user_answer == '2':
            continue_adding = False
            break
        else:
            print('Valor Ingresado Invalido')
            continue
    
passenger_to_remove= input('Digite el nombre del pasajero que desea eliminar').lower().strip()
my_bus.remove_passengers(passenger_to_remove)
