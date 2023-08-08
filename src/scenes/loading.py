#!/usr/bin/env python3

"""loading.py: LoadingState class."""

from __future__ import annotations

import pygame
from typing import Tuple, Dict
import time

from src.settings import Settings
settings = Settings()

from src.scenes.state import State

class LoadingState(State):
    def __init__(self, game: Game, execution_time_ms: int,
                 next_state: State, *next_state_args: Tuple, **next_state_kwargs: Dict) -> None:
        super().__init__(game)

        self.next_state: State = next_state

        self.loading: pygame.Surface = pygame.image.load(settings.LOADING_IMG).convert_alpha()

        scale: float = settings.LOADING_IMG_HEIGHT / self.loading.get_height()
        width: int = round(self.loading.get_width() * scale)
        height: int = round(self.loading.get_height() * scale)
        self.loading = pygame.transform.scale(self.loading, (width, height))

        self.loading_rect: pygame.Rect = self.loading.get_rect()
        self.loading_rect.x = round(settings.SCREEN_WIDTH / 2 - self.loading_rect.width / 2)
        self.loading_rect.y = round(settings.SCREEN_HEIGHT / 2 - self.loading_rect.height / 2)

        self.start_time_ms: int = round(time.time() * 1000)
        self.end_time_ms: int
        self.execution_time_ms: int = execution_time_ms

        self.next_state: State = next_state
        self.next_state_args: Tuple = next_state_args
        self.next_state_kwargs: Dict = next_state_kwargs

        self.game.display.blit(self.loading, self.loading_rect)
        
    def events(self, _: pygame.event.Event) -> None:
        return super().events(_)
    
    def update(self) -> None:
        super().update()

        self.end_time_ms: int = round(time.time() * 1000)
        if self.end_time_ms - self.start_time_ms >= self.execution_time_ms:
            self.game.change_state(self.next_state(self.game, *self.next_state_args, **self.next_state_kwargs))
    
    def draw(self) -> None:
        return super().draw()
    
from src.game import Game
