from datetime import date

class User:
    def __init__(self, date_of_birth):
        self.date_of_birth = date_of_birth

    @property
    
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


def check_adult(func):
    def wrapper(*args):
            user_age = args[0].age
            if user_age < 18:
                raise ValueError('Menor de edad')
            
            return func(*args)
    return wrapper

@check_adult
def create_bank_account(user):
     return 'Cuenta creada'

user = User(date(2000,11,3))

result = create_bank_account(user)
print(result)
