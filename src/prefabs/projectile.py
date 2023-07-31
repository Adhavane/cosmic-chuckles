#!/usr/bin/env python3

"""projectile.py: Projectile class and subclasses."""

import pygame
from abc import ABC, abstractmethod
import math

from src.settings import Settings
settings = Settings()

class Projectile(ABC, pygame.sprite.Sprite):
    def __init__(self, image: str,
                 x: int, y: int,
                 height: int, angle: float,
                 damage: int, speed: int, lifetime: int) -> None:
        super().__init__()

        self.image: pygame.Surface = pygame.image.load(image).convert_alpha()
        # self.image = pygame.transform.rotate(self.image, self.angle)
        
        scale: float = height / self.image.get_height()
        width: int = int(self.image.get_width() * scale)
        self.image = pygame.transform.scale(self.image, (width, height))

        self.rect: pygame.Rect = self.image.get_rect()
        self.rect.x = int(x - self.rect.width / 2)
        self.rect.y = int(y - self.rect.height / 2)

        self.angle: float = angle
        self.speed: int = speed
        self.damage: int = damage
        self.lifetime: int = lifetime

    def update(self) -> None:
        self.rect.x -= math.sin(math.radians(self.angle)) * self.speed
        self.rect.y -= math.cos(math.radians(self.angle)) * self.speed

        self.lifetime -= 1
        if self.lifetime <= 0:
            self.kill()
        
        if self.rect.x < 0:
            self.kill()
        if self.rect.x > settings.SCREEN_WIDTH:
            self.kill()

    def draw(self, screen) -> None:
        screen.blit(self.image, self.rect)       

class BulletPlayer(Projectile):
    def __init__(self, x: int, y: int,
                 angle: float, damage: int,
                 speed: int, lifetime: int) -> None:
        super().__init__(settings.BULLET_PLAYER_IMG,
                         x, y, settings.BULLET_PLAYER_HEIGHT,
                         angle, damage, speed, lifetime)

class BulletEnemy(Projectile):
    def __init__(self, x: int, y: int,
                 angle: float, damage: int,
                 speed: int, lifetime: int) -> None:
        super().__init__(settings.BULLET_ENEMY_IMG,
                         x, y, settings.BULLET_ENEMY_HEIGHT,
                         angle, damage, speed, lifetime)
