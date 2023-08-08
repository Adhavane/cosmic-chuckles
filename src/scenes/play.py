#!/usr/bin/env python3

"""play.py: PlayState class."""

import pygame
import random

from typing import Dict, List, Sequence

from src.settings import Settings
settings = Settings()

from src.scenes.state import State
from src.scenes.game_over import GameOverState

from src.ui.statistics import Score
from src.ui.statistics import Health

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

        self.spawn_particles()

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
        self.collisions_player_enemies()
        self.collisions_player_bullets()
        self.collisions_bullets_enemies()
        self.collisions_bullets_bullets()
        
    def collisions_player_enemies(self) -> None:
        if pygame.sprite.spritecollide(self.player, self.enemies, False):
            collisions_player_enemies: Sequence[Enemy] = \
                pygame.sprite.spritecollide(self.player, self.enemies, False,
                                            pygame.sprite.collide_mask)
            
            for enemy in collisions_player_enemies:
                self.player.health -= enemy.body_damage
                enemy.destroy()
    
    def collisions_player_bullets(self) -> None:
        for enemy in self.enemies:           
            if pygame.sprite.spritecollide(self.player, enemy.bullets, False):
                collisions_player_bullets: Sequence[Projectile] = \
                    pygame.sprite.spritecollide(self.player, enemy.bullets, False,
                                                pygame.sprite.collide_mask)
                
                for bullet in collisions_player_bullets:
                    self.player.health -= bullet.damage
                    bullet.destroy()

    def collisions_bullets_enemies(self) -> None:
        if pygame.sprite.groupcollide(self.player.bullets, self.enemies, False, False):
            collisions_bullets_enemies: Dict[Projectile, List[Enemy]] = \
                pygame.sprite.groupcollide(self.player.bullets,
                                           self.enemies, False, False,
                                           pygame.sprite.collide_mask)
            
            # For each bullet, damage the first enemy it collides with
            for bullet, enemies in collisions_bullets_enemies.items():
                for enemy in enemies:
                    enemy.health -= bullet.damage
                    self.score_counter += enemy.score
                    bullet.destroy()

    def collisions_bullets_bullets(self) -> None:
        for enemy in self.enemies:
            if pygame.sprite.groupcollide(enemy.bullets, self.player.bullets, False, False):
                collisions_bullets_bullets: Dict[Projectile, List[Projectile]] = \
                    pygame.sprite.groupcollide(enemy.bullets,
                                               self.player.bullets, False, False,
                                               pygame.sprite.collide_mask)
                
                for bullet, bullets in collisions_bullets_bullets.items():
                    for bullet in bullets:
                        bullet.destroy()

    def spawn_particles(self) -> None:
        for enemy in self.enemies:
            if enemy.destroyed:
                for _ in range(settings.PARTICLE_AMOUNT):
                    self.particles.add(Particle(enemy.colors,
                                                enemy.rect.centerx,
                                                enemy.rect.centery))
        
        for projectile in self.player.bullets:
            if projectile.destroyed:
                for _ in range(settings.PARTICLE_AMOUNT):
                    self.particles.add(Particle(projectile.colors,
                                                projectile.rect.centerx,
                                                projectile.rect.centery))
        
        for enemy in self.enemies:
            for projectile in enemy.bullets:
                if projectile.destroyed:
                    for _ in range(settings.PARTICLE_AMOUNT):
                        self.particles.add(Particle(projectile.colors,
                                                    projectile.rect.centerx,
                                                    projectile.rect.centery))

    def draw(self) -> None:
        super().draw()

        self.score.draw(self.game.display)
        self.health.draw(self.game.display)

        self.player.draw(self.game.display)
        for enemy in self.enemies:
            enemy.draw(self.game.display)

        for particle in self.particles:
            particle.draw(self.game.display)
