#!/usr/bin/env python3

"""state.py: State class."""

import sys
sys.path.append("src")

import pygame
import random
from abc import ABC, abstractmethod

from src.settings import Settings
settings = Settings()

from src.prefabs.background import Background
from src.prefabs.cloud import Cloud

class State(ABC):
    def __init__(self, game) -> None:
        self.game = game

        self.background = Background()

        self.clouds = pygame.sprite.Group()
        for _ in range(settings.CLOUD_INIT):
            cloud = Cloud()
            cloud.rect.x = random.randint(0, settings.SCREEN_WIDTH)
            self.clouds.add(cloud)
        self.cloud_timer = 0
        self.cloud_cooldown = random.randint(settings.CLOUD_TIME_MIN, settings.CLOUD_TIME_MAX)

    def spawn_clouds(self) -> None:
        current_time = pygame.time.get_ticks()
        if current_time - self.cloud_timer > self.cloud_cooldown:
            self.cloud_timer = current_time
            self.cloud_cooldown = random.randint(settings.CLOUD_TIME_MIN, settings.CLOUD_TIME_MAX)
            cloud = Cloud()
            self.clouds.add(cloud)

    def events(self, _: pygame.event.Event) -> None:
        pass

    def update(self) -> None:
        self.background.update()
        
        self.spawn_clouds()
        self.clouds.update()

    def draw(self) -> None:
        self.game.screen.fill(settings.BLACK)

        self.background.draw(self.game.screen)
        for cloud in self.clouds:
            cloud.draw(self.game.screen)
