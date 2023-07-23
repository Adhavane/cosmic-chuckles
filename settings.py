#!/usr/bin/env python

"""settings.py: Settings for the game."""

import pygame

class Settings:
    def __init__(self) -> None:
        # Screen settings
        self.WIDTH = 1280
        self.HEIGHT = 720
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
        self.BG_SPEED_KEY = 6
        self.BG_SPEED_RANDOM = 1
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
        self.PLAYER_HEIGHT = 144
        self.HEALTH = 100
        self.REGEN = 1
        self.BULLET_DAMAGE = 10
        self.BULLET_SPEED = 10
        self.RELOAD_TIME = 100
        self.MOVEMENT_SPEED = 5
