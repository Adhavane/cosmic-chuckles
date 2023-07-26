#!/usr/bin/env python

"""menu.py: Menu class and subclasses."""

import pygame
from abc import ABC, abstractmethod
from typing import Callable, Dict

from settings import *
settings = Settings()

from state import State

class Button(ABC, pygame.sprite.Sprite):
    def __init__(self, images: Dict[str, str], height: int, event: Callable) -> None:
        super().__init__()

        self.images = images
        self.image = pygame.image.load(self.images["unselected"]).convert_alpha()

        scale = height / self.image.get_height()
        self.image = pygame.transform.scale(self.image, (int(self.image.get_width() * scale), int(self.image.get_height() * scale)))

        self.rect = self.image.get_rect()

        self.event = event

    def mouse_over(self) -> bool:
        mouse_pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_pos):
            return True
        return False
    
    def mouse_click(self) -> bool:
        mouse_click = pygame.mouse.get_pressed()
        if mouse_click[0] and self.mouse_over():
            return True
        return False
    
    def update(self) -> None:
        if self.mouse_click():
            self.event()
        if self.mouse_over():
            self.image = pygame.image.load(self.images["selected"]).convert_alpha()

    def draw(self, screen) -> None:
        screen.blit(self.image, self.rect)

class ButtonPlay(Button):
    def __init__(self) -> None:
        super().__init__()

        self.image = pygame.image.load(settings.BUTTON_PLAY_IMG).convert_alpha()
        
        scale = settings.BUTTON_PLAY_HEIGHT / self.image.get_height()
        self.image = pygame.transform.scale(self.image, (int(self.image.get_width() * scale), int(self.image.get_height() * scale)))

        self.rect = self.image.get_rect()
        self.rect.center = (settings.WIDTH / 2, settings.HEIGHT / 2)


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
