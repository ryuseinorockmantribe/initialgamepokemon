import csv
import pygame
import config
import math


class Map:
    def __init__(self, screen):
        self.screen = screen
        self.map_array = []
        self.camera = [0, 0]
        self.file_name = None
        self.player_exit_position = None
        self.objects = []
        self.exit_positions = []


    def load(self, file_name, player):
        self.file_name = file_name

        self.player = player
        self.objects = [player]
        
        filas = []

        # Leer el archivo CSV
        with open('level1_data.csv', newline='') as csvfile:
            lector_csv = csv.reader(csvfile)
            for fila in lector_csv:
                filas.append(fila)
        
        self.map_array = filas


    def render(self, screen, player):
        #self.determine_camera(player)

        y_pos = 0
        for line in self.map_array:
            x_pos = 0  
            for tile in line:
                if tile not in map_tile_image:
                    x_pos = x_pos + 1
                    continue
                else:
                    image = map_tile_image[tile]
                    rect = pygame.Rect(x_pos * config.SCALE - (self.camera[0] * config.SCALE), y_pos * config.SCALE - (self.camera[1] * config.SCALE), config.SCALE, config.SCALE)
                    screen.blit(image, rect)
                    x_pos = x_pos + 1
            
            y_pos = y_pos + 1

        # draw all objects on map
        for object in self.objects:
            object.render(self.screen, self.camera)

    def determine_camera(self, player):
        # y axis
        max_y_position = len(self.map_array) - config.SCREEN_HEIGHT / config.SCALE
        y_position = player.position[1] - math.ceil(round(config.SCREEN_HEIGHT/ config.SCALE / 2))

        if y_position <= max_y_position and y_position >= 0:
            self.camera[1] = y_position
        elif y_position < 0:
            self.camera[1] = 0
        else:
            self.camera[1] = max_y_position

        # x axis
        max_x_position = len(self.map_array[0]) - config.SCREEN_WIDTH / config.SCALE
        x_position = player.position[0] - math.ceil(round(config.SCREEN_WIDTH / config.SCALE / 2))

        if x_position <= max_x_position and x_position >= 0:
            self.camera[0] = x_position
        elif x_position < 0:
            self.camera[0] = 0
        else:
            self.camera[0] = max_x_position

map_tile_image = {
    "0" : pygame.transform.scale(pygame.image.load("imgs/tile_pokemon/0.png"), (config.SCALE, config.SCALE)),
    "1" : pygame.transform.scale(pygame.image.load("imgs/tile_pokemon/1.png"), (config.SCALE, config.SCALE)),
    "2": pygame.transform.scale(pygame.image.load("imgs/tile_pokemon/2.png"), (config.SCALE, config.SCALE)),
    "3" : pygame.transform.scale(pygame.image.load("imgs/tile_pokemon/3.png"), (config.SCALE, config.SCALE)),
    "4": pygame.transform.scale(pygame.image.load("imgs/tile_pokemon/4.png"), (config.SCALE, config.SCALE)),
    "5": pygame.transform.scale(pygame.image.load("imgs/tile_pokemon/5.png"), (config.SCALE, config.SCALE)),
    "6" : pygame.transform.scale(pygame.image.load("imgs/tile_pokemon/6.png"), (config.SCALE, config.SCALE)),
    "7": pygame.transform.scale(pygame.image.load("imgs/tile_pokemon/7.png"), (config.SCALE, config.SCALE)),
    "8" : pygame.transform.scale(pygame.image.load("imgs/tile_pokemon/8.png"), (config.SCALE, config.SCALE)),
    "9": pygame.transform.scale(pygame.image.load("imgs/tile_pokemon/9.png"), (config.SCALE, config.SCALE)),
    "10": pygame.transform.scale(pygame.image.load("imgs/tile_pokemon/10.png"), (config.SCALE, config.SCALE)),
    "11" : pygame.transform.scale(pygame.image.load("imgs/tile_pokemon/11.png"), (config.SCALE, config.SCALE)),
    "12": pygame.transform.scale(pygame.image.load("imgs/tile_pokemon/12.png"), (config.SCALE, config.SCALE)),
    "13": pygame.transform.scale(pygame.image.load("imgs/tile_pokemon/13.png"), (config.SCALE, config.SCALE)),
    "14": pygame.transform.scale(pygame.image.load("imgs/tile_pokemon/14.png"), (config.SCALE, config.SCALE)),
    "15": pygame.transform.scale(pygame.image.load("imgs/tile_pokemon/15.png"), (config.SCALE, config.SCALE)),
    "16" : pygame.transform.scale(pygame.image.load("imgs/tile_pokemon/16.png"), (config.SCALE, config.SCALE)),
    "17": pygame.transform.scale(pygame.image.load("imgs/tile_pokemon/17.png"), (config.SCALE, config.SCALE)),
    "18" : pygame.transform.scale(pygame.image.load("imgs/tile_pokemon/18.png"), (config.SCALE, config.SCALE)),
    "19": pygame.transform.scale(pygame.image.load("imgs/tile_pokemon/19.png"), (config.SCALE, config.SCALE)),
    "20": pygame.transform.scale(pygame.image.load("imgs/tile_pokemon/20.png"), (config.SCALE, config.SCALE)),
    "21" : pygame.transform.scale(pygame.image.load("imgs/tile_pokemon/21.png"), (config.SCALE, config.SCALE)),
    "22": pygame.transform.scale(pygame.image.load("imgs/tile_pokemon/22.png"), (config.SCALE, config.SCALE)),
    "23": pygame.transform.scale(pygame.image.load("imgs/tile_pokemon/23.png"), (config.SCALE, config.SCALE)),
    "24": pygame.transform.scale(pygame.image.load("imgs/tile_pokemon/24.png"), (config.SCALE, config.SCALE)),
    "25" : pygame.transform.scale(pygame.image.load("imgs/tile_pokemon/25.png"), (config.SCALE, config.SCALE)),
    "26": pygame.transform.scale(pygame.image.load("imgs/tile_pokemon/26.png"), (config.SCALE, config.SCALE)),
    "27": pygame.transform.scale(pygame.image.load("imgs/tile_pokemon/27.png"), (config.SCALE, config.SCALE)),
    "28": pygame.transform.scale(pygame.image.load("imgs/tile_pokemon/28.png"), (config.SCALE, config.SCALE)),
    "29": pygame.transform.scale(pygame.image.load("imgs/tile_pokemon/29.png"), (config.SCALE, config.SCALE)),
    "30" : pygame.transform.scale(pygame.image.load("imgs/tile_pokemon/30.png"), (config.SCALE, config.SCALE)),
    "31": pygame.transform.scale(pygame.image.load("imgs/tile_pokemon/31.png"), (config.SCALE, config.SCALE)),
    "32": pygame.transform.scale(pygame.image.load("imgs/tile_pokemon/32.png"), (config.SCALE, config.SCALE)),
}