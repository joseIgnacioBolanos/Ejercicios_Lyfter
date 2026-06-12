from datetime import date

class User:
    def __init__(self, date_of_birth):
        self.date_of_birth = date_of_birth

    def isAdult(func):
        def wrapper(self):
            user_age = func(self)
            if user_age < 18:
                raise ValueError('Menor de edad')
            return user_age
        return wrapper

    @property
    @isAdult
    def age(self):
        today = date.today()

        return (

            today.year

            - self.date_of_birth.year

            - (

                (today.month, today.day)

                < (self.date_of_birth.month, self.date_of_birth.day)

            )

        )

    

user = User(date(2017,11,3))
print(user.age)