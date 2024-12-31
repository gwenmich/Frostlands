import pygame,sys
from settings import *
from character_class import Player
from level_class import Level
from button import Button

class Game:

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Frostlands")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(FONT, FONT_SIZE)
        self.menu_background = pygame.image.load("assets/menu_screen_bg.png")

        self.level = Level()
        self.running = True


    def menu_screen(self):
        menu = True
        title = pygame.image.load("assets/logo_text.png").convert_alpha()
        play_button = Button(420, 320, 100, 50, TEXT_COLOUR, MENU_BG_COLOUR, "Play", FONT_SIZE)
        quit_button = Button(420, 400, 100, 50, TEXT_COLOUR, MENU_BG_COLOUR, "Quit", FONT_SIZE)

        while menu:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    menu = False
                    self.running = False

            mouse_position = pygame.mouse.get_pos()
            mouse_pressed = pygame.mouse.get_pressed()

            if play_button.is_pressed(mouse_position, mouse_pressed):
                menu = False
                game.introduction()

            if quit_button.is_pressed(mouse_position, mouse_pressed):
                pygame.quit()
                sys.exit()

            self.screen.blit(self.menu_background, (0, 0))
            self.screen.blit(title, (260, 190))
            self.screen.blit(play_button.image, play_button.rect)
            self.screen.blit(quit_button.image, quit_button.rect)
            self.clock.tick(FPS)
            pygame.display.update()


    def render_text(self, text):
        y_pos = 0
        for line in text:
            rendered_line = self.font.render(line, True, TEXT_COLOUR)
            render_line_rect = rendered_line.get_rect(center=(WIDTH // 2, 200 + y_pos))
            y_pos += 25
            self.screen.blit(rendered_line, render_line_rect)


    def introduction(self):
        intro = True
        intro_text = [
            "Welcome to Frostlands!",
            "You were left here by your friendly tour guide",
            "but he forgot to mention there are evil snowmen",
            "lurking on the island! Fortunately for you",
            "there's enough snow around to create the",
            "deadliest of weapons:",
            "the Snowball!",
            "Rid the lands of the snowmen so you can get",
            "to enjoy your holiday in peace.",
            "",
            "Press Enter to continue and Space to attack",
            "Good luck!"]


        while intro:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        intro = False


            self.screen.blit(self.menu_background, (0, 0))
            self.render_text(intro_text)

            self.clock.tick(FPS)
            pygame.display.update()


    def victory(self):
        win = True
        win_text = [
            "Congratulations!",
            "You have defeated all the snowmen",
            "and can finally enjoy your holiday",
            "in peace. Now you're stuck in a snowy",
            "wasteland with nothing to do.",
            "Guess it's time for a nap!"
        ]

        while win:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

            self.screen.blit(self.menu_background, (0, 0))
            self.render_text(win_text)

            self.clock.tick(FPS)
            pygame.display.update()


    def game_over(self):
        loss = True
        loss_text = [
            "GAME OVER",
            "The evil snowmen have buried you",
            "under a pile of snow and are going",
            "to make you into one of their own!",
            "Who knew? Carrots suit you"
        ]

        while loss:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

            self.screen.blit(self.menu_background, (0, 0))
            self.render_text(loss_text)

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
                self.victory()
                self.running = False

            if self.level.player.check_player_health():
                self.game_over()
                self.running = False


            pygame.display.update()
            self.clock.tick(FPS)







if __name__ == "__main__":
    game = Game()
    game.menu_screen()
    game.run()
