import numpy as np

# board is stored as 2d array
# board[i][j] where i=row, j=col
b = [
    [0, 0, 0, 0, 0, 0, 8, 3, 0],
    [0, 3, 5, 4, 8, 2, 1, 0, 0],
    [0, 8, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 3, 2, 7, 6, 0, 0, 4],
    [8, 7, 2, 0, 0, 5, 0, 0, 0],
    [6, 0, 4, 0, 3, 0, 2, 5, 0],
    [9, 0, 0, 0, 1, 4, 0, 7, 0],
    [0, 0, 8, 0, 0, 7, 0, 2, 9],
    [3, 0, 0, 0, 2, 9, 5, 6, 1]
]
b_0 = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0]
]


def generate_unsolved_board(board):
    mask = np.random.randint(0, 2, size=(len(board), len(board[0])))
    for i in range(len(board)):
        for j in range(len(board[0])):
            if mask[i][j] == 0:
                board[i][j] = 0


def generate_complete_board(board):
    for i in range(9):  # select 9 random spots to place random values from 1-9 in
        row = np.random.randint(0, len(board) - 1)
        col = np.random.randint(0, len(board[0]) - 1)
        place_rand_value(board, row, col)
    solve(board)


def place_rand_value(board, row, col):
    if board[row][col] != 0:
        return None
    else:
        val = np.random.randint(1, 9)
        if valid(board, val, (row, col)):
            board[row][col] = val
        return None


# solve the board recursively-
def solve(board):
    # base case no empty spaces found, then the board is complete
    find = find_empty(board)
    if not find:
        return True
    else:
        row, col = find
    for i in range(1, 10):
        if valid(board, i, (row, col)):
            board[row][col] = i
            if solve(board):
                return True
            board[row][col] = 0
    return False


def valid(board, num, pos):
    # false if number already in row, column, box
    # check row
    for i in range(len(board[0])):
        if board[pos[0]][i] == num and pos[1] != i:
            return False
    # check column
    for j in range(len(board)):
        if board[j][pos[1]] == num and pos[0] != j:
            return False
    # check box
    box_x = pos[1] // 3
    box_y = pos[0] // 3
    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if board[i][j] == num and (i, j) != pos:
                return False
    return True


# find the next empty space on the board
def find_empty(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i, j)  #i=row, j=col
    return None


def print_board(board):
    for row in range(len(board)):
        if (row % 3 == 0) and (row != 1):
            print("- - - - - - - - - - - - - - - - -")
        for col in range(len(board[row])):
            if (col % 3 == 0) and (col != 0):
                print(" | ", end="")
            print(board[row][col], " ", end="")
        print("\n")


generate_complete_board(b_0)
print("Complete board:")
print_board(b_0)
print("----------------------------------")
print("Unsolved board:")
generate_unsolved_board(b_0)
print_board(b_0)
print("----------------------------------")
print("Solved board:")
solve(b_0)
print_board(b_0)

