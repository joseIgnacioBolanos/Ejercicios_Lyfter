class BankAccount():
    def __init__(self, balance):
        self.balance = balance

    def _addBalance(self, amount):
        self.balance+= amount

    def substract_balance(self, amount):
        self.balance = self.balance - amount
        return self.balance

class SavingsAccount(BankAccount):
    def __init__(self, min_balance, balance):
        super().__init__(balance)
        self.min_balance = min_balance

        

    def substract_balance(self, amount):
        temp_balance= self.balance - amount
        if temp_balance < self.min_balance:
            print('Su saldo no es suficiente para retrirar el dinero deseado')
        else:
            current_balance = BankAccount.substract_balance(self,amount)
            print(f'Retire su dinero. Saldo actual es de: {current_balance}')


my_SavingsAccount = SavingsAccount(2000, 5000)
my_SavingsAccount.substract_balance(2000)
print(my_SavingsAccount.balance)