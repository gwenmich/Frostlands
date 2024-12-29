import pygame
import time

class Snowball(pygame.sprite.Sprite):

    def __init__(self, player, groups):
        super().__init__(groups)
        direction = player.status.split("_")[0]
        # graphic
        self.image = pygame.image.load("assets/snowball.png")

        # lifespan
        self.created_time = time.time()
        self.lifespan = 2

        # placement
        if direction == "right":
            self.rect = self.image.get_rect(midleft = player.rect.midright)
        elif direction == "left":
            self.rect = self.image.get_rect(midright = player.rect.midleft)
        elif direction == "up":
            self.rect = self.image.get_rect(midbottom = player.rect.midtop)
        elif direction == "down":
            self.rect = self.image.get_rect(midtop = player.rect.midbottom)

