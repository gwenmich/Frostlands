import pygame


class Player(pygame.sprite.Sprite):

    def __init__(self):

        self.direction = pygame.math.Vector2()

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
