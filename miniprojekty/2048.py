import random


def board():
    return [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

def print_board(board):
    for row in board:
        print(row)

def add_new_tile(board):
    empty_tiles = []
    for i in range(4):
        for j in range(4):
            if board[i][j] == 0:
                empty_tiles.append((i, j))
    if empty_tiles:
        i, j = random.choice(empty_tiles)
        board[i][j] = 2

def move_left(board):
    for row in board:
        for i in range(3):
            for j in range(3, 0, -1):
                if row[j-1] == 0:
                    row[j-1] = row[j]
                    row[j] = 0
        for i in range(3):
            if row[i] == row[i+1]:
                row[i] *= 2
                row[i+1] = 0
        for i in range(3):
            for j in range(3, 0, -1):
                if row[j-1] == 0:
                    row[j-1] = row[j]
                    row[j] = 0

def move_right(board):
    for row in board:
        for i in range(3):
            for j in range(3):
                if row[j+1] == 0:
                    row[j+1] = row[j]
                    row[j] = 0
        for i in range(3):
            if row[i] == row[i+1]:
                row[i+1] *= 2
                row[i] = 0
        for i in range(3):
            for j in range(3):
                if row[j+1] == 0:
                    row[j+1] = row[j]
                    row[j] = 0

def move_up(board):
    """
    Moves all tiles on the board up, combining tiles of the same value.

    The function performs the following steps:
    1. Moves all tiles up to fill any empty spaces.
    2. Combines adjacent tiles of the same value, doubling the value of the tile and setting the combined tile to zero.
    3. Moves all tiles up again to fill any empty spaces created by the combination.

    Args:
        board (list of list of int): A 4x4 matrix representing the game board.

    Returns:
        None: The function modifies the board in place.
    """
    for j in range(4):
        for i in range(3):
            for k in range(3, 0, -1):
                if board[k-1][j] == 0:
                    board[k-1][j] = board[k][j]
                    board[k][j] = 0
        for i in range(3):
            if board[i][j] == board[i+1][j]:
                board[i][j] *= 2
                board[i+1][j] = 0
        for i in range(3):
            for k in range(3, 0, -1):
                if board[k-1][j] == 0:
                    board[k-1][j] = board[k][j]
                    board[k][j] = 0

def move_down(board):
    for j in range(4):
        for i in range(3):
            for k in range(3):
                if board[k+1][j] == 0:
                    board[k+1][j] = board[k][j]
                    board[k][j] = 0
        for i in range(3):
            if board[i][j] == board[i+1][j]:
                board[i+1][j] *= 2
                board[i][j] = 0
        for i in range(3):
            for k in range(3):
                if board[k+1][j] == 0:
                    board[k+1][j] = board[k][j]
                    board[k][j] = 0

def game_over(board):
    for i in range(4):
        for j in range(4):
            if board[i][j] == 0:
                return False
    for i in range(3):
        for j in range(3):
            if board[i][j] == board[i+1][j] or board[i][j] == board[i][j+1]:
                return False
    for i in range(3):
        if board[i][3] == board[i+1][3]:
            return False
    for j in range(3):
        if board[3][j] == board[3][j+1]:
            return False
    return True

def game():
    board1 = board()
    add_new_tile(board1)
    add_new_tile(board1)
    while True:
        print_board(board1)
        if game_over(board1):
            print("Game over!")
            break
        move = input("Enter move: ")
        if move == "w":
            move_up(board1)
        elif move == "s":
            move_down(board1)
        elif move == "a":
            move_left(board1)
        elif move == "d":
            move_right(board1)
        add_new_tile(board1)

game()