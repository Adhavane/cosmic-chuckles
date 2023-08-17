#!/usr/bin/env python3

"""background.py: Background class."""

import pygame
import random
import math

import paths
from constants import \
    SCREEN_WIDTH, SCREEN_HEIGHT, DELTA_TIME
from utils import scale_to_resolution

class Background(pygame.sprite.Sprite):
    # Background settings
    IMG: str = paths.IMAGES + "/background.png"
    WIDTH: int = scale_to_resolution(960)
    HEIGHT: int = scale_to_resolution(640)

    SPEED_KEYS: int = 2
    DELTA_KEYS: int = 10

    SPEED_RANDOM: int = 1
    DELTA_RANDOM: int = 30

    TIME_MIN: int = 5000
    TIME_MAX: int = 10000

    ANGLE_MIN: int = 0
    ANGLE_MAX: int = 360

    def __init__(self) -> None:
        super().__init__()

        width: int
        height: int
        
        self.image: pygame.Surface = pygame.image.load(Background.IMG).convert_alpha()
        self.rect: pygame.Rect = self.image.get_rect()
        self.rect.center = (round(SCREEN_WIDTH / 2), round(SCREEN_HEIGHT / 2))

        scale: float = max(Background.WIDTH / self.rect.width, Background.HEIGHT / self.rect.height)
        width = round(self.rect.width * scale)
        height = round(self.rect.height * scale)
        self.image = pygame.transform.scale(self.image, (width, height))

        self.rect = self.image.get_rect()
        width = round(SCREEN_WIDTH / 2)
        height = round(SCREEN_HEIGHT / 2)
        self.rect.center = (width, height)

        # Set up random movement
        self.moving_random: bool = True
        self.moving_timer_keys: int = 0
        self.moving_timer_random: int = 0
        self.moving_timer_direction: int = 0
        self.moving_cooldown: int = random.randint(Background.TIME_MIN, Background.TIME_MAX)
        self.moving_direction: float = random.uniform(Background.ANGLE_MIN, Background.ANGLE_MAX)
        
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
        if self.rect.right < SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
            self.new_moving_direction()
        if self.rect.top > 0:
            self.rect.top = 0
            self.new_moving_direction()
        if self.rect.bottom < SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT
            self.new_moving_direction()

    def move_keys(self) -> None:
        # Move background with keys
        current_time: int = pygame.time.get_ticks()
        if current_time - self.moving_timer_keys > Background.DELTA_KEYS:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_UP]:
                self.rect.y += round(Background.SPEED_KEYS * DELTA_TIME)
            if keys[pygame.K_DOWN]:
                self.rect.y -= round(Background.SPEED_KEYS * DELTA_TIME)
            if keys[pygame.K_LEFT]:
                self.rect.x += round(Background.SPEED_KEYS * DELTA_TIME)
            if keys[pygame.K_RIGHT]:
                self.rect.x -= round(Background.SPEED_KEYS * DELTA_TIME)
            self.moving_timer_keys = pygame.time.get_ticks()

    def move_random(self) -> None:
        # Move background randomly
        current_time: int = pygame.time.get_ticks()
        if current_time - self.moving_timer_random > Background.DELTA_RANDOM:
            self.rect.x += round(Background.SPEED_RANDOM * math.cos(math.radians(self.moving_direction)) * DELTA_TIME)
            self.rect.y += round(Background.SPEED_RANDOM * math.sin(math.radians(self.moving_direction)) * DELTA_TIME)
            self.moving_timer_random = pygame.time.get_ticks()

        # Set up cooldown
        if current_time - self.moving_timer_direction > self.moving_cooldown:
            self.new_moving_direction()

    def new_moving_direction(self) -> None:
        self.moving_timer_direction = pygame.time.get_ticks()
        self.moving_cooldown = random.randint(Background.TIME_MIN, Background.TIME_MAX)
        self.moving_direction = random.uniform(Background.ANGLE_MIN, Background.ANGLE_MAX)

    def draw(self, display) -> None:
        display.blit(self.image, self.rect)
