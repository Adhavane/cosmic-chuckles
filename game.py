#!/usr/bin/env python

"""game.py: Game class."""

import pygame, sys

from settings import *
settings = Settings()

import random

from background import Background
from cloud import Cloud
from player import Player
from enemy import EnemyPurple

class Game:
    def __init__(self) -> None:
        pygame.init()
        self.screen = pygame.display.set_mode((settings.WIDTH, settings.HEIGHT))
        self.clock = pygame.time.Clock()

        pygame.display.set_caption(settings.TITLE)
        pygame.display.set_icon(pygame.image.load(settings.ICON))

        self.background = Background()
        
        self.clouds = pygame.sprite.Group()
        for _ in range(settings.CLOUD_INIT):
            cloud = Cloud()
            cloud.rect.x = random.randint(0, settings.WIDTH)
            self.clouds.add(cloud)
        self.cloud_timer = 0
        self.cloud_cooldown = random.randint(settings.CLOUD_TIME_MIN, settings.CLOUD_TIME_MAX)

        self.player = Player()

        self.can_spawn = True
        self.enemy_timer = 0
        self.enemy_cooldown = random.randint(settings.ENEMY_TIME_MIN, settings.ENEMY_TIME_MAX)
        self.enemies = pygame.sprite.Group()

    def run(self) -> None:
        while True:
            self.events()
            self.update()
            self.draw()
    
    def events(self) -> None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
    def update(self) -> None:
        self.background.update()

        self.spawn_clouds()
        self.clouds.update()

        self.player.update()

        self.spawn_enemies()
        self.enemies.update(self.player)

    def spawn_clouds(self) -> None:
        current_time = pygame.time.get_ticks()
        if current_time - self.cloud_timer > self.cloud_cooldown:
            self.cloud_timer = current_time
            self.cloud_cooldown = random.randint(settings.CLOUD_TIME_MIN, settings.CLOUD_TIME_MAX)
            cloud = Cloud()
            self.clouds.add(cloud)
    
    def spawn_enemies(self) -> None:
        current_time = pygame.time.get_ticks()
        if current_time - self.enemy_timer > self.enemy_cooldown:
            self.enemy_timer = current_time
            self.enemy_cooldown = random.randint(settings.ENEMY_TIME_MIN, settings.ENEMY_TIME_MAX)
            enemy = EnemyPurple()
            self.enemies.add(enemy)

    def draw(self) -> None:
        self.screen.fill(settings.BLACK)

        self.background.draw(self.screen)
        for cloud in self.clouds: cloud.draw(self.screen)
        self.player.draw(self.screen)
        for enemy in self.enemies: enemy.draw(self.screen)

        pygame.display.update()
        self.clock.tick(settings.FPS)
