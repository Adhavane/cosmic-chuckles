#!/usr/bin/env python

"""player.py: Player class."""

import pygame
import math

from settings import *
settings = Settings()

from projectile import BulletPlayer

class Player(pygame.sprite.Sprite):
    def __init__(self,
                 health: int = settings.PLAYER_HEALTH,
                 regen: int = settings.PLAYER_REGEN,
                 bullet_damage: int = settings.PLAYER_BULLET_DAMAGE,
                 bullet_speed: int = settings.PLAYER_BULLET_SPEED,
                 bullet_lifetime: int = settings.PLAYER_BULLET_LIFETIME,
                 reload_time: int = settings.PLAYER_RELOAD_TIME,
                 movement_speed: int = settings.PLAYER_MOVEMENT_SPEED) -> None:
        super().__init__()

        self.original_image = pygame.image.load(settings.PLAYER_IMG).convert_alpha()
        
        scale = settings.PLAYER_HEIGHT / self.original_image.get_height()
        self.original_image = pygame.transform.scale(self.original_image, (int(self.original_image.get_width() * scale), int(self.original_image.get_height() * scale)))
        self.image = self.original_image.copy()

        self.rect = self.image.get_rect()
        self.rect.center = (settings.WIDTH / 2, settings.HEIGHT / 2)

        self.health = health
        self.regen = regen
        self.bullet_damage = bullet_damage
        self.bullet_speed = bullet_speed
        self.bullet_lifetime = bullet_lifetime
        self.reload_time = reload_time
        self.movement_speed = movement_speed

        self.angle = 0

        # Set up shooting
        self.can_shoot = True
        self.shoot_timer = 0
        self.shoot_cooldown = self.reload_time
        self.bullets = pygame.sprite.Group()

    def update(self) -> None:
        self.move()
        self.rotate()
        self.constraints()
        self.shoot()

    def move(self) -> None:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.rect.y -= self.movement_speed
        if keys[pygame.K_DOWN]:
            self.rect.y += self.movement_speed
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.movement_speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.movement_speed

    def rotate(self) -> None:
        mouse_x, mouse_y = pygame.mouse.get_pos()
        rel_x, rel_y = self.rect.centerx - mouse_x, self.rect.centery - mouse_y
        self.angle = (180 / math.pi) * math.atan2(rel_x, rel_y)
        self.image = pygame.transform.rotate(self.original_image, int(self.angle))
        self.rect = self.image.get_rect(center=self.rect.center)

    def constraints(self) -> None:
        # Keep player on screen
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > settings.WIDTH:
            self.rect.right = settings.WIDTH
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > settings.HEIGHT:
            self.rect.bottom = settings.HEIGHT

    def shoot(self) -> None:
        keys = pygame.key.get_pressed()
        if (pygame.mouse.get_pressed()[0] or keys[pygame.K_SPACE]) and self.can_shoot:
            # Shoot bullet
            pos_x = self.rect.centerx
            pos_y = self.rect.centery
            self.bullets.add(BulletPlayer(pos_x, pos_y, self.angle, self.bullet_speed, self.bullet_damage, self.bullet_lifetime))

            self.can_shoot = False
            self.shoot_timer = pygame.time.get_ticks()
        self.reload()
        self.bullets.update()

    def reload(self) -> None:
        # Reload weapon
        if not self.can_shoot:
            current_time = pygame.time.get_ticks()
            if current_time - self.shoot_timer >= self.shoot_cooldown:
                self.can_shoot = True

    def draw(self, screen) -> None:
        self.bullets.draw(screen)
        screen.blit(self.image, self.rect)
