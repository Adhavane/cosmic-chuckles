#!/usr/bin/env python3

"""state.py: State class and subclasses."""

from __future__ import annotations

import pygame
import random
from abc import ABC, abstractmethod

from src.constants import SCREEN_WIDTH, BLACK

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
    CLOUD_INIT: int = 4

    CLOUD_TIME_MIN: int = 1000
    CLOUD_TIME_MAX: int = 2000

    def __init__(self, game: Game) -> None:
        super().__init__(game)

        self.background: Background = Background()

        self.clouds: pygame.sprite.Group[Cloud] = pygame.sprite.Group()
        for _ in range(Scene.CLOUD_INIT):
            cloud: Cloud = Cloud()
            cloud.rect.x = random.randint(0, SCREEN_WIDTH)
            self.clouds.add(cloud)
        self.cloud_timer: int = 0
        self.cloud_cooldown: int = random.randint(Scene.CLOUD_TIME_MIN, Scene.CLOUD_TIME_MAX)

        self.fps: FPS = FPS()

    def spawn_clouds(self) -> None:
        current_time: int = pygame.time.get_ticks()
        if current_time - self.cloud_timer > self.cloud_cooldown:
            self.cloud_timer = current_time
            self.cloud_cooldown = random.randint(Scene.CLOUD_TIME_MIN, Scene.CLOUD_TIME_MAX)
            self.clouds.add(Cloud())

    def update(self) -> None:
        super().update()

        self.background.update()
        
        self.spawn_clouds()
        self.clouds.update()

        self.fps.update(self.game.clock.get_fps())

    def draw(self) -> None:
        super().draw()
        
        self.game.display.fill(BLACK)

        self.background.draw(self.game.display)
        for cloud in self.clouds:
            cloud.draw(self.game.display)

        self.fps.draw(self.game.display)

from src.game import Game
