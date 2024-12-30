import pygame
from settings import *
from abc import ABC, abstractmethod

class Screen(ABC):

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.get_surface()
        self.screen.fill(SCREEN_BG_COLOUR)
        self.draw_text()

    # @abstractmethod
    # def draw_screen(self):
    #     pass

    @abstractmethod
    def draw_text(self):
        pass




class VictoryScreen(Screen):

    def draw_text(self):
        font = pygame.font.Font(FONT, FONT_SIZE)
        message = "Congratulations!\nYou have defeated all the snowmen and can finally enjoy your holiday in peace.\nGood luck!"
        text = font.render(message, True, TEXT_COLOUR)
        text_rect = text.get_rect(center = (self.screen.get_width() // 2, self.screen.get_height() // 2))
        self.screen.blit(text, text_rect)
        pygame.display.flip()




class GameOverScreen(Screen):

    def draw_text(self):
        font = pygame.font.Font(FONT, FONT_SIZE)
        message = "GAME OVER!\nThe evil snowmen have buried you under a pile of snow\nand are going to make you one of their own!\nWho knew? Carrots suit you."
        text = font.render(message, True, TEXT_COLOUR)
        text_rect = text.get_rect(center = (self.screen.get_width() // 2, self.screen.get_height() // 2))
        self.screen.blit(text, text_rect)
        pygame.display.flip()
