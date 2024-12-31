import pygame
import time

class Snowball(pygame.sprite.Sprite):

    def __init__(self, player, groups):
        super().__init__(groups)
        direction = player.status.split("_")[0]
        # graphic
        self.image = pygame.image.load("assets/snowball.png")
        self.sprite_type = "snowball"
        # lifespan
        self.created_time = time.time()
        self.lifespan = 0.4

        self.speed = 10
        self.direction = pygame.math.Vector2()

        # placement
        if direction == "right":
            self.rect = self.image.get_rect(midleft = player.rect.midright)
            self.direction.x = 1
        elif direction == "left":
            self.rect = self.image.get_rect(midright = player.rect.midleft)
            self.direction.x = -1
        elif direction == "up":
            self.rect = self.image.get_rect(midbottom = player.rect.midtop)
            self.direction.y = -1
        elif direction == "down":
            self.rect = self.image.get_rect(midtop = player.rect.midbottom)
            self.direction.y = 1


    def update(self):
        self.rect.x += self.direction.x * self.speed
        self.rect.y += self.direction.y * self.speed

        if time.time() - self.created_time > self.lifespan:
            self.kill()

