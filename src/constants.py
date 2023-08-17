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
TRANSLUCENT = 128
TRANSPARENT = 0

class Settings:
    def __init__(self) -> None:
        self.LOADING_IMGS = ["assets/sprites/loading_0.png",
                             "assets/sprites/loading_1.png",
                             "assets/sprites/loading_2.png",
                             "assets/sprites/loading_3.png"]
        self.LOADING_IMG_HEIGHT = 34 * self.SCALE_FACTOR
        self.LOADING_IMG_DELAY = 800
        self.LOADING_TIME = 3000

        self.TRANSITION_TIME = 1000




        self.CLOUD_INIT = 5
        

        # Title settings
        self.TITLE_IMG = "assets/sprites/title.png"
        self.TITLE_Y = 74 * self.SCALE_FACTOR
        self.TITLE_HEIGHT = 210 * self.SCALE_FACTOR

        # Credit settings
        self.CREDIT_IMG = "assets/sprites/credit.png"
        self.CREDIT_Y = 288 * self.SCALE_FACTOR
        self.CREDIT_HEIGHT = 9 * self.SCALE_FACTOR

        self.FPS_X = 613 * self.SCALE_FACTOR
        self.FPS_Y = 488 * self.SCALE_FACTOR
        self.FPS_Y_PADDING = -6
        self.FPS_FONT = "assets/fonts/Pixel Gosub.otf"
        self.FPS_SIZE = round(13.5 * self.SCALE_FACTOR)
        self.FPS_COLOR = (255, 255, 255)
        self.FPS_OPACITY = 64

        # Start button settings
        self.PLAY_IMGS = {"selected": "assets/sprites/play_selected.png",
                          "unselected": "assets/sprites/play_unselected.png"}
        self.PLAY_Y = 326 * self.SCALE_FACTOR
        self.PLAY_HEIGHT = 36 * self.SCALE_FACTOR
        self.PLAY_OPACITY = {"selected": 255,
                             "unselected": 64}

        # Quit button settings
        self.QUIT_IMGS = {"selected": "assets/sprites/quit_selected.png",
                          "unselected": "assets/sprites/quit_unselected.png"}
        self.QUIT_Y = 380 * self.SCALE_FACTOR
        self.QUIT_HEIGHT = 40 * self.SCALE_FACTOR
        self.QUIT_OPACITY = {"selected": 255,
                             "unselected": 64}
        
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

        # Particle settings
        self.PARTICLE_IMG = "assets/sprites/particle.png"
        self.PARTICLE_AMOUNT = 20
        self.PARTICLE_HEIGHT_MIN = 1 * self.SCALE_FACTOR
        self.PARTICLE_HEIGHT_MAX = 6 * self.SCALE_FACTOR
        self.PARTICLE_ANGLE_MIN = 0
        self.PARTICLE_ANGLE_MAX = 360
        self.PARTICLE_DAMAGE_MIN = 0
        self.PARTICLE_DAMAGE_MAX = 0
        self.PARTICLE_SPEED_MIN = 1
        self.PARTICLE_SPEED_MAX = 10
        self.PARTICLE_LIFETIME_MIN = 1
        self.PARTICLE_LIFETIME_MAX = 30

        # Player settings
        self.PLAYER_IMG = "assets/sprites/player.png"
        self.PLAYER_HEIGHT = 64 * self.SCALE_FACTOR
        self.PLAYER_HEALTH = 100
        self.PLAYER_REGEN = 1
        self.PLAYER_BULLET_DAMAGE = 10
        self.PLAYER_BULLET_SPEED = 4
        self.PLAYER_BULLET_LIFETIME = 100
        self.PLAYER_RELOAD_TIME = 400
        self.PLAYER_MOVEMENT_SPEED = 5
        self.PLAYER_DAMAGED_TIME = 150

        # Bullet settings
        self.BULLET_PLAYER_IMG = "assets/sprites/bullet_player.png"
        self.BULLET_PLAYER_HEIGHT = 32 * self.SCALE_FACTOR
        
        self.BULLET_ENEMY_IMG = "assets/sprites/bullet_enemy.png"
        self.BULLET_ENEMY_HEIGHT = 32 * self.SCALE_FACTOR

        # Enemy settings
        self.ENEMY_TIME_MIN = 1000
        self.ENEMY_TIME_MAX = 2000


        self.GAMEOVER_IMG = "assets/sprites/game_over.png"
        self.GAMEOVER_IMG_HEIGHT = 220 * self.SCALE_FACTOR
        self.GAMEOVER_IMG_Y = 71 * self.SCALE_FACTOR

        self.GAMEOVER_SCORE_FONT = "assets/fonts/Pixel Gosub.otf"
        self.GAMEOVER_SCORE_SIZE = round(43.21 * self.SCALE_FACTOR)
        self.GAMEOVER_SCORE_Y_PADDING = -18 * self.SCALE_FACTOR
        self.GAMEOVER_SCORE_Y = 339 * self.SCALE_FACTOR

        self.GAMEOVER_PRESS_FONT = "assets/fonts/Pixel Gosub.otf"
        self.GAMEOVER_PRESS_SIZE = round(14.40 * self.SCALE_FACTOR)
        self.GAMEOVER_PRESS_Y = 466 * self.SCALE_FACTOR
