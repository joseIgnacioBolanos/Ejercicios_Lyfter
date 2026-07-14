def print_and_return(func):
        def wrapper(*args, **kwargs):
            print(args,kwargs)
            result= func(*args, **kwargs)
            print(result)
            return result 
        return wrapper

@print_and_return
def sums( *args):
        total = 0
        for numbers in args:
            total+=numbers

        return total

@print_and_return
def showPerson(**kwargs):
      text=""
      for key, value in kwargs.items():
            print(f"{key}: {value}")
           

sums(3,4)
showPerson(nombre = 'Jose', edad = 29, apellido = "Bolaños")