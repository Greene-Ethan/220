"""
Name: Ethan Greene
Lab6.py

Problem: Creating a cipher that shifts for each letter

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""
from graphics import *
def vigenere():
    win = GraphWin('Vigenere',800,600)
    win.setCoords(0,0,10,10)
    top_text = Text(Point(2,8),"message to code:")
    top_text.draw(win)
    enter_message = Entry(Point(5.2,8),40)
    enter_message.draw(win)
    bot_text = Text(Point(2,7),"Enter Keyword:")
    bot_text.draw(win)
    enter_key = Entry(Point(4.6,7),30)
    enter_key.draw(win)
    close_rect = Rectangle(Point(3.5,6),Point(5.4,5))
    encode_text = Text(Point(4.45,5.5),"ENCODE")
    encode_text.draw(win)
    close_rect.draw(win)

    win.getMouse()
    message = enter_message.getText()
    close_rect.undraw()
    encode_text.undraw()
    key = enter_key.getText()
    key = key.upper()
    key = key.replace(" ","")
    key.upper()
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
    message = message.upper()
    message = message.replace(" ", "")
    for letters in message:
        key_letts = eval(seperated_letters[num]) - 65
        mess_letts = ord(letters) - 65
        add_letts = key_letts + mess_letts
        mod_letts = add_letts % 26
        before_back = mod_letts + 65
        into_letts = chr(before_back)
        final_message = final_message + into_letts
        num = num + 1
    res_mes = Text(Point(5,4),"Resulting Message:")
    res_mes.draw(win)
    answer = Text(Point(5,3.6),final_message)
    answer.draw(win)
    close_text = Text(Point(5,1),"click to close")
    close_text.draw(win)






    win.getMouse()
    win.close()

vigenere()