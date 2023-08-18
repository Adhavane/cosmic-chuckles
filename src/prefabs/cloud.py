#!/usr/bin/env python3

"""cloud.py: Cloud class."""

import os
import pygame
import random
from typing import List

import src.paths as paths
from src.constants import \
    SCREEN_WIDTH, SCREEN_HEIGHT, TIMER

class Cloud(pygame.sprite.Sprite):
    IMG_COUNT: int = 6
    IMGS: List[str] = [f"{os.path.join(paths.SPRITES, 'cloud')}_{i}.png"
                       for i in range(IMG_COUNT)]
    
    HEIGHT_MIN: int = 50
    HEIGHT_MAX: int = 400

    SPEED_MIN: int = 1
    SPEED_MAX: int = 3

    DELTA: int = 30
    
    OPACITY_MIN: int = 8
    OPACITY_MAX: int = 64

    def __init__(self) -> None:
        super().__init__()

        image = random.choice(Cloud.IMGS) 
        self.image: pygame.Surface = pygame.image.load(image).convert_alpha()

        self.rect: pygame.Rect = self.image.get_rect()
        self.height: int = random.randint(Cloud.HEIGHT_MIN, Cloud.HEIGHT_MAX)
        scale: float = self.height / self.rect.height
        width: int = round(self.rect.width * scale)
        height: int = round(self.rect.height * scale)
        self.image = pygame.transform.scale(self.image, (width, height))
        
        self.rect = self.image.get_rect()
        self.rect.x = -self.rect.width
        self.rect.y = random.randint(0, SCREEN_HEIGHT - self.rect.height)

        self.moving_timer: int = pygame.time.get_ticks()
        self.speed: int = random.randint(Cloud.SPEED_MIN, Cloud.SPEED_MAX)
        
        self.opacity: int = random.randint(Cloud.OPACITY_MIN, Cloud.OPACITY_MAX)
        self.image.set_alpha(self.opacity)

    def update(self) -> None:
        current_time: int = pygame.time.get_ticks()
        if current_time - self.moving_timer > Cloud.DELTA:
            self.rect.x += round(self.speed * TIMER.DELTA_TIME)
            if self.rect.left > SCREEN_WIDTH:
                self.kill()

    def draw(self, display) -> None:
        display.blit(self.image, self.rect)
