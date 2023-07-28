#!/usr/bin/env python3

"""menu.py: Menu class and subclasses."""

import pygame

from src.settings import Settings
settings = Settings()

from src.scenes.state import State
from src.gui.button import ButtonPlay, ButtonQuit

class MenuState(State):
    def __init__(self, game) -> None:
        super().__init__(game)

        self.title = pygame.image.load(settings.TITLE_IMG).convert_alpha()
        
        scale = settings.TITLE_HEIGHT / self.title.get_height()
        self.title = pygame.transform.scale(self.title, (int(self.title.get_width() * scale), int(self.title.get_height() * scale)))

        self.title_rect = self.title.get_rect()
        self.title_rect.x = int(settings.SCREEN_WIDTH / 2 - self.title_rect.width / 2)
        self.title_rect.y = settings.TITLE_Y

        self.credit = pygame.image.load(settings.CREDIT_IMG).convert_alpha()

        scale = settings.CREDIT_HEIGHT / self.credit.get_height()
        self.credit = pygame.transform.scale(self.credit, (int(self.credit.get_width() * scale), int(self.credit.get_height() * scale)))

        self.credit_rect = self.credit.get_rect()
        self.credit_rect.x = self.title_rect.x + self.title_rect.width - self.credit_rect.width
        self.credit_rect.y = settings.CREDIT_Y

        self.button_play = ButtonPlay(self.game)
        self.button_quit = ButtonQuit(self.game)

        self.buttons: pygame.sprite.Group = pygame.sprite.Group()
        self.buttons.add(self.button_play)
        self.buttons.add(self.button_quit)

        self.selected_button_index = 0
        self.selected_button = self.buttons.sprites()[self.selected_button_index]

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
