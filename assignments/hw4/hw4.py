"""
Name: Ethan Greene
hw4.py

Problem: Graphing geometric problems

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""
from graphics import *
import math

def squares():
    width = 400
    height = 400
    win = GraphWin("Clicks", width, height)

    # number of times user can move circle
    num_clicks = 5

    # create a space to instruct user
    inst_pt = Point(width / 2, height - 10)
    instructions = Text(inst_pt, "Click to move square")
    instructions.draw(win)

    # builds a circle
    shape = Rectangle(Point(50, 50),Point(100,100))
    shape.setOutline("red")
    shape.setFill("red")
    shape.draw(win)

    # allows the user to click multiple times to move the circle
    for i in range(num_clicks):
        click = win.getMouse()
        # center of circle

        # move amount is distance from center of circle to the
        # point where the user clicked
        x_value = click.getX() + 25
        y_value = click.getY() + 25
        x2_value = click.getX() - 25
        y2_value = click.getY() - 25
        new_shape = Rectangle(Point(x_value,y_value),Point(x2_value,y2_value))
        new_shape.setFill('red')
        new_shape.setOutline('red')
        new_shape.draw(win)
    close_text = Text(Point(200,200),"click to close")
    close_text.draw(win)
    win.getMouse()
    win.close()


def rectangle():
    win = GraphWin('Rectangle', 500,500)
    win.setCoords(0,0,10,10)
    close_inst = Text(Point(5,5),"click to close")
    peri_box = Text(Point(5, 1), "Perimeter =")
    peri_box.draw(win)
    area_box = Text(Point(5,1.5),"Area = ")
    area_box.draw(win)
    click1 = win.getMouse()
    click2 = win.getMouse()
    x_click1 = click1.getX()
    y_click1 = click1.getY()
    x_click2 = click2.getX()
    y_click2 = click2.getY()

    drawing = Rectangle(Point(x_click2,y_click2), Point(x_click1,y_click1))
    drawing.setFill('green')
    drawing.draw(win)
    perimeter = x_click1 + x_click2 + y_click2 + y_click1
    area = x_click1 * y_click1
    area_box.setText((area))
    peri_box.setText(perimeter)

    close_inst.draw(win)
    win.getMouse()
rectangle()

def circle():
    win = GraphWin('Circle',700,700)
    win.setCoords(0,0,10,10)
    click1 = win.getMouse()
    click2 = win.getMouse()
    x_click1 = click1.getX()
    y_click1 = click1.getY()
    x_click2 = click2.getX()
    y_click2 = click2.getY()
    x_value = math.pow(x_click2 - x_click1,2)
    y_value = math.pow(y_click2 - y_click1,2)
    answer = math.sqrt(x_value + y_value)
    radius_inst = Text(Point(5,1.3),"radius")
    radius_inst.draw(win)
    radius = Text(Point(5,1),answer)
    radius.draw(win)
    circle = Circle(Point(x_click1,y_click1),answer)
    circle.setFill('blue')
    circle.draw(win)
    close_message = Text(Point(5,5),"Click again to close")
    close_message.draw(win)
    win.getMouse()


def pi2():
    loop_num = eval(input("How many terms would you like to sum?"))
    denominator_value = 1
    numerator_value = 4
    loop_num = loop_num + 1
    positive_answer = 0
    negative_answer = 0
    answer = 0
    for i in range(1, loop_num):
        negative_value = (i % 2) - 1
        positive_value = (i % 2)
        positive_answer = positive_answer + (numerator_value/denominator_value) * positive_value
        negative_answer = negative_answer + (numerator_value/denominator_value) * negative_value
        answer = positive_answer + negative_answer
        denominator_value = denominator_value + 2
    accuracy = abs(math.pi - answer)
    print("Pi approximation:", answer)
    print("accuracy:", accuracy)


if __name__ == '__main__':
    pass
