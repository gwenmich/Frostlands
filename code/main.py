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
        self.game_state = "game"
        self.level = Level()
        self.running = True

    def run(self):
        if self.game_state == "game":
            while self.running:

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()

                self.screen.fill(WATER_COLOUR)
                self.level.run()
                if self.level.sprites.check_all_enemies_health():
                    self.game_state = "victory"
                    self.running = False
                if self.level.player.check_player_health():
                    # self.running = False
                    self.game_state = "game_over"
                    self.running = False
                    # pygame.display.update()

                pygame.display.update()
                self.clock.tick(FPS)

        if self.game_state == "victory":
            self.victory = VictoryScreen()

        if self.game_state == "game_over":
            self.game_over = GameOverScreen()








if __name__ == "__main__":
    game = Game()
    game.run()