"""
Name: Ethan Greene
hw9.py

Problem: Creating Hangman in python!

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""
from random import randint
from graphics import *

def get_words(file_name):
    opener = open(file_name,"r")
    reader = ""
    for line in opener:
        reader = reader + opener.readline()
    reader = reader.strip()
    split_n = reader.split("\n")
    return split_n

def get_random_word(words):
    random_integer = randint(0, len(words))
    random_word = words[random_integer]
    return random_word

def letter_in_secret_word(letter, secret_word):
    for lets in secret_word:
        if lets == letter:
            return True
    return False


def already_guessed(letter, guesses):
    for lets in guesses:
        if letter == lets:
            return True
    return False


def make_hidden_secret(secret_word, guesses):
    guesses = guesses + " "
    guess_index = 0
    final_word = ""
    mod_num = len(guesses)
    index_word = 0
    last_word = secret_word
    while not guesses[guess_index% mod_num] == guesses[-1]:
        for letters in last_word:
            if letters == guesses[guess_index]:
                final_word = final_word + "_"
            else:
                final_word = final_word + letters
            last_word = final_word

        final_word = ""

        guess_index = guess_index + 1
    guesses = guesses[0:-1]
    output_word = ""
    for lets in last_word:
        let_may_need = secret_word[index_word]
        for guess in guesses:
            if guess == guesses[-1] and lets != "_":
                output_word = output_word + " " + "_"

            elif guess == let_may_need:
                output_word = output_word + ' ' + let_may_need
        index_word = index_word + 1
    return output_word


def won(guessed):
    for lets in guessed:
        if lets == "_":
            return False
        elif lets == guessed[-1] and lets != "_":
            return True

def draw_guy(remaining_guess_num,win):
    if remaining_guess_num == 5:
        head = Circle(Point(500,300),50)
        head.setFill('black')
        head.draw(win)
    if remaining_guess_num == 4:
        torso = Rectangle(Point(510,320),Point(490,500))
        torso.setFill('black')
        torso.draw(win)
    if remaining_guess_num == 3:
        left_arm = Rectangle(Point(510,340),Point(620,360))
        left_arm.setFill('black')
        left_arm.draw(win)
    if remaining_guess_num == 2:
        right_arm = Rectangle(Point(490, 340), Point(380, 360))
        right_arm.setFill('black')
        right_arm.draw(win)
    if remaining_guess_num == 1:
        left_leg = Rectangle(Point(500,500),Point(480,550))
        left_leg.setFill('black')
        left_leg.draw(win)
    if remaining_guess_num == 0:
        right_leg = Rectangle(Point(510,500),Point(530,550))
        right_leg.setFill('black')
        right_leg.draw(win)



def play_graphics(secret_word):
    win = GraphWin("hangman", 1000, 1000)
    play_again = 0
    while play_again == 0:
        all_words = get_words(secret_word)
        random_word = get_random_word(all_words)
        guesses_together = ""
        remaining_guess_num = 6
        playing = 0
        guesses_list = ""
        guesses_entry = Text(Point(110, 200), "guess a letter:")
        guesses = Entry(Point(210, 200), 10)
        guesses.draw(win)
        guesses_entry.draw(win)
        guessed_list_drawer = Text(Point(800, 200), "No guesses yet")
        guessed_list_drawer.draw(win)
        underscore_word = ""
        gallows_one = Rectangle(Point(500,250),Point(700,230))
        gallows_two = Rectangle(Point(690,250),Point(700,600))
        gallows_two.setFill('black')
        gallows_one.setFill('black')
        gallows_one.draw(win)
        gallows_two.draw(win)
        for i in range(len(random_word)):
            underscore_word = underscore_word + " " + "_"
        hidden_text_word = Text(Point(500,200),underscore_word)
        hidden_text_word.draw(win)
        while playing == 0:
            win.getMouse()
            guesses_from_text = guesses.getText()
            while already_guessed(guesses_from_text, guesses_list):
                guesses.draw(win)
                guesses.setText("Please enter a letter you haven't guessed")

            guesses_together = guesses_together + " " + guesses_from_text
            guesses_together = guesses_together.strip()
            guesses_list = guesses_together.split(" ")
            guessed_list_drawer.setText("Guesses: {}".format(guesses_list))

            list_as_a_string = ""
            for guess in guesses_list:
                list_as_a_string = list_as_a_string + guess
            hidden_word = make_hidden_secret(random_word, list_as_a_string)
            hidden_text_word.setText(hidden_word)

            if not letter_in_secret_word(guesses_from_text, random_word):
                remaining_guess_num = remaining_guess_num - 1
                draw_guy(remaining_guess_num, win)


            if remaining_guess_num == 0:
                guesses.undraw()
                guesses_entry.undraw()
                losing_text = Text(Point(200,200),"sorry you lost this one")
                losing_text.draw(win)
                secret_revealed = Text(Point(200, 180), "The secret word was: {}".format(random_word))
                secret_revealed.draw(win)
                playing = playing + 1
            if won(hidden_word):
                guesses.undraw()
                guesses_entry.undraw()
                winning_text = Text(Point(200, 200), "Congratulations! You guessed it!")
                winning_text.draw(win)
                playing = playing + 1
        play_again = 1
        closing_message = Text(Point(500,100),"CLICK AGAIN TO CLOSE")
        closing_message.draw(win)
        win.getMouse()
        win.close()

def play_command_line(secret_word):
    play_again = 0
    while play_again == 0:
        all_words = get_words(secret_word)
        random_word = get_random_word(all_words)
        guesses_together = ""
        guesses_list = []
        remaining_guess_num = 6
        playing = 0
        while playing == 0:
            guesses = input("guess a letter")

            while already_guessed(guesses, guesses_list):
                guesses = input("Please enter a letter you haven't guessed")

            guesses_together = guesses_together + " " + guesses
            guesses_together = guesses_together.strip()
            guesses_list = guesses_together.split(" ")

            print("already guessed: {}".format(guesses_list))
            list_as_a_string = ""
            for guess in guesses_list:
                list_as_a_string = list_as_a_string + guess
            hidden_word = make_hidden_secret(random_word,list_as_a_string)
            print(hidden_word)
            if not letter_in_secret_word(guesses, random_word):
                remaining_guess_num = remaining_guess_num - 1

            print(remaining_guess_num)

            if remaining_guess_num == 0:
                print("sorry you lost this one")
                print("The secret word was: {}".format(random_word))
                playing = playing + 1
            if won(hidden_word):
                print("Congratulations! You guessed it!")
                playing = playing + 1


        play_again_question = input("play again?")
        if play_again_question[0] == "y":
            play_again = 0
        else:
            play_again = 1


if __name__ == '__main__':
    pass
    # play_command_line(secret_word)
    # play_graphics(secret_word)
