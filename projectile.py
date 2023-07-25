#!/usr/bin/env python

"""projectile.py: Projectile class and subclasses."""

import pygame
from abc import ABC, abstractmethod
import math

from settings import *
settings = Settings()

class Projectile(ABC, pygame.sprite.Sprite):
    def __init__(self, angle: int, speed: int, damage: int, lifetime: int) -> None:
        super().__init__()

        self.angle = angle
        self.speed = speed
        self.damage = damage
        self.lifetime = lifetime

    def update(self) -> None:
        self.rect.x -= math.sin(math.radians(self.angle)) * self.speed
        self.rect.y -= math.cos(math.radians(self.angle)) * self.speed

        self.lifetime -= 1
        if self.lifetime <= 0:
            self.kill()
        
        if self.rect.x < 0:
            self.kill()
        if self.rect.x > settings.WIDTH:
            self.kill()

    def draw(self, screen) -> None:
        screen.blit(self.image, self.rect)

class Bullet(Projectile):
    def __init__(self, image: str, x: int, y: int, angle: int, speed: int, damage: int, lifetime: int) -> None:
        super().__init__(angle, speed, damage, lifetime)

        self.image = pygame.image.load(image).convert_alpha()
        # self.image = pygame.transform.rotate(self.image, self.angle)
        
        scale = settings.BULLET_HEIGHT / self.image.get_height()
        self.image = pygame.transform.scale(self.image, (int(self.image.get_width() * scale), int(self.image.get_height() * scale)))

        self.rect = self.image.get_rect()
        self.rect.x = x - self.rect.width / 2
        self.rect.y = y - self.rect.height / 2

class BulletPlayer(Bullet):
    def __init__(self, x: int, y: int, angle: int, speed: int, damage: int, lifetime: int) -> None:
        super().__init__(settings.BULLET_PLAYER_IMG, x, y, angle, speed, damage, lifetime)

class BulletEnemy(Bullet):
    def __init__(self, x: int, y: int, angle: int, speed: int, damage: int, lifetime: int) -> None:
        super().__init__(settings.BULLET_ENEMY_IMG, x, y, angle, speed, damage, lifetime)
