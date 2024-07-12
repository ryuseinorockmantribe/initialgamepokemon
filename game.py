import random

import pygame
import config
import math
from player import Player
from game_state import GameState, CurrentGameState
from game_view.map import Map


class Game:
    def __init__(self, screen):
        self.screen = screen
        self.game_state = 0
        self.player_has_moved = False
        #self.monster_factory = MonsterFactory()
        self.map = Map(screen)
        self.maps = [self.map]
        self.battle = None
        self.player = None
        self.event = None
        player = Player(1, 1)
        self.player = player
        print("do set up")
        self.game_state = int(1)
        self.map.load("01", self.player)

    def update(self):
        self.player_has_moved = False
        self.screen.fill(config.BLACK)
        # print("update")
        self.handle_events()

        self.map.render(self.screen, self.player)


    def handle_events(self):
        if self.event is not None:
            return

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("salir")
                self.game_state = int(2)
            #     handle key events

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.game_state = int(2)
                elif event.key == pygame.K_w: # up
                    self.move_unit(self.player, [0, -1])
                elif event.key == pygame.K_s: # down
                    self.move_unit(self.player, [0, 1])
                elif event.key == pygame.K_a: # left
                    self.move_unit(self.player, [-1, 0])
                elif event.key == pygame.K_d: # right
                    self.move_unit(self.player, [1, 0])
                #these are for debug
                elif event.key == pygame.K_UP: # up
                    self.move_unit(self.player, [0, -1])
                elif event.key == pygame.K_DOWN: # down
                    self.move_unit(self.player, [0, 1])
                elif event.key == pygame.K_LEFT: # left
                    self.move_unit(self.player, [-1, 0])
                elif event.key == pygame.K_RIGHT: # right
                    self.move_unit(self.player, [1, 0])

    def move_unit(self, unit, position_change):
        new_position = [unit.position[0] + position_change[0], unit.position[1] + position_change[1]]

        # check if off map
        if new_position[0] < 0 or new_position[0] > (len(self.map.map_array[0]) - 1):
            return

        if new_position[1] < 0 or new_position[1] > (len(self.map.map_array) - 1):
            return

        # check for valid movement
        if self.map.map_array[new_position[1]][new_position[0]] in config.IMPASSIBLE:
            return

        self.player_has_moved = True

        unit.update_position(new_position)