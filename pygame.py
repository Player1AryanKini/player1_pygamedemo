import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simple Python Game")

# Colors
WHITE = (255, 255, 255)

# Player attributes
player_width, player_height = 50, 50
player_x, player_y = (WIDTH - player_width) // 2, HEIGHT - player_height - 20
player_speed = 5

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move the player
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_x -= player_speed
    if keys[pygame.K_RIGHT]:
        player_x += player_speed

    # Clear the screen
    screen.fill(WHITE)

    # Draw the player
    pygame.draw.rect(screen, (0, 0, 255), (player_x, player_y, player_width, player_height))

    # Update the display
    pygame.display.update()

# Quit Pygame
pygame.quit()
sys.exit()
