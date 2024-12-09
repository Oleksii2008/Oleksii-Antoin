
import pygame

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)

# Affichage de la planche
def draw_board(screen, board, selected_piece, CELL_SIZE, BOARD_SIZE):
    for row in range(BOARD_SIZE):
        for col in range(BOARD_SIZE):
            # Case : noire ou blanche
            color = BLACK if (row + col) % 2 == 1 else WHITE
            pygame.draw.rect(screen, color, (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE))

            # Dessiner les pièces
            piece = board[row][col]
            if piece == "R":  # Pièce rouge
                pygame.draw.circle(screen, RED, (col * CELL_SIZE + CELL_SIZE // 2, row * CELL_SIZE + CELL_SIZE // 2), CELL_SIZE // 3)
            elif piece == "B":  # Pièce bleue
                pygame.draw.circle(screen, BLUE, (col * CELL_SIZE + CELL_SIZE // 2, row * CELL_SIZE + CELL_SIZE // 2), CELL_SIZE // 3)

            # Affichage de la pièce sélectionnée
            if selected_piece and selected_piece == (row, col):
                pygame.draw.circle(screen, GREEN, (col * CELL_SIZE + CELL_SIZE // 2, row * CELL_SIZE + CELL_SIZE // 2), CELL_SIZE // 3, 5)
