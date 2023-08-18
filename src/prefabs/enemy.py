#!/usr/bin/env python3

"""enemy.py: Enemy class and subclasses."""

from __future__ import annotations

import os
import pygame
from abc import ABC, abstractmethod
from typing import Optional, Callable, List, Tuple
import random
import math

import src.paths as paths
from src.constants import \
    SCREEN_WIDTH, SCREEN_HEIGHT, TIMER, RED
from src.utils import extract_color_palette, scale_to_resolution

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
            self.rect.x = random.randint(0, SCREEN_WIDTH)
            self.rect.y = -self.rect.height + 1
        elif area == "bottom":
            self.rect.x = random.randint(0, SCREEN_WIDTH)
            self.rect.y = SCREEN_HEIGHT - 1
        elif area == "left":
            self.rect.x = -self.rect.width + 1
            self.rect.y = random.randint(0, SCREEN_HEIGHT)
        elif area == "right":
            self.rect.x = SCREEN_WIDTH - 1
            self.rect.y = random.randint(0, SCREEN_HEIGHT)
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
        self.rect_x_float += math.sin(math.radians(self.angle)) * self.movement_speed * TIMER.DELTA_TIME
        self.rect_y_float += math.cos(math.radians(self.angle)) * self.movement_speed * TIMER.DELTA_TIME
        self.rect.x = round(self.rect_x_float)
        self.rect.y = round(self.rect_y_float)

    def move_target(self, player: Player) -> None:
        rel_x: int = self.rect.centerx - player.rect.centerx
        rel_y: int = self.rect.centery - player.rect.centery
        self.angle = (180 / math.pi) * math.atan2(rel_x, rel_y)
        self.rect_x_float -= math.sin(math.radians(self.angle)) * self.movement_speed * TIMER.DELTA_TIME
        self.rect_y_float -= math.cos(math.radians(self.angle)) * self.movement_speed * TIMER.DELTA_TIME
        self.rect.x = round(self.rect_x_float)
        self.rect.y = round(self.rect_y_float)

    def constraints(self) -> None:
        # Kill enemy if goes off screen
        if self.rect.x - self.rect.width > SCREEN_WIDTH:
            self.kill()
        if self.rect.x + self.rect.width < 0:
            self.kill()
        if self.rect.y - self.rect.height > SCREEN_HEIGHT:
            self.kill()
        if self.rect.y + self.rect.height < 0:
            self.kill()
    
    def destroy(self) -> None:
        self.destroyed = True
    
    def spawn(self) -> List[Enemy]:
        return []
    
    def damage(self) -> None:
        if self.damaged:
            self.tint(RED)
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
        super().__init__(image=os.path.join(paths.SPRITES, "enemy_purple.png"),
                         height=scale_to_resolution(72),
                         health=10,
                         body_damage=10,
                         bullet_damage=None,
                         bullet_speed=None,
                         bullet_lifetime=None,
                         reload_time=None,
                         movement_speed=1,
                         movement_cooldown=30,
                         movement_pattern="move_random",
                         damaged_time=150,
                         score=10)

class EnemyRed(Enemy):
    def __init__(self) -> None:
        super().__init__(image=os.path.join(paths.SPRITES, "enemy_red.png"),
                         height=scale_to_resolution(96),
                         health=20,
                         body_damage=10,
                         bullet_damage=5,
                         bullet_speed=1,
                         bullet_lifetime=600,
                         reload_time=3000,
                         movement_speed=1,
                         movement_cooldown=30,
                         movement_pattern="move_target",
                         damaged_time=150,
                         score=10)
        
class EnemyGreen(Enemy):
    BABY_AMOUNT: int = 6
    BABY_SPAWN_RADIUS: int = scale_to_resolution(100)

    def __init__(self) -> None:
        super().__init__(image=os.path.join(paths.SPRITES, "enemy_green.png"),
                         height=scale_to_resolution(104),
                         health=50,
                         body_damage=50,
                         bullet_damage=None,
                         bullet_speed=None,
                         bullet_lifetime=None,
                         reload_time=None,
                         movement_speed=1,
                         movement_cooldown=120,
                         movement_pattern="move_target",
                         damaged_time=150,
                         score=10)
        
    def spawn(self) -> List[Enemy]:
        enemies: List[Enemy] = []
        for _ in range(EnemyGreen.BABY_AMOUNT):
            new_enemy: Enemy = EnemyGreenBaby()
            new_enemy.rect_x_float = self.rect.centerx + random.randint(-EnemyGreen.BABY_SPAWN_RADIUS, EnemyGreen.BABY_SPAWN_RADIUS)
            new_enemy.rect_y_float = self.rect.centery + random.randint(-EnemyGreen.BABY_SPAWN_RADIUS, EnemyGreen.BABY_SPAWN_RADIUS)
            enemies.append(new_enemy)
        return enemies

class EnemyGreenBaby(Enemy):
    def __init__(self) -> None:
        super().__init__(image=os.path.join(paths.SPRITES, "enemy_green_baby.png"),
                         height=scale_to_resolution(36),
                         health=5,
                         body_damage=5,
                         bullet_damage=None,
                         bullet_speed=None,
                         bullet_lifetime=None,
                         reload_time=None,
                         movement_speed=1,
                         movement_cooldown=120,
                         movement_pattern="move_random",
                         damaged_time=150,
                         score=5)
        
class EnemyYellow(Enemy):
    def __init__(self) -> None:
        super().__init__(image=os.path.join(paths.SPRITES, "enemy_yellow.png"),
                            height=scale_to_resolution(76),
                            health=10,
                            body_damage=10,
                            bullet_damage=None,
                            bullet_speed=None,
                            bullet_lifetime=None,
                            reload_time=None,
                            movement_speed=5,
                            movement_cooldown=30,
                            movement_pattern="move_target",
                            damaged_time=150,
                            score=20)
