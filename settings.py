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
        self.BG_IMG = "assets/background_4.png"
        self.BG_WIDTH = 1380 * 1.25
        self.BG_HEIGHT = 1024 * 1.25

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
                            # "assets/cloud_2.png",
                            "assets/cloud_3.png",
                            # "assets/cloud_4.png",
                            "assets/cloud_5.png"]
        self.CLOUD_INIT = 5
        self.CLOUD_HEIGHT_MIN = 50
        self.CLOUD_HEIGHT_MAX = 400
        self.CLOUD_SPEED_MIN = 1
        self.CLOUD_SPEED_MAX = 3
        self.CLOUD_DELTA = 30
        self.OPACITY_MIN = 8
        self.OPACITY_MAX = 64
        self.CLOUD_TIME_MIN = 1000
        self.CLOUD_TIME_MAX = 2000

        # Title settings
        self.TITLE_IMG = "assets/title.png"
        self.TITLE_Y = 74 * 2
        self.TITLE_HEIGHT = 42 * 10

        # Credit settings
        self.CREDIT_IMG = "assets/credit.png"
        self.CREDIT_Y = 288 * 2
        self.CREDIT_HEIGHT = 8 * 2

        # Start button settings
        self.PLAY_IMGS = {"selected": "assets/play_selected.png",
                          "unselected": "assets/play_unselected.png"}
        self.PLAY_Y = 326 * 2
        self.PLAY_HEIGHT = 9 * 8
        self.PLAY_OPACITY = {"selected": 255,
                             "unselected": 64}

        # Quit button settings
        self.QUIT_IMGS = {"selected": "assets/quit_selected.png",
                          "unselected": "assets/quit_unselected.png"}
        self.QUIT_Y = 383 * 2
        self.QUIT_HEIGHT = 10 * 8
        self.QUIT_OPACITY = {"selected": 255,
                             "unselected": 64}
        
        # Score settings
        self.SCORE_X = 12 * 2
        self.SCORE_Y = 12 * 2
        self.SCORE_FONT = "assets/SUPERNAT1001.TTF"
        self.SCORE_SIZE = 24 * 2

        # Particle settings
        self.PARTICLE_IMG = "assets/particle.png"
        self.PARTICLE_HEIGHT = 2 * 2

        # Player settings
        self.PLAYER_IMG = "assets/player_bis.png"
        self.PLAYER_HEIGHT = 32 * 4
        self.PLAYER_HEALTH = 100
        self.PLAYER_REGEN = 1
        self.PLAYER_BULLET_DAMAGE = 10
        self.PLAYER_BULLET_SPEED = 2
        self.PLAYER_BULLET_LIFETIME = 1000
        self.PLAYER_RELOAD_TIME = 600
        self.PLAYER_MOVEMENT_SPEED = 5

        # Bullet settings
        self.BULLET_PLAYER_IMG = "assets/bullet_player_bis.png"
        self.BULLET_PLAYER_HEIGHT = 32 * 2
        self.BULLET_ENEMY_IMG = "assets/bullet_enemy.png"
        self.BULLET_ENEMY_HEIGHT = 32 * 2

        # Enemy settings
        self.ENEMY_TIME_MIN = 1000
        self.ENEMY_TIME_MAX = 2000

        self.ENEMY_PURPLE_IMG = "assets/enemy_purple_bis.png"
        self.ENEMY_PURPLE_HEIGHT = 36 * 4
        self.ENEMY_PURPLE_HEALTH = 10
        self.ENEMY_PURPLE_BODY_DAMAGE = 10
        self.ENEMY_PURPLE_BULLET_DAMAGE = None
        self.ENEMY_PURPLE_BULLET_SPEED = None
        self.ENEMY_PURPLE_BULLET_LIFETIME = None
        self.ENEMY_PURPLE_RELOAD_TIME = None
        self.ENEMY_PURPLE_MOVEMENT_SPEED = 1
        self.ENEMY_PURPLE_MOVEMENT_COOLDOWN = 30
        self.ENEMY_PURPLE_MOVEMENT_PATTERN = "move_target"
        self.ENEMY_PURPLE_SCORE = 10
        
        self.ENEMY_RED_IMG = "assets/enemy_red_bis.png"
        
        self.ENEMY_GREEN_IMG = "assets/enemy_green_bis.png"

        self.ENEMY_GREEN_BABY_IMG = "assets/enemy_green_baby_bis.png"


