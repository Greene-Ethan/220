"""
Name: Ethan Greene
hw7.py

Problem: A python program used to solve different real life application problems.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""
from encryption import encode, encode_better

def number_words(in_file_name, out_file_name):
    opener = open(in_file_name,"r")
    write_file = open(out_file_name,"w")
    reader = opener.read()
    splitter_n = reader.split("\n")
    sentence_with_spaces = ""
    for words in splitter_n:
        sentence_with_spaces = sentence_with_spaces + " " + words
    strip_sentence = sentence_with_spaces.strip()
    splitter = strip_sentence.split(" ")
    num = 1
    for words in splitter:
        num_str = str(num)
        print(num_str + " " + words , file = write_file)
        num = num + 1




def hourly_wages(in_file_name, out_file_name):
    opener = open(in_file_name,"r")
    write_file = open(out_file_name,"w")
    reader = opener.read()
    splitter_n = reader.split("\n")
    sentence = ""
    for words in splitter_n:
        sentence = sentence + words + " "
    strip_sentence = sentence.strip()
    splitter = strip_sentence.split(" ")
    first_name = 0
    last_name = 1
    wage = 2
    hours = 3
    loop_val = len(splitter) // 4


    for i in range(loop_val):
        first_name_write = splitter[first_name]
        last_name_write = splitter[last_name]
        added_nums = (eval(splitter[wage]) + 1.65) * eval(splitter[hours])
        wage = wage + 4
        hours = hours + 4
        first_name = first_name + 4
        last_name = last_name + 4
        close_to_writing = first_name_write + " " + last_name_write
        what_to_write = close_to_writing + " " + "{:.2f}".format(added_nums)
        print_my_file = what_to_write
        print(print_my_file, file = write_file)


def calc_check_sum(isbn):
    user_input = isbn.split("-")
    one_string = ""
    total = 0
    for parts in user_input:
        one_string = one_string + parts
    ten_to_one = 10
    for numbers in one_string:
        into_int = int(numbers)
        total = total + ten_to_one * into_int
        ten_to_one = ten_to_one - 1
    return total



def send_message(file_name, name_file):
    write_name_file = name_file + ".txt"
    opener = open(file_name,"r")
    write_file = open(write_name_file,'w')
    file_to_write = write_file
    for lines in opener:
        print(lines, end = "", file = file_to_write)




def send_safe_message(file_name, friend_name, key):
    opener = open(file_name, "r")
    file_to_be_written = friend_name + ".txt"
    write_file = open(file_to_be_written, "w")
    read_lines = opener.read()
    splitter = read_lines.split("\n")
    encoder = encode(splitter, key)
    encoder = encoder.strip()
    print(encoder, file = write_file)



def send_uncrackable_message(file_name, friend_name, pad_file_name):
    opener = open(file_name, "r")
    open_pad = open(pad_file_name, "r")
    file_to_be_written = friend_name + ".txt"
    write_file = open(file_to_be_written, "w")
    message = opener.read()
    message = message.split("\n")
    key = open_pad.read()
    for lines in message:
        encoder = encode_better(lines,key)
        print(encoder, end = "", file = write_file)



if __name__ == '__main__':
    pass
