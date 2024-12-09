# Dames_bkend.py

BOARD_SIZE = 10

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

# Vérifier si la case est dans les limites de la planche
def is_valid_position(row, col):
    return 0 <= row < BOARD_SIZE and 0 <= col < BOARD_SIZE

# Vérifier si un mouvement est valide (sans retour en arrière)
def is_valid_move(start_row, start_col, end_row, end_col, board):
    if not is_valid_position(end_row, end_col):
        return False
    if board[end_row][end_col] != " ":  # La case doit être vide
        return False
    piece = board[start_row][start_col]
    if piece == "R" and end_row > start_row and abs(end_col - start_col) == 1:
        return True
    if piece == "B" and end_row < start_row and abs(end_col - start_col) == 1:
        return True
    return False

# Vérifier si une capture est possible (battre une pièce, y compris en arrière)
def is_valid_capture(start_row, start_col, end_row, end_col, board):
    if not is_valid_position(end_row, end_col):
        return False
    if board[end_row][end_col] != " ":  # La case doit être vide
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
def can_capture(row, col, board):
    directions = [(-2, -2), (-2, 2), (2, -2), (2, 2)]
    for dr, dc in directions:
        if is_valid_capture(row, col, row + dr, col + dc, board):
            return True
    return False

# Effectuer un mouvement
def make_move(start_row, start_col, end_row, end_col, board):
    board[end_row][end_col] = board[start_row][start_col]
    board[start_row][start_col] = " "
    # Si c'est une capture, supprimer la pièce battue
    if abs(end_row - start_row) == 2:
        mid_row = (start_row + end_row) // 2
        mid_col = (start_col + end_col) // 2
        board[mid_row][mid_col] = " "
        # Vérifier les captures supplémentaires
        if can_capture(end_row, end_col, board):
            return None # Le joueur continue de capturer
    return "B" if board[end_row][end_col] == "R" else "R" # Changer de joueur après le coup

