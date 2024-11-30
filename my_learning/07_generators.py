"""
 Generators are a special type of iterable that allow you to iterate over a sequence of values without storing
 the entire sequence in memory. They are defined using functions and the yield statement.

 Key Features of Generators
1. Lazy Evaluation: Generators produce values on-the-fly, which means they only generate values as needed.
This is useful for working with large datasets or streams of data.
2. Memory Efficiency: Since they don’t store the entire sequence in memory, generators are more memory-efficient
than lists, especially for large datasets.
3. Easy to Implement: Generators are simpler to create than custom iterator classes, as they use
standard function syntax.
"""

def count_up_to(n):
    count = 1
    while count <= n:
        yield count  # Yield the current value and pause the function
        count += 1

# Usage
counter = count_up_to(5)

for number in counter:
    print(number)  # Output: 1, 2, 3, 4, 5

def infinite_sequence():
    num = 1
    while True:  # Infinite loop
        yield num
        num += 1

# Usage (be careful with infinite loops!)
infinite_gen = infinite_sequence()

for _ in range(5):  # Limiting output to 5 values
    print(next(infinite_gen))  # Output: 1, 2, 3, 4, 5

# Generator Expression: provide a shorthand way to create generators
squares = (x * x for x in range(1, 6))  # Generator expression for squares

for square in squares:
    print(square)  # Output: 1, 4, 9, 16, 25