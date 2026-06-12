class Calculator:
       
    def summingNumbers(func):
        def wrapper(*args):
            print(*args)
            result= func(*args)
            print(result)
            return result 
        return wrapper

    @summingNumbers
    def sums(self, *args):
        total = 0
        for numbers in args:
            total+=numbers

        return total

sum1 = Calculator()
sum1.sums(5,8)