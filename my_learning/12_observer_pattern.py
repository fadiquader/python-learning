from abc import ABC, abstractmethod

"""
he Observer pattern is a behavioral design pattern that
defines a one-to-many dependency between objects so that
when one object (the subject) changes state, all its dependents (observers)
are notified and updated automatically. This pattern is especially
useful in situations where a change in one object requires updating others,
and you want to maintain loose coupling between these objects.
"""

# Simple observer
class Subscriber:
    def __init__(self, name):
        self.name = name

    def update(self, message):
        print(f"{self.name} received message: {message}")

class Publisher:
    def __init__(self):
        self.subscribers = set()
    def register(self, subscriber):
        self.subscribers.add(subscriber)
    def unregister(self, subscriber):
        self.subscribers.discard(subscriber)
    def dispatch(self, message): # notify
        for subscriber in self.subscribers:
            subscriber.update(message)

# Create a publisher with some subscribers
pub = Publisher()
bob = Subscriber("bob")
alice = Subscriber("Alice")
# Register subscribers
pub.register(bob)
pub.register(alice)
# Send a message
pub.dispatch("It's lunchtime!")
pub.unregister(bob)
pub.dispatch("Time for dinner!")

# with callback
class Publisher2:
    def __init__(self):
        self.subscribers = dict()
    def register(self, subscriber, callback=None):
        if callback is None:
            callback = subscriber.update
        self.subscribers[subscriber] = callback
    def dispatch(self, message):
        for callback in self.subscribers.values():
            callback(message)
    def unregister(self, subscriber):
        del self.subscribers[subscriber]

pub2 = Publisher2()
bob2 = Subscriber("bob")
pub2.register(bob2, bob.update)
alice2 = Subscriber("alice")
pub2.register(alice2, lambda message: print(message))
pub2.dispatch("Pub2: It's lunchtime!")

# Several channels
class Publisher3:
    def __init__(self, channels):
        self.channels = { channel: dict() for channel in channels }

    def register(self, channel, subscriber, callback=None):
        if callback is None:
            callback = subscriber.update
        subscribers = self.channels[channel]
        subscribers[subscriber] = callback

    def dispatch(self, channel, message):
        subscribers = self.channels[channel]
        for callback in subscribers.values():
            callback(message)

pub3 = Publisher3(['lunch', 'dinner'])
bob3 = Subscriber('bob3')
alice3 = Subscriber('alice3')
pub3.register("lunch", bob3)
pub3.register("dinner", alice3)
pub3.dispatch("lunch", "It's lunchtime!")
pub3.dispatch("dinner", "Time for dinner!")

# Weather example

class Observer(ABC):
    @abstractmethod
    def update(self, temperature):
        pass

class Subject(ABC):
    @abstractmethod
    def attach(self, observer: Observer):
        pass

    @abstractmethod
    def detach(self, observer: Observer):
        pass

    @abstractmethod
    def notify(self):
        pass

class WeatherStation(Subject):
    def __init__(self):
        self._observers = []
        self._temperature = 0

    def attach(self, observer: Observer):
        self._observers.append(observer)

    def detach(self, observer: Observer):
        self._observers.remove(observer)

    def notify(self):
        for observer in self._observers:
            observer.update(self._temperature)

    def set_temperature(self, temperature):
        self._temperature = temperature
        self.notify()  # Notify all observers of the temperature change

class CurrentConditionsDisplay(Observer):
    def update(self, temperature):
        print(f"Current conditions: {temperature}°C")

class StatisticsDisplay(Observer):
    def update(self, temperature):
        print(f"Statistics updated: Average temperature is now {temperature}°C")

# Usage
weather_station = WeatherStation()
current_display = CurrentConditionsDisplay()
statistics_display = StatisticsDisplay()
weather_station.attach(current_display)
weather_station.attach(statistics_display)
# Change the temperature and notify observers
weather_station.set_temperature(25)
weather_station.set_temperature(30)