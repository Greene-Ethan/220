"""
Name: Ethan Greene
Lab11.py

Problem: Using last week's lab in order to create a three door game.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""
from lab10.door import Door
from lab10.button import Button
from graphics import *
from random import randint

def three_door_game():
    win = GraphWin("door and button", 800, 600)
    my_button = Button(Rectangle(Point(725,0),Point(800,50)),"Quit")
    my_button.draw(win)
    door_one = Door(Rectangle(Point(100,150),Point(250,500)),"Door 1")
    door_two = Door(Rectangle(Point(300,150),Point(450,500)),"Door 2")
    door_two.draw(win)
    door_three = Door(Rectangle(Point(500,150),Point(650,500)),"Door 3")
    door_three.draw(win)
    door_one.draw(win)
    scoreboard = Rectangle(Point(0,0),Point(75,75))
    scoreboard.draw(win)
    scoreboard_losses = Rectangle(Point(75,0),Point(150,75))
    scoreboard_losses.draw(win)
    wins_text = Text(Point(35,25),"wins")
    wins_text.draw(win)
    losses_text = Text(Point(110,25),"losses")
    losses_text.draw(win)
    win_tracker = 0
    wins_tracker = Text(Point(35,50),win_tracker)
    wins_tracker.draw(win)
    loss_tracker = 0
    losses_tracker = Text(Point(105, 50), loss_tracker)
    losses_tracker.draw(win)

    door_one.color_door('brown')
    door_two.color_door('brown')
    door_three.color_door('brown')

    win.setBackground('lightblue')

    i_have_door = Text(Point(375,100),"I have a door!")
    i_have_door.draw(win)
    click_door_prompt = Text(Point(375,550),"Click to guess which is the secret door")
    click_door_prompt.draw(win)
    while True:
        click_door_prompt.setText("Click to guess which is the secret door")
        door_one.color_door('brown')
        door_two.color_door('brown')
        door_three.color_door('brown')
        door_one.set_secret(False)
        door_two.set_secret(False)
        door_three.set_secret(False)
        i_have_door.setText("I have a door!")
        secret_door = randint(1,3)
        check_click = win.getMouse()

        if my_button.is_clicked(check_click):
            break

        if secret_door == 1:
            door_one.set_secret(True)
        elif secret_door == 2:
            door_two.set_secret(True)
        else:
            door_three.set_secret(True)

        if door_one.is_clicked(check_click):
            if door_one.is_secret():
                door_one.color_door('green')
                i_have_door.setText("you win!")
                win_tracker += 1
            else:
                door_one.color_door("red")
                i_have_door.setText("Sorry, incorrect!")
                loss_tracker += 1
                if door_two.is_secret():
                    door_two.color_door("green")
                else:
                    door_three.color_door('green')
        elif door_two.is_clicked(check_click):
            if door_two.is_secret():
                door_two.color_door('green')
                i_have_door.setText("you win!")
                win_tracker += 1
            else:
                door_two.color_door("red")
                i_have_door.setText("Sorry, incorrect!")
                loss_tracker += 1
                if door_three.is_secret():
                    door_three.color_door("green")
                else:
                    door_one.color_door('green')

        elif door_three.is_clicked(check_click):
            if door_three.is_secret():
                door_three.color_door('green')
                i_have_door.setText("you win!")
                win_tracker += 1
            else:
                door_three.color_door("red")
                i_have_door.setText("Sorry, incorrect!")
                loss_tracker += 1
                if door_one.is_secret():
                    door_one.color_door("green")
                else:
                    door_two.color_door('green')
        click_door_prompt.setText("click anywhere to play again!")
        wins_tracker.setText(win_tracker)
        losses_tracker.setText(loss_tracker)
        check_click = win.getMouse()

        if my_button.is_clicked(check_click):
            break
    win.close()
three_door_game()