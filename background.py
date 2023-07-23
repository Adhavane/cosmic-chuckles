#!/usr/bin/env python

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

        # Set up random movement
        self.moving_random = True
        self.moving_speed = 0
        self.moving_random_speed = 0
        self.moving_random_timer = 0
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
        if current_time - self.moving_speed > settings.BG_SPEED_KEYS:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_UP]:
                self.rect.y += 1
            if keys[pygame.K_DOWN]:
                self.rect.y -= 1
            if keys[pygame.K_LEFT]:
                self.rect.x += 1
            if keys[pygame.K_RIGHT]:
                self.rect.x -= 1
            self.moving_speed = pygame.time.get_ticks()
            self.moving_random = True

    def move_random(self) -> None:
        # Move background randomly
        current_time = pygame.time.get_ticks()
        if current_time - self.moving_random_speed > settings.BG_SPEED_RANDOM:
            self.rect.x += math.cos(math.radians(self.moving_direction))
            self.rect.y += math.sin(math.radians(self.moving_direction))
            self.moving_random_speed = pygame.time.get_ticks()
        
        # Set up cooldown
        current_time = pygame.time.get_ticks()
        if current_time - self.moving_random_timer > self.moving_cooldown:
            self.new_moving_direction()
        self.moving_random = False
    
    def new_moving_direction(self) -> None:
        self.moving_random_timer = pygame.time.get_ticks()
        self.moving_cooldown = random.randint(settings.BG_TIME_MIN, settings.BG_TIME_MAX)
        self.moving_direction = random.randint(settings.BG_ANGLE_MIN, settings.BG_ANGLE_MAX)

    def draw(self, screen) -> None:
        screen.blit(self.image, self.rect)
