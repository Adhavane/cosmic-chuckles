#!/usr/bin/env python3

"""settings.py: Settings for the game."""

import time
import pygame

LAST_TIME = time.time()
DELTA_TIME = 0

# Screen settings for format 4:3
SCALE_FACTOR = 2
SCREEN_WIDTH = 690 * SCALE_FACTOR
SCREEN_HEIGHT = 512 * SCALE_FACTOR

FPS = 60

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0 , 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

OPAQUE = 255
SEMI_OPAQUE = 192
TRANSLUCENT = 128
SEMI_TRANSLUCENT = 64
TRANSPARENT = 0

class Settings:
    def __init__(self) -> None:

        self.TRANSITION_TIME = 1000

        self.CLOUD_INIT = 5

        # Bullet settings
        self.BULLET_PLAYER_IMG = "assets/sprites/bullet_player.png"
        self.BULLET_PLAYER_HEIGHT = 32 * self.SCALE_FACTOR
        
        self.BULLET_ENEMY_IMG = "assets/sprites/bullet_enemy.png"
        self.BULLET_ENEMY_HEIGHT = 32 * self.SCALE_FACTOR

        # Enemy settings
        self.ENEMY_TIME_MIN = 1000
        self.ENEMY_TIME_MAX = 2000
