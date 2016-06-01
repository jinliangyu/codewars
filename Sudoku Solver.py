# Sudoku Solver
"""
Description:

Write a function that will solve a 9x9 Sudoku puzzle. The function will take
one argument consisting of the 2D puzzle array, with the value 0
representing an unknown square.

The Sudokus tested against your function will be "easy" (i.e. determinable;
there will be no need to assume and test possibilities on unknowns) and can
be solved with a brute-force approach.
"""

# clever method
"""
from itertools import product

def possibles(puzzle, x, y):
    a, b = 3*(x/3), 3*(y/3)
    square = set([puzzle[r][c] for r, c in product(range(a,a + 3), range(b,b + 3))])
    row = set(puzzle[x])
    col = set(zip(*puzzle)[y])
    return set(range(1,10)).difference(square.union(row).union(col))

def sudoku(puzzle):
    z = [(r,c) for (r,c) in product(range(9),range(9)) if puzzle[r][c] == 0]    
    if z == []: 
        return puzzle
    for (r,c) in z:
        p = possibles(puzzle, r, c)
        if len(p) == 1:
            puzzle[r][c] = p.pop()
    return sudoku(puzzle)
"""

# clever method
"""
def sudoku(puzzle):
    '''return the solved puzzle as a 2d array of 9 x 9'''
            '''    while [l for l in puzzle if 0 in l]:
        for x, y in ((x, y) for x, l in enumerate(puzzle)
                     for y in xrange(len(l)) if not puzzle[x][y]):
            opt = set(xrange(1, 10)) - set(puzzle[x]) \
                  - {l[y] for l in puzzle} \
                  - {puzzle[m][n]
                     for m in xrange(x - (x % 3), x - (x % 3) + 3)
                     for n in xrange(y - (y % 3), y - (y % 3) + 3)}
            if len(opt) == 1:
                puzzle[x][y] = opt.pop()
                break
    return puzzle
"""

def checkSol(num, sol):
    if num and num in sol:
        del sol[sol.index(num)]


def checkSquare(board, qx, qy, sol):
    qx *= 3
    qy *= 3
    for i in range(qx, qx + 3):
        for j in range(qy, qy + 3):
            checkSol(board[i][j], sol)


def checkVertical(board, x, sol):
    for i in range(0, 9):
        checkSol(board[x][i], sol)


def checkHorizontal(board, y, sol):
    for i in range(0, 9):
        checkSol(board[i][y], sol)


def getPossible(board, x, y):
    if board[x][y] != 0:
        return [board[x][y]]

    sol = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    checkSquare(board, x / 3, y / 3, sol)
    checkVertical(board, x, sol)
    checkHorizontal(board, y, sol)
    return sol


def isSolved(board):
    for line in range(0, 9):
        horizontal = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        vertical = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        square = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        checkHorizontal(board, line, horizontal)
        checkVertical(board, line, vertical)
        checkSquare(board, line % 3, line / 3, square)
        if horizontal != [] or vertical != [] or square != []:
            return False
    return True


def findOpen(board):
    for i in range(0, 9):
        for j in range(0, 9):
            if board[i][j] == 0:
                return (i, j)


def sudoku(board):
    if isSolved(board):
        return board

    x, y = findOpen(board)
    for possible in getPossible(board, x, y):
        board[x][y] = possible
        # Traverse down
        solved = sudoku(board)
        if solved:
            return solved
    board[x][y] = 0
    return None

# test

puzzle = [[5, 3, 0, 0, 7, 0, 0, 0, 0],
          [6, 0, 0, 1, 9, 5, 0, 0, 0],
          [0, 9, 8, 0, 0, 0, 0, 6, 0],
          [8, 0, 0, 0, 6, 0, 0, 0, 3],
          [4, 0, 0, 8, 0, 3, 0, 0, 1],
          [7, 0, 0, 0, 2, 0, 0, 0, 6],
          [0, 6, 0, 0, 0, 0, 2, 8, 0],
          [0, 0, 0, 4, 1, 9, 0, 0, 5],
          [0, 0, 0, 0, 8, 0, 0, 7, 9]]
result = sudoku(puzzle)
for i in result:
    print i
