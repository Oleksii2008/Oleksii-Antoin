# État initial de la planche
from Dames import board


def create_board(size):
    global board_size,board
    board_size=size
    board = [[" " for _ in range(board_size)] for _ in range(board_size)]
    for row in range(board_size):
        for col in range(board_size):
            # Placer les pièces rouges
            if row < 4 and (row + col) % 2 == 1:
                board[row][col] = "R"
            # Placer les pièces bleues
            elif row > 5 and (row + col) % 2 == 1:
                board[row][col] = "B"

    return board
def get_board():
    global board
    return board
bord_size=None
board=None