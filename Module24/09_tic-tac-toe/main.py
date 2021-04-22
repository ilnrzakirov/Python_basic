import random


class Board:

    def __init__(self):
        self.board = [cell for cell in range(1, 10)]

    def prescribe(self, user, cell):
        if isinstance(user, User):
            self.board[cell - 1] = user.symbol
        else:
            self.board[cell - 1] = user

    def print_board(self):
        print("-" * 14, "\n",
              "|", self.board[0], "|", self.board[1], "|", self.board[2], "| \n"
                                                                          " |", self.board[3], "|", self.board[4], "|",
              self.board[5], "| \n"
                             " |", self.board[6], "|", self.board[7], "|", self.board[8], "| \n",
              "-" * 13
              )


class User:

    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol


board = Board()
user1 = User("User1", "X")

computer_bord = []
for round in range(9):
    board.print_board()
    print("{} выбери ячейку".format(user1.name))
    answer = int(input())
    if answer > 0 and answer <= 9:
        board.prescribe(user1, answer)
    else:
        print("Такой ячейки нет")
    for item in board.board:
        if item != "X" and item != "O":
            computer_bord.append(item)
    computer_answer = random.choice(computer_bord)
    board.prescribe("O", computer_answer)
    computer_bord.clear()

#  пока что при вводе проставляются только "0".
#  Возможно, "X" будет проставлять наш код, выбирая рандомное число из доступных чисел.
# TODO, если победили, из игры выходим.
#  http://joxi.ru/BA0Byx4TpQLg5m
