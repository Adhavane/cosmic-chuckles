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

        self.title = pygame.image.load(settings.TITLE_IMG).convert_alpha()
        
        scale = settings.TITLE_HEIGHT / self.title.get_height()
        self.title = pygame.transform.scale(self.title, (int(self.title.get_width() * scale), int(self.title.get_height() * scale)))

        self.title_rect = self.title.get_rect()
        self.title_rect.center = (settings.WIDTH / 2, settings.HEIGHT / 2)


    def update(self) -> None:
        super().update()

    def draw(self) -> None:
        super().draw()

        self.game.screen.blit(self.title, self.title_rect)
