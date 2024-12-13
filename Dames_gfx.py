import pygame

BLANC = (255, 255, 255)
NOIR = (0, 0, 0)
ROUGE = (255, 0, 0)
BLEU = (0, 0, 255)
VERT = (0, 255, 0)

def dessiner_plateau(ecran, plateau, piece_selectionnee, TAILLE_CASE, TAILLE_PLATEAU):
    """Dessine le plateau et les pièces"""
    for ligne in range(TAILLE_PLATEAU):
        for colonne in range(TAILLE_PLATEAU):
            couleur = NOIR if (ligne + colonne) % 2 == 1 else BLANC
            pygame.draw.rect(ecran, couleur, (colonne * TAILLE_CASE, ligne * TAILLE_CASE, TAILLE_CASE, TAILLE_CASE))

            piece = plateau[ligne][colonne]
            if piece == "R":
                pygame.draw.circle(ecran, ROUGE, (colonne * TAILLE_CASE + TAILLE_CASE // 2, ligne * TAILLE_CASE + TAILLE_CASE // 2), TAILLE_CASE // 3)
            elif piece == "B":
                pygame.draw.circle(ecran, BLEU, (colonne * TAILLE_CASE + TAILLE_CASE // 2, ligne * TAILLE_CASE + TAILLE_CASE // 2), TAILLE_CASE // 3)
            elif piece == "QR":
                pygame.draw.circle(ecran, ROUGE, (colonne * TAILLE_CASE + TAILLE_CASE // 2, ligne * TAILLE_CASE + TAILLE_CASE // 2), TAILLE_CASE // 3)
                pygame.draw.circle(ecran, BLANC, (colonne * TAILLE_CASE + TAILLE_CASE // 2, ligne * TAILLE_CASE // 2), TAILLE_CASE // 4, 3)
            elif piece == "QB":
                pygame.draw.circle(ecran, BLEU, (colonne * TAILLE_CASE + TAILLE_CASE // 2, ligne * TAILLE_CASE + TAILLE_CASE // 2), TAILLE_CASE // 3)
                pygame.draw.circle(ecran, BLANC, (colonne * TAILLE_CASE + TAILLE_CASE // 2, ligne * TAILLE_CASE // 2), TAILLE_CASE // 4, 3)

            if piece_selectionnee and piece_selectionnee == (ligne, colonne):
                pygame.draw.circle(ecran, VERT, (colonne * TAILLE_CASE + TAILLE_CASE // 2, ligne * TAILLE_CASE + TAILLE_CASE // 2), TAILLE_CASE // 3, 5)
