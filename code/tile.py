import pygame
from settings import *

class Tile(pygame.sprite.Sprite):

    def __init__(self, position, tileset, column, row, groups):
        super().__init__(groups)
        self.image = self.get_tile(tileset, column, row)
        self.rect = self.image.get_rect(topleft=position)

    def get_tile(self, tileset, column, row):
        x = column * TILESIZE
        y = row * TILESIZE
        rect = pygame.Rect(x, y, TILESIZE, TILESIZE)
        return tileset.subsurface(rect)