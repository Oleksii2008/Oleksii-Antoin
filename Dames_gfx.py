import pygame

# Load the texture
pion_image = pygame.image.load("pion.png")  # Ensure this is the correct path
pion_image = pygame.transform.scale(pion_image, (55, 55))  # Scale image to fit the square size

def dessiner_plateau(ecran, plateau, piece_selectionnee, taille_case, taille_plateau):
    """Fonction pour dessiner le plateau et les pièces avec leurs textures"""
    # Dessiner les cases
    for ligne in range(taille_plateau):
        for colonne in range(taille_plateau):
            if (ligne + colonne) % 2 == 0:
                color = (245, 222, 179)  # Beige clair pour les cases blanches
            else:
                color = (139, 69, 19)  # Marron foncé pour les cases noires
            pygame.draw.rect(ecran, color, (colonne * taille_case, ligne * taille_case, taille_case, taille_case))

    # Dessiner les pièces
    for ligne in range(taille_plateau):
        for colonne in range(taille_plateau):
            piece = plateau[ligne][colonne]
            if piece:
                # Définir la couleur de la pièce
                if piece == "R":  # Pièce rouge -> Blanc
                    couleur_piece = (255, 255, 255)  # Blanc
                elif piece == "B":  # Pièce bleue -> Gris foncé
                    couleur_piece = (125, 125, 125)  # Gris foncé
                elif piece == "QR":  # Dame rouge -> Blanc
                    couleur_piece = (255, 255, 255)  # Blanc
                elif piece == "QB":  # Dame bleue -> Gris foncé
                    couleur_piece = (125, 125, 125)  # Gris foncé

                # Dessiner l'image de la pièce
                if piece in ("R", "B", "QR", "QB"):
                    piece_surface = pion_image.copy()

                    # Appliquer une teinte plus sombre ou plus claire selon le type de pièce
                    if piece == "R" or piece == "QR":
                        piece_surface.fill((255, 255, 255), special_flags=pygame.BLEND_RGB_MULT)  # White pieces
                    elif piece == "B" or piece == "QB":
                        piece_surface.fill((125, 125, 125), special_flags=pygame.BLEND_RGB_MULT)  # Gray pieces

                    ecran.blit(piece_surface, (colonne * taille_case, ligne * taille_case))

    # Dessiner la pièce sélectionnée avec une bordure ou surlignage si nécessaire
    if piece_selectionnee:
        x, y = piece_selectionnee
        pygame.draw.rect(ecran, (255, 255, 0), (y * taille_case, x * taille_case, taille_case, taille_case), 5)
