#!/usr/bin/env python

"""background.py: Background class."""

import pygame

from settings import *
settings = Settings()

import random
import math

class Background:
    def __init__(self) -> None:
        self.image = pygame.image.load(settings.BG_IMG).convert()
        self.rect = self.image.get_rect()
        self.rect.center = (settings.WIDTH / 2, settings.HEIGHT / 2)

        # Set up random movement
        self.moving_random = False
        self.moving_timer = 0
        self.moving_cooldown = random.randint(settings.BG_TIME_MIN, settings.BG_TIME_MAX)
        self.moving_direction = random.randint(settings.BG_ANGLE_MIN, settings.BG_ANGLE_MAX)

    def update(self) -> None:
        if self.moving_random:
            self.move_random()
        else:
            self.move_keys()
        self.constraints()

    def constraints(self) -> None:
        # Keep background on screen
        if self.rect.x < 0:
            self.rect.x = 0
        if self.rect.x > settings.WIDTH - self.rect.width:
            self.rect.x = settings.WIDTH - self.rect.width
        if self.rect.y < 0:
            self.rect.y = 0
        if self.rect.y > settings.HEIGHT - self.rect.height:
            self.rect.y = settings.HEIGHT - self.rect.height

    def move_keys(self) -> None:
        # Move background with keys
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.rect.y += settings.BG_SPEED
        if keys[pygame.K_DOWN]:
            self.rect.y -= settings.BG_SPEED
        if keys[pygame.K_LEFT]:
            self.rect.x += settings.BG_SPEED
        if keys[pygame.K_RIGHT]:
            self.rect.x -= settings.BG_SPEED

        print(self.rect.x, self.rect.y)

    def move_random(self) -> None:
        # Move background randomly
        self.rect.x += settings.BG_SPEED * math.cos(math.radians(self.moving_direction))
        self.rect.y += settings.BG_SPEED * math.sin(math.radians(self.moving_direction))
        
        # Set up cooldown
        current_time = pygame.time.get_ticks()
        if current_time - self.moving_timer > self.moving_cooldown:
            self.moving_timer = current_time
            self.moving_cooldown = random.randint(settings.BG_TIME_MIN, settings.BG_TIME_MAX)
            self.moving_direction = random.randint(settings.BG_ANGLE_MIN, settings.BG_ANGLE_MAX)

    def draw(self, screen) -> None:
        screen.blit(self.image, self.rect)
