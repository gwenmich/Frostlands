import pygame
from settings import *
from tile import Tile
from character_class import Player
from csv_file_conversion import import_csv_layout, import_folder
from snowball import Snowball
import time
from bar import Bar
from enemy import Enemy


class Level:

    def __init__(self):

        self.display = pygame.display.get_surface()
        # sprites (character, enemies, obstacles and map) and obstacles (anything that can collide with the player)
        self.sprites = YAxisCameraGroup()
        self.obstacles = pygame.sprite.Group()
        self.music_playing = False

        self.snowball_sprites = pygame.sprite.Group()
        self.enemy_sprites = pygame.sprite.Group()

        self.snowball = None
        self.tileset_1 = pygame.image.load("assets/Tileset_1.png").convert_alpha()
        self.tileset_2 = pygame.image.load("assets/Tileset_2.png").convert_alpha()
        self.tileset_3 = pygame.image.load("assets/Tileset_3.png").convert_alpha()
        self.draw_map()
        self.play_music()
        self.bar = Bar()

    def draw_map(self):

        map_layout = {
            "boundaries" : import_csv_layout("assets/csv_map_files/map_blocks.csv"),
            "small_object" : import_csv_layout("assets/csv_map_files/map_small_objects.csv"),
            "medium_object" : import_csv_layout("assets/csv_map_files/map_medium_objects.csv"),
            "large_object": import_csv_layout("assets/csv_map_files/map_large_objects.csv"),
            "tent": import_csv_layout("assets/csv_map_files/map_tent.csv"),
            "entities" : import_csv_layout("assets/csv_map_files/map_entities.csv")
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
                            Tile((x, y),[self.sprites, self.obstacles], "object", graphics["small_objects"][object_index])

                        if layer == "medium_object":
                            object_index = int(column)
                            Tile((x, y),[self.sprites, self.obstacles], "object", graphics["medium_objects"][object_index])

                        if layer == "large_object":
                            object_index = int(column)
                            Tile((x, y), [self.sprites, self.obstacles], "object", graphics["large_objects"][object_index])

                        if layer == "tent":
                            object_index = int(column)
                            Tile((x, y), [self.sprites, self.obstacles], "object", graphics["tents"][object_index])

                        if layer == "entities":
                            if int(column) == 300:
                                self.player = Player(
                                    (x, y),
                                    [self.sprites],
                                    self.obstacles,
                                    self.draw_attack,
                                    self.destroy_snowball)
                            if int(column) == 230:
                                self.enemy = Enemy(
                                    (x,y),
                                    [self.sprites, self.enemy_sprites],
                                    self.obstacles,
                                    self.enemy_attack)


    def draw_attack(self):
        self.snowball = Snowball(self.player, [self.sprites, self.snowball_sprites])

    def destroy_snowball(self):
        if self.snowball and int(time.time() - self.snowball.created_time) > self.snowball.lifespan:
           self.snowball.kill()
           self.snowball = None


    def player_attack_logic(self):
        if self.snowball_sprites:
            for snow in self.snowball_sprites:
                collision_sprites = pygame.sprite.spritecollide(snow, self.enemy_sprites, False)
                if collision_sprites:
                    for target in collision_sprites:
                        target.get_damage(self.player, snow.sprite_type)


    def enemy_attack(self, amount):
        if self.player.vulnerable:
            self.player.health -= amount
            self.player.vulnerable = False
            self.player.get_hit_time = pygame.time.get_ticks()


    def run(self):
        self.sprites.camera_draw(self.player)
        self.sprites.update()
        self.sprites.enemy_update(self.player)
        self.destroy_snowball()
        self.player_attack_logic()
        self.bar.display(self.player)


    def play_music(self):
        if not self.music_playing:
            pygame.mixer.music.load("music/open-fields-aaron-paul-low-main-version-25198-02-16.mp3")
            pygame.mixer.music.set_volume(0.2)
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

    def enemy_update(self, player):
        enemy_sprites = [sprite for sprite in self.sprites() if hasattr(sprite, "sprite_type") and sprite.sprite_type == "enemy"]
        for enemy in enemy_sprites:
            enemy.update_enemies(player)

    def check_all_enemies_health(self):
        enemy_sprites = [sprite for sprite in self.sprites() if hasattr(sprite, "sprite_type") and sprite.sprite_type == "enemy"]
        if not enemy_sprites:
            return True
        else:
            return False


