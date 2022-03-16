"""
Name: Ethan Greene
Lab8.py

Problem: Simulate bumper cars in a 2d plane and see if they collided.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""
from random import randint
from graphics import *
import math



def get_random(move_amount):
    return randint(-move_amount,move_amount)

def did_collide(circle_ball1, circle_ball2):
    circle_1 = circle_ball1.getCenter()
    circle_2 = circle_ball2.getCenter()
    x_circle1 = circle_1.getX()
    y_circle1 = circle_1.getY()
    x_circle2 = circle_2.getX()
    y_circle2 = circle_2.getY()
    inside = math.pow((x_circle1 - x_circle2),2) + math.pow((y_circle1 - y_circle2),2)
    distance = math.sqrt(inside)
    radius_1 = circle_ball1.getRadius()
    radius_2 = circle_ball2.getRadius()
    return distance <= radius_1 + radius_2

def hit_vertical(circle_ball, win):
    center_circle = circle_ball.getCenter()
    check_top = center_circle.getY() + circle_ball.getRadius()
    check_bottom = center_circle.getY() - circle_ball.getRadius()
    if check_bottom <= 0:
        return True
    elif check_top >= win.getHeight():
        return True
    else:
        return False

def hit_horizontal(circle_ball, win):
    center_circle = circle_ball.getCenter()
    check_right = center_circle.getX() + circle_ball.getRadius()
    check_left = center_circle.getX() - circle_ball.getRadius()
    if check_left <= 0:
        return True
    elif check_right >= win.width:
        return True
    else:
        return False

def get_random_color():
    color = color_rgb(randint(0,255),randint(0,255),randint(0,255))
    return color

def bumper():
    win = GraphWin("bumper",800,800)
    circle_1 = Circle(Point(randint(50,750),randint(50,750)),50)
    circle_2 = Circle(Point(randint(50,750),randint(50,750)),50)
    circle_1.setFill(get_random_color())
    circle_2.setFill(get_random_color())
    circle_1.draw(win)
    circle_2.draw(win)
    dx_circle1 = get_random(10)
    dy_circle1 = get_random(10)
    dx_circle2 = get_random(10)
    dy_circle2 = get_random(10)
    while not(win.checkMouse()):
        time.sleep(.1)
        circle_1.move(dx_circle1,dy_circle1)
        circle_2.move(dx_circle2,dy_circle2)
        if hit_horizontal(circle_1,win):
            dx_circle1 = -dx_circle1
        if hit_horizontal(circle_2,win):
            dx_circle2 = -dx_circle2
        if hit_vertical(circle_1,win):
            dy_circle1 = -dy_circle1
        if hit_vertical(circle_2,win):
            dy_circle2 = -dy_circle2
        if did_collide(circle_1,circle_2):
            dx_circle1 = -dx_circle1
            dx_circle2 = -dx_circle2
            dy_circle1 = -dy_circle1
            dy_circle2 = -dy_circle2
    win.close()



