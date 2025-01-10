# Dames_main.py
import pygame
from Dames_gfx import dessiner_plateau
from Dames_bkend import creer_plateau, mouvement_valide, capture_valide, effectuer_mouvement, peut_continuer_capture, verifier_coups_possibles
from Dames_menu import afficher_menu_final

pygame.init()

# Demander la taille du plateau
TAILLE_CASE = 55

# S'assurer que la largeur est au moins 4 et la hauteur au moins 4, et maximum 16
longueur = int(input("Entrez le nombre de cases en largeur (minimum 4, maximum 16) : "))
while longueur < 4 or longueur > 16:
    longueur = int(input("La largeur doit être entre 4 et 16. Entrez à nouveau le nombre de cases en largeur : "))

hauteur = int(input("Entrez le nombre de cases en hauteur (minimum 9, maximum 16) : "))
while hauteur < 9 or hauteur > 16:
    hauteur = int(input("La hauteur doit être entre 9 et 16. Entrez à nouveau le nombre de cases en hauteur : "))

LARGEUR = TAILLE_CASE * longueur
HAUTEUR = TAILLE_CASE * hauteur

ecran = pygame.display.set_mode((LARGEUR, HAUTEUR))
pygame.display.set_caption("Dames")

plateau = creer_plateau(longueur, hauteur)  # Créer un plateau avec la taille spécifiée
historique = [creer_plateau(longueur, hauteur)]  # Historique des états du plateau
joueur_actuel = "R"
piece_selectionnee = None
coups_rouge = 0
coups_bleu = 0

en_cours = True

# Fonction pour vérifier si un joueur a gagné
def verifier_victoire(plateau):
    rouge = False
    bleu = False
    for ligne in plateau:
        for case in ligne:
            if case == "R" or case == "QR":
                rouge = True
            if case == "B" or case == "QB":
                bleu = True
    if not rouge:
        return "Bleu"
    if not bleu:
        return "Rouge"
    return None

# Vérification de la capture obligatoire
def capture_obligatoire(joueur, plateau):
    for ligne in range(hauteur):
        for colonne in range(longueur):
            piece = plateau[ligne][colonne]
            if piece and piece[0] == joueur and peut_continuer_capture(ligne, colonne, plateau):
                return True
    return False

while en_cours:
    for evenement in pygame.event.get():
        if evenement.type == pygame.QUIT:
            en_cours = False

        if evenement.type == pygame.MOUSEBUTTONDOWN:
            colonne, ligne = evenement.pos[0] // TAILLE_CASE, evenement.pos[1] // TAILLE_CASE
            if piece_selectionnee:
                depart_ligne, depart_colonne = piece_selectionnee
                if capture_valide(depart_ligne, depart_colonne, ligne, colonne, plateau) or mouvement_valide(depart_ligne, depart_colonne, ligne, colonne, plateau):
                    historique.append([ligne[:] for ligne in plateau])
                    joueur_actuel = effectuer_mouvement(depart_ligne, depart_colonne, ligne, colonne, plateau)
                    piece_selectionnee = None
                else:
                    piece_selectionnee = (ligne, colonne)
            elif plateau[ligne][colonne] and plateau[ligne][colonne][0] == joueur_actuel:
                piece_selectionnee = (ligne, colonne)

    # Перевірка чи є можливі ходи
    if not verifier_coups_possibles(joueur_actuel, plateau):
        gagnant = "Bleu" if joueur_actuel == "R" else "Rouge"
        choix = afficher_menu_final(ecran, gagnant, coups_rouge, coups_bleu, LARGEUR, HAUTEUR)
        if choix == "restart":
            plateau = creer_plateau(longueur, hauteur)
            historique = [creer_plateau(longueur, hauteur)]
            joueur_actuel = "R"
            coups_rouge = 0
            coups_bleu = 0
            piece_selectionnee = None
        else:
            en_cours = False

    dessiner_plateau(ecran, plateau, piece_selectionnee, TAILLE_CASE, longueur, hauteur)
    pygame.display.flip()

pygame.quit()
