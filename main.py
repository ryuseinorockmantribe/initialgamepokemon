import sys
import pygame
import config
from game_state import GameState

from game import Game


pygame.init()

screen = pygame.display.set_mode((config.SCREEN_WIDTH, config.SCREEN_HEIGHT))

pygame.display.set_caption("Pokemon Clone")

clock = pygame.time.Clock()

game = Game(screen)
black = (0, 0, 0)
gold = (218, 165, 32)
grey = (200, 200, 200)
green = (0, 200, 0)
red = (200, 0, 0)
white = (255, 255, 255)


while game.game_state != int(2):
    clock.tick(50)
    game.update()
    pygame.display.flip()

pygame.quit()
sys.exit()