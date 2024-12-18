import pygame.display
from settings import *
from tile import Tile
from character_class import Player

class Level:

    def __init__(self):

        self.display = pygame.display.get_surface()
        # sprites (character, enemies, obstacles and map) and obstacles (anything that can collide with the player)
        self.sprites = pygame.sprite.Group()
        self.obstacles = pygame.sprite.Group()

        self.draw_map()

    def draw_map(self):
        for row_index, row in enumerate(WORLD_MAP):
            for column_index, column in enumerate(row):
                x = column_index * TILESIZE
                y = row_index * TILESIZE
                if column == "w":
                    tileset = pygame.image.load("../assets/Tileset_2.png").convert_alpha()
                    Tile((x,y), tileset, 0, 3, [self.sprites])

    def run(self):
        self.sprites.draw(self.display)





