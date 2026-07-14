def verifyingNumbers(func):
    def wrapper(*args):
            for number in args:
                if not isinstance(number, int) and not isinstance(number, float):
                    raise ValueError('No todos los valores son numeros')
                
            sum_total= func(*args)
            return sum_total
    return wrapper
    
@verifyingNumbers
def sum( *args):
        total = 0
        for num in args:
            total += num
        return total
    


print(sum( 1,2,3,4,5,6, "m"))
