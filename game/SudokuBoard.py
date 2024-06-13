import numpy as np
from SolveSudoku import *

difficulty = [(30, 36), (28, 34), (26, 32), (24, 30), (22, 28)]

class SudokuBoard:
  def __init__(self, diff):
    # Set the difficulty of the game
    self.difficulty = diff
    
    # Create a 9x9 numpy array to represent the solution board
    self.solution = createBoard()
    
    # Create a 9x9 numpy array to represent the game board
    self.board = np.zeros((9,9), dtype=int)
    self.setBoard(diff)
    
    # Create a 9x9x9 numpy array to represent the possible values for each cell
    self.notes = np.zeros((9,9,9), dtype=bool)
    
  def __str__(self):
    res = ""
    for i in range(9):
      if (i % 3 == 0 and i != 0):
        res += "- " * 11 + "  |   " + "- " * 10 + "-\n"
      for j in range(18):
        if (j == 9):
          res += "  |   "
        if (j < 9):
          if (j % 3 == 2 and j != 8):
            res += str(self.board[i][j]) + " | "
          else: 
            res += str(self.board[i][j]) + " "
        else:
          if (j % 3 == 2 and j != 17):
            res += str(self.solution[i][j - 9]) + " | "
          else:
            res += str(self.solution[i][j - 9]) + " "
      res += "\n"
    return res

  # Sets the board from difficulty
  def setBoard(self, diff):
    board = np.zeros((9,9), dtype=int)
    startSet = rand.randint(difficulty[diff][0], difficulty[diff][1])
    tiles = rand.sample(range(81), startSet)
    
    for i in tiles:
      row = i // 9
      col = i % 9
      board[row][col] = self.solution[row][col]
    self.board = board