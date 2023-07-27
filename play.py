#!/usr/bin/env python3

"""play.py: PlayState class."""

import pygame
import random

from settings import *
settings = Settings()

from game import State
from score import Score
from health import Health
from player import Player
from enemy import EnemyPurple
from particle import Particle

class PlayState(State):
    def __init__(self, game) -> None:
        super().__init__(game)

        self.player = Player()

        self.score_counter = 0
        self.score = Score()

        self.health = Health(self.player.health)

        self.can_spawn = True
        self.enemy_timer = 0
        self.enemy_cooldown = random.randint(settings.ENEMY_TIME_MIN, settings.ENEMY_TIME_MAX)
        self.enemies = pygame.sprite.Group()

        self.particles = pygame.sprite.Group()

    def update(self) -> None:
        super().update()

        self.score.update(self.score_counter)
        self.health.update(self.player.health)

        self.player.update()

        self.spawn_enemies()
        self.enemies.update(self.player)

        self.particles.update()

        self.collisions()
    
    def spawn_enemies(self) -> None:
        current_time = pygame.time.get_ticks()
        if current_time - self.enemy_timer > self.enemy_cooldown:
            self.enemy_timer = current_time
            self.enemy_cooldown = random.randint(settings.ENEMY_TIME_MIN, settings.ENEMY_TIME_MAX)
            enemy = EnemyPurple()
            self.enemies.add(enemy)

    def collisions(self) -> None:
        collisions_bullets_enemies = pygame.sprite.groupcollide(self.player.bullets, self.enemies, False, False, pygame.sprite.collide_mask)
        # For each bullet, damage the first enemy it collides with
        for bullet, enemies in collisions_bullets_enemies.items():
            for enemy in enemies:
                enemy.health -= bullet.damage
                # Destroy bullet and add particle effect
                for _ in range(10):
                    self.particles.add(Particle((255, 255, 255), bullet.rect.x, bullet.rect.y))
                bullet.kill()
                self.score_counter += enemy.score

    def draw(self) -> None:
        super().draw()

        self.score.draw(self.game.screen)
        self.health.draw(self.game.screen)

        self.player.draw(self.game.screen)
        for enemy in self.enemies:
            enemy.draw(self.game.screen)

        for particle in self.particles:
            particle.draw(self.game.screen)
