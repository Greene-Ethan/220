"""
Name: Ethan Greene
hw1.py

Problem: Python program that solves multiple conversion problems

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""


def calc_rec_area():
    length = eval(input("Enter the length: "))
    width = eval(input("Enter the width: "))
    area = length * width
    print("Area =", area)


def calc_volume():
    length = eval(input("Enter the length: "))
    width = eval(input("Enter the width: "))
    height = eval(input("Enter the height: "))
    volume = length * width * height
    print("volume =", volume)


def shooting_percentage():
    shots = eval(input("how many shots did you shoot? "))
    shots_made = eval(input("How many shots did you make? "))
    percent_made = shots_made / shots * 100
    print("You made",percent_made,"% of your shots")


def coffee():
    pounds = eval(input("How many pounds of coffee would you like?"))
    price = pounds * 10.5 + pounds * .86 + 1.50
    print("That's",price,"$")


def kilometers_to_miles():
    kilometers = eval(input("How many kilometers did you travel?"))
    miles = kilometers / 1.61
    print("That's",miles,"miles!")


if __name__ == '__main__':
    pass
