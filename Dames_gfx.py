#Dames_gfx.py
import pygame

pion_image = pygame.image.load("pion.png")  # Vérifiez le chemin de l'image
pion_image = pygame.transform.scale(pion_image, (55, 55))  # Redimensionner l'image pour correspondre à la taille des cases

def dessiner_plateau(ecran, plateau, piece_selectionnee, taille_case, longueur, hauteur):
    """Fonction pour dessiner le plateau et les pièces avec leurs textures"""
    # Dessiner les cases
    for ligne in range(hauteur):
        for colonne in range(longueur):
            if (ligne + colonne) % 2 == 0:
                color = (245, 222, 179)  # Beige clair pour les cases blanches
            else:
                color = (139, 69, 19)  # Marron foncé pour les cases noires
            pygame.draw.rect(ecran, color, (colonne * taille_case, ligne * taille_case, taille_case, taille_case))

    # Dessiner les pièces
    for ligne in range(hauteur):
        for colonne in range(longueur):
            piece = plateau[ligne][colonne]
            if piece:
                if piece == "R":
                    couleur_piece = (255, 255, 255)  # Blanc pour les pièces rouges
                elif piece == "B":
                    couleur_piece = (125, 125, 125)  # Gris foncé pour les pièces bleues
                elif piece == "QR":
                    couleur_piece = (255, 255, 255)  # Blanc pour les dames rouges
                elif piece == "QB":
                    couleur_piece = (125, 125, 125)  # Gris foncé pour les dames bleues

                if piece in ("R", "B", "QR", "QB"):
                    piece_surface = pion_image.copy()

                    # Appliquer une teinte plus claire ou plus foncée selon le type de pièce
                    if piece == "R" or piece == "QR":
                        piece_surface.fill((255, 255, 255), special_flags=pygame.BLEND_RGB_MULT)
                    elif piece == "B" or piece == "QB":
                        piece_surface.fill((125, 125, 125), special_flags=pygame.BLEND_RGB_MULT)

                    ecran.blit(piece_surface, (colonne * taille_case, ligne * taille_case))

    # Dessiner la pièce sélectionnée avec une bordure ou un surlignage
    if piece_selectionnee:
        x, y = piece_selectionnee
        pygame.draw.rect(ecran, (255, 255, 0), (y * taille_case, x * taille_case, taille_case, taille_case), 5)
