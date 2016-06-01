# Make a spiral
"""
Description:

Your task, is to create a NxN spiral with a given size.
Return value should contain array of arrays, of 0 and 1, for example for given
size 5 result should be:

[[1,1,1,1,1],[0,0,0,0,1],[1,1,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]
Because of the edge-cases for tiny spirals, the size will be at least 5.

General rule-of-a-thumb is, that the snake made with '1' cannot touch to
itself.
"""

"""
def spiralize(size):
    if size == 0:
        return
    mat = [[0 for i in range(size)] for j in range(size)]
    mat = snake(mat, size)
    return mat


def snake(mat, n):
    m = len(mat) - n
    if m + 1 == n:
        mat[m][m] = 1
        return mat
    elif m + 2 == n:
        mat[m][m] = 1
        mat[m][m + 1] = 1
        mat[m + 1][m + 1] = 1
        return mat
    elif m + 3 == n:
        mat[m][m] = 1
        mat[m][m + 1] = 1
        mat[m][m + 2] = 1
        mat[m + 1][m + 2] = 1
        mat[m + 2][m + 2] = 1
        mat[m + 2][m + 1] = 1
        mat[m + 2][m] = 1
        return mat
    elif m + 4 == n:
        for i in range(4):
            mat[m][m + i] = 1
            mat[m + 3][m + i] = 1
        mat[m + 2][m] = 1
        mat[m + 1][m + 3] = 1
        mat[m + 2][m + 3] = 1
        return mat

    elif m + 4 < n:
        for j in range(m, n):
            mat[m][j] = 1
        for i in range(m, n - 1):
            mat[i + 1][n - 1] = 1
        for j in range(m, n - 1):
            mat[n - 1][j] = 1
        for i in range(m + 2, n - 1):
            mat[i][m] = 1
        mat[m + 2][m + 1] = 1
        snake(mat, n - 2)
        return mat
"""

# clever method 1
"""
def spiralize(size):
    
    def on_board(x, y):
        return 0 <= x < size and 0 <= y < size
        
    def is_one(x, y):
        return on_board(x, y) and spiral[y][x] == 1
        
    def can_move():
        return on_board(x+dx, y+dy) and not (is_one(x+2*dx, y+2*dy) or is_one(x+dx-dy, y+dy+dx) or is_one(x+dx+dy, y+dy-dx))
    
    
    spiral = [[0 for x in range(size)] for y in range(size)]   
    x, y = -1, 0
    dx, dy = 1, 0
    turns = 0
    
    while (turns < 2):
        if can_move():
            x += dx
            y += dy
            spiral[y][x] = 1
            turns = 0
        else:
            dx, dy = -dy, dx
            turns += 1
    
    return spiral
"""

# clever method 2
"""
def spiralize(size):
    spiral = [[1]*size for _ in xrange(size)]
    def ok(y, x):
        return y < size and x < size and y >= 0 and x >= 0 and spiral[y][x]
    y, x, dy, dx = 1, -1, 0, 1
    while ok(y + dy, x + dx):
        if ok(y + 2*dy, x + 2*dx):
            y += dy
            x += dx
        else:
            dx, dy = dy*(2*dx-1), dx
        spiral[y][x] = 0
    return spiral
"""

# clever method 3


def spiralize(size):
    # Make a snake
    spiral = [[1 - min(i, j, size - max(i, j) - 1) %
               2 for j in xrange(size)] for i in xrange(size)]
    for i in xrange(size / 2 - (size % 4 == 0)):
        spiral[i + 1][i] = 1 - spiral[i + 1][i]
    return spiral

s = spiralize(8)
# print s
for i in s:
    print i
