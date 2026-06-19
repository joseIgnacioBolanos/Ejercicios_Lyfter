import time


def log_call(func):
    def wrapper(*args, **kwargs):
        print(func.__name__)
        print(*args, **kwargs)
        print(time.ctime())
        result = func(*args, **kwargs)
        print(result)
        return result
    return wrapper

def validate_numbers(func):
    def wrapper(*args, **kwargs):
        for number in args:
            if not isinstance(number, (int,float)):
                raise ValueError('No es un numero')

        return func(*args, **kwargs) 
    return wrapper

@validate_numbers
@log_call
def multiply(num1, num2):
    total = 0
    total = num1 * num2
    return total

letter = "nona"
result = multiply(8,9)
print(result)



