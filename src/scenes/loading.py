#!/usr/bin/env python3

"""loading.py: LoadingState class."""

from __future__ import annotations

import pygame
from typing import List

from constants import Settings
settings = Settings()

from src.scenes.state import State

class LoadingState(State):
    def __init__(self, game: Game, execution_time: int) -> None:
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

        self.start_time: int = pygame.time.get_ticks()
        self.end_time: int = self.start_time + execution_time

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

        current_time: int = pygame.time.get_ticks()
        if current_time >= self.end_time:
            self.game.next_state()
    
    def draw(self) -> None:
        super().draw()

        self.game.display.fill(settings.BLACK)
        self.game.display.blit(self.loading, self.loading_rect)
    
from src.game import Game
