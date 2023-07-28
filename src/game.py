#!/usr/bin/env python3

"""game.py: Game class."""

from __future__ import annotations

import pygame
import sys

from src.settings import Settings
settings = Settings()

class Game:
    def __init__(self) -> None:
        from src.scenes.menu import MenuState

        pygame.init()
        self.screen: pygame.Surface = pygame.display.set_mode((settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT))
        self.clock: pygame.time.Clock = pygame.time.Clock()

        pygame.display.set_caption(settings.TITLE)
        pygame.display.set_icon(pygame.image.load(settings.ICON))

        self.state: State = MenuState(self)

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

        pygame.display.update()
        self.clock.tick(settings.FPS)

    def draw(self) -> None:
        self.state.draw()

from src.scenes.state import State
