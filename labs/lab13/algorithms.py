"""
Name: Ethan Greene
algorithms.py

Problem: Practicing python algorithms

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""
from graphics import *

def data_sorted(file_name):
    open_file = open(file_name, "r")
    line = open_file.readline()
    final_list = []
    while line:
        strip_my_line = line.strip()
        split_my_line = strip_my_line.split(" ")
        final_list += split_my_line
        line = open_file.readline()


def is_in_linear(search_val, values):
    loop_value = 0
    while loop_value < len(values):
        if values[loop_value] == search_val:
            return True

        loop_value += 1
    return False


def selection_sort(values):
    for index_value in range(len(values)):
        for i in range(index_value, len(values)):
            if values[i] < values[index_value]:
                values[i], values[index_value] = values[index_value], values[i]

my_rect = [Rectangle(Point(1.0, 1.0), Point(20.0, 20.0)),
           Rectangle(Point(1.0, 1.0), Point(2.0, 2.0)),
           Rectangle(Point(1.0, 1.0), Point(10.0, 10.0))]

def calc_area(rect):
    my_x_one = rect.getP1().getX()
    my_y_one = rect.getP1().getY()
    my_x_two = rect.getP2().getX()
    my_y_two = rect.getP2().getY()
    length = abs(my_x_one - my_x_two)
    width = abs(my_y_one - my_y_two)
    return length * width

def rect_sort(rectangles):
    for index_value in range(len(rectangles)):
        for i in range(index_value, len(rectangles)):
            if calc_area(rectangles[i]) < calc_area(rectangles[index_value]):
                rectangles[i], rectangles[index_value] = rectangles[index_value], rectangles[i]
