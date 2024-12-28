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
        self.music_playing = False

        self.tileset_1 = pygame.image.load("assets/Tileset_1.png").convert_alpha()
        self.tileset_2 = pygame.image.load("assets/Tileset_2.png").convert_alpha()
        self.tileset_3 = pygame.image.load("assets/Tileset_3.png").convert_alpha()
        self.draw_map()
        self.play_music()

    def draw_map(self):

        map_layout = {
            "boundaries" : import_csv_layout("assets/csv_map_files/map_blocks.csv"),
            "small_object" : import_csv_layout("assets/csv_map_files/map_small_objects.csv"),
            "medium_object" : import_csv_layout("assets/csv_map_files/map_medium_objects.csv"),
            "large_object": import_csv_layout("assets/csv_map_files/map_large_objects.csv"),
            "tent": import_csv_layout("assets/csv_map_files/map_tent.csv")
        }

        graphics = {
            "small_objects" : import_folder("assets/small_obj"),
            "medium_objects" : import_folder("assets/med_obj"),
            "large_objects" : import_folder("assets/large_obj"),
            "tents": import_folder("assets/tent")

        }


        for layer, layout in map_layout.items():
            for row_index, row in enumerate(layout):
                for column_index, column in enumerate(row):
                    if column != "-1":
                        x = column_index * TILESIZE
                        y = row_index * TILESIZE
                        if layer == "boundaries":
                            Tile((x,y), [self.obstacles], "invisible")

                        if layer == "small_object":
                            object_index = int(column)
                            if 0 <= object_index < len(graphics["small_objects"]):
                                # (graphics)["objects"][int(column)]
                                Tile((x, y),[self.sprites, self.obstacles], "object",
                                     graphics["small_objects"][object_index])

                        if layer == "medium_object":
                            object_index = int(column)
                            if 0 <= object_index < len(graphics["medium_objects"]):
                                Tile((x, y),[self.sprites, self.obstacles], "object",
                                     graphics["medium_objects"][object_index])

                        if layer == "large_object":
                            object_index = int(column)
                            if 0 <= object_index < len(graphics["large_objects"]):
                                Tile((x, y), [self.sprites, self.obstacles], "object",
                                     graphics["large_objects"][object_index])

                        if layer == "tent":
                            object_index = int(column)
                            if 0 <= object_index < len(graphics["tents"]):
                                Tile((x, y), [self.sprites, self.obstacles], "object",
                                     graphics["tents"][object_index])


        self.player = Player((510, 440), [self.sprites], self.obstacles)



    def run(self):
        self.sprites.camera_draw(self.player)
        self.sprites.update()


    def play_music(self):
        if not self.music_playing:
            pygame.mixer.music.load("music/open-fields-aaron-paul-low-main-version-25198-02-16.mp3")
            pygame.mixer.music.play(-1)
            self.music_playing = True




class YAxisCameraGroup(pygame.sprite.Group):

    def __init__(self):
        super().__init__()
        self.display = pygame.display.get_surface()
        self.half_width = self.display.get_size()[0] // 2
        self.half_height = self.display.get_size()[1] // 2
        self.offset = pygame.math.Vector2()

        # floor
        self.floor_surface = pygame.image.load("assets/map.png").convert()
        self.floor_rect = self.floor_surface.get_rect(topleft = (0,0))

    def camera_draw(self, player):

        self.offset.x = player.rect.centerx - self.half_width
        self.offset.y = player.rect.centery - self.half_height

        floor_adjusted_rect = self.floor_rect.topleft - self.offset
        self.display.blit(self.floor_surface, floor_adjusted_rect)

        for sprite in sorted(self.sprites(), key = lambda sprite: sprite.rect.centery):
            sprite_adjusted_rect = sprite.rect.topleft - self.offset
            self.display.blit(sprite.image, sprite_adjusted_rect)




