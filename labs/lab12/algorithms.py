"""
Name: Ethan Greene
algorithms.py

Problem: Practicing python problems without the use of for loops

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""


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
