"""
Name: <your name goes here – first and last>
<ProgramName>.py

Problem: <Brief, one or two sentence description of the problem that this program solves, in your own words.>

Certification of Authenticity:
<include one of the following>
I certify that this assignment is entirely my own work.
I certify that this assignment is my own work, but I discussed it with: <Name(s)>
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
tip_jar()




def newton():



def sequence():
    pass


def pi():
    pass


if __name__ == '__main__':
    pass
