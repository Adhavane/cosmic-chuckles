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
        self.CLOUD_HEIGHT_MIN = 50
        self.CLOUD_HEIGHT_MAX = 200
        self.CLOUD_SPEED_MIN = 1
        self.CLOUD_SPEED_MAX = 3
        self.OPACITY_MIN = 50
        self.OPACITY_MAX = 128
        self.CLOUD_SPAWN_RATE = 60

        # Player settings

        # Game settings

        # # Layers
        # self.WALL_LAYER = 1
        # self.PLAYER_LAYER = 2
        # self.BULLET_LAYER = 3
        # self.ENEMY_LAYER = 2
        # self.ITEM_LAYER = 1
        # self.EFFECTS_LAYER = 4

        # # Items
        # self.ITEM_IMAGES = {
        #     "health": "assets/health_pack.png",
        #     "shotgun": "assets/shotgun.png",
        #     "barrel": "assets/barrel.png",
        #     "ammo": "assets/ammo.png",
        #     "laser": "assets/laser.png",
        #     "speed": "assets/boot.png"
        # }

        # # Sounds
        # self.BG_MUSIC = "assets/music.wav"
        # self.SOUND_DICT = {
        #     "level_start": pygame.mixer.Sound("assets/level_start.wav"),
        #     "health_up": pygame.mixer.Sound("assets/health_pack.wav"),
        #     "gun_pickup": pygame.mixer.Sound("assets/gun_pickup.wav"),
        #     "gun_upgrade": pygame.mixer.Sound("assets/gun_upgrade.wav"),
        #     "player_jump": pygame.mixer.Sound("assets/jump.wav"),
        #     "player_hurt": pygame.mixer.Sound("assets/player_hurt.wav"),
        #     "enemy_hit": pygame.mixer.Sound("assets/enemy_hit.wav"),
        #     "enemy_death": pygame.mixer.Sound("assets/enemy_death.wav"),
        #     "bullet_hit": pygame.mixer.Sound("assets/bullet_hit.wav"),
        #     "powerup": pygame.mixer.Sound("assets/powerup.wav"),
        #     "laser": pygame.mixer.Sound("assets/laser.wav")
        # }

        # # Gun settings
        # self.BULLET_IMG = "assets/bullet.png"
        # self.BULLET_SPEED = 500
        # self.BULLET_LIFETIME = 1000
        # self.BULLET_RATE = 150
        # self.KICKBACK = 200
        # self.GUN_SPREAD = 5
        # self.BULLET_DAMAGE = 10

        # # Mob settings
        # self.MOB_IMG = "assets/mob.png"

        # # Effects
        # self.MUZZLE_FLASHES = ["assets/whitePuff15.png", "assets/whitePuff16.png", "assets/whitePuff17.png", "assets/whitePuff18.png"]
        # self.FLASH_DURATION = 40
        # self.DAMAGE_ALPHA = [i for i in range(0, 255, 55)]
        # self.NIGHT_COLOR = (20, 20, 20)
        # self.LIGHT_RADIUS = (500, 500)
        # self.LIGHT_MASK = "assets/light_350_soft.png"
 