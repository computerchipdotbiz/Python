import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the screen
screen = pygame.display.set_mode((1000, 800))
pygame.display.set_caption('Pacman Game by Chip')

# Set up colors
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)

# Set up Pacman
pacman_x = 500
pacman_y = 400
pacman_radius = 15

# Set up game loop
while True:
    screen.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        pacman_x -= 1
    if keys[pygame.K_RIGHT]:
        pacman_x += 1
    if keys[pygame.K_UP]:
        pacman_y -= 1
    if keys[pygame.K_DOWN]:
        pacman_y += 1

    pygame.draw.circle(screen, YELLOW, (pacman_x, pacman_y), pacman_radius)

    pygame.display.flip()