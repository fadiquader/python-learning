import time

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

# Class based decorator
# A class-based decorator that measures the execution time of a function.
class Timer:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        start_time = time.time()  # Record the start time
        result = self.func(*args, **kwargs)  # Call the original function
        end_time = time.time()    # Record the end time
        print(f"Function '{self.func.__name__}' executed in {end_time - start_time:.4f} seconds")
        return result

# Usage
@Timer
def slow_function():
    time.sleep(2)  # Simulate a slow operation
    print("Finished processing")

# Call the decorated function
slow_function()

# Class-Based Decorator with State
class CallCounter:
    def __init__(self, func):
        self.func = func
        self.call_count = 0  # Initialize call count

    def __call__(self, *args, **kwargs):
        self.call_count += 1  # Increment call count
        print(f"Call count: {self.call_count}")
        return self.func(*args, **kwargs)  # Call the original function

# Usage
@CallCounter
def greet(name):
    print(f"Hello, {name}!")

# Call the decorated function multiple times
greet("Alice")  # Call count: 1
greet("Bob")    # Call count: 2
greet("Charlie")  # Call count: 3

# Class-Based Decorator with State with a parameter


Copy
class Repeat:
    def __init__(self, times):
        self.times = times  # Store the number of times to repeat

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            for _ in range(self.times):
                result = func(*args, **kwargs)  # Call the original function
            return result
        return wrapper

# Usage
@Repeat(times=3)
def greet(name):
    print(f"Hello, {name}!")

# Call the decorated function
greet("Alice")

# Decorators for Classes
# A class decorator that adds a custom string representation to any class it decorates.
def add_repr(cls):
    cls.__repr__ = lambda self: f"{self.__class__.__name__}(name={self.name}, age={self.age})"
    return cls

@add_repr
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# Usage
person = Person("Alice", 30)
print(person)  # Output: Person(name=Alice, age=30)

# A class decorator for access control, ensuring that certain methods can only be
# called by instances of the class that have a specific attribute.
def requires_attribute(attr_name):
    def decorator(cls):
        original_method = cls.method  # Save a reference to the original method

        def new_method(self, *args, **kwargs):
            if not hasattr(self, attr_name):
                raise AttributeError(f"{self.__class__.__name__} requires '{attr_name}' attribute")
            return original_method(self, *args, **kwargs)

        cls.method = new_method  # Replace the original method with the new one
        return cls
    return decorator

@requires_attribute('is_admin')
class Admin:
    def __init__(self, name, is_admin):
        self.name = name
        self.is_admin = is_admin

    def method(self):
        return f"{self.name} has admin access."

# Usage
admin_user = Admin("Alice", True)

# This will work
print(admin_user.method())  # Output: Alice has admin access.

# Creating a user without the 'is_admin' attribute
class RegularUser:
    def __init__(self, name):
        self.name = name

    @requires_attribute('is_admin')
    def method(self):
        return f"{self.name} has admin access."

regular_user = RegularUser("Bob")

# This will raise an AttributeError
try:
    print(regular_user.method())
except AttributeError as e:
    print(e)  # Output: RegularUser requires 'is_admin' attribute