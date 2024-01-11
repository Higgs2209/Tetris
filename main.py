import pygame
from pygame import *
import sys
from grid import Grid

# Initialize pygame
pygame.init()

# Set up colours
dark_blue = (44, 44, 127)

# Set the default width and height
width = 300
height = 600

# Set screen size and caption
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Tetris")

# Create a clock instance
clock = pygame.time.Clock()

# Instantiate Grid class
game_grid = Grid()
game_grid.print_grid()

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Fill screen with color
    screen.fill(dark_blue)

    # Draw grid
    game_grid.draw(screen)

    # Update the display
    pygame.display.update()

    # Set frame rate
    clock.tick(60)


