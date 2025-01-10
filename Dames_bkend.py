#Dames_bkend.py
def creer_plateau(longueur, hauteur):
    """Créer un plateau avec les pièces initiales"""
    plateau = [[None] * longueur for _ in range(hauteur)]

    # Placer les pièces bleues sur les 4 premières lignes
    for ligne in range(4):
        for colonne in range(longueur):
            if (ligne + colonne) % 2 == 1:
                plateau[ligne][colonne] = "B"  # Pièces bleues

    # Placer les pièces rouges sur les 4 dernières lignes
    for ligne in range(hauteur - 4, hauteur):
        for colonne in range(longueur):
            if (ligne + colonne) % 2 == 1:
                plateau[ligne][colonne] = "R"  # Pièces rouges

    return plateau

def promouvoir_dame(ligne, colonne, plateau):
    """Promouvoir un pion en dame s'il atteint l'autre côté du plateau"""
    # Si un pion rouge atteint la première ligne, il devient une dame rouge
    if plateau[ligne][colonne] == "R" and ligne == 0:
        plateau[ligne][colonne] = "QR"
    # Si un pion bleu atteint la dernière ligne, il devient une dame bleue
    elif plateau[ligne][colonne] == "B" and ligne == len(plateau) - 1:
        plateau[ligne][colonne] = "QB"



def mouvement_valide(depart_ligne, depart_colonne, arrivee_ligne, arrivee_colonne, plateau):
    """Vérifie si le mouvement est valide pour une pièce"""
    piece = plateau[depart_ligne][depart_colonne]
    direction = -1 if piece in ("R", "QR") else 1
    if abs(depart_ligne - arrivee_ligne) == 1 and abs(depart_colonne - arrivee_colonne) == 1:
        if plateau[arrivee_ligne][arrivee_colonne] is None:
            return (arrivee_ligne - depart_ligne) == direction or piece in ("QR", "QB")
    return False


def capture_valide(depart_ligne, depart_colonne, arrivee_ligne, arrivee_colonne, plateau):
    """Vérifie si une capture est valide"""
    piece = plateau[depart_ligne][depart_colonne]
    direction = -1 if piece in ("R", "QR") else 1
    milieu_ligne = (depart_ligne + arrivee_ligne) // 2
    milieu_colonne = (depart_colonne + arrivee_colonne) // 2
    adversaire = "B" if piece in ("R", "QR") else "R"
    adversaire_dame = "QB" if piece in ("R", "QR") else "QR"

    if abs(depart_ligne - arrivee_ligne) == 2 and abs(depart_colonne - arrivee_colonne) == 2:
        if plateau[arrivee_ligne][arrivee_colonne] is None:
            return plateau[milieu_ligne][milieu_colonne] in (adversaire, adversaire_dame)
    return False


def promouvoir_dame(ligne, colonne, plateau):
    """Promouvoir un pion en dame"""
    if plateau[ligne][colonne] == "R" and ligne == 0:
        plateau[ligne][colonne] = "QR"
    elif plateau[ligne][colonne] == "B" and ligne == len(plateau) - 1:
        plateau[ligne][colonne] = "QB"


def effectuer_mouvement(depart_ligne, depart_colonne, arrivee_ligne, arrivee_colonne, plateau):
    """Effectue un mouvement et retourne le joueur suivant"""
    piece = plateau[depart_ligne][depart_colonne]
    plateau[depart_ligne][depart_colonne] = None
    plateau[arrivee_ligne][arrivee_colonne] = piece

    # Si c'est une capture, supprimer la pièce adverse
    if abs(depart_ligne - arrivee_ligne) == 2:
        milieu_ligne = (depart_ligne + arrivee_ligne) // 2
        milieu_colonne = (depart_colonne + arrivee_colonne) // 2
        plateau[milieu_ligne][milieu_colonne] = None

        # Vérifier s'il est possible de continuer à capturer
        if peut_continuer_capture(arrivee_ligne, arrivee_colonne, plateau):
            return None  # Le joueur peut continuer à jouer

    # Promouvoir en dame si nécessaire
    promouvoir_dame(arrivee_ligne, arrivee_colonne, plateau)

    # Changer de joueur
    return "B" if piece in ("R", "QR") else "R"


def peut_continuer_capture(ligne, colonne, plateau):
    """Vérifie si une pièce peut continuer a capturer"""
    piece = plateau[ligne][colonne]
    directions = [(-2, -2), (-2, 2), (2, -2), (2, 2)]  # Toutes les directions possibles de capture
    for dr, dc in directions:
        nouvelle_ligne, nouvelle_colonne = ligne + dr, colonne + dc
        milieu_ligne, milieu_colonne = ligne + dr // 2, colonne + dc // 2

        # Vérifier si la nouvelle position est dans les limites du plateau
        if 0 <= nouvelle_ligne < len(plateau) and 0 <= nouvelle_colonne < len(plateau[0]):
            if plateau[nouvelle_ligne][nouvelle_colonne] is None:
                adversaire = "B" if piece in ("R", "QR") else "R"
                adversaire_dame = "QB" if piece in ("R", "QR") else "QR"
                if plateau[milieu_ligne][milieu_colonne] in (adversaire, adversaire_dame):
                    return True
    return False