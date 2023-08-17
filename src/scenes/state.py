#!/usr/bin/env python3

"""state.py: State class and subclasses."""

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
        super().__init__()
        self.game: Game = game

    @abstractmethod
    def events(self, _: pygame.event.Event) -> None:
        pass

    @abstractmethod
    def update(self) -> None:
        pass

    @abstractmethod
    def draw(self) -> None:
        pass

class Scene(State):
    def __init__(self, game: Game) -> None:
        super().__init__(game)

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

    def update(self) -> None:
        super().update()

        self.background.update()
        
        self.spawn_clouds()
        self.clouds.update()

        self.fps.update(self.game.clock.get_fps())

    def draw(self) -> None:
        super().draw()
        
        self.game.display.fill(settings.BLACK)

        self.background.draw(self.game.display)
        for cloud in self.clouds:
            cloud.draw(self.game.display)

        self.fps.draw(self.game.display)

from src.game import Game
