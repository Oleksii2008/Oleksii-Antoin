import pygame
import sys

pygame.init()


labyrinthe = [
    ["*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*"],
    ["*", "#", " ", "#", " ", "#", " ", "#", " ", "#", " ", "*"],
    ["*", " ", "#", " ", "#", " ", "#", " ", "#", " ", "#", "*"],
    ["*", "#", " ", "#", " ", "#", " ", "#", " ", "#", " ", "*"],
    ["*", " ", "#", " ", "#", " ", "#", " ", "#", " ", "#", "*"],
    ["*", "#", " ", "#", " ", "#", " ", "#", " ", "#", " ", "*"],
    ["*", " ", "#", " ", "#", " ", "#", " ", "#", " ", "#", "*"],
    ["*", "#", " ", "#", " ", "#", " ", "#", " ", "#", " ", "*"],
    ["*", " ", "#", " ", "#", " ", "#", " ", "#", " ", "#", "*"],
    ["*", "#", " ", "#", " ", "#", " ", "#", " ", "#", " ", "*"],
    ["*", " ", "#", " ", "#", " ", "#", " ", "#", " ", "#", "*"],
    ["*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*"]
]


CELL_SIZE = 40

position_joueur = [1, 1]

WIDTH = CELL_SIZE * len(labyrinthe[0])
HEIGHT = CELL_SIZE * len(labyrinthe)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Labyrinthe")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
GREY = (128, 128, 128)

def afficher_labyrinthe():
    screen.fill(WHITE)
    for i, ligne in enumerate(labyrinthe):
        for j, cellule in enumerate(ligne):
            x, y = j * CELL_SIZE, i * CELL_SIZE
            if cellule == "#":
                color = BLACK
            elif cellule == "E":
                color = GREEN
            elif cellule == "*":
                color = GREY
            else:
                color = WHITE
            pygame.draw.rect(screen, color, (x, y, CELL_SIZE, CELL_SIZE))
            pygame.draw.rect(screen, GREY, (x, y, CELL_SIZE, CELL_SIZE), 1)
    x, y = position_joueur[1] * CELL_SIZE, position_joueur[0] * CELL_SIZE
    pygame.draw.rect(screen, BLUE, (x, y, CELL_SIZE, CELL_SIZE))

def deplacer_joueur(dx, dy):
    global position_joueur
    ligne, colonne = position_joueur
    nouvelle_position = [ligne + dy, colonne + dx]
    if labyrinthe[nouvelle_position[0]][nouvelle_position[1]] in [" ", "#"]:
        position_joueur = nouvelle_position

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        deplacer_joueur(-1, -1)
    elif keys[pygame.K_e]:
        deplacer_joueur(1, -1)
    elif keys[pygame.K_s]:
        deplacer_joueur(-1, 1)
    elif keys[pygame.K_d]:
        deplacer_joueur(1, 1)

    afficher_labyrinthe()
    pygame.display.flip()
    pygame.time.delay(100)

pygame.quit()
sys.exit()
