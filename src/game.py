#!/usr/bin/env python3

"""game.py: Game class."""

import pygame
import sys

from src.settings import Settings
settings = Settings()

from src.scenes.state import State
from src.scenes.menu import MenuState

class Game:
    def __init__(self) -> None:
        pygame.init()
        self.screen = pygame.display.set_mode((settings.WIDTH, settings.HEIGHT))
        self.clock = pygame.time.Clock()

        pygame.display.set_caption(settings.TITLE)
        pygame.display.set_icon(pygame.image.load(settings.ICON))

        self.state = MenuState(self)

    def change_state(self, state: State) -> None:
        self.state = state

    def run(self) -> None:
        while True:
            self.events()
            self.update()
            self.draw()
    
    def quit(self) -> None:
        pygame.quit()
        sys.exit()
    
    def events(self) -> None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit()
            self.state.events(event)
        
    def update(self) -> None:
        self.state.update()

    def draw(self) -> None:
        self.state.draw()

        pygame.display.update()
        self.clock.tick(settings.FPS)
