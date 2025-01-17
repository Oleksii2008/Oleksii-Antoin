import pygame

def afficher_menu_final(ecran, gagnant, coups_blanc, coups_noir, largeur, hauteur):
    """Affiche le menu final avec les résultats."""
    # Set a fixed size for the final menu
    FINAL_MENU_SIZE = 500
    ecran = pygame.display.set_mode((FINAL_MENU_SIZE, FINAL_MENU_SIZE))

    font = pygame.font.SysFont(None, 36)

    ecran.fill((0, 0, 0))
    texte_gagnant = font.render(f"Le gagnant est: {gagnant}", True, (255, 255, 255))
    texte_coups_rouge = font.render(f"Coups blanc: {coups_blanc}", True, (255, 255, 255))
    texte_coups_bleu = font.render(f"Coups noir: {coups_noir}", True, (255, 255, 255))

    # Center the text in the middle of the window
    ecran.blit(texte_gagnant, (FINAL_MENU_SIZE // 2 - texte_gagnant.get_width() // 2, FINAL_MENU_SIZE // 3))
    ecran.blit(texte_coups_rouge,
               (FINAL_MENU_SIZE // 2 - texte_coups_rouge.get_width() // 2, FINAL_MENU_SIZE // 3 + 50))
    ecran.blit(texte_coups_bleu, (FINAL_MENU_SIZE // 2 - texte_coups_bleu.get_width() // 2, FINAL_MENU_SIZE // 3 + 100))

    pygame.display.flip()

    # Wait for user input to either restart or quit
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
