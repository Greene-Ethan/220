"""
Name: Ethan Greene
hw2.py

Problem: Using python to facilitate solving math equations.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""
import math

def sum_of_threes():
    upper_bound = eval(input('What is the upper bound?'))
    loop_value = upper_bound // 3
    arithmetic_value = 0
    final_sum = 0
    for i in range(loop_value):
        arithmetic_value = arithmetic_value + 3
        final_sum = final_sum + arithmetic_value
    print('The sum of threes is:',final_sum)


def multiplication_table():
    my_table = 0
    for i in range(10):
        my_table = my_table + 1
        print(end = '\n')
        for j in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
            j = j * my_table
            print(j, end ='\t')


def triangle_area():
    side_a = eval(input("Enter side a:"))
    side_b = eval(input("Enter side b:"))
    side_c = eval(input("Enter side c:"))
    sides = (side_a + side_b + side_c) / 2
    squared_value = sides * (sides - side_a) * (sides - side_b) * (sides - side_c)
    area = math.sqrt(squared_value)
    print("Area is",area)


def sum_squares():
    lower_bound = eval(input("What's the lower range?"))
    upper_bound = eval(input("What's the upper range?"))
    squared_sum = 0
    upper_bound = upper_bound + 1
    for i in range(lower_bound, upper_bound):
        my_square = i * i
        squared_sum = squared_sum + my_square
    print(squared_sum)



def power():
    base = eval(input("What's the base?"))
    exponent = eval(input("what's the exponent?"))
    answer = base
    exponent = exponent - 1
    for i in range(exponent):
        answer = answer * base
    exponent = exponent + 1
    print(base,"^",exponent,"=",answer)


if __name__ == '__main__':
    pass
