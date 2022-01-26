"""
Name: Ethan Greene
Lab2.py

Problem: A python program that computes arithmetics

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""
import math
def means():
    num_loop = eval(input("How many numbers will you be entering?"))
    added_rms_values = 0
    added_harmonic_values = 0
    added_geometric_values = 1
    for i in range(num_loop):
        values = eval(input("enter value:"))
        added_rms_values = (values ** 2) + added_rms_values
        added_harmonic_values = (1 / values) + added_harmonic_values
        added_geometric_values = values * added_geometric_values
    divided_rms = added_rms_values/ num_loop
    root_mean_square = round(math.sqrt(divided_rms), 3)
    harmonic_mean = round(num_loop / added_harmonic_values, 3)
    geometric_mean = round(added_geometric_values ** (1 / num_loop),3)
    print("Your root-mean-square is:",root_mean_square,"\nYour harmonic mean is:"
    ,harmonic_mean,"\nYour geometric mean is:",geometric_mean)


