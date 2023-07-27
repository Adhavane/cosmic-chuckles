#!/usr/bin/env python

"""play.py: PlayState class."""

import pygame
import random
from typing import List, Tuple
from abc import ABC, abstractmethod

from settings import *
settings = Settings()

from game import State
from player import Player
from enemy import EnemyPurple

class Caption(pygame.sprite.Sprite):
    def __init__(self,
                 text: str,
                 font: str | None,
                 size: int,
                 antialias: bool,
                 color: Tuple[int, int, int],
                 x: int, y: int) -> None:
        super().__init__()

        self.text = text
        self.size = size
        self.font = pygame.font.Font(font, size)
        
        self.antialias = antialias
        self.color = color

        self.text_render = self.font.render(self.text, self.antialias, self.color)
        self.rect = self.text_render.get_rect()
        
        self.x = x
        self.y = y

    def update(self) -> None:
        self.text_render = self.font.render(self.text, self.antialias, self.color)
        self.rect = self.text_render.get_rect()

    def draw(self, screen: pygame.Surface) -> None:
        screen.blit(self.text_render, (self.x, self.y))

class CaptionList(ABC, List[Caption]):
    def __init__(self, *captions: Caption) -> None:
        super().__init__(*captions)

    def __add__(self, caption: Caption) -> None:
        super().append(caption)

    def __sub__(self, caption: Caption) -> None:
        super().remove(caption)

    def append(self, caption: Caption) -> None:
        super().append(caption)

    def update(self) -> None:
        self[0].update()
        for i in range(1, len(self)):
            self[i].x = self[i - 1].x + self[i - 1].rect.width
            self[i].update()

    def draw(self, screen: pygame.Surface) -> None:
        for caption in self:
            caption.draw(screen)

class Score(CaptionList):
    def __init__(self) -> None:
        score_label = Caption("SCORE<", settings.SCORE_FONT, settings.SCORE_SIZE,
                             True, settings.WHITE,
                             settings.SCORE_X, settings.SCORE_Y)
        score = Caption("0", settings.SCORE_FONT, settings.SCORE_SIZE,
                        True, settings.GREEN,
                        settings.SCORE_X + score_label.rect.width,
                        settings.SCORE_Y)
        score_arrow = Caption(">", settings.SCORE_FONT, settings.SCORE_SIZE,
                              True, settings.WHITE,
                              settings.SCORE_X + score_label.rect.width + score.rect.width,
                              settings.SCORE_Y)
        self.append(score_label)
        self.append(score)
        self.append(score_arrow)

    def update(self, score: int) -> None:
        self[1].text = str(score)
        super().update()

    def draw(self, screen: pygame.Surface) -> None:
        super().draw(screen)

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

        self.sc += 1
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
