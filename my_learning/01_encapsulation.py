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

    @staticmethod
    def calculate_annual_salary(hourly_wage, hours_per_week):
        """Calculate the annual salary based on hourly wage and hours worked per week."""
        return hourly_wage * hours_per_week * 52  # Assuming 52 weeks in a year
# Usage
emp = Employee("Alice", 50000)
emp.display_info()

# Accessing attributes
print(emp.name)               # Public: Accessible
print(emp._department)       # Protected: Accessible, but should be avoided
# print(emp.__salary)        # Private: Raises AttributeError
print(emp.get_salary())      # Access private salary through public method