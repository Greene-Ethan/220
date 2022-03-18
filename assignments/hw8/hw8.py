"""
Name: Ethan Greene
hw8.py

Problem:

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""
import math
from graphics import *


def add_ten(nums):
    index = 0
    for digits in nums:
        nums[index] = nums[index] + 10
        index = index + 1


def square_each(nums):
    index = 0
    for digits in nums:
        nums[index] = nums[index] * nums[index]
        index = index + 1


def sum_list(nums):
    index = 0
    all_added = 0
    for digits in nums:
        all_added = all_added + nums[index]
        index = index + 1
    return all_added


def to_numbers(nums):
    index = 0
    for i in nums:
        nums[index] = eval(nums[index])
        index = index + 1


tester = ['4.16, 5.37, 2.87, 2.51', '5.99, 7.76, 9.0, 4.55, 2.07']


def sum_of_squares(nums):
    adder = ""
    for digits in nums:
        nums = digits.split(",")
        to_numbers(nums)
        square_each(nums)
        adder = adder + " " + str(sum_list(nums))
    adder = adder.strip()
    adder = adder.split(" ")
    index = 0
    for digits in adder:
        adder[index] = eval(adder[index])
        index = index + 1
    return adder


def starter(weight, wins):
    if weight >= 150 and weight < 160 and wins >= 5:
        return True
    elif weight > 199:
        return True
    elif wins > 20:
        return True
    else:
        return False


def leap_year(year):
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    if year % 400 == 0:
        return True
    else:
        return False


def did_overlap(circle_one, circle_two):
    circle_1 = circle_one.getCenter()
    circle_2 = circle_two.getCenter()
    x_circle1 = circle_1.getX()
    y_circle1 = circle_1.getY()
    x_circle2 = circle_2.getX()
    y_circle2 = circle_2.getY()
    inside = math.pow((x_circle1 - x_circle2), 2) + math.pow((y_circle1 - y_circle2), 2)
    distance = math.sqrt(inside)
    radius_1 = circle_one.getRadius()
    radius_2 = circle_two.getRadius()
    return distance <= radius_1 + radius_2

def circle_overlap():
    width_px = 700
    height_px = 700
    win = GraphWin("Circle", width_px, height_px)
    width = 10
    height = 10
    win.setCoords(0, 0, width, height)

    center = win.getMouse()
    circumference_point = win.getMouse()
    radius = math.sqrt(
        (center.getX() - circumference_point.getX()) ** 2 + (center.getY() - circumference_point.getY()) ** 2)
    circle_one = Circle(center, radius)
    circle_one.setFill("light blue")
    circle_one.draw(win)
    center2 = win.getMouse()
    circumference_point2 = win.getMouse()
    radius2 = math.sqrt((center2.getX() - circumference_point2.getX()) ** 2
                        + (center2.getY() - circumference_point2.getY()) ** 2)
    circle_two = Circle(center2, radius2)
    circle_two.draw(win)
    circle_two.setFill('green')
    test_condition = did_overlap(circle_one,circle_two)
    if test_condition == True:
        text_true = Text(Point(5,5),"They Overlap!")
        text_true.draw(win)
    else:
        text_false = Text(Point(5,5),"They don't overlap!")
        text_false.draw(win)
    text_close = Text(Point(5,4),"click again to close")
    text_close.draw(win)

    win.getMouse()




if __name__ == '__main__':
    pass
