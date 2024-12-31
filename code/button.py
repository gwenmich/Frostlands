import pygame
from settings import *

class Button:

    def __init__(self, x, y, width, height, colour, bg_colour, text, font_size):
        self.font = pygame.font.Font(FONT, font_size)
        self.text = text

        self.x = x
        self.y = y
        self.width = width
        self.height = height

        self.colour = colour
        self.bo_colour = bg_colour

        self.image = pygame.Surface((self.width, self.height))
        self.rect = self.image.get_rect(topleft = (self.x, self.y))

        self.content = self.font.render(self.text, True, self.colour)
        self.content_rect = self.content.get_rect(center = (self.width / 2, self.height / 2))
        self.image.blit(self.content, self.content_rect)


    def is_pressed(self, position, pressed):
        if self.rect.collidepoint(position):
            if pressed[0]:
                return True
            else:
                return False
        return False