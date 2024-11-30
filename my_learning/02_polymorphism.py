"""
Polymorphism allows methods to be used interchangeably, even if they act on different object types.
It enables a single interface to represent different underlying forms (data types).

Types of Polymorphism:
1. Method Overriding: A child class provides a specific implementation of a method that is already
defined in its parent class.
2. Method Overloading: (Not natively supported in Python, but can be simulated with default arguments
or variable arguments).
"""

class Shape:
    def area(self):
        raise NotImplementedError("Subclasses must implement this method")

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * (self.radius ** 2)

# Polymorphism in action
shapes = [Rectangle(5, 3), Circle(4)]

for shape in shapes:
    print(f"Area: {shape.area()}")

"""
Dynamic Binding
Definition: Dynamic binding (or late binding) refers to the process where the method to be executed is determined 
at runtime, rather than at compile time. This is a key feature of polymorphism in object-oriented programming.
"""

class Animal:
    def speak(self):
        return "Animal sound"

class Dog(Animal):
    def speak(self):
        return "Bark"

class Cat(Animal):
    def speak(self):
        return "Meow"

def make_animal_speak(animal):
    print(animal.speak())  # Method is determined at runtime

# Usage
dog = Dog()
cat = Cat()

make_animal_speak(dog)  # Output: Bark
make_animal_speak(cat)  # Output: Meow