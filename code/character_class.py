import pygame
from settings import *



class Player(pygame.sprite.Sprite):

    def __init__(self, position, groups, obstacles):
        super().__init__(groups)
        self.image = pygame.image.load("assets/player/down_idle.png").convert_alpha()
        self.rect = self.image.get_rect(topleft = position)
        self.hitbox = self.rect.inflate(0, -30)

        self.import_spritesheet()
        self.status = "down"
        self.frame = 0
        self.animation_speed = 0.2

        self.direction = pygame.math.Vector2()
        self.speed = 5
        self.attack = False
        self.attack_cooldown = 400
        self.attack_time = None

        self.obstacles = obstacles


    def import_spritesheet(self):

        self.animations = {
            "up" : [], "down" : [], "left" : [], "right" : [],
            "up_idle" : [], "down_idle" : [], "left_idle" : [], "right_idle" : [],
            "up_attack" : [], "down_attack" : [], "left_attack" : [], "right_attack" : []
        }

        for animation in self.animations.keys():
            spritesheet_path = "assets/player/" + animation + ".png"
            spritesheet_img = pygame.image.load(spritesheet_path).convert_alpha()
            if "idle" in animation:
                self.load_frames(spritesheet_img, 1, animation)
            else:
                self.load_frames(spritesheet_img, 6, animation)


    def load_frames(self, spritesheet_image, frames, animation):

        for frame in range(frames):
            frame_image = pygame.Surface((2 * TILESIZE, 2 * TILESIZE)).convert_alpha()
            frame_image.blit(spritesheet_image, (0, 0), ((frame * 2 * TILESIZE), 0, 2 * TILESIZE, 2 * TILESIZE))
            frame_image.set_colorkey("#e71d1d")
            self.animations[animation].append(frame_image)


    def key_input(self):
        keys = pygame.key.get_pressed()
        if not self.attack:
            if keys[pygame.K_UP]:
                self.direction.y -= 1
                self.status = "up"
            elif keys[pygame.K_DOWN]:
                self.direction.y += 1
                self.status = "down"
            else:
                self.direction.y = 0

            if keys[pygame.K_LEFT]:
                self.direction.x -= 1
                self.status = "left"
            elif keys[pygame.K_RIGHT]:
                self.direction.x += 1
                self.status = "right"
            else:
                self.direction.x = 0
        else:
            self.direction.x = 0
            self.direction.y = 0

        # attack input
        if keys[pygame.K_SPACE] and not self.attack:
            self.attack = True
            self.animation_speed = 0.6
            self.attack_time = pygame.time.get_ticks()


    def get_status(self):
        # idle state
        if self.direction.x == 0 and self.direction.y == 0:
            if not "idle" in self.status and not "attack" in self.status:
                self.status = self.status + "_idle"

        # attack state
        if self.attack:
            self.direction.x = 0
            self.direction.y = 0
            if "attack" not in self.status:
                if "idle" in self.status:
                    self.status = self.status.replace("_idle", "_attack")
                else:
                    self.status = self.status + "_attack"
        else:
            if "attack" in self.status:
                self.status = self.status.replace("_attack", "")



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


    def cooldown(self):
        current_time = pygame.time.get_ticks()
        if self.attack:
            if current_time >= self.attack_cooldown:
                self.attack = False
                self.animation_speed = 0.2


    def animate_player(self):
        animation = self.animations[self.status]
        self.frame += self.animation_speed
        if self.frame >= len(animation):
            self.frame = 0

        self.image = animation[int(self.frame)]
        self.rect = self.image.get_rect(center = self.hitbox.center)


    def update(self):
        self.animate_player()
        self.key_input()
        self.get_status()
        self.cooldown()
        self.move(self.speed)