# lists
for i in range(1, 5):
    print(i ** 2)

list = list(range(1, 10, 2))
print(list, min(list), list[0:3])
squares = [i ** 2 for i in range(1, 10)]
squares_1 = [i ** 2 for i in list[:3]]
# Copy a list
squares_2 = squares_1[:]
# Copy but in reverse
squares_2_reversed = squares_1[::-1]
blocks = {n: "x" * n for n in range(5)}  # {0: '', 1: 'x', 2: 'xx', 3: 'xxx', 4: 'xxxx'}

# lists with filter
numbers = [9, -1, -4, 20, 17, -3]
odd_positives = [
    num for num in numbers
    if num > 0
    if num % 2 == 1
]

# Dicts
class Student:
    def __init__(self, name, gpa, major):
        self.name = name
        self.gpa = gpa
        self.major = major


students = [Student('A', 1, 'cs'), Student('B', 2, 'eng'), Student('C', 3, 'med')]
students_by_gpa = sorted(students, key=lambda s: s.gpa)

student_names = { student.name: student.gpa for student in students } # { 'A': 1, 'B': 2 }

# tuples
student_gpas = tuple(student.gpa for student in students if student.major == 'cs') # (1)
"""
The *args syntax allows you to pass a variable number of non-keyword arguments to a function.
Usage: When you prefix a parameter with an asterisk (*), it collects any extra positional arguments
passed to the function into a tuple.
"""

def add_numbers(*args):
    return sum(args)

# Usage
result = add_numbers(1, 2, 3, 4)  # Output: 10
print(result)

"""
The **kwargs syntax allows you to pass a variable number of keyword arguments (i.e., named arguments) to a function.
"""
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

# Usage
print_info(name="Alice", age=30, city="New York")