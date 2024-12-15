import pygame,sys

class Game:

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((700, 500))
        pygame.display.set_caption("Frostlands")
        self.clock = pygame.time.Clock()

    def run(self):
        while True:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.screen.fill("gold")
            pygame.display.update()
            self.clock.tick(60)









if __name__ == "__main__":
    game = Game()
    game.run()