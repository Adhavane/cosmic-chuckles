#!/usr/bin/env python3

"""transition.py: TransitionState class."""

from __future__ import annotations

import pygame

from src.settings import Settings
settings = Settings()

from src.scenes.state import State

class TransitionState(State):
    def __init__(self, game: Game, execution_time: int,
                 next_state: State, *next_state_args: tuple, **next_state_kwargs: dict) -> None:
        super().__init__(game)

        self.start_time: int = pygame.time.get_ticks()
        self.end_time: int = self.start_time + execution_time

        self.next_state: State = next_state
        self.next_state_args: tuple = next_state_args
        self.next_state_kwargs: dict = next_state_kwargs

        self.circle_radius: int = 0
        self.circle_color: tuple = settings.BLACK
        self.circle_center: tuple = (settings.SCREEN_WIDTH / 2, settings.SCREEN_HEIGHT / 2)
        self.circle: pygame.Surface = pygame.Surface((self.circle_radius * 2, self.circle_radius * 2))
        self.circle_rect: pygame.Rect = self.circle.get_rect()
        self.circle_rect.center = self.circle_center

    def events(self, _: pygame.event.Event) -> None:
        return super().events(_)
    
    def update(self) -> None:
        super().update()

        current_time: int = pygame.time.get_ticks()
        if current_time >= self.end_time:
            self.game.change_state(self.next_state, *self.next_state_args, **self.next_state_kwargs)

        self.circle_radius = round((current_time - self.start_time) / (self.end_time - self.start_time) * settings.SCREEN_WIDTH / 2)
        self.circle = pygame.Surface((self.circle_radius * 2, self.circle_radius * 2))
        self.circle_rect = self.circle.get_rect()
        self.circle_rect.center = self.circle_center

    def draw(self) -> None:
        super().draw()
        
        pygame.draw.circle(self.circle, self.circle_color, (self.circle_radius, self.circle_radius), self.circle_radius)
        # self.game.screen.blit(self.circle, self.circle_rect)
        self.game.screen.blit(self.circle, self.circle_rect, special_flags=pygame.BLEND_RGBA_ADD)
    
from src.game import Game
