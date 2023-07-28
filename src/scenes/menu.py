#!/usr/bin/env python3

"""menu.py: Menu class and subclasses."""

from __future__ import annotations

import pygame

from src.settings import Settings
settings = Settings()

from src.scenes.state import State
from src.gui.button import Button, ButtonPlay, ButtonQuit

class MenuState(State):
    def __init__(self, game: Game) -> None:
        super().__init__(game)

        scale: float
        width: int
        height: int

        self.title: pygame.Surface = pygame.image.load(settings.TITLE_IMG).convert_alpha()
        
        scale = settings.TITLE_HEIGHT / self.title.get_height()
        width = int(self.title.get_width() * scale)
        height = int(self.title.get_height() * scale)
        self.title = pygame.transform.scale(self.title, (width, height))

        self.title_rect: pygame.Rect = self.title.get_rect()
        self.title_rect.x = int(settings.SCREEN_WIDTH / 2 - self.title_rect.width / 2)
        self.title_rect.y = settings.TITLE_Y

        self.credit: pygame.Surface = pygame.image.load(settings.CREDIT_IMG).convert_alpha()

        scale = settings.CREDIT_HEIGHT / self.credit.get_height()
        width = int(self.credit.get_width() * scale)
        height = int(self.credit.get_height() * scale)
        self.credit = pygame.transform.scale(self.credit, (width, height))

        self.credit_rect: pygame.Rect = self.credit.get_rect()
        self.credit_rect.x = self.title_rect.x + self.title_rect.width - self.credit_rect.width
        self.credit_rect.y = settings.CREDIT_Y

        self.button_play: ButtonPlay = ButtonPlay(self.game)
        self.button_quit: ButtonQuit = ButtonQuit(self.game)

        self.buttons: pygame.sprite.Group[Button] = pygame.sprite.Group()
        self.buttons.add(self.button_play)
        self.buttons.add(self.button_quit)

        self.selected_button_index: int = 0
        self.selected_button: Button = self.buttons.sprites()[self.selected_button_index]

    def events(self, event: pygame.event.Event) -> None:
        super().events(event)

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                self.selected_button_index -= 1
            if event.key == pygame.K_DOWN:
                self.selected_button_index += 1

    def update(self) -> None:
        super().update()
        
        if self.selected_button_index < 0:
            self.selected_button_index = len(self.buttons) - 1
        if self.selected_button_index > len(self.buttons) - 1:
            self.selected_button_index = 0

        # self.selected_button_index = max(0, min(self.selected_button_index, len(self.buttons) - 1))
        
        self.selected_button = self.buttons.sprites()[self.selected_button_index]
        for button in self.buttons:
            button.change_state("unselected")
        self.selected_button.change_state("selected")

        for button in self.buttons:
            button.update()

    def draw(self) -> None:
        super().draw()

        self.game.screen.blit(self.title, self.title_rect)
        self.game.screen.blit(self.credit, self.credit_rect)
        for button in self.buttons:
            button.draw(self.game.screen)

from src.game import Game
