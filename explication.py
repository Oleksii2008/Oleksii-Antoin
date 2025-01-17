def creer_plateau(longueur, hauteur):
    plateau = [[None] * longueur for _ in range(hauteur)]
    for ligne in range(4):
        for colonne in range(longueur):
            if (ligne + colonne) % 2 == 1:
                plateau[ligne][colonne] = "B"
    for ligne in range(hauteur - 4, hauteur):
        for colonne in range(longueur):
            if (ligne + colonne) % 2 == 1:
                plateau[ligne][colonne] = "R"
    return plateau

def mouvement_valide(depart_ligne, depart_colonne, arrivee_ligne, arrivee_colonne, plateau):
    if not (0 <= arrivee_ligne < len(plateau) and 0 <= arrivee_colonne < len(plateau[0])):
        return False
    piece = plateau[depart_ligne][depart_colonne]
    if piece in ("R", "B"):
        if abs(depart_ligne - arrivee_ligne) == 1 and abs(depart_colonne - arrivee_colonne) == 1:
            if plateau[arrivee_ligne][arrivee_colonne] is None:
                return (arrivee_ligne - depart_ligne) == (-1 if piece == "R" else 1)
    return False

def capture_valide(depart_ligne, depart_colonne, arrivee_ligne, arrivee_colonne, plateau):
    if not (0 <= arrivee_ligne < len(plateau) and 0 <= arrivee_colonne < len(plateau[0])):
        return False
    piece = plateau[depart_ligne][depart_colonne]
    milieu_ligne = (depart_ligne + arrivee_ligne) // 2
    milieu_colonne = (depart_colonne + arrivee_colonne) // 2
    adversaire = "B" if piece == "R" else "R"
    if piece in ("R", "B"):
        if abs(depart_ligne - arrivee_ligne) == 2 and abs(depart_colonne - arrivee_colonne) == 2:
            if plateau[arrivee_ligne][arrivee_colonne] is None:
                return plateau[milieu_ligne][milieu_colonne] == adversaire
    return False

def mouvement_valide_damka(depart_ligne, depart_colonne, arrivee_ligne, arrivee_colonne, plateau):
    if abs(depart_ligne - arrivee_ligne) == abs(depart_colonne - arrivee_colonne): # Діагональ
        step_ligne = 1 if arrivee_ligne > depart_ligne else -1
        step_colonne = 1 if arrivee_colonne > depart_colonne else -1
        ligne, colonne = depart_ligne + step_ligne, depart_colonne + step_colonne
        while ligne != arrivee_ligne and colonne != arrivee_colonne:
            if plateau[ligne][colonne] is not None: # Шлях зайнятий
                return False
            ligne += step_ligne
            colonne += step_colonne
        return plateau[arrivee_ligne][arrivee_colonne] is None
    return False

def capture_valide_damka(depart_ligne, depart_colonne, arrivee_ligne, arrivee_colonne, plateau):
    if abs(depart_ligne - arrivee_ligne) == abs(depart_colonne - arrivee_colonne):
        step_ligne = 1 if arrivee_ligne > depart_ligne else -1
        step_colonne = 1 if arrivee_colonne > depart_colonne else -1
        ligne, colonne = depart_ligne + step_ligne, depart_colonne + step_colonne
        захоплення = False
        while ligne != arrivee_ligne and colonne != arrivee_colonne:
            if plateau[ligne][colonne] in ("R", "B", "RD", "BD"):
                if захоплення: # Якщо вже було захоплення
                    return False
                захоплення = True
            elif plateau[ligne][colonne] is not None:
                return False
            ligne += step_ligne
            colonne += step_colonne
        return захоплення and plateau[arrivee_ligne][arrivee_colonne] is None
    return False

def effectuer_mouvement(depart_ligne, depart_colonne, arrivee_ligne, arrivee_colonne, plateau):
    piece = plateau[depart_ligne][depart_colonne]
    plateau[depart_ligne][depart_colonne] = None
    plateau[arrivee_ligne][arrivee_colonne] = piece
    if abs(depart_ligne - arrivee_ligne) == 2: # Захоплення
        milieu_ligne = (depart_ligne + arrivee_ligne) // 2
        milieu_colonne = (depart_colonne + arrivee_colonne) // 2
        plateau[milieu_ligne][milieu_colonne] = None
    # Перетворення в дамку
    if piece == "R" and arrivee_ligne == 0:
        plateau[arrivee_ligne][arrivee_colonne] = "RD"
    elif piece == "B" and arrivee_ligne == len(plateau) - 1:
        plateau[arrivee_ligne][arrivee_colonne] = "BD"
    return plateau

def effectuer_mouvement_damka(depart_ligne, depart_colonne, arrivee_ligne, arrivee_colonne, plateau):
    piece = plateau[depart_ligne][depart_colonne]
    plateau[depart_ligne][depart_colonne] = None
    plateau[arrivee_ligne][arrivee_colonne] = piece
    if abs(depart_ligne - arrivee_ligne) > 1:
        step_ligne = 1 if arrivee_ligne > depart_ligne else -1
        step_colonne = 1 if arrivee_colonne > depart_colonne else -1
        ligne, colonne = depart_ligne + step_ligne, depart_colonne + step_colonne
        while ligne != arrivee_ligne and colonne != arrivee_colonne:
            if plateau[ligne][colonne] in ("R", "B", "RD", "BD"):
                plateau[ligne][colonne] = None
                break
            ligne += step_ligne
            colonne += step_colonne
    return plateau

# Основна гра
import pygame

TAILLE_CASE = 55
longueur = 8
hauteur = 8
LARGEUR = TAILLE_CASE * longueur
HAUTEUR = TAILLE_CASE * hauteur

pygame.init()
ecran = pygame.display.set_mode((LARGEUR, HAUTEUR))
pygame.display.set_caption("Jeu de Dames")
plateau = creer_plateau(longueur, hauteur)
joueur_actuel = "R"
piece_selectionnee = None
en_cours = True

while en_cours:
    for evenement in pygame.event.get():
        if evenement.type == pygame.QUIT:
            en_cours = False
        if evenement.type == pygame.MOUSEBUTTONDOWN:
            colonne, ligne = evenement.pos[0] // TAILLE_CASE, evenement.pos[1] // TAILLE_CASE
            if piece_selectionnee:
                depart_ligne, depart_colonne = piece_selectionnee
                piece = plateau[depart_ligne][depart_colonne]
                if piece in ("RD", "BD"):
                    if capture_valide_damka(depart_ligne, depart_colonne, ligne, colonne, plateau):
                        effectuer_mouvement_damka(depart_ligne, depart_colonne, ligne, colonne, plateau)
                        piece_selectionnee = None
                        joueur_actuel = "B" if joueur_actuel == "R" else "R"
                    elif mouvement_valide_damka(depart_ligne, depart_colonne, ligne, colonne, plateau):
                        effectuer_mouvement_damka(depart_ligne, depart_colonne, ligne, colonne, plateau)
                        piece_selectionnee = None
                        joueur_actuel = "B" if joueur_actuel == "R" else "R"
                else:
                    if capture_valide(depart_ligne, depart_colonne, ligne, colonne, plateau):
                        effectuer_mouvement(depart_ligne, depart_colonne, ligne, colonne, plateau)
                        piece_selectionnee = None
                        joueur_actuel = "B" if joueur_actuel == "R" else "R"
                    elif mouvement_valide(depart_ligne, depart_colonne, ligne, colonne, plateau):
                        effectuer_mouvement(depart_ligne, depart_colonne, ligne, colonne, plateau)
                        piece_selectionnee = None
                        joueur_actuel = "B" if joueur_actuel == "R" else "R"
            elif plateau[ligne][colonne] and plateau[ligne][colonne][0] == joueur_actuel:
                piece_selectionnee = (ligne, colonne)

pygame.quit()
