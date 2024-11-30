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