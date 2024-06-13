import numpy as np
import random as rand

# Check if a number is valid in a given position
def checkValid(board, row, col, num):
  # Check the row
  for i in range(9):
    if board[row][i] == num:
      return False
  
  # Check the column
  for i in range(9):
    if board[i][col] == num:
      return False
  
  # Check the 3x3 square
  startRow = row - row % 3
  startCol = col - col % 3
  for i in range(3):
    for j in range(3):
      if board[i + startRow][j + startCol] == num:
        return False
  
  return True

# Get legal values for a certain cell
def getValidNumbers(board, row, col):
  validNumbers = []
  for i in range(1, 10):
    if checkValid(board, row, col, i):
      validNumbers.append(i)
  return validNumbers

def createBoard():
  # Create the solution board
  board = np.zeros((9,9), dtype=int)
  
  # Get the first row of the board
  row1 = [i for i in range(1, 10)]
  rand.shuffle(row1)
  
  # Put the randomized order into the first row of the board
  for i in range(9):
    board[0][i] = row1[i]
    
  # Solve the board using backtracking
  solveBoard(board, 1, 0)
  
  # Return the rest of the board
  return board

# Solve the board using backtracking
def solveBoard(board, row, col):
  # Backtracking basecase
  if (row == 8 and col == 9):
    return True
  
  # If we get to the end of a row, move to the next row
  if (col == 9):
    row += 1
    col = 0
  
  # Check if a value already exists in the cell
  if (board[row][col] != 0):
    return solveBoard(board, row, col + 1)
  
  # Get possible numbers and iterate through them
  validNumbers = getValidNumbers(board, row, col)
  rand.shuffle(validNumbers)
  for i in validNumbers:
    board[row][col] = i
    if (solveBoard(board, row, col + 1)):
      return True
    board[row][col] = 0
  return False