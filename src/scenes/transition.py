#!/usr/bin/env python3

"""transition.py: TransitionState class."""

from __future__ import annotations

import pygame
from typing import Tuple

from src.settings import Settings
settings = Settings()

from src.scenes.state import State

class TransitionState(State):
    def __init__(self, game: Game, execution_time: int) -> None:
        super().__init__(game)

        self.start_time: int = pygame.time.get_ticks()
        self.end_time: int = self.start_time + execution_time

        self.circle_radius: int = 5
        self.circle_color: Tuple = settings.RED
        self.circle_center: Tuple = (settings.SCREEN_WIDTH / 2, settings.SCREEN_HEIGHT / 2)
        self.circle: pygame.Surface = pygame.Surface((self.circle_radius * 2, self.circle_radius * 2))
        self.circle_rect: pygame.Rect = self.circle.get_rect()
        self.circle_rect.center = self.circle_center

    def events(self, _: pygame.event.Event) -> None:
        return super().events(_)
    
    def update(self) -> None:
        super().update()

        current_time: int = pygame.time.get_ticks()
        if current_time >= self.end_time:
            self.game.next_state()

        self.circle_radius += 30 * Settings.DELTA_TIME
        self.circle = pygame.Surface((self.circle_radius * 2, self.circle_radius * 2))
        self.circle_rect = self.circle.get_rect()
        self.circle_rect.center = self.circle_center

    def draw(self) -> None:
        super().draw()

        pygame.draw.circle(self.circle, self.circle_color, (self.circle_radius, self.circle_radius), self.circle_radius)
        self.game.display.blit(self.circle, self.circle_rect)
        self.game.display.blit(self.circle, self.circle_rect, special_flags=pygame.BLEND_RGBA_ADD)
    
from src.game import Game
