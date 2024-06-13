import numpy as np
from SolveSudoku import *

# Look for singles on the board
def findSingles(board):
  res = []
  for i in range(9):
    for j in range(9):
      if board[i][j] > 0:
        continue
      validNumbers = getValidNumbers(board, i, j)
      if len(validNumbers) == 1:
        res.append((i, j, validNumbers[0]))
        i = 0
        j = 0
  return res

# Fill the board with the resulting singles
def fillSingles(board, singles):
  for single in singles:
    board[single[0]][single[1]] = single[2]