#!/usr/bin/env python

"""play.py: PlayState class."""

import pygame
import random

from settings import *
settings = Settings()

from game import State
from score import Score
from player import Player
from enemy import EnemyPurple

class PlayState(State):
    def __init__(self, game) -> None:
        super().__init__(game)

        self.score = Score()
        self.sc = 0

        self.player = Player()

        self.can_spawn = True
        self.enemy_timer = 0
        self.enemy_cooldown = random.randint(settings.ENEMY_TIME_MIN, settings.ENEMY_TIME_MAX)
        self.enemies = pygame.sprite.Group()

    def update(self) -> None:
        super().update()

        self.score.update(self.sc)
        self.player.update()

        self.spawn_enemies()
        self.enemies.update(self.player)

        self.collisions()
    
    def spawn_enemies(self) -> None:
        current_time = pygame.time.get_ticks()
        if current_time - self.enemy_timer > self.enemy_cooldown:
            self.enemy_timer = current_time
            self.enemy_cooldown = random.randint(settings.ENEMY_TIME_MIN, settings.ENEMY_TIME_MAX)
            enemy = EnemyPurple()
            self.enemies.add(enemy)

    def collisions(self) -> None:
        pass

    def draw(self) -> None:
        super().draw()

        self.score.draw(self.game.screen)

        self.player.draw(self.game.screen)
        for enemy in self.enemies:
            enemy.draw(self.game.screen)
