"""
Name: Ethan Greene
button.py

Problem: creating a button object

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""
from graphics import *
class Button:
    def __init__(self, shape, label):
        self.shape = shape
        self.text = Text(self.shape.getCenter(),label)

    def get_label(self):
        return self.text.getText()

    def set_label(self,label):
        self.text.setText(label)

    def draw(self,win):
        self.shape.draw(win)
        self.text.draw(win)

    def undraw(self):
        self.shape.undraw()
        self.text.undraw()

    def is_clicked(self,point):
        if point.getX() >= self.shape.getP1().getX() and point.getX() <= self.shape.getP2().getX():
            if point.getY() >= self.shape.getP1().getY() and point.getY() <= self.shape.getP2().getY():
                return True
        return False

    def color_button(self,color):
        self.shape.setFill(color)
