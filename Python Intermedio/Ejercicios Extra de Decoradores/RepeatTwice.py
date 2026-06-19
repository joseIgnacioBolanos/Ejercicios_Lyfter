def repeat_twice(func):
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        func(*args, **kwargs)

    return wrapper
    
@repeat_twice
def printHello(name):
    print(f'Hello, {name}')


printHello('Nacho')
    



