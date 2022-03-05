"""
Name: Ethan Greene
lab5.py

Problem: Practicing both graphic and list objects in Python

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""
from graphics import *
import math

def triangle():
    win = GraphWin('Triangle',700,700)
    win.setCoords(0,0,10,10)
    perimeter = Text(Point(3.3, 1), "Perimeter=")
    area = Text(Point(3.3, 2), "Area=")
    perimeter.draw(win)
    area.draw(win)
    click1 = win.getMouse()
    click2 = win.getMouse()
    click3 = win.getMouse()
    tri_drawn = Polygon(click1,click2,click3)
    x_click1 = click1.getX()
    y_click1 = click1.getY()
    x_click2 = click2.getX()
    y_click2 = click2.getY()
    x_click3 = click3.getX()
    y_click3 = click3.getY()
    line_1 = math.sqrt(math.pow((x_click2 - x_click1),2) + math.pow((y_click2 - y_click1),2))
    line_2 = math.sqrt(math.pow((x_click3 - x_click2),2) + math.pow((y_click3 - y_click2),2))
    line_3 = math.sqrt(math.pow((x_click3 - x_click1),2) + math.pow((y_click3 - y_click1),2))
    total_peri = line_1 + line_2 + line_3
    sides = (line_1 + line_2 + line_3) / 2
    total_area = math.sqrt(sides*(sides-line_1)*(sides-line_2)*(sides-line_3))
    peri_text = Text(Point(5,1),total_peri)
    area_text = Text(Point(5,2),total_area)
    peri_text.draw(win)
    area_text.draw(win)
    close_text = Text(Point(5,9),"Click to close")


    tri_drawn.draw(win)
    win.getMouse()
    win.close()



def color_shape():
    '''Create code to allow a user to color a shape by entering rgb amounts'''

    # create window
    win_width = 400
    win_height = 400
    win = GraphWin("Color Shape", win_width, win_height)
    win.setBackground("white")

    # create text instructions
    msg = "Enter color values between 0 - 255\nClick window to color shape"
    inst = Text(Point(win_width / 2, win_height - 20), msg)
    inst.draw(win)

    # create circle in window's center
    shape = Circle(Point(win_width / 2, win_height / 2 - 30), 50)
    shape.draw(win)

    # redTexPt is 50 pixels to the left and forty pixels down from center
    red_text_pt = Point(win_width / 2 - 50, win_height / 2 + 40)
    red_text = Text(red_text_pt, "Red: ")
    red_text.setTextColor("red")


    # green_text_pt is 30 pixels down from red
    green_text_pt = red_text_pt.clone()
    green_text_pt.move(0, 30)
    green_text = Text(green_text_pt, "Green: ")
    green_text.setTextColor("green")


    # blue_text_pt is 60 pixels down from red
    blue_text_pt = red_text_pt.clone()
    blue_text_pt.move(0, 60)
    blue_text = Text(blue_text_pt, "Blue: ")
    blue_text.setTextColor("blue")


    # display rgb text
    red_text.draw(win)
    green_text.draw(win)
    blue_text.draw(win)

    for i in range(5):
        red_var_pt = red_text_pt.clone()
        red_var_pt.move(80, 0)
        red_variable = Entry(red_var_pt, 10)
        red_variable.draw(win)

        green_var_pt = green_text_pt.clone()
        green_var_pt.move(80, 0)
        green_variable = Entry(green_var_pt, 10)
        green_variable.draw(win)

        blue_var_pt = blue_text_pt.clone()
        blue_var_pt.move(80, 0)
        blue_variable = Entry(blue_var_pt, 10)
        blue_variable.draw(win)

        win.getMouse()
        color_one = eval(red_variable.getText())
        color_two = eval(green_variable.getText())
        color_three = eval(blue_variable.getText())

        shape.setFill(color_rgb(color_one,color_two,color_three))

    close_text = Text(Point(200,100),"Click to close")
    close_text.draw(win)


    # Wait for another click to exit
    win.getMouse()
    win.close()

def process_string():
    user_input = input("Please type out a string")
    print(user_input[0])
    print(user_input[-1])
    print(user_input[1:5])
    first_last = user_input[0] + user_input[-1]
    print(first_last)
    first_three = user_input[0:3] * 10
    print(first_three)

    for letters in user_input:
        print(letters)

    len_input = len(user_input)
    print(len_input)


def process_list():
    pt = Point(5,10)
    values = [5, "hi", 2.5, "there", pt, "7.2"]
    x = values[1] + values[3]
    print(x)
    x = values[0] + values[2]
    print(x)
    x = values[1] * 5
    print(x)
    x = values[2:5]
    print(x)
    x = values[2:4] + values[:1]
    print(x)
    x = [values[2],values[0],float(values[5])]
    print(x)
    x = values[0] + values[2] + float(values[5])
    print(x)
    x = len(values)
    print(x)


def another_series():
    loop_value = eval(input("How many terms would you like?"))
    output = 0
    for i in range(loop_value):
        output = output + i % 3 + i % 3 + 2

    print("sum =",output)


def target():
    win = GraphWin('target',600,600)
    win.setCoords(0,0,10,10)
    outer_circle = Circle(Point(5,5),5)
    outer_circle.setFill('white')
    outer_circle.draw(win)
    black_circle = Circle(Point(5,5),4)
    black_circle.setFill('black')
    black_circle.draw(win)
    blue_circle = Circle(Point(5,5),3)
    blue_circle.setFill('blue')
    blue_circle.draw(win)
    red_circle = Circle(Point(5,5),2)
    red_circle.setFill('red')
    red_circle.draw(win)
    inner_circle = Circle(Point(5,5),1)
    inner_circle.setFill('yellow')
    inner_circle.draw(win)
    close_text = Text(Point(5,9.5),"Click to close")
    close_text.draw(win)
    win.getMouse()
    win.close()
