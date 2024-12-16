import pygame.display


class Level:
    # visible sprite (character, enemies, obstacles and map) and obstacle sprites (anything that can collide with the player)
    def __init__(self):

        self.display = pygame.display.get_surface()
        self.sprites = pygame.sprite.Group()
        self.obstacles = pygame.sprite.Group()

    def draw_map(self):
        pass






