import pygame
import sys

# Initialisation de Pygame
pygame.init()

# Taille de la cellule et de la planche
CELL_SIZE = 50
BOARD_SIZE = 10
WIDTH = HEIGHT = CELL_SIZE * BOARD_SIZE

# Couleurs
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)

# Création de la fenêtre
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dames")


# État initial de la planche
def create_board():
    board = [[" " for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]
    for row in range(BOARD_SIZE):
        for col in range(BOARD_SIZE):
            # Placer les pièces rouges
            if row < 4 and (row + col) % 2 == 1:
                board[row][col] = "R"
            # Placer les pièces bleues
            elif row > 5 and (row + col) % 2 == 1:
                board[row][col] = "B"
    return board


board = create_board()

# Tour du joueur ("R" ou "B")
current_player = "R"

# Pièce sélectionnée
selected_piece = None


# Affichage de la planche
def draw_board():
    for row in range(BOARD_SIZE):
        for col in range(BOARD_SIZE):
            # Case : noire ou blanche
            color = BLACK if (row + col) % 2 == 1 else WHITE
            pygame.draw.rect(screen, color, (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE))

            # Dessiner les pièces
            piece = board[row][col]
            if piece == "R": # Pièce rouge
                pygame.draw.circle(screen, RED, (col * CELL_SIZE + CELL_SIZE // 2, row * CELL_SIZE + CELL_SIZE // 2),
                                   CELL_SIZE // 3)
            elif piece == "B": # Pièce bleue
                pygame.draw.circle(screen, BLUE, (col * CELL_SIZE + CELL_SIZE // 2, row * CELL_SIZE + CELL_SIZE // 2),
                                   CELL_SIZE // 3)

            # Affichage de la pièce sélectionnée
            if selected_piece and selected_piece == (row, col):
                pygame.draw.circle(screen, GREEN, (col * CELL_SIZE + CELL_SIZE // 2, row * CELL_SIZE + CELL_SIZE // 2),
                                   CELL_SIZE // 3, 5)


# Vérifier si la case est dans les limites de la planche
def is_valid_position(row, col):
    return 0 <= row < BOARD_SIZE and 0 <= col < BOARD_SIZE


# Vérifier si un mouvement est valide (sans retour en arrière)
def is_valid_move(start_row, start_col, end_row, end_col):
    if not is_valid_position(end_row, end_col):
        return False
    if board[end_row][end_col] != " ": # La case doit être vide
        return False
    piece = board[start_row][start_col]
    if piece == "R" and end_row > start_row and abs(end_col - start_col) == 1:
        return True
    if piece == "B" and end_row < start_row and abs(end_col - start_col) == 1:
        return True
    return False


# Vérifier si une capture est possible (battre une pièce, y compris en arrière)
def is_valid_capture(start_row, start_col, end_row, end_col):
    if not is_valid_position(end_row, end_col):
        return False
    if board[end_row][end_col] != " ": # La case doit être vide
        return False
    piece = board[start_row][start_col]
    mid_row = (start_row + end_row) // 2
    mid_col = (start_col + end_col) // 2
    if abs(end_row - start_row) == 2 and abs(end_col - start_col) == 2:
        if piece == "R":
            return board[mid_row][mid_col] == "B"
        if piece == "B":
            return board[mid_row][mid_col] == "R"
    return False


# Vérifier s'il y a encore des captures possibles
def can_capture(row, col):
    directions = [(-2, -2), (-2, 2), (2, -2), (2, 2)]
    for dr, dc in directions:
        if is_valid_capture(row, col, row + dr, col + dc):
            return True
    return False


# Effectuer un mouvement
def make_move(start_row, start_col, end_row, end_col):
    global current_player, selected_piece
    board[end_row][end_col] = board[start_row][start_col]
    board[start_row][start_col] = " "
    # Si c'est une capture, supprimer la pièce battue
    if abs(end_row - start_row) == 2:
        mid_row = (start_row + end_row) // 2
        mid_col = (start_col + end_col) // 2
        board[mid_row][mid_col] = " "
        # Vérifier les captures supplémentaires
        if can_capture(end_row, end_col):
            selected_piece = (end_row, end_col)
            return
    # Passer le tour à l'autre joueur
    current_player = "B" if current_player == "R" else "R"
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
                    if is_valid_move(start_row, start_col, row, col) or is_valid_capture(start_row, start_col, row, col):
                        make_move(start_row, start_col, row, col)
            elif board[row][col] == current_player:
                selected_piece = (row, col)

    # Dessiner la planche et les pièces
    draw_board()
    pygame.display.flip()

pygame.quit()
sys.exit()
