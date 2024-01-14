import pygame
from pygame import *
import sys
from game import Game
from colours import Colours

# Initialize pygame
pygame.init()

title_font = pygame.font.Font(None, 40)
score_surface = title_font.render("Score", True, Colours.white)
next_surface = title_font.render("Next", True, Colours.white)
game_over_surface = title_font.render("Game Over", True, Colours.white)

score_rect = pygame.Rect(320, 55, 170, 60)
next_rect = pygame.Rect(320, 215, 170, 180)

# Set up colours
dark_blue = (44, 44, 127)

# Set the default width and height
width = 500
height = 620

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
            if game.game_over is True:
                game.game_over = False
                game.reset()
            if event.key == pygame.K_LEFT and game.game_over is False:
                game.move_left()
            if event.key == pygame.K_RIGHT and game.game_over is False:
                game.move_right()
            if event.key == pygame.K_DOWN and game.game_over is False:
                game.move_down()
                game.update_score(0, 1)
            if event.key == pygame.K_UP and game.game_over is False:
                game.rotate()
        if event.type == GAME_UPDATE and game.game_over is False:
            game.move_down()

    # Fill screen with color
    screen.fill(Colours.dark_blue)
    screen.blit(score_surface, (365, 20, 50, 50))
    screen.blit(next_surface, (375, 180, 50, 50))

    score_value_surface = title_font.render(str(game.score), True, Colours.white)

    if game.game_over:
        screen.blit(game_over_surface, (320, 450, 50, 50))

    pygame.draw.rect(screen, Colours.light_blue, score_rect, 0, 10)
    screen.blit(score_value_surface, score_value_surface.get_rect(centerx=score_rect.centerx,
                                                                  centery=score_rect.centery))
    pygame.draw.rect(screen, Colours.light_blue, next_rect, 0, 10)

    game.draw(screen)

    # Update the display
    pygame.display.update()

    # Set frame rate
    clock.tick(60)
