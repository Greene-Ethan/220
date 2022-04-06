"""
Name: Ethan Greene
hw10.py

Problem: Solving problems without for loops

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""

def fibonacci(number):
    check_num = 0
    fibby = 1
    fibby_last_time = 1
    number_to_add = 0
    if number <= 1:
        return None
    while check_num < number:
        number_to_add += number_to_add
        fibby += number_to_add
        final_number = fibby + number_to_add
        check_num += 1


def double_investment(principle, rate):
    years = 0
    annual_rate = 0
    original_principle = principle * 2
    while annual_rate <= original_principle:
        years = years + 1
        annual_rate = principle * (1 + rate)
        principle = annual_rate
    return years

