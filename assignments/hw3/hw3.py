"""
Name: Ethan Greene
hw3.py

Problem: A group of python problems used to solve arithmetics using loops.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""


def average():
    loop_value = eval(input("How many grades will you enter?"))
    added_values = 0
    for i in range(loop_value):
        values = eval(input("Enter a value: "))
        added_values = added_values + values
    final_value = added_values / loop_value
    print(final_value)


def tip_jar():
    total_tips = 0
    for i in range (5):
        tips = eval(input("How much would you like to donate?"))
        total_tips = total_tips + tips
    print("Total tips:",total_tips)




def newton():
    x_value = eval(input("What number do you want to be the square root?"))
    loop_value = eval(input("How many times should we improve the approximation?"))
    initial_approximation = x_value
    for i in range(loop_value):
        stored_value = initial_approximation + x_value / initial_approximation
        final_answer = stored_value / 2
        initial_approximation = final_answer
    print(final_answer)

def sequence():
    user_input = eval(input("How many terms would you like?"))
    output = 1
    for i in range(user_input):
        print(output, end = "\t")
        output = output + i % 2 + i % 2

def pi():
    user_input = eval(input("How many terms are in the series?"))
    numerator_value = 0
    denominator_value = 1
    answer = 1
    for i in range(user_input):
        numerator_value = numerator_value + (i - 1) % 2 + (i - 1) % 2
        denominator_value = denominator_value + i % 2 + i % 2
        answer = answer * (numerator_value / denominator_value)
    answer = answer * 2
    print(answer)


if __name__ == '__main__':
    pass
