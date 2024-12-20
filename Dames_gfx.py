"""Dames_gfx.py"""
import pygame

# Load the texture
pion_image = pygame.image.load("pion.png")  # Ensure this is the correct path
pion_image = pygame.transform.scale(pion_image, (55, 55))  # Scale image to fit the square size


def dessiner_plateau(ecran, plateau, piece_selectionnee, taille_case, taille_plateau):
    """Fonction pour dessiner le plateau et les pièces avec leurs textures"""
    # Dessiner les cases
    for ligne in range(taille_plateau):
        for colonne in range(taille_plateau):
            color = (255, 255, 255) if (ligne + colonne) % 2 == 0 else (0, 0, 0)
            pygame.draw.rect(ecran, color, (colonne * taille_case, ligne * taille_case, taille_case, taille_case))

    # Dessiner les pièces
    for ligne in range(taille_plateau):
        for colonne in range(taille_plateau):
            piece = plateau[ligne][colonne]
            if piece:
                # Définir la couleur de la pièce
                if piece == "R":  # Pièce rouge
                    couleur_piece = (200, 0, 0)  # Rouge foncé
                elif piece == "B":  # Pièce bleue
                    couleur_piece = (173, 216, 230)  # Bleu clair
                elif piece == "QR":  # Dame rouge
                    couleur_piece = (255, 0, 0)  # Rouge vif
                elif piece == "QB":  # Dame bleue
                    couleur_piece = (0, 0, 255)  # Bleu vif

                # Dessiner l'image de la pièce
                if piece in ("R", "B", "QR", "QB"):
                    piece_surface = pion_image.copy()

                    # Appliquer une teinte plus sombre ou plus claire selon le type de pièce
                    if piece == "R" or piece == "QR":
                        piece_surface.fill((139, 230, 0), special_flags=pygame.BLEND_RGB_MULT)  # Darken the piece
                    elif piece == "B" or piece == "QB":
                        piece_surface.fill((173, 216, 230), special_flags=pygame.BLEND_RGB_MULT)  # Lighten the piece

                    ecran.blit(piece_surface, (colonne * taille_case, ligne * taille_case))

    # Dessiner la pièce sélectionnée avec une bordure ou surlignage si nécessaire
    if piece_selectionnee:
        x, y = piece_selectionnee
        pygame.draw.rect(ecran, (255, 255, 0), (y * taille_case, x * taille_case, taille_case, taille_case), 5)

