import pygame

def afficher_menu_final(ecran, gagnant, coups_rouge, coups_bleu, largeur, hauteur):
    """Affiche le menu final avec les résultats."""
    font = pygame.font.SysFont(None, 36)

    ecran.fill((0, 0, 0))
    texte_gagnant = font.render(f"Le gagnant est: {gagnant}", True, (255, 255, 255))
    texte_coups_rouge = font.render(f"Coups rouges: {coups_rouge}", True, (255, 255, 255))
    texte_coups_bleu = font.render(f"Coups bleus: {coups_bleu}", True, (255, 255, 255))

    ecran.blit(texte_gagnant, (largeur // 2 - texte_gagnant.get_width() // 2, hauteur // 3))
    ecran.blit(texte_coups_rouge, (largeur // 2 - texte_coups_rouge.get_width() // 2, hauteur // 3 + 50))
    ecran.blit(texte_coups_bleu, (largeur // 2 - texte_coups_bleu.get_width() // 2, hauteur // 3 + 100))

    pygame.display.flip()

    # Attendre la fin de la partie
    choix = None
    while choix not in ["restart", "quit"]:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                choix = "quit"
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    choix = "restart"
                elif event.key == pygame.K_q:
                    choix = "quit"

    return choix
