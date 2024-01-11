import pygame
from pygame import *
import sys

# Initialize pygame
pygame.init()

# Set screen size and caption
screen = pygame.display.set_mode((300, 600))
pygame.display.set_caption("Tetris")

# Create a clock instance
clock = pygame.time.Clock()


# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Update the display
    pygame.display.update()

    # Set frame rate
    clock.tick(60)


