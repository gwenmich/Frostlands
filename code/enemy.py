import pygame
from settings import *
from entity import Entity

class Enemy(Entity):

    def __init__(self, position, groups):
        super().__init__(groups)
        self.sprite_type = "enemy"

        self.image = pygame.image.load(enemy["image"])
        self.rect = self.image.get_rect(topleft = position)