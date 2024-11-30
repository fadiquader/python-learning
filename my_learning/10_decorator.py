"""
A decorator is a special type of function that can modify or enhance the behavior of another function or method.
Decorators are commonly used to add functionality to existing code in a clean and readable way,
without modifying the original function.
"""

# A Simple Decorator
def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()  # Call the original function
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

# Usage
say_hello()

# A Decorator with Arguments
def repeat(num_times):
    def decorator_repeat(func):
        def wrapper(*args, **kwargs):
            for _ in range(num_times):
                func(*args, **kwargs)
        return wrapper
    return decorator_repeat

@repeat(num_times=3)
def greet(name):
    print(f"Hello, {name}!")

# Usage
greet("Alice")