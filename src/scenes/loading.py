#!/usr/bin/env python3

"""loading.py: LoadingState class."""

from __future__ import annotations

import pygame
from typing import Tuple, Dict, List
import time

from src.settings import Settings
settings = Settings()

from src.scenes.state import State

class LoadingState(State):
    def __init__(self, game: Game, execution_time_ms: int,
                 next_state: State, *next_state_args: Tuple, **next_state_kwargs: Dict) -> None:
        super().__init__(game)

        self.loading_images: List[str] = [pygame.image.load(image).convert_alpha() for image in settings.LOADING_IMGS]
        self.loading_index: int = 0
        self.loading: pygame.Surface = self.loading_images[self.loading_index]
        
        self.loading_rect: pygame.Rect = self.loading.get_rect()
        scale: float = settings.LOADING_IMG_HEIGHT / self.loading_rect.height
        width: int = round(self.loading_rect.width * scale)
        height: int = round(self.loading_rect.height * scale)
        self.loading = pygame.transform.scale(self.loading, (width, height))

        self.loading_rect = self.loading.get_rect()
        self.loading_rect.x = round(settings.SCREEN_WIDTH / 2 - self.loading_rect.width / 2)
        self.loading_rect.y = round(settings.SCREEN_HEIGHT / 2 - self.loading_rect.height / 2)
        
        self.loading_timer: int = 0

        self.start_time_ms: int = round(time.time() * 1000)
        self.end_time_ms: int
        self.execution_time_ms: int = execution_time_ms

        self.next_state: State = next_state
        self.next_state_args: Tuple = next_state_args
        self.next_state_kwargs: Dict = next_state_kwargs

    def events(self, _: pygame.event.Event) -> None:
        return super().events(_)
    
    def animations(self) -> None:
        current_time: int = pygame.time.get_ticks()
        if current_time - self.loading_timer > settings.LOADING_IMG_DELAY:
            self.loading_index += 1
            if self.loading_index >= len(self.loading_images):
                self.loading_index = 0
            self.loading = self.loading_images[self.loading_index]
            self.loading = pygame.transform.scale(self.loading, (self.loading_rect.width, self.loading_rect.height))
            self.loading_timer = current_time

    def update(self) -> None:
        super().update()

        self.animations()

        self.end_time_ms = round(time.time() * 1000)
        if self.end_time_ms - self.start_time_ms >= self.execution_time_ms:
            self.game.change_state(self.next_state(self.game, *self.next_state_args, **self.next_state_kwargs))
    
    def draw(self) -> None:
        super().draw()

        self.game.display.blit(self.loading, self.loading_rect)
    
from src.game import Game
