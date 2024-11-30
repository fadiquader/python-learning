"""
Public Attributes: Accessible from anywhere.
Protected Attributes: Indicated by a single underscore (_). Intended to be protected from outside access, but still accessible.
Private Attributes: Indicated by double underscores (__). Not accessible from outside the clas
"""

class Employee:
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

# Usage
emp = Employee("Alice", 50000)
emp.display_info()

# Accessing attributes
print(emp.name)               # Public: Accessible
print(emp._department)       # Protected: Accessible, but should be avoided
# print(emp.__salary)        # Private: Raises AttributeError
print(emp.get_salary())      # Access private salary through public method