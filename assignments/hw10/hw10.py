"""
Name: Ethan Greene
hw10.py

Problem: Solving problems without the use of for loops

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""

def fibonacci(number):
    fibby = 1
    fibby_last_time = 1
    if number <= 1:
        return None
    if number == 2:
        return 1
    loop_val = 0
    finish_loop = 0
    number -= 2
    while finish_loop < number:
        number_to_add = fibby
        while loop_val == 0:
            fibby += fibby_last_time
            fibby_last_time = number_to_add
            loop_val += 1
            finish_loop = finish_loop + 1
        loop_val -= 1
    return fibby


def double_investment(principle, rate):
    years = 0
    annual_rate = 0
    original_principle = principle * 2
    while annual_rate <= original_principle:
        years = years + 1
        annual_rate = principle * (1 + rate)
        principle = annual_rate
    return years


# x even divide by two
# 3x + 1 if it is odd


def syracuse(n):
    final_list = [n]
    while n != 1:
        if n % 2 == 0:
            n = n / 2
            int_n = (int(n))
            final_list.append(int_n)
        else:
            n = (3 * n) + 1
            int_n = (int(n))
            final_list.append(int_n)
    return final_list

def goldbach(n):
    if n % 2 != 0:
        return None
    return "Goldbach is impossible"
