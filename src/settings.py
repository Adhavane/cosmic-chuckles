#!/usr/bin/env python3

"""settings.py: Settings for the game."""

class Settings:
    def __init__(self) -> None:
        # Screen settings for format 4:3
        self.SCALE_FACTOR = 2

        self.SCREEN_WIDTH = 690 * self.SCALE_FACTOR
        self.SCREEN_HEIGHT = 512 * self.SCALE_FACTOR

        self.FPS = 60

        self.LAST_TIME = 0
        self.DELTA_TIME = 0

        self.TITLE = "Cosmic Chuckles - Python/Pygame"
        self.ICON = "assets/images/icon.png"

        # Colors
        self.WHITE = (255, 255, 255)
        self.BLACK = (0, 0, 0)
        self.RED = (255, 0, 0)
        self.GREEN = (0, 255, 0)
        self.BLUE = (0, 0, 255)

        # Opacity
        self.OPAQUE = 255
        self.TRANSLUCENT = 128
        self.TRANSPARENT = 0

        # Background settings
        self.BG_IMG = "assets/sprites/pixel_art/background.png"
        self.BG_WIDTH = 960 * self.SCALE_FACTOR
        self.BG_HEIGHT = 640 * self.SCALE_FACTOR

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
                            "assets/sprites/pixel_art/cloud_2.png",
                            "assets/sprites/pixel_art/cloud_3.png",
                            "assets/sprites/pixel_art/cloud_4.png",
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
        self.TITLE_Y = 74 * self.SCALE_FACTOR
        self.TITLE_HEIGHT = 210 * self.SCALE_FACTOR

        # Credit settings
        self.CREDIT_IMG = "assets/sprites/pixel_art/credit.png"
        self.CREDIT_Y = 288 * self.SCALE_FACTOR
        self.CREDIT_HEIGHT = 8 * self.SCALE_FACTOR

        self.FPS_X = 613 * self.SCALE_FACTOR
        self.FPS_Y = 488 * self.SCALE_FACTOR
        self.FPS_Y_PADDING = -6
        self.FPS_FONT = "assets/fonts/Pixel Gosub.otf"
        self.FPS_SIZE = round(13.5 * self.SCALE_FACTOR)
        self.FPS_COLOR = (255, 255, 255)
        self.FPS_OPACITY = 64

        # Start button settings
        self.PLAY_IMGS = {"selected": "assets/sprites/pixel_art/play_selected.png",
                          "unselected": "assets/sprites/pixel_art/play_unselected.png"}
        self.PLAY_Y = 326 * self.SCALE_FACTOR
        self.PLAY_HEIGHT = 36 * self.SCALE_FACTOR
        self.PLAY_OPACITY = {"selected": 255,
                             "unselected": 64}

        # Quit button settings
        self.QUIT_IMGS = {"selected": "assets/sprites/pixel_art/quit_selected.png",
                          "unselected": "assets/sprites/pixel_art/quit_unselected.png"}
        self.QUIT_Y = 379 * self.SCALE_FACTOR
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
        self.COIN_IMG = "assets/sprites/pixel_art/coin.png"
        self.COIN_HEIGHT = 33 * self.SCALE_FACTOR
        
        self.SCORE_X = 24 * self.SCALE_FACTOR
        self.SCORE_Y = 24 * self.SCALE_FACTOR

        # Health settings
        self.HEART_IMG = "assets/sprites/pixel_art/heart.png"
        self.HEART_HEIGHT = 30 * self.SCALE_FACTOR

        self.HEALTH_X = 24 * self.SCALE_FACTOR
        self.HEALTH_Y = 71 * self.SCALE_FACTOR

        # Particle settings
        self.PARTICLE_IMG = "assets/sprites/pixel_art/particle.png"
        self.PARTICLE_HEIGHT = 2 * 2

        # Player settings
        self.PLAYER_IMG = "assets/sprites/pixel_art/player.png"
        self.PLAYER_HEIGHT = 32 * 4
        self.PLAYER_HEALTH = 100
        self.PLAYER_REGEN = 1
        self.PLAYER_BULLET_DAMAGE = 10
        self.PLAYER_BULLET_SPEED = 3
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
        self.ENEMY_PURPLE_HEALTH = 10
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
        self.ENEMY_RED_HEIGHT = 48 * 4
        self.ENEMY_RED_HEALTH = 20
        self.ENEMY_RED_BODY_DAMAGE = 10
        self.ENEMY_RED_BULLET_DAMAGE = 5
        self.ENEMY_RED_BULLET_SPEED = 1
        self.ENEMY_RED_BULLET_LIFETIME = 600
        self.ENEMY_RED_RELOAD_TIME = 3000
        self.ENEMY_RED_MOVEMENT_SPEED = 1
        self.ENEMY_RED_MOVEMENT_COOLDOWN = 30
        self.ENEMY_RED_MOVEMENT_PATTERN = "move_target"
        self.ENEMY_RED_SCORE = 10
        
        self.ENEMY_GREEN_IMG = "assets/sprites/pixel_art/enemy_green.png"
        self.ENEMY_GREEN_HEIGHT = 52 * 4
        self.ENEMY_GREEN_HEALTH = 50
        self.ENEMY_GREEN_BODY_DAMAGE = 50
        self.ENEMY_GREEN_BULLET_DAMAGE = None
        self.ENEMY_GREEN_BULLET_SPEED = None
        self.ENEMY_GREEN_BULLET_LIFETIME = None
        self.ENEMY_GREEN_RELOAD_TIME = None
        self.ENEMY_GREEN_MOVEMENT_SPEED = 1
        self.ENEMY_GREEN_MOVEMENT_COOLDOWN = 120
        self.ENEMY_GREEN_MOVEMENT_PATTERN = "move_target"
        self.ENEMY_GREEN_SCORE = 10

        self.ENEMY_GREEN_BABY_IMG = "assets/sprites/pixel_art/enemy_green_baby.png"
        self.ENEMY_GREEN_BABY_HEIGHT = 18 * 4
        self.ENEMY_GREEN_BABY_HEALTH = 5
        self.ENEMY_GREEN_BABY_BODY_DAMAGE = 5
        self.ENEMY_GREEN_BABY_BULLET_DAMAGE = None
        self.ENEMY_GREEN_BABY_BULLET_SPEED = None
        self.ENEMY_GREEN_BABY_BULLET_LIFETIME = None
        self.ENEMY_GREEN_BABY_RELOAD_TIME = None
        self.ENEMY_GREEN_BABY_MOVEMENT_SPEED = 1
        self.ENEMY_GREEN_BABY_MOVEMENT_COOLDOWN = 120
        self.ENEMY_GREEN_BABY_MOVEMENT_PATTERN = "move_random"
        self.ENEMY_GREEN_BABY_SCORE = 5

        self.ENEMY_YELLOW_IMG = "assets/sprites/pixel_art/enemy_yellow.png"
        self.ENEMY_YELLOW_HEIGHT = 38 * 4
        self.ENEMY_YELLOW_HEALTH = 10
        self.ENEMY_YELLOW_BODY_DAMAGE = 10
        self.ENEMY_YELLOW_BULLET_DAMAGE = None
        self.ENEMY_YELLOW_BULLET_SPEED = None
        self.ENEMY_YELLOW_BULLET_LIFETIME = None
        self.ENEMY_YELLOW_RELOAD_TIME = None
        self.ENEMY_YELLOW_MOVEMENT_SPEED = 5
        self.ENEMY_YELLOW_MOVEMENT_COOLDOWN = 30
        self.ENEMY_YELLOW_MOVEMENT_PATTERN = "move_target"
        self.ENEMY_YELLOW_SCORE = 20

        self.GAMEOVER_IMG = "assets/sprites/pixel_art/gameover.png"
        self.GAMEOVER_HEIGHT = 19 * 4 * 2
        self.GAMEOVER_Y = 74 * 2
        self.GAMEOVER_LABEL_Y = 500
        self.GAMEOVER_PRESS_Y = 600
