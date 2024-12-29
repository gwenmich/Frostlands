import pygame
from settings import *

class Bar:

    def __init__(self):
        self.display_surface = pygame.display.get_surface()
        self.font = pygame.font.Font(FONT, FONT_SIZE)

        # health bar
        self.health_bar_rect = pygame.Rect(10, 10, HEALTH_BAR_WIDTH, HEALTH_BAR_HEIGHT)


    def create_bar(self, current, max, bg_rect, colour):
        pygame.draw.rect(self.display_surface, BG_COLOUR, bg_rect)

        ratio = current / max
        current_width = bg_rect.width * ratio
        current_rect = bg_rect.copy()
        current_rect.width = current_width

        pygame.draw.rect(self.display_surface, colour, current_rect)
        pygame.draw.rect(self.display_surface, BORDER_COLOUR, bg_rect, 3)



    def display(self, player):
        self.create_bar(player.health, player.max_health, self.health_bar_rect, HEALTH_COLOUR)