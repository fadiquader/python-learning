"""
Metaclasses are a deep and advanced feature in Python that allow you to modify
the behavior of classes. In Python, everything is an object,
including classes themselves, and metaclasses define how classes behave.
"""

class UppercaseMeta(type):
    """A metaclass that converts class names to uppercase."""

    def __new__(cls, name, bases, attrs):
        uppercase_name = name.upper()
        return super().__new__(cls, uppercase_name, bases, attrs)

class MyClass(metaclass=UppercaseMeta):
    pass

print(MyClass.__name__)  # Output: MYCLASS

class StringAttributeMeta(type):
    """A metaclass that ensures all class attributes are strings."""

    def __new__(cls, name, bases, attrs):
        for attr_name, attr_value in attrs.items():
            if not isinstance(attr_value, str):
                raise TypeError(f"Attribute '{attr_name}' must be a string.")
        return super().__new__(cls, name, bases, attrs)

class MyClass(metaclass=StringAttributeMeta):
    name = "Alice"
    city = "Wonderland"
    age = 30  # This will raise an error

# Uncommenting the following line will raise an error
# class InvalidClass(metaclass=StringAttributeMeta):
#     name = "Bob"
#     age = "thirty"  # This will raise an error

# Automatically adds a method to any class that uses it.
# The added method will return the class name.
# This can be useful for classes that need a standardized way to report their name.

# auto_method_metaclass.py
class AutoMethodMeta(type):
    """A metaclass that adds a 'get_class_name' method to classes."""

    def __new__(cls, name, bases, attrs):
        # Define a new method
        def get_class_name(self):
            return self.__class__.__name__

        # Add the new method to the class attributes
        attrs['get_class_name'] = get_class_name
        return super().__new__(cls, name, bases, attrs)

class BaseClass(metaclass=AutoMethodMeta):
    pass

class DerivedClass(BaseClass):
    pass

# Creating instances of the classes
base_instance = BaseClass()
derived_instance = DerivedClass()

# Calling the added method
print(base_instance.get_class_name())  # Output: BaseClass
print(derived_instance.get_class_name())  # Output: DerivedClass