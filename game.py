#!/usr/bin/env python

"""game.py: Game class."""

import pygame, sys

from settings import *
settings = Settings()

import random

from background import Background
from cloud import Cloud
from player import Player

class Game:
    def __init__(self) -> None:
        pygame.init()
        self.screen = pygame.display.set_mode((settings.WIDTH, settings.HEIGHT))
        self.clock = pygame.time.Clock()

        pygame.display.set_caption(settings.TITLE)
        pygame.display.set_icon(pygame.image.load(settings.ICON))

        self.background = Background()
        self.clouds = pygame.sprite.Group()
        self.player = Player()

        self.cloud_timer = 0
        self.cloud_cooldown = random.randint(settings.CLOUD_TIME_MIN, settings.CLOUD_TIME_MAX)

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

    def spawn_clouds(self) -> None:
        current_time = pygame.time.get_ticks()
        if current_time - self.cloud_timer > self.cloud_cooldown:
            self.cloud_timer = current_time
            self.cloud_cooldown = random.randint(settings.CLOUD_TIME_MIN, settings.CLOUD_TIME_MAX)
            cloud = Cloud()
            self.clouds.add(cloud)

    def draw(self) -> None:
        self.screen.fill(settings.BLACK)

        self.background.draw(self.screen)
        for cloud in self.clouds: cloud.draw(self.screen)
        self.player.draw(self.screen)

        pygame.display.update()
        self.clock.tick(settings.FPS)
