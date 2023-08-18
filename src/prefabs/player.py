#!/usr/bin/env python3

"""player.py: Player class."""

import pygame
import math
from typing import Tuple, Optional

import paths
from constants import \
    SCREEN_WIDTH, SCREEN_HEIGHT, DELTA_TIME, RED
from utils import scale_to_resolution

from src.prefabs.projectile import BulletPlayer

class Player(pygame.sprite.Sprite):
    IMG: str = paths.IMAGES + "/player.png"
    HEIGHT: int = scale_to_resolution(64)
    
    HEALTH: int = 100
    REGEN_TIME: int = 1000
    REGEN_AMOUNT: int = 1
    BULLET_DAMAGE: int = 10
    BULLET_SPEED: int = 4
    BULLET_LIFETIME: int = 100
    RELOAD_TIME: int = 400
    MOVEMENT_SPEED: int = 5
    DAMAGED_TIME: int = 1000

    def __init__(self) -> None:
        super().__init__()

        self.original_image: pygame.Surface = pygame.image.load(Player.IMG).convert_alpha()
        
        scale: float = Player.HEIGHT / self.original_image.get_height()
        width: int = round(self.original_image.get_width() * scale)
        height: int = round(self.original_image.get_height() * scale)
        self.original_image = pygame.transform.scale(self.original_image, (width, height))
        self.image: pygame.Surface = self.original_image.copy()

        self.rect: pygame.Rect = self.image.get_rect()
        self.rect.center = (round(SCREEN_WIDTH / 2), round(SCREEN_HEIGHT / 2))

        self.mask: pygame.mask.Mask = pygame.mask.from_surface(self.image)

        self.health: int = Player.HEALTH
        self.max_health: int = Player.HEALTH
        self.bullet_damage: int = Player.BULLET_DAMAGE
        self.bullet_speed: int = Player.BULLET_SPEED
        self.bullet_lifetime: int = Player.BULLET_LIFETIME
        self.movement_speed: int = Player.MOVEMENT_SPEED
        self.damaged_time: int = Player.DAMAGED_TIME

        self.angle: float
        self.rotate()

        # Set up shooting
        self.can_shoot: bool = True
        self.shoot_timer: int = 0
        self.shoot_cooldown: int = Player.RELOAD_TIME
        self.bullets: pygame.sprite.Group[BulletPlayer] = pygame.sprite.Group()

        # Set up regen
        self.regen_timer: int = 0
        self.regen_cooldown: int = Player.REGEN_TIME
        self.regen_amount: int = Player.REGEN_AMOUNT
        
        self.damaged: bool = False
        self.damaged_timer: int = 0
        self.damaged_cooldown: int = self.damaged_time

    def update(self) -> None:
        self.regenerate()
        self.move()
        self.rotate()
        self.constraints()
        self.shoot()
        self.damage()

    def regenerate(self) -> None:
        # Regenerate health
        if self.health < self.max_health:
            current_time: int = pygame.time.get_ticks()
            if current_time - self.regen_timer >= self.regen_cooldown:
                self.health += self.regen_amount
                self.regen_timer = pygame.time.get_ticks()

    def move(self) -> None:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.rect.y -= round(self.movement_speed * DELTA_TIME)
        if keys[pygame.K_DOWN]:
            self.rect.y += round(self.movement_speed * DELTA_TIME)
        if keys[pygame.K_LEFT]:
            self.rect.x -= round(self.movement_speed * DELTA_TIME)
        if keys[pygame.K_RIGHT]:
            self.rect.x += round(self.movement_speed * DELTA_TIME)

    def rotate(self) -> None:
        mouse_x: int = pygame.mouse.get_pos()[0]
        mouse_y: int = pygame.mouse.get_pos()[1]
        rel_x: int = self.rect.centerx - mouse_x
        rel_y: int = self.rect.centery - mouse_y
        self.angle = (180 / math.pi) * math.atan2(rel_x, rel_y)
        self.image = pygame.transform.rotate(self.original_image, self.angle)
        self.rect = self.image.get_rect(center=self.rect.center)

    def constraints(self) -> None:
        # Keep player on screen
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT

    def shoot(self) -> None:
        if self.can_shoot:
            keys: pygame.key.ScancodeWrapper = pygame.key.get_pressed()
            if (pygame.mouse.get_pressed()[0] or keys[pygame.K_SPACE]) and self.can_shoot:
                # Shoot bullet
                self.bullets.add(BulletPlayer(self.rect.centerx,
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
        # Reload weapon
        if not self.can_shoot:
            current_time: int = pygame.time.get_ticks()
            if current_time - self.shoot_timer >= self.shoot_cooldown:
                self.can_shoot = True

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
