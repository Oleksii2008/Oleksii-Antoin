import tkinter as tk

# Définition du labyrinthe comme une liste de listes
labyrinthe = [
    ["#", " ", "#", " ", "#", " ", "#", " ", "#", " "],
    [" ", "#", " ", "#", " ", "#", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", " ", "#", " "],
    [" ", "#", " ", "#", " ", "#", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", " ", "#", " "],
    [" ", "#", " ", "#", " ", "#", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", " ", "#", " "],
    [" ", "#", " ", "#", " ", "#", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", " ", "#", " "],  # "E" représente la sortie
    [" ", "#", " ", "#", " ", "#", " ", "#", " ", "#"]
]



# Position initiale du joueur (ligne, colonne)
position_joueur = [0, 0]

# Création de la fenêtre principale
root = tk.Tk()
root.title("Jeu du Labyrinthe")

# Taille de chaque cellule dans le labyrinthe (en pixels)
cell_size = 40

# Création d'un canevas pour dessiner le labyrinthe
canvas = tk.Canvas(root, width=cell_size * len(labyrinthe[0]), height=cell_size * len(labyrinthe))
canvas.pack()


# Fonction pour afficher le labyrinthe sur le canevas
def afficher_labyrinthe():
    # Effacer tout le contenu précédent du canevas
    canvas.delete("all")

    # Parcours du labyrinthe ligne par ligne
    for i, ligne in enumerate(labyrinthe):
        for j, cellule in enumerate(ligne):
            # Calcul des coordonnées pour chaque cellule
            x1, y1 = j * cell_size, i * cell_size
            x2, y2 = x1 + cell_size, y1 + cell_size

            # Définir la couleur de la cellule selon son type
            color = "black" if cellule == "#" else "white"  # Mur noir, espace blanc
            if cellule == "E":  # Si c'est la sortie, on la colore en vert
                color = "green"

            # Dessiner le rectangle représentant la cellule sur le canevas
            canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline="grey")

    # Dessiner la position actuelle du joueur
    x1, y1 = position_joueur[1] * cell_size, position_joueur[0] * cell_size
    x2, y2 = x1 + cell_size, y1 + cell_size
    canvas.create_rectangle(x1, y1, x2, y2, fill="blue", outline="grey")


# Fonction pour déplacer le joueur selon les touches pressées
def deplacer_joueur(event):
    ligne, colonne = position_joueur

    # Calcul de la nouvelle position en fonction de la touche pressée
    if event.keysym == "w":  # Déplacement vers le haut
        nouvelle_position = [ligne - 1, colonne]
    elif event.keysym == "s":  # Déplacement vers le bas
        nouvelle_position = [ligne + 1, colonne]
    elif event.keysym == "a":  # Déplacement vers la gauche
        nouvelle_position = [ligne, colonne - 1]
    elif event.keysym == "d":  # Déplacement vers la droite
        nouvelle_position = [ligne, colonne + 1]
    else:
        return  # Si une touche autre que w, a, s, d est pressée, rien ne se passe

    # Vérification si la nouvelle position est un espace vide ou la sortie
    if labyrinthe[nouvelle_position[0]][nouvelle_position[1]] != "#" and labyrinthe[nouvelle_position[0]][nouvelle_position[1]] != " ":
        return  # Si c'est un mur (ou autre obstacle), ne rien faire

    # Mise à jour de la position du joueur
    position_joueur[0], position_joueur[1] = nouvelle_position

    # Si le joueur atteint la sortie ("E"), on affiche un message
    if labyrinthe[nouvelle_position[0]][nouvelle_position[1]] == "E":
        # Changer la couleur de fond du canevas pour gris et celle de la fenêtre pour blanc
        canvas.config(bg="grey")  # Fond gris du canevas
        root.config(bg="white")  # Fond blanc de la fenêtre
        # Afficher un message de victoire
        canvas.create_text(cell_size * len(labyrinthe[0]) // 2, cell_size * len(labyrinthe) // 2,
                           text="Vous avez trouvé la sortie!", fill="grey", font=("Helvetica", 24, "bold"))
    else:
        afficher_labyrinthe()  # Réafficher le labyrinthe après le déplacement


# Lier la fonction de déplacement à la pression des touches
root.bind("<Key>", deplacer_joueur)

# Afficher le labyrinthe initial
afficher_labyrinthe()

# Démarrer la boucle principale de l'application
root.mainloop()
