from abc import ABC, abstractmethod
import math

class Shape(ABC):

    @abstractmethod
    def calculate_perimeter(self): 
        pass

    @abstractmethod
    def calculate_area(self):
        pass


class Circle(Shape):
    def __init__(self, radio):
        self.radio = radio

    def calculate_area(self):
        area= math.pi * self.radio**2
        return area
    
    def calculate_perimeter(self):
        perimeter = 2*math.pi*self.radio
        return perimeter

    
class Square(Shape):
    def __init__(self, side):
        self.side = side

    def calculate_area(self):
        area = self.side**2
        return area
    
    def calculate_perimeter(self):
        perimeter = self.side * 4
        return perimeter
    

class Rectangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height 


    def calculate_area(self):
        area = self.base * self.height
        return  area
        
    
    def calculate_perimeter(self):
        perimeter =  2*(self.base + self.height)
        return perimeter
    


circle = Circle(24)
print(circle.calculate_area())
print(circle.calculate_perimeter())

square = Square(24)
print(square.calculate_area())
print(square.calculate_perimeter())

rectangle = Rectangle(10, 20)
print(rectangle.calculate_area())
print(rectangle.calculate_perimeter())




    
        



        