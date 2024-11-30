
class Car:
    def __init__(self, make, model, year, odemeter_reading = 0):
        self.make = make
        self.model = model
        self.year = year
        self.odemeter_reading = odemeter_reading

    def update_odemeter_reading(self, mileage):
        self.odemeter_reading = mileage

class Battery:
    def __init__(self, battery_size = 40):
        self.battery_size = battery_size

    def describe_battery(self):
        """Initialize the battery's attributes."""
        print(f"This battery has a {self.battery_size} kwh battery.")

class ElectricCar(Car):
    def __init__(self, make, model, year, odemeter_reading = 0):
        super().__init__(make, model, year)
        self.battery = Battery()

    def update_odemeter_reading(self, mileage):
        self.battery.describe_battery()
        if mileage > self.battery.battery_size:
            self.odemeter_reading = mileage - self.battery.battery_size
        else:
            self.odemeter_reading = mileage

