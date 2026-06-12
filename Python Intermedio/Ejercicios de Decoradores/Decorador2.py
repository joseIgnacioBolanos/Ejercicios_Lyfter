class Numbers:
    def verifyingNumbers(func):
        def wrapper(self, *args):
            for number in args:
                if not isinstance(number, int) and not isinstance(number, float):
                    raise ValueError('No todos los valores son numeros')
                
            sum_total= func(self,*args)
            return sum_total
        return wrapper
    
    @verifyingNumbers
    def sum(self,  *args):
        total = 0
        for num in args:
            total += num
        return total
    

numbers = Numbers()
print(numbers.sum( 1,2,3,4,5,6))
