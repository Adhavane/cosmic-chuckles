#!/usr/bin/env python3

"""background.py: Background class."""

import pygame

from settings import *
settings = Settings()

import random
import math

class Background(pygame.sprite.Sprite):
    def __init__(self) -> None:
        super().__init__()
        
        self.image = pygame.image.load(settings.BG_IMG).convert()
        self.rect = self.image.get_rect()
        self.rect.center = (settings.WIDTH / 2, settings.HEIGHT / 2)

        scale = max(settings.BG_WIDTH / self.rect.width, settings.BG_HEIGHT / self.rect.height)
        self.image = pygame.transform.scale(self.image, (int(self.rect.width * scale), int(self.rect.height * scale)))

        self.rect = self.image.get_rect()
        self.rect.center = (settings.WIDTH / 2, settings.HEIGHT / 2)

        # Set up random movement
        self.moving_random = True
        self.moving_timer_keys = 0
        self.moving_timer_random = 0
        self.moving_timer_direction = 0
        self.moving_cooldown = random.randint(settings.BG_TIME_MIN, settings.BG_TIME_MAX)
        self.moving_direction = random.randint(settings.BG_ANGLE_MIN, settings.BG_ANGLE_MAX)

    def update(self) -> None:
        self.move_keys()
        self.move_random()
        self.constraints()

    def constraints(self) -> None:
        # Keep background on screen
        if self.rect.left > 0:
            self.rect.left = 0
            self.new_moving_direction()
        if self.rect.right < settings.WIDTH:
            self.rect.right = settings.WIDTH
            self.new_moving_direction()
        if self.rect.top > 0:
            self.rect.top = 0
            self.new_moving_direction()
        if self.rect.bottom < settings.HEIGHT:
            self.rect.bottom = settings.HEIGHT
            self.new_moving_direction()

    def move_keys(self) -> None:
        # Move background with keys
        current_time = pygame.time.get_ticks()
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
            self.moving_random = True

    def move_random(self) -> None:
        # Move background randomly
        current_time = pygame.time.get_ticks()
        if current_time - self.moving_timer_random > settings.BG_DELTA_RANDOM:
            self.rect.x += settings.BG_SPEED_RANDOM * math.cos(math.radians(self.moving_direction))
            self.rect.y += settings.BG_SPEED_RANDOM * math.sin(math.radians(self.moving_direction))
            self.moving_timer_random = pygame.time.get_ticks()

        # Set up cooldown
        if current_time - self.moving_timer_direction > self.moving_cooldown:
            self.new_moving_direction()
        self.moving_random = False

    def new_moving_direction(self) -> None:
        self.moving_timer_direction = pygame.time.get_ticks()
        self.moving_cooldown = random.randint(settings.BG_TIME_MIN, settings.BG_TIME_MAX)
        self.moving_direction = random.randint(settings.BG_ANGLE_MIN, settings.BG_ANGLE_MAX)

    def draw(self, screen) -> None:
        screen.blit(self.image, self.rect)