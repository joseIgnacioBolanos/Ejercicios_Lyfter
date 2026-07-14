class Employee:
    def __init__(self, name, salary):
            self.salary = salary
            self._name = name

    @property
    def name(self):
        return self._name
    
    @property
    def salary(self):
        return self._salary
    
    @salary.setter
    def salary(self, salary_value):
        if salary_value < 0:
            raise ValueError("El salario no puede ser negativo")
        else:
            self._salary = salary_value

    def promote(self, salary_increase):
        new_salary = self._salary + (self._salary * salary_increase)
        self.salary= new_salary

try: 
    employee =  Employee('Ana', -1000)
    employee.promote(0.1)
    print(employee.salary)
except ValueError as error:
    print(error)