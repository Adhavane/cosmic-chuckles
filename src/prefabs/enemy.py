#!/usr/bin/env python3

"""enemy.py: Enemy class and subclasses."""

from __future__ import annotations

import pygame
from abc import ABC, abstractmethod
from typing import Optional, Callable, List, Tuple
import random
import math

from src.settings import Settings, extract_color_palette
settings = Settings()

from src.prefabs.player import Player
from src.prefabs.projectile import BulletEnemy

class Enemy(ABC, pygame.sprite.Sprite):
    def __init__(self,
                 image: str,
                 height: int,
                 health: int,
                 body_damage: int,
                 bullet_damage: Optional[int],
                 bullet_speed: Optional[int],
                 bullet_lifetime: Optional[int],
                 reload_time: Optional[int],
                 movement_speed: int,
                 movement_cooldown: int,
                 movement_pattern: str,
                 damaged_time: int,
                 score: int) -> None:
        from src.prefabs.projectile import BulletEnemy

        ABC.__init__(self)
        pygame.sprite.Sprite.__init__(self)

        self.original_image: pygame.Surface = pygame.image.load(image).convert_alpha()

        scale: float = height / self.original_image.get_height()
        width: int = round(self.original_image.get_width() * scale)
        self.original_image = pygame.transform.scale(self.original_image, (width, height))
        self.image: pygame.Surface = self.original_image.copy()

        self.rect: pygame.Rect = self.image.get_rect()
        # Spawn enemy off screen
        area: str = random.choice(["top", "bottom", "left", "right"])
        if area == "top":
            self.rect.x = random.randint(0, settings.SCREEN_WIDTH)
            self.rect.y = -self.rect.height + 1
        elif area == "bottom":
            self.rect.x = random.randint(0, settings.SCREEN_WIDTH)
            self.rect.y = settings.SCREEN_HEIGHT - 1
        elif area == "left":
            self.rect.x = -self.rect.width + 1
            self.rect.y = random.randint(0, settings.SCREEN_HEIGHT)
        elif area == "right":
            self.rect.x = settings.SCREEN_WIDTH - 1
            self.rect.y = random.randint(0, settings.SCREEN_HEIGHT)
        self.rect_x_float: float = float(self.rect.x)
        self.rect_y_float: float = float(self.rect.y)

        self.mask: pygame.mask.Mask = pygame.mask.from_surface(self.image)

        self.colors: Tuple[List[Tuple[int, int, int]], List[int]] = extract_color_palette(image)

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

        self.damaged: bool = False
        self.damaged_timer: int = 0
        self.damaged_cooldown: int = damaged_time

        self.destroyed: bool = False

    def update(self, player: Player) -> None:
        self.render()
        self.move(player)
        self.constraints()

        if self.bullet_damage:
            self.shoot()

        self.damage()

        if self.health <= 0:
            self.destroy()

    def render(self) -> None:
        self.image = self.original_image.copy()
        self.rect = self.image.get_rect(center=self.rect.center)

    def move(self, player: Player) -> None:
        current_time: int = pygame.time.get_ticks()
        if current_time - self.moving_timer > self.movement_cooldown:
            self.movement_pattern(player)
            self.moving_timer = current_time

    def shoot(self) -> None:
        if self.can_shoot:
            self.bullets.add(BulletEnemy(self.rect.centerx,
                                         self.rect.centery,
                                         self.angle,
                                         self.bullet_damage,
                                         self.bullet_speed,
                                         self.bullet_lifetime))
            self.can_shoot = False
            self.shoot_timer = pygame.time.get_ticks()
        self.reload()
        self.bullets.update()

    def reload(self) -> None:
        if not self.can_shoot:
            current_time: int = pygame.time.get_ticks()
            if current_time - self.shoot_timer > self.shoot_cooldown:
                self.can_shoot = True

    def move_random(self, _: Player) -> None:
        self.rect_x_float += math.sin(math.radians(self.angle)) * self.movement_speed * Settings.DELTA_TIME
        self.rect_y_float += math.cos(math.radians(self.angle)) * self.movement_speed * Settings.DELTA_TIME
        self.rect.x = round(self.rect_x_float)
        self.rect.y = round(self.rect_y_float)

    def move_target(self, player: Player) -> None:
        rel_x: int = self.rect.centerx - player.rect.centerx
        rel_y: int = self.rect.centery - player.rect.centery
        self.angle = (180 / math.pi) * math.atan2(rel_x, rel_y)
        self.rect_x_float -= math.sin(math.radians(self.angle)) * self.movement_speed * Settings.DELTA_TIME
        self.rect_y_float -= math.cos(math.radians(self.angle)) * self.movement_speed * Settings.DELTA_TIME
        self.rect.x = round(self.rect_x_float)
        self.rect.y = round(self.rect_y_float)

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
    
    def destroy(self) -> None:
        self.destroyed = True
    
    def spawn(self) -> List[Enemy]:
        return []
    
    def damage(self) -> None:
        if self.damaged:
            self.tint(settings.RED)
            current_time: int = pygame.time.get_ticks()
            if current_time - self.damaged_timer >= self.damaged_cooldown:
                self.damaged = False

    def take_damage(self, damage: int) -> None:
        self.health -= damage
        self.damaged = True
        self.damaged_timer = pygame.time.get_ticks()

    def tint(self, color: Tuple[int, int, int, Optional[int]]) -> None:
        self.image.fill(color, special_flags=pygame.BLEND_RGBA_MULT)

    def draw(self, display) -> None:
        self.bullets.draw(display)
        display.blit(self.image, self.rect)

class EnemyPurple(Enemy):
    def __init__(self) -> None:
        super().__init__(settings.ENEMY_PURPLE_IMG,
                         settings.ENEMY_PURPLE_HEIGHT,
                         settings.ENEMY_PURPLE_HEALTH,
                         settings.ENEMY_PURPLE_BODY_DAMAGE,
                         settings.ENEMY_PURPLE_BULLET_DAMAGE,
                         settings.ENEMY_PURPLE_BULLET_SPEED,
                         settings.ENEMY_PURPLE_BULLET_LIFETIME,
                         settings.ENEMY_PURPLE_RELOAD_TIME,
                         settings.ENEMY_PURPLE_MOVEMENT_SPEED,
                         settings.ENEMY_PURPLE_MOVEMENT_COOLDOWN,
                         settings.ENEMY_PURPLE_MOVEMENT_PATTERN,
                         settings.ENEMY_PURPLE_DAMAGED_TIME,
                         settings.ENEMY_PURPLE_SCORE)

class EnemyRed(Enemy):
    def __init__(self) -> None:
        super().__init__(settings.ENEMY_RED_IMG,
                         settings.ENEMY_RED_HEIGHT,
                         settings.ENEMY_RED_HEALTH,
                         settings.ENEMY_RED_BODY_DAMAGE,
                         settings.ENEMY_RED_BULLET_DAMAGE,
                         settings.ENEMY_RED_BULLET_SPEED,
                         settings.ENEMY_RED_BULLET_LIFETIME,
                         settings.ENEMY_RED_RELOAD_TIME,
                         settings.ENEMY_RED_MOVEMENT_SPEED,
                         settings.ENEMY_RED_MOVEMENT_COOLDOWN,
                         settings.ENEMY_RED_MOVEMENT_PATTERN,
                         settings.ENEMY_RED_DAMAGED_TIME,
                         settings.ENEMY_RED_SCORE)
        
class EnemyGreen(Enemy):
    def __init__(self) -> None:
        super().__init__(settings.ENEMY_GREEN_IMG,
                         settings.ENEMY_GREEN_HEIGHT,
                         settings.ENEMY_GREEN_HEALTH,
                         settings.ENEMY_GREEN_BODY_DAMAGE,
                         settings.ENEMY_GREEN_BULLET_DAMAGE,
                         settings.ENEMY_GREEN_BULLET_SPEED,
                         settings.ENEMY_GREEN_BULLET_LIFETIME,
                         settings.ENEMY_GREEN_RELOAD_TIME,
                         settings.ENEMY_GREEN_MOVEMENT_SPEED,
                         settings.ENEMY_GREEN_MOVEMENT_COOLDOWN,
                         settings.ENEMY_GREEN_MOVEMENT_PATTERN,
                         settings.ENEMY_GREEN_DAMAGED_TIME,
                         settings.ENEMY_GREEN_SCORE)
        
    def spawn(self) -> List[Enemy]:
        enemies: List[Enemy] = []
        for _ in range(settings.ENEMY_GREEN_BABY_AMOUNT):
            new_enemy: Enemy = EnemyGreenBaby()
            new_enemy.rect_x_float = self.rect.centerx + random.randint(-settings.ENEMY_GREEN_BABY_SPAWN_RADIUS, settings.ENEMY_GREEN_BABY_SPAWN_RADIUS)
            new_enemy.rect_y_float = self.rect.centery + random.randint(-settings.ENEMY_GREEN_BABY_SPAWN_RADIUS, settings.ENEMY_GREEN_BABY_SPAWN_RADIUS)
            enemies.append(new_enemy)
        return enemies

class EnemyGreenBaby(Enemy):
    def __init__(self) -> None:
        super().__init__(settings.ENEMY_GREEN_BABY_IMG,
                         settings.ENEMY_GREEN_BABY_HEIGHT,
                         settings.ENEMY_GREEN_BABY_HEALTH,
                         settings.ENEMY_GREEN_BABY_BODY_DAMAGE,
                         settings.ENEMY_GREEN_BABY_BULLET_DAMAGE,
                         settings.ENEMY_GREEN_BABY_BULLET_SPEED,
                         settings.ENEMY_GREEN_BABY_BULLET_LIFETIME,
                         settings.ENEMY_GREEN_BABY_RELOAD_TIME,
                         settings.ENEMY_GREEN_BABY_MOVEMENT_SPEED,
                         settings.ENEMY_GREEN_BABY_MOVEMENT_COOLDOWN,
                         settings.ENEMY_GREEN_BABY_MOVEMENT_PATTERN,
                         settings.ENEMY_GREEN_BABY_DAMAGED_TIME,
                         settings.ENEMY_GREEN_BABY_SCORE)
        
class EnemyYellow(Enemy):
    def __init__(self) -> None:
        super().__init__(settings.ENEMY_YELLOW_IMG,
                         settings.ENEMY_YELLOW_HEIGHT,
                         settings.ENEMY_YELLOW_HEALTH,
                         settings.ENEMY_YELLOW_BODY_DAMAGE,
                         settings.ENEMY_YELLOW_BULLET_DAMAGE,
                         settings.ENEMY_YELLOW_BULLET_SPEED,
                         settings.ENEMY_YELLOW_BULLET_LIFETIME,
                         settings.ENEMY_YELLOW_RELOAD_TIME,
                         settings.ENEMY_YELLOW_MOVEMENT_SPEED,
                         settings.ENEMY_YELLOW_MOVEMENT_COOLDOWN,
                         settings.ENEMY_YELLOW_MOVEMENT_PATTERN,
                         settings.ENEMY_YELLOW_DAMAGED_TIME,
                         settings.ENEMY_YELLOW_SCORE)
