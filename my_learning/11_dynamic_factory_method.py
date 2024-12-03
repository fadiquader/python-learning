import abc
import os

"""
The Factory Method pattern is a creational design pattern that provides an interface 
for creating objects in a superclass but allows subclasses to alter the type of objects 
that will be created. This pattern is particularly useful when the exact type of 
the object to be created isn't known until runtime.
"""

# Image reader example
class ImageReader(metaclass=abc.ABCMeta):
    def __init__(self, path):
        self.path = path

    @abc.abstractmethod
    def read(self):
        pass

    def __repr__(self):
        return f'{self.__class__.__name__}({self.path})'

class GIFReader(ImageReader):
    def read(self):
        print(f'Reading GIF {self.path}')

class JPEGReader(ImageReader):
    def read(self):
        print(f'Reading JPEG {self.path}')
class RawByteReader(ImageReader):
    def read(self):
        print(f'Reading Raw Byte {self.path}')

def extension_of(path):
    # return os.path.splitext(path)[1]
    # returns "gif", "jpeg"
    position_of_last_dot = path.rfind('.')
    return path[position_of_last_dot+1:]

READERS = {
    'gif': GIFReader,
    'jpeg': JPEGReader,
}

def get_image_readers(path):
    reader_class = READERS.get(extension_of(path), RawByteReader)
    return reader_class(path)


# Vehicle example
# 1. Define product interface
class Vehicle(abc.ABC):
    @abc.abstractmethod
    def drive(self):
        pass

# 2. implement concrete products
class Car(Vehicle):
    def drive(self):
        return "Driving a car"

class Bike(Vehicle):
    def drive(self):
        return "Riding a bike"

# 3. Define the creator class
class VehicleFactory(abc.ABC):
    @abc.abstractmethod
    def create_vehicle(self):
        pass

# 4. Implement concrete examples
class CarFactory(VehicleFactory):
    @abc.abstractmethod
    def create_vehicle(self):
        return Car()

class BikeFactory(VehicleFactory):
    def create_vehicle(self):
        return Bike()

# client code
def client_code(factory: VehicleFactory):
    vehicle = factory.create_vehicle()
    print(vehicle.drive())