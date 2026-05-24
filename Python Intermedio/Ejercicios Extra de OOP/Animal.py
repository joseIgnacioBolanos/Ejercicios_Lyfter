class Animal():
    def __init__(self, name):
        self.name = name

    def speak(self):
        return print('Hace un sonido')
    
class Dog(Animal):
    def speak(self):
        return print("Guau")

class Cat(Animal):
    def speak(self):
        return print('Miau')
    
my_dog= Dog('Bubbles')
my_dog.speak()

my_cat = Cat('Nina')
my_cat.speak()