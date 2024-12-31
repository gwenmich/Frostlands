import pygame,sys
from settings import *
from character_class import Player
from level_class import Level
from screens import VictoryScreen, GameOverScreen
from button import Button

class Game:

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Frostlands")
        self.clock = pygame.time.Clock()

        self.menu_background = pygame.image.load("assets/menu_screen_bg.png")


        self.level = Level()
        self.running = True

    def menu_screen(self):
        intro = True
        title = pygame.image.load("assets/logo_text.png").convert_alpha()
        play_button = Button(200, 500, 100, 50, "white", "black", "Play", FONT_SIZE)

        while intro:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    intro = False
                    self.running = False

            mouse_position = pygame.mouse.get_pos()
            mouse_pressed = pygame.mouse.get_pressed()

            if play_button.is_pressed(mouse_position, mouse_pressed):
                intro = False

            self.screen.blit(self.menu_background, (0, 0))
            self.screen.blit(title, (260, 190))
            self.screen.blit(play_button.image, play_button.rect)
            self.clock.tick(FPS)
            pygame.display.update()



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
    game.menu_screen()
    game.run()