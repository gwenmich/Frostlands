import pygame
from settings import *

class Tile(pygame.sprite.Sprite):

    def __init__(self, position, groups, sprite_type, surface = pygame.Surface((TILESIZE, TILESIZE))):
        super().__init__(groups)
        self.sprite_type = sprite_type
        self.image = surface
        self.rect = self.image.get_rect(topleft = position)
        self.hitbox = self.rect.inflate(0, -10)


    # def __init__(self, position, tileset, column, row, groups):
    #     super().__init__(groups)
    #     self.image = self.get_tile(tileset, column, row)
    #     self.rect = self.image.get_rect(topleft=position)
    #     self.hitbox = self.rect.inflate(0, -10)
    #
    # def get_tile(self, tileset, column, row):
    #     x = column * TILESIZE
    #     y = row * TILESIZE
    #     rect = pygame.Rect(x, y, TILESIZE, TILESIZE)
    #     tile = tileset.subsurface(rect)
    #     return tile

