import pygame
import sys

# Initialisation de Pygame
pygame.init()

# Taille des cellules et de la planche
CELL_SIZE = 55  # Taille de chaque cellule sur le plateau
board_size = 10  # Taille de la planche (10x10)
WIDTH = HEIGHT = CELL_SIZE * board_size  # Largeur et hauteur de la fenêtre (10x10 cellules)

# Définition des couleurs
WHITE = (255, 255, 255)  # Blanc
BLACK = (0, 0, 0)  # Noir
RED = (255, 0, 0)  # Rouge
BLUE = (0, 0, 255)  # Bleu
GREEN = (0, 255, 0)  # Vert (pour mettre en surbrillance une pièce sélectionnée)

# Création de la fenêtre
screen = pygame.display.set_mode((WIDTH, HEIGHT))  # Définir la taille de la fenêtre
pygame.display.set_caption("Dames")  # Titre de la fenêtre

# Fonction pour créer l'état initial du plateau
def create_board():
    board = [[" " for _ in range(board_size)] for _ in range(board_size)]  # Création d'une planche vide
    # Placer les pièces
    for row in range(board_size):
        for col in range(board_size):
            # Placer les pièces rouges (dans les rangées supérieures)
            if row < 4 and (row + col) % 2 == 1:
                board[row][col] = "R"
            # Placer les pièces bleues (dans les rangées inférieures)
            elif row > 5 and (row + col) % 2 == 1:
                board[row][col] = "B"
    return board  # Retourner le plateau créé

# Initialiser le plateau
board = create_board()

# Joueur actuel ("R" pour les rouges, "B" pour les bleus)
current_player = "R"

# Variable pour garder la pièce sélectionnée
selected_piece = None

# Fonction pour dessiner le plateau
def draw_board():
    for row in range(board_size):
        for col in range(board_size):
            # Déterminer la couleur de la cellule (noir ou blanc)
            color = BLACK if (row + col) % 2 == 1 else WHITE
            # Dessiner la cellule
            pygame.draw.rect(screen, color, (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE))

            # Dessiner les pièces
            piece = board[row][col]
            if piece == "R":  # Pièce rouge
                pygame.draw.circle(screen, RED, (col * CELL_SIZE + CELL_SIZE // 2, row * CELL_SIZE + CELL_SIZE // 2),
                                   CELL_SIZE // 3)
            elif piece == "B":  # Pièce bleue
                pygame.draw.circle(screen, BLUE, (col * CELL_SIZE + CELL_SIZE // 2, row * CELL_SIZE + CELL_SIZE // 2),
                                   CELL_SIZE // 3)

            # Dessiner la pièce sélectionnée (si elle existe)
            if selected_piece and selected_piece == (row, col):
                pygame.draw.circle(screen, GREEN, (col * CELL_SIZE + CELL_SIZE // 2, row * CELL_SIZE + CELL_SIZE // 2),
                                   CELL_SIZE // 3, 5)

# Fonction pour vérifier si une position est valide (dans les limites de la planche)
def is_valid_position(row, col):
    return 0 <= row < board_size and 0 <= col < board_size

# Fonction pour vérifier si un mouvement est valide
def is_valid_move(start_row, start_col, end_row, end_col):
    if not is_valid_position(end_row, end_col):  # Vérifier si la case de destination est dans les limites
        return False
    if board[end_row][end_col] != " ":  # La case doit être vide
        return False
    piece = board[start_row][start_col]
    # Pour les pièces rouges (qui se déplacent vers le bas)
    if piece == "R" and end_row > start_row and abs(end_col - start_col) == 1:
        return True
    # Pour les pièces bleues (qui se déplacent vers le haut)
    if piece == "B" and end_row < start_row and abs(end_col - start_col) == 1:
        return True
    return False

# Fonction pour vérifier si une capture est valide
def is_valid_capture(start_row, start_col, end_row, end_col):
    if not is_valid_position(end_row, end_col):  # Vérifier si la case de destination est dans les limites
        return False
    if board[end_row][end_col] != " ":  # La case de destination doit être vide
        return False
    piece = board[start_row][start_col]
    mid_row = (start_row + end_row) // 2  # La case intermédiaire entre le départ et l'arrivée
    mid_col = (start_col + end_col) // 2
    # Vérifier que le mouvement est de 2 cases et que la case intermédiaire contient l'adversaire
    if abs(end_row - start_row) == 2 and abs(end_col - start_col) == 2:
        if piece == "R":
            return board[mid_row][mid_col] == "B"  # Si c'est une pièce rouge, la case intermédiaire doit être bleue
        if piece == "B":
            return board[mid_row][mid_col] == "R"  # Si c'est une pièce bleue, la case intermédiaire doit être rouge
    return False

# Fonction pour vérifier si une pièce peut capturer
def can_capture(row, col):
    directions = [(-2, -2), (-2, 2), (2, -2), (2, 2)]  # Les 4 directions possibles pour une capture
    for dr, dc in directions:
        if is_valid_capture(row, col, row + dr, col + dc):  # Vérifier si une capture est possible dans chaque direction
            return True
    return False

# Fonction pour effectuer un mouvement
def make_move(start_row, start_col, end_row, end_col):
    global current_player, selected_piece
    board[end_row][end_col] = board[start_row][start_col]  # Déplacer la pièce vers la nouvelle case
    board[start_row][start_col] = " "  # Vider la case de départ
    # Si c'est une capture (mouvement de 2 cases), supprimer la pièce capturée
    if abs(end_row - start_row) == 2:
        mid_row = (start_row + end_row) // 2
        mid_col = (start_col + end_col) // 2
        board[mid_row][mid_col] = " "
        # Vérifier s'il y a d'autres captures possibles après ce mouvement
        if can_capture(end_row, end_col):
            selected_piece = (end_row, end_col)  # Conserver la pièce sélectionnée pour une capture supplémentaire
            return
    # Passer le tour au joueur suivant
    current_player = "B" if current_player == "R" else "R"
    selected_piece = None

# Boucle principale de la partie
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False  # Quitter la partie si l'utilisateur ferme la fenêtre

        if event.type == pygame.MOUSEBUTTONDOWN:
            col, row = event.pos[0] // CELL_SIZE, event.pos[1] // CELL_SIZE  # Calculer la cellule cliquée
            if selected_piece:
                # Si une pièce est déjà sélectionnée, essayer de déplacer ou de capturer
                if selected_piece == (row, col):
                    selected_piece = None  # Annuler la sélection si on clique sur la même cellule
                else:
                    start_row, start_col = selected_piece
                    # Vérifier si le mouvement ou la capture est valide
                    if is_valid_move(start_row, start_col, row, col) or is_valid_capture(start_row, start_col, row, col):
                        make_move(start_row, start_col, row, col)  # Effectuer le mouvement
            elif board[row][col] == current_player:  # Si une pièce du joueur actuel est sélectionnée
                selected_piece = (row, col)  # Sélectionner cette pièce

    # Dessiner la planche et les pièces sur l'écran
    draw_board()
    pygame.display.flip()  # Mettre à jour l'affichage

pygame.quit()  # Quitter Pygame
sys.exit()  # Quitter le programme
