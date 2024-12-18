import pygame,sys
from settings import *
from character_class import Player
from level_class import Level

class Game:

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Frostlands")
        self.clock = pygame.time.Clock()

        self.level = Level()

    def run(self):
        while True:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.screen.fill((225, 250, 165))
            self.level.run()
            pygame.display.update()
            self.clock.tick(FPS)









if __name__ == "__main__":
    game = Game()
    game.run()