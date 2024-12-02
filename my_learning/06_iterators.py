"""
An iterator is an object that allows you to traverse through a collection (like a list, tuple, or dictionary)
without exposing the underlying structure.
An iterator implements two methods: __iter__() and __next__().
"""

"""
Python has a built-in function called iter(). When you pass it a
collection, you get back an iterator object. Python effectively does under the hood is call
iter() on that collection.
"""

numbers = [1, 2, 3, 4, 5]
numbers_iter = iter(numbers)
for num in numbers_iter:
    print(num)

class Countdown:
    def __init__(self, start):
        self.current = start

    def __iter__(self): # The __iter__() method returns the iterator object itself.
        return self

    def __next__(self):
        if self.current <= 0:
            raise StopIteration
        else:
            self.current -= 1
            return self.current + 1  # Return the current value before decrementing

# Usage
countdown = Countdown(5)

for number in countdown:
    print(number)  # Output: 5, 4, 3, 2, 1
"""
Reverse Iterate example
Normal Iteration: The __iter__() method returns self, allowing iteration over the collection in the standard order.
Reverse Iteration: The reverse_iter method returns a new ReverseIterator class, which allows for iterating through 
the collection in reverse.
"""

class NumberCollection:
    def __init__(self, numbers):
        self.numbers = numbers

    def __iter__(self):
        return self  # Returning the object itself

    def __next__(self):
        if not self.numbers:
            raise StopIteration
        return self.numbers.pop(0)  # Return and remove the first element

    def reverse_iter(self):
        class ReverseIterator:
            def __init__(self, collection): # collection is NumberCollection instance
                self.index = len(collection.numbers) - 1
                self.collection = collection

            def __iter__(self):
                return self

            def __next__(self):
                if self.index < 0:
                    raise StopIteration
                value = self.collection.numbers[self.index]
                self.index -= 1
                return value

        return ReverseIterator(self)

# Usage
collection = NumberCollection([1, 2, 3, 4, 5])

# Normal iteration
for number in collection:
    print(number)  # Output: 1, 2, 3, 4, 5

# Reverse iteration
reverse_iterator = collection.reverse_iter()
for number in reverse_iterator:
    print(number)  # Output: 5, 4, 3, 2, 1