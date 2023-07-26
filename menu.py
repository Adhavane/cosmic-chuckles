#!/usr/bin/env python

"""menu.py: Menu class and subclasses."""

import pygame

from settings import *
settings = Settings()

from state import State
from background import Background

class MenuState(State):
    def __init__(self, game) -> None:
        super().__init__(game)

        self.background = Background()

        self.title = pygame.image.load(settings.TITLE_IMG).convert_alpha()

    def update(self) -> None:
        self.background.update()

    def draw(self) -> None:
        self.game.screen.fill(settings.BLACK)

        self.background.draw(self.game.screen)
        