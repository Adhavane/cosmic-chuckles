#!/usr/bin/env python3

"""background.py: Background class."""

import pygame
import random
import math

from src.settings import Settings
settings = Settings()

class Background(pygame.sprite.Sprite):
    def __init__(self) -> None:
        super().__init__()

        width: int
        height: int
        
        self.image: pygame.Surface = pygame.image.load(settings.BG_IMG).convert_alpha()
        self.rect: pygame.Rect = self.image.get_rect()
        self.rect.center = (int(settings.SCREEN_WIDTH / 2), int(settings.SCREEN_HEIGHT / 2))

        scale: float = max(settings.BG_WIDTH / self.rect.width, settings.BG_HEIGHT / self.rect.height)
        width = int(self.rect.width * scale)
        height = int(self.rect.height * scale)
        self.image = pygame.transform.scale(self.image, (width, height))

        self.rect = self.image.get_rect()
        width = int(settings.SCREEN_WIDTH / 2)
        height = int(settings.SCREEN_HEIGHT / 2)
        self.rect.center = (width, height)

        # Set up random movement
        self.moving_random: bool = True
        self.moving_timer_keys: int = 0
        self.moving_timer_random: int = 0
        self.moving_timer_direction: int = 0
        self.moving_cooldown: int = random.randint(settings.BG_TIME_MIN, settings.BG_TIME_MAX)
        self.moving_direction: float = random.uniform(settings.BG_ANGLE_MIN, settings.BG_ANGLE_MAX)
        
    def update(self) -> None:
        self.move_keys()
        if self.moving_random:
            self.move_random()
        self.constraints()

    def constraints(self) -> None:
        # Keep background on screen
        if self.rect.left > 0:
            self.rect.left = 0
            self.new_moving_direction()
        if self.rect.right < settings.SCREEN_WIDTH:
            self.rect.right = settings.SCREEN_WIDTH
            self.new_moving_direction()
        if self.rect.top > 0:
            self.rect.top = 0
            self.new_moving_direction()
        if self.rect.bottom < settings.SCREEN_HEIGHT:
            self.rect.bottom = settings.SCREEN_HEIGHT
            self.new_moving_direction()

    def move_keys(self) -> None:
        # Move background with keys
        current_time: int = pygame.time.get_ticks()
        if current_time - self.moving_timer_keys > settings.BG_DELTA_KEYS:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_UP]:
                self.rect.y += settings.BG_SPEED_KEYS
            if keys[pygame.K_DOWN]:
                self.rect.y -= settings.BG_SPEED_KEYS
            if keys[pygame.K_LEFT]:
                self.rect.x += settings.BG_SPEED_KEYS
            if keys[pygame.K_RIGHT]:
                self.rect.x -= settings.BG_SPEED_KEYS
            self.moving_timer_keys = pygame.time.get_ticks()

    def move_random(self) -> None:
        # Move background randomly
        current_time: int = pygame.time.get_ticks()
        if current_time - self.moving_timer_random > settings.BG_DELTA_RANDOM:
            self.rect.x += round(settings.BG_SPEED_RANDOM * math.cos(math.radians(self.moving_direction)))
            self.rect.y += round(settings.BG_SPEED_RANDOM * math.sin(math.radians(self.moving_direction)))
            self.moving_timer_random = pygame.time.get_ticks()

        # Set up cooldown
        if current_time - self.moving_timer_direction > self.moving_cooldown:
            self.new_moving_direction()

    def new_moving_direction(self) -> None:
        self.moving_timer_direction = pygame.time.get_ticks()
        self.moving_cooldown = random.randint(settings.BG_TIME_MIN, settings.BG_TIME_MAX)
        self.moving_direction = random.uniform(settings.BG_ANGLE_MIN, settings.BG_ANGLE_MAX)

    def draw(self, screen) -> None:
        screen.blit(self.image, self.rect)
