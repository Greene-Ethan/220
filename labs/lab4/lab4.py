"""
Name: Ethan Greene
lab4.py

Problem: create a valentines day card

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""
from graphics import *
def greeting_card():
    win = GraphWin('card',700,700)
    win.setCoords(0,0,10,10)
    heart = Polygon(Point(5,3),Point(3,6),Point(4,7),Point(5,6),Point(6,7),Point(7,6),Point(5,3))
    heart.setFill('red')
    message = Text(Point(5,8),"Do you like raisins? How do you feel about a date?")
    arrow_head = Polygon(Point(10, 5.25), Point(11, 6), Point(11, 4), Point(10, 5))
    arrow_head.setFill('silver')
    arrow = Rectangle(Point(13.75,5),Point(10,5.25))
    arrow.setFill('brown')
    x_point = -.4
    y_point = 0
    win.setBackground('pink')
    heart.draw(win)
    heart_two = heart.clone()
    heart_two.move(-3.3,3)
    heart_two.setFill('purple')
    heart_three = heart.clone()
    heart_three.move(3.3,3)
    heart_three.setFill('yellow')
    heart_four = heart_two.clone()
    heart_four.move(0,-6)
    heart_four.setFill('yellow')
    heart_five = heart_three.clone()
    heart_five.move(0,-6)
    heart_five.setFill('purple')
    heart_four.draw(win)
    heart_five.draw(win)
    heart_three.draw(win)
    heart_two.draw(win)
    arrow.draw(win)
    arrow_head.draw(win)
    message.draw(win)
    for i in range(18):
        time.sleep(.2)
        arrow.move(x_point,y_point)
        arrow_head.move(x_point,y_point)
    message.setText("Click to Close")

    win.getMouse()
    win.close()
