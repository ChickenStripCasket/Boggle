import random
import numpy as np
def generate_board():
    #distribution of letters of a typical boggle machine
    combinations=[['A', 'E', 'A', 'N', 'E', 'G'], ['A' ,'H' ,'S', 'P' ,'C', 'O'],['A', 'S', 'P', 'F', 'F', 'K'],['O', 'B', 'J' ,'O' ,'A', 'B'],
              ['I', 'O', 'T' ,'M', 'U', 'C'], ['R' ,'Y' ,'V', 'D', 'E' ,'L'],['L', 'R', 'E', 'I' ,'X', 'D'],['E' ,'I', 'U' ,'N' ,'E' ,'S'],
              ['W', 'N' ,'G', 'E', 'E' ,'H'],['L', 'N', 'H' ,'N', 'R' ,'Z'],['T' ,'S' ,'T', 'I', 'Y' ,'D'],['O', 'W', 'T', 'O' ,'A', 'T'],
              ['E' ,'R', 'T', 'T' ,'Y', 'L'],['T' ,'O', 'E', 'S', 'S' ,'I'],['T', 'E', 'R', 'W', 'H', 'V'],['N' ,'U' ,'I', 'H' ,'M' ,'Q']]
    #initialize board
    board=[]
    for i in range(0,len(combinations)):
        #fill board with 1 random value from each die
        board.append(combinations[i][random.randint(0,len(combinations[i])-1)])
    return np.array(board, dtype=str).reshape(4,4)