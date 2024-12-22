import pygame.display
from settings import *
from tile import Tile
from character_class import Player
from csv_file_conversion import import_csv_layout, import_folder

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

        map_layout = {
            "boundaries" : import_csv_layout("../assets/csv_map_files/map_blocks.csv"),
            "object" : import_csv_layout("../assets/csv_map_files/map_objects.csv")
        }

        graphics = {
            "objects" : import_folder("../assets/objects")
        }


        for layer, layout in map_layout.items():
            for row_index, row in enumerate(layout):
                for column_index, column in enumerate(row):
                    if column != "-1":
                        x = column_index * TILESIZE
                        y = row_index * TILESIZE
                        if layer == "boundaries":
                            Tile((x,y), [self.obstacles], "invisible")
                        if layer == "objects":
                            surface = graphics["objects"][int(column)]
                            Tile((x, y), [self.sprites, self.obstacles], "object", surface)

        #         if column == "w":
        #             Tile((x,y), self.tileset_2, 0, 2, [self.sprites, self.obstacles])
        #         if column == "p":
        #             self.player = Player((x, y), [self.sprites], self.obstacles)
        self.player = Player((510, 440), [self.sprites], self.obstacles)



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

        # floor
        self.floor_surface = pygame.image.load("../assets/map.png").convert()
        self.floor_rect = self.floor_surface.get_rect(topleft = (0,0))

    def camera_draw(self, player):

        self.offset.x = player.rect.centerx - self.half_width
        self.offset.y = player.rect.centery - self.half_height

        floor_adjusted_rect = self.floor_rect.topleft - self.offset
        self.display.blit(self.floor_surface, floor_adjusted_rect)

        for sprite in sorted(self.sprites(), key = lambda sprite: sprite.rect.centery):
            sprite_adjusted_rect = sprite.rect.topleft - self.offset
            self.display.blit(sprite.image, sprite_adjusted_rect)




