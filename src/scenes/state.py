#!/usr/bin/env python3

"""state.py: State class."""

from __future__ import annotations

import pygame
import random
from abc import ABC, abstractmethod

from src.settings import Settings
settings = Settings()

from src.prefabs.background import Background
from src.prefabs.cloud import Cloud
from src.ui.fps import FPS

class State(ABC):
    def __init__(self, game: Game) -> None:
        self.game: Game = game

        self.background: Background = Background()

        self.clouds: pygame.sprite.Group[Cloud] = pygame.sprite.Group()
        for _ in range(settings.CLOUD_INIT):
            cloud: Cloud = Cloud()
            cloud.rect.x = random.randint(0, settings.SCREEN_WIDTH)
            self.clouds.add(cloud)
        self.cloud_timer: int = 0
        self.cloud_cooldown: int = random.randint(settings.CLOUD_TIME_MIN, settings.CLOUD_TIME_MAX)

        self.fps: FPS = FPS()

    def spawn_clouds(self) -> None:
        current_time: int = pygame.time.get_ticks()
        if current_time - self.cloud_timer > self.cloud_cooldown:
            self.cloud_timer = current_time
            self.cloud_cooldown = random.randint(settings.CLOUD_TIME_MIN, settings.CLOUD_TIME_MAX)
            self.clouds.add(Cloud())

    def events(self, _: pygame.event.Event) -> None:
        pass

    def update(self) -> None:
        self.background.update()
        
        # self.spawn_clouds()
        self.clouds.update()

        self.fps.update(self.game.clock.get_fps())

    def draw(self) -> None:
        self.game.screen.fill(settings.BLACK)

        self.background.draw(self.game.screen)
        for cloud in self.clouds:
            cloud.draw(self.game.screen)

        self.fps.draw(self.game.screen)

from src.game import Game
