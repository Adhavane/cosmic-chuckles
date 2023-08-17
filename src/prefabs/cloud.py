#!/usr/bin/env python3

"""cloud.py: Cloud class."""

import pygame
import random

from constants import Settings
settings = Settings()

class Cloud(pygame.sprite.Sprite):
    def __init__(self) -> None:
        super().__init__()

        image = random.choice(settings.CLOUD_IMGS) 
        self.image: pygame.Surface = pygame.image.load(image).convert_alpha()

        self.rect: pygame.Rect = self.image.get_rect()
        self.height: int = random.randint(settings.CLOUD_HEIGHT_MIN, settings.CLOUD_HEIGHT_MAX)
        scale: float = self.height / self.rect.height
        width: int = round(self.rect.width * scale)
        height: int = round(self.rect.height * scale)
        self.image = pygame.transform.scale(self.image, (width, height))
        
        self.rect = self.image.get_rect()
        self.rect.x = -self.rect.width
        self.rect.y = random.randint(0, settings.SCREEN_HEIGHT - self.rect.height)

        self.moving_timer: int = pygame.time.get_ticks()
        self.speed: int = random.randint(settings.CLOUD_SPEED_MIN, settings.CLOUD_SPEED_MAX)
        
        self.opacity: int = random.randint(settings.CLOUD_OPACITY_MIN, settings.CLOUD_OPACITY_MAX)
        self.image.set_alpha(self.opacity)

    def update(self) -> None:
        current_time: int = pygame.time.get_ticks()
        if current_time - self.moving_timer > settings.CLOUD_DELTA:
            self.rect.x += round(self.speed * Settings.DELTA_TIME)
            if self.rect.left > settings.SCREEN_WIDTH:
                self.kill()

    def draw(self, display) -> None:
        display.blit(self.image, self.rect)
