"""
Name: Ethan Greene
Lab9.py

Problem: Tic Tac Toe in Python!

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""


def build_board():
    return ["1","2","3","4","5","6","7","8","9"]

def print_board(board):
    """ prints the values of board """
    RED = "\033[1;31m"
    BLUE = "\033[1;36m"
    LIGHT_GRAY = "\033[0;37m"
    reset = "\033[0m"
    new_board = []
    for v in board:
        new_board.append(v)
    for i in range(len(board)):
        if str(board[i]).find('x') >= 0:
            new_board[i] = RED + board[i] + LIGHT_GRAY
        elif str(board[i]).find('o') >= 0:
            new_board[i] = BLUE + board[i] + LIGHT_GRAY
    row_format = ' {0} | {1} | {2} '
    row_1 = row_format.format(new_board[0], new_board[1], new_board[2])
    row_2 = row_format.format(new_board[3], new_board[4], new_board[5])
    row_3 = row_format.format(new_board[6], new_board[7], new_board[8])
    row_separator = '-' * 11
    print(LIGHT_GRAY)
    print(row_1)
    print(row_separator)
    print(row_2)
    print(row_separator)
    print(row_3)
    print(reset)

def is_legal(board, position):
    position = position -1
    return board[position].isnumeric()


def fill_spot(board, position, character):
    position = position - 1
    character = character.strip()
    character = character.lower()
    if character == "x":
        board[position] = "x"
    else:
        board[position] = "o"



def winning_game(board):
    for i in range(0,8,3):
        if board[i] == board[i + 1] == board[i+2]:
            return True
    for i in range(3):
        if board[i] == board[i + 3] == board[i+6]:
            return True
    if board[0] == board[4]  == board[8]:
        return True
    if board[2] == board[4]  == board[6]:
        return True
    return False



def game_over(board):
    if winning_game(board) == True:
        return True
    for i in range(9):
        if board[i].isnumeric() == True:
            return False
    return True

def get_winner(board):
    if board.count("x") > board.count("o"):
        return "x"
    elif board.count("o") == board.count("x"):
        return "o"
    return None

def play(board):
    go_again = True
    while go_again:
        print("\n Each player takes turns putting their x's or o's in an open square."
              " You do so by typing in the number that you would like to place your "
              "square in. You win by getting three of your letters in a row."
              " Good luck!")
        turn = 1
        while not game_over(board):
            print_board(board)
            if turn % 2 == 0:
                position = eval(input("o's choose a position!"))
                character = "o"
            else:
                position = eval(input("x's choose a position!"))
                character = "x"
            turn = turn + 1
            while is_legal(board, position) == False:
                position = eval(input("Sorry that didn't work, please enter a spot where no one is"))
            fill_spot(board, position, character)
        if winning_game(board):
            print(get_winner(board),"won the game!! great job!")
        else:
            print("Uh oh it's tie!")
        play_again = input("Would you like to go again?")
        if play_again[0] == "y" or play_again[0] == "Y":
            go_again = True
        else:
            go_again = False
        board = build_board()


def main():
    pass


if __name__ == '__main__':
    main()
