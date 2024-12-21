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

        self.tileset_1 = pygame.image.load("../assets/Tileset_1.png").convert_alpha()
        self.tileset_2 = pygame.image.load("../assets/Tileset_2.png").convert_alpha()
        self.tileset_3 = pygame.image.load("../assets/Tileset_3.png").convert_alpha()
        self.draw_map()

    def draw_map(self):
        for row_index, row in enumerate(WORLD_MAP):
            for column_index, column in enumerate(row):
                x = column_index * TILESIZE
                y = row_index * TILESIZE
                if column == "w":
                    Tile((x,y), self.tileset_2, 0, 2, [self.sprites, self.obstacles])
                if column == "p":
                    self.player = Player((x, y), [self.sprites])



    def run(self):
        self.sprites.draw(self.display)
        self.sprites.update()





