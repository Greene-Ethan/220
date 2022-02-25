"""
Name: Ethan Greene
HW6.py

Problem: Multiple different python problems being solved with the help of string and functions

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""
import math

def cash_converter():
    dollar_num = eval(input("enter a dollar amount:"))
    print("That is ${:.2f}".format(dollar_num))


def encode():
    message = input("Enter a message:")
    key = eval(input("Enter in a key"))
    secret_message = ""
    for words in message:
        converter = ord(words)
        mes_add_three = converter + key
        back_to_words = chr(mes_add_three)
        secret_message = secret_message + back_to_words
    print(secret_message)


def sphere_area(radius):
    return 4 * math.pi * math.pow(radius,2)


def sphere_volume(radius):
    return 4 / 3 * math.pi * math.pow(radius,3)


def sum_n(number):
    number = number + 1
    total = 0
    for num_singular in range(number):
        total = total + num_singular
    return total




def sum_n_cubes(number):
    number = number + 1
    total = 0
    for num_singular in range(number):
        total = total + math.pow(num_singular,3)
    return total


def encode_better():
    message = input("Enter a message")
    key = input("Enter a key")
    loop_val = len(message) - len(key)
    new_key = key
    mod_num = 0
    for i in range(loop_val):
        new_key = new_key + key[mod_num % len(key)]
        mod_num = mod_num + 1
    seperated_letters = ""

    for letters in new_key:
        num_letts = str(ord(letters))
        seperated_letters = seperated_letters + " " + num_letts
    seperated_letters = seperated_letters[1:]
    seperated_letters = seperated_letters.split(" ")
    num = 0
    final_message = ""
    for letters in message:
        key_letts = eval(seperated_letters[num]) - 65
        message_letts = ord(letters) - 65
        add_letts = key_letts + message_letts
        mod_letts = add_letts % 58
        mod_letts = mod_letts + 65
        into_letts = chr(mod_letts)
        final_message = final_message + into_letts
        num = num + 1
    print(final_message)





if __name__ == '__main__':
    # cash_converter()
    # encode()
    # res = sphere_area(13)
    # print(res)
    # res = sphere_volume(13)
    # print(res)
    # res = sum_n(100)
    # print(res)
    # res = sum_n_cubes(13)
    # print(res)
    # encode_better()
    pass
