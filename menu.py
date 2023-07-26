#!/usr/bin/env python

"""menu.py: Menu class and subclasses."""

import pygame
from abc import ABC, abstractmethod
from typing import Callable, Dict

from settings import *
settings = Settings()

from state import State
from play import PlayState

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
    
    def change_state(self, state: str) -> None:
        self.image = pygame.image.load(self.images[state]).convert_alpha()

        scale = self.rect.height / self.image.get_height()
        self.image = pygame.transform.scale(self.image, (int(self.image.get_width() * scale), int(self.image.get_height() * scale)))

        self.rect = self.image.get_rect()
    
    def update(self) -> None:
        if self.mouse_over():
            self.change_state("selected")
        else:
            self.change_state("unselected")
        if self.mouse_click():
            self.event()

    def draw(self, screen) -> None:
        screen.blit(self.image, self.rect)
class ButtonPlay(Button):
    def __init__(self, event: Callable) -> None:
        super().__init__(settings.PLAY_IMGS, settings.PLAY_HEIGHT, event)

class ButtonQuit(Button):
    def __init__(self, event: Callable) -> None:
        super().__init__(settings.QUIT_IMGS, settings.QUIT_HEIGHT, event)

class MenuState(State):
    def __init__(self, game) -> None:
        super().__init__(game)

        self.title = pygame.image.load(settings.TITLE_IMG).convert_alpha()
        
        scale = settings.TITLE_HEIGHT / self.title.get_height()
        self.title = pygame.transform.scale(self.title, (int(self.title.get_width() * scale), int(self.title.get_height() * scale)))

        self.title_rect = self.title.get_rect()
        self.title_rect.center = (settings.WIDTH / 2, 300)

        self.button_play = ButtonPlay(self.game.change_state(PlayState(self.game)))
        self.button_play.rect.center = (settings.WIDTH / 2, settings.HEIGHT / 2 + settings.PLAY_HEIGHT / 2)
        self.button_quit = ButtonQuit(self.game.quit)
        self.button_quit.rect.center = (settings.WIDTH / 2, settings.HEIGHT / 2 + settings.PLAY_HEIGHT / 2 + settings.QUIT_HEIGHT)

        self.buttons = pygame.sprite.Group()
        self.buttons.add(self.button_play)
        self.buttons.add(self.button_quit)

    def update(self) -> None:
        super().update()

        self.buttons.update()

    def draw(self) -> None:
        super().draw()

        self.game.screen.blit(self.title, self.title_rect)
        for button in self.buttons:
            button.draw(self.game.screen)
