#!/usr/bin/env python

"""main.py: Main file for the game."""

import pygame, sys
import ctypes
ctypes.windll.user32.SetProcessDPIAware()

from settings import *
settings = Settings()

from background import Background
from cloud import Cloud

class Game:
    def __init__(self) -> None:
        pygame.init()
        self.screen = pygame.display.set_mode((settings.WIDTH, settings.HEIGHT))
        self.clock = pygame.time.Clock()

        pygame.display.set_caption(settings.TITLE)
        pygame.display.set_icon(pygame.image.load(settings.ICON))

        self.background = Background()
        self.clouds = pygame.sprite.Group()

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
        self.background.update()
        self.clouds.update()

    def draw(self) -> None:
        self.screen.fill(settings.BLACK)

        self.background.draw(self.screen)
        for cloud in self.clouds: cloud.draw(self.screen)

        pygame.display.update()
        self.clock.tick(settings.FPS)

if __name__ == "__main__":
    game = Game()
    game.run()
