# Did I Finish my Sudoku?
"""
Description:

Write a function done_or_not passing a board (list[list_lines]) as parameter.
If the board is valid return 'Finished!', otherwise return 'Try again!'

Sudoku rules:

Complete the Sudoku puzzle so that each and every row, column, and region
contains the numbers one through nine only once.

"""


def hassame(x):
    test = []
    for i in x:
        if i not in test:
            test.append(i)
        else:
            return False
    return True


def done_or_not(board):
    # row
    for i in board:
        if not hassame(i):
            return "Try again!"

    # col
    for i in zip(*board):
        if not hassame(i):
            return "Try again!"

    # block
    blocks = [[] for i in range(9)]
    for i in range(9):
        for j in range(9):
            blocks[(i / 3) * 3 + j / 3].append(board[i][j])
    for i in blocks:
        if not hassame(i):
            return "Try again!"

    return "Finished!"


# test
print done_or_not([[1, 3, 2, 5, 7, 9, 4, 6, 8],
                   [4, 9, 8, 2, 6, 1, 3, 7, 5],
                   [7, 5, 6, 3, 8, 4, 2, 1, 9],
                   [6, 4, 3, 1, 5, 8, 7, 9, 2],
                   [5, 2, 1, 7, 9, 3, 8, 4, 6],
                   [9, 8, 7, 4, 2, 6, 5, 3, 1],
                   [2, 1, 4, 9, 3, 5, 6, 8, 7],
                   [3, 6, 5, 8, 1, 7, 9, 2, 4],
                   [8, 7, 9, 6, 4, 2, 1, 5, 3]])

print done_or_not([[1, 3, 2, 5, 7, 9, 4, 6, 8],
                   [4, 9, 8, 2, 6, 1, 3, 7, 5],
                   [7, 5, 6, 3, 8, 4, 2, 1, 9],
                   [6, 4, 3, 1, 5, 8, 7, 9, 2],
                   [5, 2, 1, 7, 9, 3, 8, 4, 6],
                   [9, 8, 7, 4, 2, 6, 5, 3, 1],
                   [2, 1, 4, 9, 3, 5, 6, 8, 7],
                   [3, 6, 5, 8, 1, 7, 9, 2, 4],
                   [8, 7, 9, 6, 4, 2, 1, 3, 5]])
# clever method 1

"""
def done_or_not(board):
  rows = board
  cols = [map(lambda x: x[i], board) for i in range(9)]
  squares = [
    board[i][j:j + 3] + board[i + 1][j:j + 3] + board[i + 2][j:j + 3]
      for i in range(0, 9, 3)
      for j in range(0, 9, 3)]
    
  for clusters in (rows, cols, squares):
    for cluster in clusters:
      if len(set(cluster)) != 9:
        return 'Try again!'
  return 'Finished!'
  """

# clever method 2
"""
import numpy as np
def done_or_not(aboard): #board[i][j]
  board = np.array(aboard)

  rows = [board[i,:] for i in range(9)]
  cols = [board[:,j] for j in range(9)]
  sqrs = [board[i:i+3,j:j+3].flatten() for i in [0,3,6] for j in [0,3,6]]
  
  for view in np.vstack((rows,cols,sqrs)):
      if len(np.unique(view)) != 9:
          return 'Try again!'
  
  return 'Finished!'
"""
