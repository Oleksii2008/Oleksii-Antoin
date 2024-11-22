import pygame

pygame.init()

WIDTH, HEIGHT = 500, 500
CELL_SIZE = WIDTH // 10

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Chessboard with Moving Circle")

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
CIRCLE_COLOR = (255, 0, 0)  # Red color for the circle

# Initial position of the circle (at the top-left corner of the board)
circle_row, circle_col = 0, 0  # Start position at (0, 0)


def draw_chess_board():
    for row in range(10):
        for col in range(10):
            color = BLACK if (row + col) % 2 == 0 else WHITE
            pygame.draw.rect(screen, color, (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE))


def draw_circle():
    # Draw the circle at the specified row and column
    pygame.draw.circle(screen, CIRCLE_COLOR,
                       (circle_col * CELL_SIZE + CELL_SIZE // 2,
                        circle_row * CELL_SIZE + CELL_SIZE // 2),
                       CELL_SIZE // 3)


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Handle key presses for circle movement
    keys = pygame.key.get_pressed()

    # Ensure movement is restricted to 1 square per key press, diagonally
    if keys[pygame.K_w] and circle_row > 0 and circle_col > 0:  # Move up-left
        circle_row -= 1
        circle_col -= 1
    if keys[pygame.K_e] and circle_row > 0 and circle_col < 9:  # Move up-right
        circle_row -= 1
        circle_col += 1
    if keys[pygame.K_s] and circle_row < 9 and circle_col > 0:  # Move down-left
        circle_row += 1
        circle_col -= 1
    if keys[pygame.K_d] and circle_row < 9 and circle_col < 9:  # Move down-right
        circle_row += 1
        circle_col += 1

    screen.fill((0, 0, 0))  # Clear the screen
    draw_chess_board()  # Draw the chessboard
    draw_circle()  # Draw the circle
    pygame.display.flip()  # Update the display

pygame.quit()
