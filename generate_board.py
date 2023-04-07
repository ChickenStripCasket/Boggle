import random
import string

def generate_board(size=4):
    board = [[random.choice(string.ascii_uppercase)
              for i in range(size)]
                    for j in range(size)]
    return board