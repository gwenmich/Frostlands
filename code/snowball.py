import pygame

class Snowball(pygame.sprite.Sprite):

    def __init__(self, player, groups):
        super().__init__(groups)
        self.image = pygame.Surface((12,12))
        self.rect = self.image.get_rect(center = player.rect.center)