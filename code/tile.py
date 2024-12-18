import pygame
from settings import *

class Tile(pygame.sprite.Sprite):

    def __init__(self, position, groups):
        super().__init__(groups)
        self.image = pygame.image.load("../assets/Tileset_2.png").convert_alpha()
        self.rect = self.image.get_rect(topleft=position)
