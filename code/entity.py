import pygame

class Entity(pygame.sprite.Sprite):

    def __init__(self, groups):
        super().__init__(groups)

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