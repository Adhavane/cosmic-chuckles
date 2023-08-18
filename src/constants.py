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
        
        # Statistics settings
        self.STATISTICS_LABEL_FONT = "assets/fonts/awesome.ttf"
        self.STATISTICS_LABEL_SIZE = round(16.22 * self.SCALE_FACTOR)
        self.STATISTICS_LABEL_X_OFFSET = 10 * self.SCALE_FACTOR
        self.STATISTICS_LABEL_Y_OFFSET = -6 * self.SCALE_FACTOR

        self.STATISTICS_STAT_FONT = "assets/fonts/Pixel Gosub.otf"
        self.STATISTICS_STAT_SIZE = round(27.01 * self.SCALE_FACTOR)
        self.STATISTICS_STAT_X_OFFSET = 10 * self.SCALE_FACTOR
        self.STATISTICS_STAT_Y_OFFSET = -16 * self.SCALE_FACTOR

        # Score settings
        self.COIN_IMG = "assets/sprites/coin.png"
        self.COIN_HEIGHT = 33 * self.SCALE_FACTOR
        
        self.SCORE_X = 24 * self.SCALE_FACTOR
        self.SCORE_Y = 24 * self.SCALE_FACTOR

        # Health settings
        self.HEART_IMG = "assets/sprites/heart.png"
        self.HEART_HEIGHT = 30 * self.SCALE_FACTOR

        self.HEALTH_X = 24 * self.SCALE_FACTOR
        self.HEALTH_Y = 71 * self.SCALE_FACTOR

        # Bullet settings
        self.BULLET_PLAYER_IMG = "assets/sprites/bullet_player.png"
        self.BULLET_PLAYER_HEIGHT = 32 * self.SCALE_FACTOR
        
        self.BULLET_ENEMY_IMG = "assets/sprites/bullet_enemy.png"
        self.BULLET_ENEMY_HEIGHT = 32 * self.SCALE_FACTOR

        # Enemy settings
        self.ENEMY_TIME_MIN = 1000
        self.ENEMY_TIME_MAX = 2000
