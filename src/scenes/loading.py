#!/usr/bin/env python3

"""loading.py: LoadingState class."""

from __future__ import annotations

import os
import pygame
from typing import List, Optional

import src.paths as paths
from src.constants import \
    SCREEN_WIDTH, SCREEN_HEIGHT, BLACK
from src.utils import scale_to_resolution

from src.scenes.state import State

class LoadingState(State):
    IMG_COUNT: int = 4
    IMGS: List[str] = [f"{os.path.join(paths.SPRITES, 'loading')}_{i}.png"
                       for i in range(IMG_COUNT)]
    IMG_HEIGHT: int = scale_to_resolution(34)
    IMG_DELAY: int = 800
    TIME: int = 3000

    def __init__(self, game: Game, execution_time: Optional[int] = None) -> None:
        super().__init__(game)

        self.loading_images: List[str] = [pygame.image.load(image).convert_alpha() for image in LoadingState.IMGS]
        self.loading_index: int = 0
        self.loading: pygame.Surface = self.loading_images[self.loading_index]
        
        self.loading_rect: pygame.Rect = self.loading.get_rect()
        scale: float = LoadingState.IMG_HEIGHT / self.loading_rect.height
        width: int = round(self.loading_rect.width * scale)
        height: int = round(self.loading_rect.height * scale)
        self.loading = pygame.transform.scale(self.loading, (width, height))

        self.loading_rect = self.loading.get_rect()
        self.loading_rect.x = round(SCREEN_WIDTH / 2 - self.loading_rect.width / 2)
        self.loading_rect.y = round(SCREEN_HEIGHT / 2 - self.loading_rect.height / 2)
        
        self.loading_timer: int = 0

        self.start_time: int = pygame.time.get_ticks()
        if execution_time is None:
            self.execution_time: int = LoadingState.TIME
        else:
            self.execution_time: int = execution_time
        self.end_time: int = self.start_time + self.execution_time

    def events(self, _: pygame.event.Event) -> None:
        return super().events(_)
    
    def animations(self) -> None:
        current_time: int = pygame.time.get_ticks()
        if current_time - self.loading_timer > LoadingState.IMG_DELAY:
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

        self.game.display.fill(BLACK)
        self.game.display.blit(self.loading, self.loading_rect)
    
from src.game import Game
