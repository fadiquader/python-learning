"""
Diamond Problem
The diamond problem arises in multiple inheritance when a class inherits from two classes that
both inherit from a common ancestor. This creates ambiguity because the child class may inherit
the same attribute or method from both parent classes
       A
      / \
     B   C
      \ /
       D
In this diagram:
Class A is the common ancestor.
Classes B and C inherit from A.
Class D inherits from both B and C.
"""
class A:
    def show(self):
        return "Class A"

class B(A):
    def show(self):
        return "Class B"

class C(A):
    def show(self):
        return "Class C"

class D(B, C):
    pass

# Usage
d = D()
print(d.show())  # Output: Class B
"""
Python uses the Method Resolution Order (MRO) to determine the order in which classes are searched 
when calling methods. The MRO follows the C3 linearization algorithm, which ensures a consistent and predictable method 
resolution order.
You can view the MRO of a class using the mro() method
"""
print(D.mro())
"""
# Output
[<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>]
"""

"""
Example: Vehicles and Their Features
Classes:
* Base Class: Vehicle
* Intermediate Classes: LandVehicle and WaterVehicle
* Derived Class: AmphibiousVehicle (inherits from both LandVehicle and WaterVehicle)
"""
class Vehicle:
    def start_engine(self):
        return "Engine started"

class LandVehicle(Vehicle):
    def drive(self):
        return "Driving on land"

class WaterVehicle(Vehicle):
    def float(self):
        return "Floating on water"

class AmphibiousVehicle(LandVehicle, WaterVehicle):
    def traverse(self):
        return "Traversing both land and water"

# Usage
amphibious_vehicle = AmphibiousVehicle()

# Accessing methods
print(amphibious_vehicle.start_engine())  # Inherited from Vehicle
print(amphibious_vehicle.drive())          # From LandVehicle
print(amphibious_vehicle.float())          # From WaterVehicle
print(amphibious_vehicle.traverse())       # From AmphibiousVehicle

# Check Method Resolution Order
print(AmphibiousVehicle.mro())
"""
# Output
Engine started
Driving on land
Floating on water
Traversing both land and water
[<class '__main__.AmphibiousVehicle'>, <class '__main__.LandVehicle'>, <class '__main__.WaterVehicle'>, <class '__main__.Vehicle'>, <class 'object'>]
"""