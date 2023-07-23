#!/usr/bin/env python

"""cloud.py: Cloud class."""

import pygame

from settings import *
settings = Settings()

import random

class Cloud(pygame.sprite.Sprite):
    def __init__(self) -> None:
        super().__init__()

        self.images = []
        for img in settings.CLOUD_IMGS:
            self.images.append(pygame.image.load(img).convert_alpha())
        self.image = random.choice(self.images)

        self.rect = self.image.get_rect()
        self.height = random.randint(settings.CLOUD_HEIGHT_MIN, settings.CLOUD_HEIGHT_MAX)
        scale = self.height / self.rect.height
        self.image = pygame.transform.scale(self.image, (int(self.rect.width * scale), int(self.rect.height * scale)))
        
        self.rect = self.image.get_rect()
        self.rect.x = -self.rect.width
        self.rect.y = random.randint(0, settings.HEIGHT)

        self.speed = random.randint(settings.CLOUD_SPEED_MIN, settings.CLOUD_SPEED_MAX)
        self.opacity = random.randint(settings.OPACITY_MIN, settings.OPACITY_MAX)
        self.image.set_alpha(self.opacity)

    def update(self) -> None:
        self.rect.x += self.speed
        if self.rect.left > settings.WIDTH:
            self.kill()

    def draw(self, screen) -> None:
        screen.blit(self.image, self.rect)
