import pygame, sys
from random import randint, choice

import ctypes
ctypes.windll.user32.SetProcessDPIAware()

WIDTH = 1380
HEIGHT = 1024
FPS = 60

class Game:
    def __init__(self) -> None:
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()

        pygame.display.set_caption("Cosmic Chuckles Python/Pygame")

    def run(self) -> None:
        while True:
            self.events()
            self.update()
            self.draw()
    
    def events(self) -> None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    def update(self) -> None:
        pass

    def draw(self) -> None:
        self.screen.fill((0, 0, 0))
        pygame.display.update()
        self.clock.tick(FPS)

if __name__ == "__main__":
    game = Game()
    game.run()
