"""
Name: <your name goes here – first and last>
<ProgramName>.py

Problem: <Brief, one or two sentence description of the problem that this program solves, in your own words.>

Certification of Authenticity:
<include one of the following>
I certify that this assignment is entirely my own work.
I certify that this assignment is my own work, but I discussed it with: <Name(s)>
"""


def name_reverse():
    name = input("What's your name?")
    first = name.split(" ")
    print(first[1] +","+ " " + first[0])

def company_name():
    company_website = input("Please enter a three-part internet domain:")
    split_names = company_website.split(".")
    print(split_names[1])


def initials():
    num_students = eval(input("How many students are in the class?"))
    num_students = num_students + 1
    for i in range(1, num_students):
        name = input("What's the name of student " + str(i)+"?")
        output = name.split(" ")
        first_initial = output[0]
        last_initial = output[1]
        print(first_initial[0] + last_initial[0])



def names():
    names_list = input("Enter a list of names:")
    loop_value = names_list.count(",") + 1
    names_no_commas = names_list.split(",")
    n = " ".join(names_no_commas)
    n = n.split("  ")
    output = ""
    for words in n:
        first_word = words.split(" ")
        last_word = words.split(" ")
        first_initial = first_word[0]
        last_initial = last_word[1]
        output = output + first_initial[0] + last_initial[0] + " "
    print(output[:-1])





def thirds():
    user_input = eval(input("How many strings will you be entering?"))
    output = ""
    for i in range(user_input):
        sentence = input("Enter sentence " + str(i + 1) + ":")
        saving_variable = sentence[0::3]
        output = output + saving_variable  + "\n"
    print(output[:-1])



def word_average():
    sentence = input("Please enter in a sentence:")
    sentence = sentence.split(" ")
    loop_value = len(sentence)
    word_total = 0
    for words in range(loop_value):
        num_words = len(sentence[words])
        word_total = word_total + num_words
    average = word_total / loop_value
    print(average)


def pig_latin():
    sentence = input("Enter a sentence to be converted to pig latin:")
    list_sentence = sentence.split(" ")
    loop_value = len(list_sentence)
    output = ""
    for i in range(loop_value):
        word = list_sentence[i]
        take_letter = word[0]
        latin = word[1:] + take_letter + "ay"
        output = output + " " + latin
        output = output.lower()
    print(output[1:])

if __name__ == '__main__':
    # name_reverse()
    # company_name()
    # initials()
    # names()
    # thirds()
    # word_average()
    # pig_latin()
    pass
