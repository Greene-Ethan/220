"""
Name: Ethan Greene
Lab12.py

Problem: Practicing python problems without the use of for loops

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""
from random import randint


def find_and_remove_first(list, value):
    indexing_val = 0
    stop_while = 0
    while stop_while == 0:
        if list[indexing_val] == value:
            list.remove(value)
            list.insert(indexing_val ,"Ethan")
            stop_while += 1
        indexing_val = indexing_val + 1


def good_input():
    user_input = eval(input("Please enter a number between 1-10 (inclusive): "))
    while user_input > 10 or user_input < 1:
        if user_input > 10:
            user_input = eval(input("That numbers too big, please enter a number 1-10: "))
        elif user_input < 1:
            user_input = eval(input("That numbers too small, please enter a number 1-10: "))
    return user_input


def num_digits():
    entering_data = True
    user_input = eval(input("Please enter a positive number: "))
    while entering_data:

        digit_num = 0
        my_division = user_input
        while my_division != 0:
            my_division //= 10
            digit_num += 1
        print(digit_num)

        user_input = eval(input("Please enter a number(use 0 or a negative number to stop): "))
        if user_input <= 0:
            entering_data = False


def hi_lo_game():
    secret_num = randint(1, 100)
    game_stopper = 7
    how_many_turns = 0
    check_print_lose = 0
    while game_stopper >= 0:
        how_many_turns += 1
        stop_checking = 0
        user_input = eval(input("Please enter a number 1-100(inclusive): "))
        if 1 > user_input or user_input > 100:
            stop_checking = 1
        while stop_checking == 1:
            user_input = eval(input("That number wasn't in the correct range. "
                                    "Please enter a number 1-100(inclusive): "))
            if 1 <= user_input <= 100:
                stop_checking -= 1
        if user_input == secret_num:
            print("Congratulations!! You guessed it!! It took ya "
                  "{} turns!".format(how_many_turns))
            game_stopper -= 7
            check_print_lose = 1
        elif user_input < secret_num:
            print("That's not the number, guess higher")
        else:
            print("That's not the number, guess lower")
        game_stopper -= 1
    if check_print_lose == 0:
        print("Uh oh, it looks like you ran out of turns. "
              "The secret number was: {}".format(secret_num))
