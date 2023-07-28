#!/usr/bin/env python3

"""settings.py: Settings for the game."""

class Settings:
    def __init__(self) -> None:
        # Screen settings for format 4:3
        self.SCREEN_WIDTH = 1380
        self.SCREEN_HEIGHT = 1024
        self.FPS = 60

        self.TITLE = "Cosmic Chuckles - Python/Pygame"
        self.ICON = "assets/images/icon.png"

        # Colors
        self.WHITE = (255, 255, 255)
        self.BLACK = (0, 0, 0)
        self.RED = (255, 0, 0)
        self.GREEN = (0, 255, 0)
        self.BLUE = (0, 0, 255)

        # Background settings
        self.BG_IMG = "assets/sprites/pixel_art/background.png"
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
        self.CLOUD_IMGS = ["assets/sprites/pixel_art/cloud_0.png",
                           "assets/sprites/pixel_art/cloud_1.png",
                            # "assets/sprites/pixel_art/cloud_2.png",
                            "assets/sprites/pixel_art/cloud_3.png",
                            # "assets/sprites/pixel_art/cloud_4.png",
                            "assets/sprites/pixel_art/cloud_5.png"]
        self.CLOUD_INIT = 5
        self.CLOUD_HEIGHT_MIN = 50
        self.CLOUD_HEIGHT_MAX = 400
        self.CLOUD_SPEED_MIN = 1
        self.CLOUD_SPEED_MAX = 3
        self.CLOUD_DELTA = 30
        self.CLOUD_OPACITY_MIN = 8
        self.CLOUD_OPACITY_MAX = 64
        self.CLOUD_TIME_MIN = 1000
        self.CLOUD_TIME_MAX = 2000

        # Title settings
        self.TITLE_IMG = "assets/sprites/pixel_art/title.png"
        self.TITLE_Y = 74 * 2
        self.TITLE_HEIGHT = 42 * 10

        # Credit settings
        self.CREDIT_IMG = "assets/sprites/pixel_art/credit.png"
        self.CREDIT_Y = 288 * 2
        self.CREDIT_HEIGHT = 8 * 2

        # Start button settings
        self.PLAY_IMGS = {"selected": "assets/sprites/pixel_art/play_selected.png",
                          "unselected": "assets/sprites/pixel_art/play_unselected.png"}
        self.PLAY_Y = 326 * 2
        self.PLAY_HEIGHT = 9 * 8
        self.PLAY_OPACITY = {"selected": 255,
                             "unselected": 64}

        # Quit button settings
        self.QUIT_IMGS = {"selected": "assets/sprites/pixel_art/quit_selected.png",
                          "unselected": "assets/sprites/pixel_art/quit_unselected.png"}
        self.QUIT_Y = 383 * 2
        self.QUIT_HEIGHT = 10 * 8
        self.QUIT_OPACITY = {"selected": 255,
                             "unselected": 64}
        
        # Score settings
        self.SCORE_X = 12 * 2
        self.SCORE_Y = 12 * 2
        self.SCORE_FONT = "assets/fonts/SUPERNAT1001.TTF"
        self.SCORE_SIZE = 24 * 2

        # Health settings
        self.HEART_IMG = "assets/sprites/pixel_art/heart.png"
        self.HEART_X = 512
        self.HEART_Y = 18 * 2
        self.HEART_HEIGHT = 10 * 4

        self.HEALTH_Y = 12 * 2
        self.HEALTH_FONT = "assets/fonts/SUPERNAT1001.TTF"
        self.HEALTH_SIZE = 24 * 2

        # Particle settings
        self.PARTICLE_IMG = "assets/sprites/pixel_art/particle.png"
        self.PARTICLE_HEIGHT = 2 * 2

        # Player settings
        self.PLAYER_IMG = "assets/sprites/pixel_art/player.png"
        self.PLAYER_HEIGHT = 32 * 4
        self.PLAYER_HEALTH = 100
        self.PLAYER_REGEN = 1
        self.PLAYER_BULLET_DAMAGE = 10
        self.PLAYER_BULLET_SPEED = 2
        self.PLAYER_BULLET_LIFETIME = 1000
        self.PLAYER_RELOAD_TIME = 600
        self.PLAYER_MOVEMENT_SPEED = 5

        # Bullet settings
        self.BULLET_PLAYER_IMG = "assets/sprites/pixel_art/bullet_player.png"
        self.BULLET_PLAYER_HEIGHT = 32 * 2
        self.BULLET_ENEMY_IMG = "assets/sprites/pixel_art/bullet_enemy.png"
        self.BULLET_ENEMY_HEIGHT = 32 * 2

        # Enemy settings
        self.ENEMY_TIME_MIN = 1000
        self.ENEMY_TIME_MAX = 2000

        self.ENEMY_PURPLE_IMG = "assets/sprites/pixel_art/enemy_purple.png"
        self.ENEMY_PURPLE_HEIGHT = 36 * 4
        self.ENEMY_PURPLE_HEALTH = 20
        self.ENEMY_PURPLE_BODY_DAMAGE = 10
        self.ENEMY_PURPLE_BULLET_DAMAGE = None
        self.ENEMY_PURPLE_BULLET_SPEED = None
        self.ENEMY_PURPLE_BULLET_LIFETIME = None
        self.ENEMY_PURPLE_RELOAD_TIME = None
        self.ENEMY_PURPLE_MOVEMENT_SPEED = 1
        self.ENEMY_PURPLE_MOVEMENT_COOLDOWN = 30
        self.ENEMY_PURPLE_MOVEMENT_PATTERN = "move_random"
        self.ENEMY_PURPLE_SCORE = 10
        
        self.ENEMY_RED_IMG = "assets/sprites/pixel_art/enemy_red.png"
        
        self.ENEMY_GREEN_IMG = "assets/sprites/pixel_art/enemy_green.png"

        self.ENEMY_GREEN_BABY_IMG = "assets/sprites/pixel_art/enemy_green_baby.png"
