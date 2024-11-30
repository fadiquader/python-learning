# import this
# This is a sample Python script.
# from Car import Car, ElectricCar
import car
# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    first_name = "fadi"
    last_name = "quader"
    full_name = f"{first_name} {last_name}"
    print_hi(full_name.title())
    for i in range(1, 5):
        print(i**2)
    list = list(range(1, 10, 2))
    print(list, min(list), list[0:3])
    squares = [i**2 for i in range(1, 10)]
    squares_1 = [i**2 for i in list[:3]]
    # Copy a list
    squares_2 = squares_1[:]

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
