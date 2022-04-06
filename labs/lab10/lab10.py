"""
Name: Ethan Greene
Lab10.py

Problem: Creating a door that opens and closes and an exit button

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""
from button import Button
from graphics import *
from door import Door
def main():
    win = GraphWin("door and button", 700,700)
    my_button = Button(Rectangle(Point(250,75),Point(450,200)),"Exit")
    my_door = Door(Rectangle(Point(250,250),Point(450,700)),"Closed")
    my_door.color_door("red")
    my_button.draw(win)
    my_door.draw(win)

    check_click = win.getMouse()
    while not my_button.is_clicked(check_click):
        if my_door.is_clicked(check_click):
            if my_door.get_label() == "Open":
                my_door.close("red","Closed")
            elif my_door.get_label() == "Closed":
                my_door.open("white","Open")



        check_click = win.getMouse()


    win.close()
main()