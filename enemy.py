#!/usr/bin/env python

"""enemy.py: Enemy class and subclasses."""

import pygame
from abc import ABC, abstractmethod
from typing import Optional, Callable
import random
import math

from pygame.sprite import _Group

from settings import *
settings = Settings()

from player import Player

class Enemy(ABC, pygame.sprite.Sprite):
    def __init__(self,
                 health: int,
                 body_damage: Optional[int],
                 bullet_damage: Optional[int],
                 bullet_speed: Optional[int],
                 bullet_lifetime: Optional[int],
                 reload_time: Optional[int],
                 movement_speed: int,
                 movement_cooldown: int,
                 movement_pattern: Callable[[Player], None]) -> None:
        super().__init__()

        self.health = health
        self.body_damage = body_damage
        self.bullet_damage = bullet_damage
        self.bullet_speed = bullet_speed
        self.bullet_lifetime = bullet_lifetime
        self.reload_time = reload_time

        self.moving_timer = 0
        self.movement_cooldown = movement_cooldown
        self.movement_speed = movement_speed
        self.movement_pattern = movement_pattern

        self.angle = random.randint(0, 360)

        self.can_shoot = True
        self.shoot_timer = 0
        self.shoot_cooldown = self.reload_time
        self.bullets = pygame.sprite.Group()

    def update(self, player: Player) -> None:
        current_time = pygame.time.get_ticks()
        if current_time - self.moving_timer > self.movement_cooldown:
            self.movement_pattern(player)
            self.moving_timer = current_time
        self.constraints()

    def move_random(self, _: Player) -> None:
        self.rect.x += math.sin(math.radians(self.direction)) * self.movement_speed
        self.rect.y += math.cos(math.radians(self.direction)) * self.movement_speed

    def move_target(self, player: Player) -> None:
        rel_x, rel_y = self.rect.centerx - player.rect.centerx, self.rect.centery - player.rect.centery
        self.angle = (180 / math.pi) * math.atan2(rel_x, rel_y)
        self.rect.x -= math.sin(math.radians(self.angle)) * self.movement_speed
        self.rect.y -= math.cos(math.radians(self.angle)) * self.movement_speed

    def constraints(self) -> None:
        # Kill enemy if goes off screen
        if self.rect.x - self.rect.width > settings.WIDTH:
            self.kill()
        if self.rect.x + self.rect.width < 0:
            self.kill()
        if self.rect.y - self.rect.height > settings.HEIGHT:
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
                         None)
                         
        self.movement_pattern = self.move_random

        self.image = pygame.image.load(settings.ENEMY_PURPLE_IMG).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, settings.WIDTH - self.rect.width)
        self.rect.y = random.randint(0, settings.HEIGHT - self.rect.height)

        self.direction = random.randint(0, 360)
        
        
                 
