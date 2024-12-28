import pygame
from settings import *



class Player(pygame.sprite.Sprite):

    def __init__(self, position, groups, obstacles):
        super().__init__(groups)
        self.image = pygame.image.load("assets/player.png").convert_alpha()
        self.rect = self.image.get_rect(topleft = position)
        self.hitbox = self.rect.inflate(0, -20)

        self.direction = pygame.math.Vector2()
        self.speed = 5

        self.obstacles = obstacles

    def key_input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP]:
            self.direction.y -= 1
        elif keys[pygame.K_DOWN]:
            self.direction.y += 1
        else:
            self.direction.y = 0

        if keys[pygame.K_LEFT]:
            self.direction.x -= 1
        elif keys[pygame.K_RIGHT]:
            self.direction.x += 1
        else:
            self.direction.x = 0

    def move(self, speed):
        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize()

        self.hitbox.x += self.direction.x * speed
        self.collide("horizontal")
        self.hitbox.y += self.direction.y * speed
        self.collide("vertical")
        self.rect.center = self.hitbox.center

    def collide(self, direction):
        if direction == "horizontal":
            for obstacle in self.obstacles:
                if obstacle.hitbox.colliderect(self.hitbox):
                    if self.direction.x > 0: # moving right
                        self.hitbox.right = obstacle.hitbox.left
                    if self.direction.x < 0: # moving left
                        self.hitbox.left = obstacle.hitbox.right

        if direction == "vertical":
            for obstacle in self.obstacles:
                if obstacle.hitbox.colliderect(self.hitbox):
                    if self.direction.y > 0:  # moving down
                        self.hitbox.bottom = obstacle.hitbox.top
                    if self.direction.y < 0:  # moving up
                        self.hitbox.top = obstacle.hitbox.bottom

    def update(self):
        self.key_input()
        self.move(self.speed)