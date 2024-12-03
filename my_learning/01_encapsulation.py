import re

"""
Public Attributes: Accessible from anywhere.
Protected Attributes: Indicated by a single underscore (_). Intended to be protected from outside access, but still accessible.
Private Attributes: Indicated by double underscores (__). Not accessible from outside the clas
"""

class Employee:
    # Static attribute to count the number of employees
    employee_count = 0

    def __init__(self, name, salary):
        self.name = name              # Public attribute
        self._department = "HR"      # Protected attribute
        self.__salary = salary        # Private attribute

    def get_salary(self):            # Public method to access private attribute
        return self.__salary

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Department: {self._department}")
        print(f"Salary: {self.get_salary()}")

    @property # hybrid property: you can't call it as function or set the value
    def name_with_department(self):
        return f"{self.name} ({self._department})"

    @staticmethod
    def calculate_annual_salary(hourly_wage, hours_per_week):
        """Calculate the annual salary based on hourly wage and hours worked per week."""
        return hourly_wage * hours_per_week * 52  # Assuming 52 weeks in a year
# Usage
emp = Employee("Alice", 50000)
emp.display_info()
print(emp.name_with_department) # Alice HR

# Accessing attributes
print(emp.name)               # Public: Accessible
print(emp._department)       # Protected: Accessible, but should be avoided
# print(emp.__salary)        # Private: Raises AttributeError
print(emp.get_salary())      # Access private salary through public method

class Ticket:
    def __init__(self, price):
        self._price = price

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, new_price):
        if new_price < 0:
            raise ValueError("Nice try")
        self._price = new_price

# Return an instance of the same class from a function
class Money:
    def __init__(self, dollars, cents):
        self.dollars = dollars
        self.cents = cents

    @classmethod
    def from_pennies(cls, total_cents):
        dollars = total_cents // 100
        cents = total_cents % 100
        return cls(dollars, cents)

    @classmethod
    def from_string(cls, amount):
        match = re.search(
            r'^\$(?P<dollars>\d+)\.(?P<cents>\d\d)$', amount)
        if match is None:
            raise ValueError(f"Invalid amount: {amount}")
        dollars = int(match.group('dollars'))
        cents = int(match.group('cents'))

        return cls(dollars, cents)

piggie_bank_cash = Money.from_pennies(3217)