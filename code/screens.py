import pygame

class Screen():

    def __init__(self):
        self.running = False
        self.screen = pygame.display.get_surface()
        self.screen.fill("#D6F9FC")

    def draw_screen(self):
        pass

    def draw_text(self):
        pass




class VictoryScreen(Screen):

    def __init__(self):
        pass




class GameOverScreen(Screen):

    pass
