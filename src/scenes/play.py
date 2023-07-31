#!/usr/bin/env python3

"""play.py: PlayState class."""

import pygame
import random

from typing import Dict, List, Sequence

from src.settings import Settings
settings = Settings()

from src.scenes.state import State
from src.scenes.gameover import GameOverState

from src.gui.score import Score
from src.gui.health import Health

from src.prefabs.player import Player
from src.prefabs.enemy import Enemy, EnemyPurple, EnemyRed, EnemyGreen, EnemyYellow
from src.prefabs.projectile import Projectile
from src.prefabs.particle import Particle

class PlayState(State):
    def __init__(self, game) -> None:
        super().__init__(game)

        self.player: Player = Player()

        self.score_counter: int = 0
        self.score = Score()

        self.health: Health = Health(self.player.health)

        self.can_spawn: bool = True
        self.enemy_timer: int = 0
        self.enemy_cooldown: int = random.randint(settings.ENEMY_TIME_MIN, settings.ENEMY_TIME_MAX)
        self.enemies: pygame.sprite.Group[Enemy] = pygame.sprite.Group()

        self.particles: pygame.sprite.Group[Particle] = pygame.sprite.Group()

    def update(self) -> None:
        super().update()

        self.score.update(self.score_counter)
        self.health.update(self.player.health)

        self.player.update()

        self.spawn_enemies()
        self.enemies.update(self.player)

        self.particles.update()
    
        self.collisions()

        if self.player.health <= 0:
            self.game.change_state(GameOverState(self.game, self.score_counter))
    
    def spawn_enemies(self) -> None:
        current_time: int = pygame.time.get_ticks()
        if current_time - self.enemy_timer > self.enemy_cooldown:
            self.enemy_timer = current_time
            self.enemy_cooldown = random.randint(settings.ENEMY_TIME_MIN, settings.ENEMY_TIME_MAX)
            enemy = random.choice([EnemyPurple(), EnemyRed(), EnemyGreen(), EnemyYellow()])
            self.enemies.add(enemy)

    def collisions(self) -> None:
        if pygame.sprite.groupcollide(self.player.bullets, self.enemies, False, False):
            collisions_bullets_enemies: Dict[Projectile, List[Enemy]] = \
                pygame.sprite.groupcollide(self.player.bullets,
                                           self.enemies, False, False,
                                           pygame.sprite.collide_mask)
            
            # For each bullet, damage the first enemy it collides with
            for bullet, enemies in collisions_bullets_enemies.items():
                for enemy in enemies:
                    enemy.health -= bullet.damage

                    # Destroy bullet and add particle effect
                    for _ in range(10):
                        self.particles.add(Particle((255, 255, 255), bullet.rect.x, bullet.rect.y))
                    bullet.kill()
                    self.score_counter += enemy.score

        if pygame.sprite.spritecollide(self.player, self.enemies, False):
            collisions_player_enemies: Sequence[Enemy] = \
                pygame.sprite.spritecollide(self.player, self.enemies, True,
                                            pygame.sprite.collide_mask)
            
            for enemy in collisions_player_enemies:
                self.player.health -= enemy.body_damage
                enemy.health = 0

    def draw(self) -> None:
        super().draw()

        self.score.draw(self.game.screen)
        self.health.draw(self.game.screen)

        self.player.draw(self.game.screen)
        for enemy in self.enemies:
            enemy.draw(self.game.screen)

        for particle in self.particles:
            particle.draw(self.game.screen)
