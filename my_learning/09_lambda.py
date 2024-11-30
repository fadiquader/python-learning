"""
Lambda Function
a small anonymous function defined using the lambda keyword.
It can take any number of arguments but can only have a single expression.
Lambda functions are often used for short, throwaway functions where
defining a full function using def would be overkill.

Syntax
lambda arguments: expression

Characteristics of Lambda Functions
1. Anonymous: Lambda functions do not have a name (unless you assign them to a variable).
2. Single Expression: They can only consist of a single expression, which is evaluated and returned.
3. Useful for Functional Programming: They are often used in conjunction with functions like map(), filter(), and reduce().
"""
from functools import reduce

# A simple lambda function to add two numbers
add = lambda x, y: x + y
result = add(3, 5)  # Output: 8
print(result)

# Using with map()
numbers = [1, 2, 3, 4, 5]
squared = map(lambda x: x ** 2, numbers)

# Convert map object to list and print
print(list(squared))  # Output: [1, 4, 9, 16, 25]

# Using with filter()
numbers = [1, 2, 3, 4, 5, 6]
even_numbers = filter(lambda x: x % 2 == 0, numbers)

# Convert filter object to list and print
print(list(even_numbers))  # Output: [2, 4, 6]

# Using with sorted()
students = [
    {'name': 'Alice', 'grade': 90},
    {'name': 'Bob', 'grade': 75},
    {'name': 'Charlie', 'grade': 85}
]

# Sort students by grade
sorted_students = sorted(students, key=lambda student: student['grade'])
print(sorted_students)

numbers = [1, 2, 3, 4]

# Using reduce with an initializer to sum the numbers, starting from 10
total_with_initializer = reduce(lambda x, y: x + y, numbers, 10)

print(total_with_initializer)  # Output: 20 (10 + 1 + 2 + 3 + 4)

# convert list to dict
list_of_tuples = [('a', 1), ('b', 2), ('c', 3)]
# Using reduce to convert list of tuples to a dictionary
result_dict = reduce(lambda acc, item: {**acc, item[0]: item[1]}, list_of_tuples, {})
print(result_dict)  # Output: {'a': 1, 'b': 2, 'c': 3}

# Immediately invoked function
(lambda x: x**4)(3)

