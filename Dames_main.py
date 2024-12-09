# Dames_main.py
import pygame
import sys
from Dames_gfx import draw_board
from Dames_bkend import create_board, is_valid_move, is_valid_capture, make_move

# Initialisation de Pygame
pygame.init()

# Taille de la cellule et de la planche
CELL_SIZE = 55
BOARD_SIZE = 10
WIDTH = HEIGHT = CELL_SIZE * BOARD_SIZE

# Création de la fenêtre
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dames")

# État initial de la planche
board = create_board()

# Tour du joueur ("R" ou "B")
current_player = "R"

# Pièce sélectionnée
selected_piece = None

# Boucle principale
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            col, row = event.pos[0] // CELL_SIZE, event.pos[1] // CELL_SIZE
            if selected_piece:
                # Annuler sélection si clique sur la même case
                if selected_piece == (row, col):
                    selected_piece = None
                else:
                    start_row, start_col = selected_piece
                    if is_valid_move(start_row, start_col, row, col, board) or is_valid_capture(start_row, start_col, row, col, board):
                        selected_piece = make_move(start_row, start_col, row, col, board, current_player)
            elif board[row][col] == current_player:
                selected_piece = (row, col)

    # Dessiner la planche et les pièces
    draw_board(screen, board, selected_piece, CELL_SIZE, BOARD_SIZE)
    pygame.display.flip()

pygame.quit()
sys.exit()
