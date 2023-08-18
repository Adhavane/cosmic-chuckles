#!/usr/bin/env python3

"""projectile.py: Projectile class and subclasses."""

import os
import pygame
from abc import ABC, abstractmethod
import math
from typing import List, Tuple

import src.paths as paths
from src.constants import \
    SCREEN_WIDTH, SCREEN_HEIGHT, TIMER
from src.utils import extract_color_palette, scale_to_resolution

class Projectile(ABC, pygame.sprite.Sprite):
    def __init__(self, image: str,
                 x: int, y: int,
                 height: int, angle: float,
                 damage: int, speed: int, lifetime: int) -> None:
        super().__init__()

        self.image: pygame.Surface = pygame.image.load(image).convert_alpha()
        # self.image = pygame.transform.rotate(self.image, self.angle)
        
        scale: float = height / self.image.get_height()
        width: int = round(self.image.get_width() * scale)
        self.image = pygame.transform.scale(self.image, (width, height))

        self.rect: pygame.Rect = self.image.get_rect()
        self.rect.x = round(x - self.rect.width / 2)
        self.rect.y = round(y - self.rect.height / 2)

        self.colors: Tuple[List[Tuple[int, int, int]], List[int]] = extract_color_palette(image)

        self.angle: float = angle
        self.speed: int = speed
        self.damage: int = damage
        self.lifetime: int = lifetime

        self.destroyed: bool = False

    def update(self) -> None:
        self.rect.x -= round(math.sin(math.radians(self.angle)) * self.speed * TIMER.DELTA_TIME)
        self.rect.y -= round(math.cos(math.radians(self.angle)) * self.speed * TIMER.DELTA_TIME)

        self.lifetime -= 1
        if self.lifetime <= 0:
            self.destroy()

        self.constraints()

    def constraints(self) -> None:
        if self.rect.x + self.rect.width < 0:
            self.kill()
        if self.rect.x > SCREEN_WIDTH:
            self.kill()
        if self.rect.y + self.rect.height < 0:
            self.kill()
        if self.rect.y > SCREEN_HEIGHT:
            self.kill()

    def destroy(self) -> None:
        self.destroyed = True

    def draw(self, display) -> None:
        display.blit(self.image, self.rect)       

class BulletPlayer(Projectile):
    IMG: str = os.path.join(paths.SPRITES, "bullet_player.png")
    HEIGHT: int = scale_to_resolution(32)

    def __init__(self, x: int, y: int,
                 angle: float, damage: int,
                 speed: int, lifetime: int) -> None:
        super().__init__(image=BulletPlayer.IMG,
                         x=x, y=y,
                         height=BulletPlayer.HEIGHT,
                         angle=angle, damage=damage,
                         speed=speed, lifetime=lifetime)

class BulletEnemy(Projectile):
    IMG: str = os.path.join(paths.SPRITES, "bullet_enemy.png")
    HEIGHT: int = scale_to_resolution(32)

    def __init__(self, x: int, y: int,
                 angle: float, damage: int,
                 speed: int, lifetime: int) -> None:
        super().__init__(image=BulletEnemy.IMG,
                         x=x, y=y,
                         height=BulletEnemy.HEIGHT,
                         angle=angle, damage=damage,
                         speed=speed, lifetime=lifetime)
