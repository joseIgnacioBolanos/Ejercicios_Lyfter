class Rectangle():
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_area(self):
        area = self.width * self.height
        return area
    

    def get_perimeter(self):
        perimeter= (self.width * 2) + (self.height * 2)
        return perimeter
    

def calculate_area():
    try: 
        width_input = float(input('Ingrese la medida del lado del rectangulo '))
        height_input = float(input('Ingrese la medida de la altura del rectangulo '))
        rectangle = Rectangle(width_input,height_input )
        if width_input > 0 and height_input > 0:
            area = rectangle.get_area()
            print(f'El area del rectangulo es {area}')
        else: 
            print('Existe un valor negativo, los valores deben ser positivos')
    except ValueError:
        print('Valor ingresado no valido')


def calculating_perimeter():
    try: 
        width_input = float(input('Ingrese la medida del lado del rectangulo '))
        height_input = float(input('Ingrese la medida de la altura del rectangulo '))
        rectangle = Rectangle(width_input,height_input )
        if width_input > 0 and height_input > 0:
            perimeter = rectangle.get_perimeter()
            print(f'El perimetro del rectangulo es {perimeter}')
        else: 
            print('Existe un valor negativo, los valores deben ser positivos')
    except ValueError:
        print('Valor ingresado no valido')

calculate_area()


calculating_perimeter()

