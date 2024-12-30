import pygame
from settings import *
from entity import Entity

class Enemy(Entity):

    def __init__(self, position, groups, obstacles):
        super().__init__(groups)
        self.sprite_type = "enemy"
        self.status = "idle"

        self.image = pygame.image.load(enemy["image"])
        self.rect = self.image.get_rect(topleft = position)
        self.hitbox = self.rect.inflate(0, -10)
        self.obstacles = obstacles

        self.health = enemy["health"]
        self.speed = enemy["speed"]
        self.damage = enemy["damage"]
        self.resistance = enemy["resistance"]
        self.attack_radius = enemy["attack_radius"]
        self.notice_radius = enemy["notice_radius"]

        self.can_attack = True
        self.attack_time = None
        self.attack_cooldown = 400

        self.vulnerable = True
        self.hit_time = None
        self.invincibility_duration = 300


    def get_distance_from_player(self, player):
        enemy_vector = pygame.math.Vector2(self.rect.center)
        player_vector = pygame.math.Vector2(player.rect.center)
        distance = (player_vector - enemy_vector).magnitude()

        if distance > 0:
            direction = (player_vector - enemy_vector).normalize()
        else:
            direction = pygame.math.Vector2()
        return (distance, direction)


    def set_status(self, player):
        distance = self.get_distance_from_player(player)[0]

        if distance <= self.attack_radius and self.can_attack == True:
            self.status = "attack"
        elif distance <= self.notice_radius:
            self.status = "move"
        else:
            self.status = "idle"

    def action(self, player):
        if self.status == "attack":
            self.attack_time = pygame.time.get_ticks()
            print("attack")
            self.can_attack = False
        elif self.status == "move":
            self.direction = self.get_distance_from_player(player)[1]
        else:
            self.direction = pygame.math.Vector2()

    def cooldown(self):
        if not self.can_attack:
            current_time = pygame.time.get_ticks()
            if current_time - self.attack_time >= self.attack_cooldown:
                self.can_attack = True

    def get_damage(self, player, attack_type):
        if self.vulnerable:
            if attack_type == "snowball":
                self.health -= snowball["damage"]

            self.hit_time = pygame.time.get_ticks()
            self.vulnerable = False

    def check_death(self):
        if self.health <= 0:
            self.kill()


    def update(self):
        self.move(self.speed)
        self.cooldown()

    def update_enemies(self, player):
        self.set_status(player)
        self.action(player)
