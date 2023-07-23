#!/usr/bin/env python

"""settings.py: Settings for the game."""

import pygame

class Settings:
    def __init__(self) -> None:
        # Screen settings
        # format 4:3
        self.WIDTH = 1380
        self.HEIGHT = 1024
        self.FPS = 60

        self.TITLE = "Cosmic Chuckles - Python/Pygame"
        self.ICON = "assets/icon.png"

        # Colors
        self.WHITE = (255, 255, 255)
        self.BLACK = (0, 0, 0)
        self.RED = (255, 0, 0)
        self.GREEN = (0, 255, 0)
        self.BLUE = (0, 0, 255)

        # Background settings
        self.BG_IMG = "assets/background.png"

        # x pixels per T frames
        self.BG_SPEED_KEYS = 2
        self.BG_SPEED_RANDOM = 1
        self.BG_DELTA_KEYS = 10
        self.BG_DELTA_RANDOM = 30

        self.BG_TIME_MIN = 5000
        self.BG_TIME_MAX = 10000
        self.BG_ANGLE_MIN = 0
        self.BG_ANGLE_MAX = 360

        # Cloud settings
        self.CLOUD_IMGS = ["assets/cloud_0.png",
                           "assets/cloud_1.png",
                            "assets/cloud_2.png",
                            "assets/cloud_3.png",
                            "assets/cloud_4.png"]
        self.CLOUD_HEIGHT_MIN = 30
        self.CLOUD_HEIGHT_MAX = 200
        self.CLOUD_SPEED_MIN = 1
        self.CLOUD_SPEED_MAX = 3
        self.OPACITY_MIN = 16
        self.OPACITY_MAX = 128
        self.CLOUD_SPAWN_RATE = 60

        # Player settings
        self.PLAYER_IMG = "assets/player.png"
        self.PLAYER_HEIGHT = 176
        self.PLAYER_HEALTH = 100
        self.PLAYER_REGEN = 1
        self.PLAYER_BULLET_DAMAGE = 10
        self.PLAYER_BULLET_SPEED = 10
        self.PLAYER_BULLET_LIFETIME = 1000
        self.PLAYER_RELOAD_TIME = 600
        self.PLAYER_MOVEMENT_SPEED = 5

        # Bullet settings
        self.BULLET_PLAYER_IMG = "assets/bullet_player.png"
        self.BULLET_ENEMY_IMG = "assets/bullet_enemy.png"
        self.BULLET_HEIGHT = 64
