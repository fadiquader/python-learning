"""
Operator overloading allows you to define how operators behave with custom objects.
"""

class Money:
    def __init__(self, amount):
        self.amount = amount

    def __add__(self, other):
        return Money(self.amount + other.amount)

    def __str__(self):
        return f"${self.amount}"

money1 = Money(50)
money2 = Money(75)
total = money1 + money2
print(total)  # Output: $125