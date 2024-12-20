#Dames_main.py
import pygame
from Dames_gfx import dessiner_plateau
from Dames_bkend import creer_plateau, mouvement_valide, capture_valide, effectuer_mouvement, peut_continuer_capture

pygame.init()

TAILLE_CASE = 55
TAILLE_PLATEAU = 10
LARGEUR = HAUTEUR = TAILLE_CASE * TAILLE_PLATEAU

ecran = pygame.display.set_mode((LARGEUR, HAUTEUR))
pygame.display.set_caption("Dames")

plateau = creer_plateau()
historique = [creer_plateau()]  # Historique des états du plateau
joueur_actuel = "R"
piece_selectionnee = None

en_cours = True

# Vérification si une capture est possible pour le joueur actuel
def capture_obligatoire(joueur, plateau):
    for ligne in range(TAILLE_PLATEAU):
        for colonne in range(TAILLE_PLATEAU):
            piece = plateau[ligne][colonne]
            if piece and piece[0] == joueur and peut_continuer_capture(ligne, colonne, plateau):
                return True
    return False

# Vérification de l'absence de capture obligatoire
def capture_possible(joueur, plateau):
    for ligne in range(TAILLE_PLATEAU):
        for colonne in range(TAILLE_PLATEAU):
            piece = plateau[ligne][colonne]
            if piece and piece[0] == joueur:
                if peut_continuer_capture(ligne, colonne, plateau):
                    return True
    return False

while en_cours:
    for evenement in pygame.event.get():
        if evenement.type == pygame.QUIT:
            en_cours = False

        if evenement.type == pygame.KEYDOWN:
            if evenement.key == pygame.K_BACKSPACE and len(historique) > 1:
                historique.pop()
                plateau = [ligne[:] for ligne in historique[-1]]
                joueur_actuel = "B" if joueur_actuel == "R" else "R"
                piece_selectionnee = None

        if evenement.type == pygame.MOUSEBUTTONDOWN:
            colonne, ligne = evenement.pos[0] // TAILLE_CASE, evenement.pos[1] // TAILLE_CASE
            if piece_selectionnee:
                depart_ligne, depart_colonne = piece_selectionnee
                if capture_valide(depart_ligne, depart_colonne, ligne, colonne, plateau):
                    # Si capture valide, faire le mouvement
                    historique.append([ligne[:] for ligne in plateau])
                    nouveau_joueur = effectuer_mouvement(depart_ligne, depart_colonne, ligne, colonne, plateau)
                    if nouveau_joueur:
                        joueur_actuel = nouveau_joueur
                        piece_selectionnee = None
                    else:
                        piece_selectionnee = (ligne, colonne)
                elif mouvement_valide(depart_ligne, depart_colonne, ligne, colonne, plateau) and not capture_possible(joueur_actuel, plateau):
                    # Si aucune capture n'est possible, permettre un mouvement normal
                    historique.append([ligne[:] for ligne in plateau])
                    nouveau_joueur = effectuer_mouvement(depart_ligne, depart_colonne, ligne, colonne, plateau)
                    if nouveau_joueur:
                        joueur_actuel = nouveau_joueur
                        piece_selectionnee = None
                    else:
                        piece_selectionnee = (ligne, colonne)
                else:
                    piece_selectionnee = None  # Désélectionner si mouvement non valide
            elif plateau[ligne][colonne] and plateau[ligne][colonne][0] == joueur_actuel:
                # Vérifier s'il y a une capture obligatoire
                if capture_possible(joueur_actuel, plateau):
                    # Si une capture est possible, ne pas permettre la sélection d'une pièce sans possibilité de capture
                    if peut_continuer_capture(ligne, colonne, plateau):
                        piece_selectionnee = (ligne, colonne)
                else:
                    piece_selectionnee = (ligne, colonne)

    dessiner_plateau(ecran, plateau, piece_selectionnee, TAILLE_CASE, TAILLE_PLATEAU)
    pygame.display.flip()

pygame.quit()

