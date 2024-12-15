import pygame
from abc import ABC, abstractmethod

class Character(ABC):

    def __init__(self, name, max_health):
        self.name = name
        self.health = max_health
        self.max_health = max_health

    @abstractmethod
    def move(self):
        pass



class Player(Character):

    def move(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP]:
            pass
        if keys[pygame.K_DOWN]:
            pass
        if keys[pygame.K_LEFT]:
            pass
        if keys[pygame.K_RIGHT]:
            pass