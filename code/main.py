import pygame,sys
from settings import *
from character_class import Player
from level_class import Level
from screens import VictoryScreen, GameOverScreen

class Game:

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Frostlands")
        self.clock = pygame.time.Clock()

        self.level = Level()
        self.running = True

    def run(self):
        while self.running:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.screen.fill(WATER_COLOUR)
            self.level.run()
            if self.level.sprites.check_all_enemies_health():
                self.victory = VictoryScreen()
                self.running = False
            if self.level.player.check_player_health():

                self.game_over = GameOverScreen()
                self.running = False


            pygame.display.update()
            self.clock.tick(FPS)







if __name__ == "__main__":
    game = Game()
    game.run()