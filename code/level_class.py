import pygame.display
from settings import *
from tile import Tile
from character_class import Player

class Level:

    def __init__(self):

        self.display = pygame.display.get_surface()
        # sprites (character, enemies, obstacles and map) and obstacles (anything that can collide with the player)
        self.sprites = YAxisCameraGroup()
        self.obstacles = pygame.sprite.Group()

        self.tileset_1 = pygame.image.load("../assets/Tileset_1.png").convert_alpha()
        self.tileset_2 = pygame.image.load("../assets/Tileset_2.png").convert_alpha()
        self.tileset_3 = pygame.image.load("../assets/Tileset_3.png").convert_alpha()
        self.draw_map()

    def draw_map(self):
        for row_index, row in enumerate(WORLD_MAP):
            for column_index, column in enumerate(row):
                x = column_index * TILESIZE
                y = row_index * TILESIZE
                if column == "w":
                    Tile((x,y), self.tileset_2, 0, 2, [self.sprites, self.obstacles])
                if column == "p":
                    self.player = Player((x, y), [self.sprites], self.obstacles)



    def run(self):
        self.sprites.camera_draw(self.player)
        self.sprites.update()




class YAxisCameraGroup(pygame.sprite.Group):

    def __init__(self):
        super().__init__()
        self.display = pygame.display.get_surface()
        self.half_width = self.display.get_size()[0] // 2
        self.half_height = self.display.get_size()[1] // 2
        self.offset = pygame.math.Vector2()

    def camera_draw(self, player):

        self.offset.x = player.rect.centerx - self.half_width
        self.offset.y = player.rect.centery - self.half_height

        for sprite in sorted(self.sprites(), key = lambda sprite: sprite.rect.centery):
            camera_adjusted_rect = sprite.rect.topleft - self.offset
            self.display.blit(sprite.image, camera_adjusted_rect)




