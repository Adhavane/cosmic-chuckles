#!/usr/bin/env python3

"""cloud.py: Cloud class."""

import pygame
import random

from src.settings import Settings
settings = Settings()

class Cloud(pygame.sprite.Sprite):
    def __init__(self) -> None:
        super().__init__()

        self.image = pygame.image.load(random.choice(settings.CLOUD_IMGS)).convert_alpha()

        self.rect = self.image.get_rect()
        self.height = random.randint(settings.CLOUD_HEIGHT_MIN, settings.CLOUD_HEIGHT_MAX)
        scale = self.height / self.rect.height
        self.image = pygame.transform.scale(self.image, (int(self.rect.width * scale), int(self.rect.height * scale)))
        
        self.rect = self.image.get_rect()
        self.rect.x = -self.rect.width
        self.rect.y = random.randint(0, settings.SCREEN_HEIGHT - self.rect.height)

        self.moving_timer = 0
        self.speed = random.randint(settings.CLOUD_SPEED_MIN, settings.CLOUD_SPEED_MAX)
        
        self.opacity = random.randint(settings.OPACITY_MIN, settings.OPACITY_MAX)
        self.image.set_alpha(self.opacity)

    def update(self) -> None:
        current_time = pygame.time.get_ticks()
        if current_time - self.moving_timer > settings.CLOUD_DELTA:
            self.rect.x += self.speed
            if self.rect.left > settings.SCREEN_WIDTH:
                self.kill()

    def draw(self, screen) -> None:
        screen.blit(self.image, self.rect)
