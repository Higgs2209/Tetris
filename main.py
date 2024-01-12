import pygame
from pygame import *
import sys
from game import Game

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

game = Game()

GAME_UPDATE = pygame.USEREVENT
pygame.time.set_timer(GAME_UPDATE, 200)


# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                game.move_left()
            if event.key == pygame.K_RIGHT:
                game.move_right()
            if event.key == pygame.K_DOWN:
                game.move_down()
            if event.key == pygame.K_UP:
                game.rotate()
        if event.type == GAME_UPDATE:
            game.move_down()

    # Fill screen with color
    screen.fill(dark_blue)

    game.draw(screen)

    # Update the display
    pygame.display.update()

    # Set frame rate
    clock.tick(60)


