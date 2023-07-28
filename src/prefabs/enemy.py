#!/usr/bin/env python3

"""enemy.py: Enemy class and subclasses."""

import pygame
from abc import ABC, abstractmethod
from typing import Optional, Callable
import random
import math

from src.settings import Settings
settings = Settings()

from src.prefabs.player import Player

class Enemy(ABC, pygame.sprite.Sprite):
    def __init__(self,
                 health: int,
                 body_damage: int,
                 bullet_damage: Optional[int],
                 bullet_speed: Optional[int],
                 bullet_lifetime: Optional[int],
                 reload_time: Optional[int],
                 movement_speed: int,
                 movement_cooldown: int,
                 movement_pattern: str,
                 score: int) -> None:
        from src.prefabs.projectile import BulletEnemy

        ABC.__init__(self)
        pygame.sprite.Sprite.__init__(self)

        self.health: int = health
        self.body_damage: int = body_damage
        self.bullet_damage: Optional[int] = bullet_damage
        self.bullet_speed: Optional[int] = bullet_speed
        self.bullet_lifetime: Optional[int] = bullet_lifetime
        self.reload_time: Optional[int] = reload_time

        self.moving_timer: int = 0
        self.movement_cooldown: int = movement_cooldown
        self.movement_speed: int = movement_speed
        self.movement_pattern: Callable[[Player], None] = getattr(self, movement_pattern)

        self.angle: float = random.uniform(0, 360)
        self.score: int = score

        self.can_shoot: bool = True
        self.shoot_timer: int = 0
        self.shoot_cooldown = self.reload_time
        self.bullets: pygame.sprite.Group[BulletEnemy] = pygame.sprite.Group()

        self.image: pygame.Surface
        self.rect: pygame.Rect

    def update(self, player: Player) -> None:
        current_time: int = pygame.time.get_ticks()
        if current_time - self.moving_timer > self.movement_cooldown:
            self.movement_pattern(player)
            self.moving_timer = current_time
        self.constraints()

        if self.health <= 0:
            self.kill()

    def move_random(self, _: Player) -> None:
        self.rect.x += math.ceil(math.sin(math.radians(self.angle)) * self.movement_speed)
        self.rect.y += math.ceil(math.cos(math.radians(self.angle)) * self.movement_speed)

    def move_target(self, player: Player) -> None:
        rel_x: int = self.rect.centerx - player.rect.centerx
        rel_y: int = self.rect.centery - player.rect.centery
        self.angle = (180 / math.pi) * math.atan2(rel_x, rel_y)
        self.rect.x -= math.ceil(math.sin(math.radians(self.angle)) * self.movement_speed)
        self.rect.y -= math.ceil(math.cos(math.radians(self.angle)) * self.movement_speed)

    def constraints(self) -> None:
        # Kill enemy if goes off screen
        if self.rect.x - self.rect.width > settings.SCREEN_WIDTH:
            self.kill()
        if self.rect.x + self.rect.width < 0:
            self.kill()
        if self.rect.y - self.rect.height > settings.SCREEN_HEIGHT:
            self.kill()
        if self.rect.y + self.rect.height < 0:
            self.kill()

    def draw(self, screen) -> None:
        screen.blit(self.image, self.rect)

class EnemyPurple(Enemy):
    def __init__(self) -> None:
        super().__init__(settings.ENEMY_PURPLE_HEALTH,
                         settings.ENEMY_PURPLE_BODY_DAMAGE,
                         settings.ENEMY_PURPLE_BULLET_DAMAGE,
                         settings.ENEMY_PURPLE_BULLET_SPEED,
                         settings.ENEMY_PURPLE_BULLET_LIFETIME,
                         settings.ENEMY_PURPLE_RELOAD_TIME,
                         settings.ENEMY_PURPLE_MOVEMENT_SPEED,
                         settings.ENEMY_PURPLE_MOVEMENT_COOLDOWN,
                         settings.ENEMY_PURPLE_MOVEMENT_PATTERN,
                         settings.ENEMY_PURPLE_SCORE)
                         
        self.image = pygame.image.load(settings.ENEMY_PURPLE_IMG).convert_alpha()

        scale: float = settings.ENEMY_PURPLE_HEIGHT / self.image.get_height()
        width: int = int(self.image.get_width() * scale)
        height: int = int(self.image.get_height() * scale)
        self.image = pygame.transform.scale(self.image, (width, height))
                                            
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, settings.SCREEN_WIDTH - self.rect.width)
        self.rect.y = random.randint(0, settings.SCREEN_HEIGHT - self.rect.height)
