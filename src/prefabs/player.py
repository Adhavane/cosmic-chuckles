#!/usr/bin/env python3

"""player.py: Player class."""

import pygame
import math

from src.settings import Settings
settings = Settings()

from src.prefabs.projectile import BulletPlayer

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

        self.original_image: pygame.Surface = pygame.image.load(settings.PLAYER_IMG).convert_alpha()
        
        scale: float = settings.PLAYER_HEIGHT / self.original_image.get_height()
        width: int = round(self.original_image.get_width() * scale)
        height: int = round(self.original_image.get_height() * scale)
        self.original_image = pygame.transform.scale(self.original_image, (width, height))
        self.image: pygame.Surface = self.original_image.copy()

        self.rect: pygame.Rect = self.image.get_rect()
        self.rect.center = (round(settings.SCREEN_WIDTH / 2), round(settings.SCREEN_HEIGHT / 2))

        self.mask: pygame.mask.Mask = pygame.mask.from_surface(self.image)

        self.health: int = health
        self.max_health: int = health
        self.regen: int = regen
        self.bullet_damage: int = bullet_damage
        self.bullet_speed: int = bullet_speed
        self.bullet_lifetime: int = bullet_lifetime
        self.reload_time: int = reload_time
        self.movement_speed: int = movement_speed

        self.angle: float
        self.rotate()

        # Set up shooting
        self.can_shoot: bool = True
        self.shoot_timer: int = 0
        self.shoot_cooldown: int = self.reload_time
        self.bullets: pygame.sprite.Group[BulletPlayer] = pygame.sprite.Group()

        self.damaged: bool = False
        self.damaged_timer: int = 0
        self.damaged_cooldown: int = 100

    def update(self) -> None:
        self.move()
        self.rotate()
        self.constraints()
        self.shoot()

    def move(self) -> None:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.rect.y -= round(self.movement_speed * Settings.DELTA_TIME)
        if keys[pygame.K_DOWN]:
            self.rect.y += round(self.movement_speed * Settings.DELTA_TIME)
        if keys[pygame.K_LEFT]:
            self.rect.x -= round(self.movement_speed * Settings.DELTA_TIME)
        if keys[pygame.K_RIGHT]:
            self.rect.x += round(self.movement_speed * Settings.DELTA_TIME)

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
        if self.rect.right > settings.SCREEN_WIDTH:
            self.rect.right = settings.SCREEN_WIDTH
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > settings.SCREEN_HEIGHT:
            self.rect.bottom = settings.SCREEN_HEIGHT

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

    def take_damage(self, damage: int) -> None:
        self.health -= damage
        self.damaged = True
        self.tint()

    def tint(self) -> None:
        if self.damaged:
            self.image.fill((255, 0, 0, 100), special_flags=pygame.BLEND_RGBA_MULT)
            self.damaged_timer = pygame.time.get_ticks()
            self.damaged = False

    def draw(self, display) -> None:
        self.bullets.draw(display)
        display.blit(self.image, self.rect)
