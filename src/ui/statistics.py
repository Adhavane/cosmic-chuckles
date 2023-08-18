#!/usr/bin/env python3

"""statistics.py: Statistics class."""

import os
import pygame
from abc import ABC, abstractmethod

import src.paths as paths
from src.constants import WHITE, GREEN, OPAQUE
from src.utils import scale_to_resolution

from src.ui.label import Label

class Statistics(ABC):
    LABEL_FONT: str = os.path.join(paths.FONTS, "awesome.ttf")
    LABEL_SIZE: int = scale_to_resolution(16.22)
    LABEL_X_OFFSET: int = scale_to_resolution(10)
    LABEL_Y_OFFSET: int = scale_to_resolution(-6)

    STAT_FONT: str = os.path.join(paths.FONTS, "Pixel Gosub.otf")
    STAT_SIZE: int = scale_to_resolution(27.01)
    STAT_X_OFFSET: int = scale_to_resolution(10)
    STAT_Y_OFFSET: int = scale_to_resolution(-16)

    def __init__(self, icon: str, icon_height: int,
                 label: str, stat: int, x: int, y: int) -> None:
        self.icon: pygame.Surface = pygame.image.load(icon).convert_alpha()

        scale: float = icon_height / self.icon.get_height()
        width: int = round(self.icon.get_width() * scale)
        self.icon = pygame.transform.scale(self.icon, (width, icon_height))

        self.icon_rect: pygame.Rect = self.icon.get_rect()
        self.icon_rect.x = x
        self.icon_rect.y = y

        self.label: Label = Label(text=label,
                                  font=Statistics.LABEL_FONT,
                                  size=Statistics.LABEL_SIZE,
                                  antialias=True,
                                  color=WHITE,
                                  opacity=OPAQUE,
                                  x=x + self.icon_rect.width + Statistics.LABEL_X_OFFSET,
                                  y=y + Statistics.LABEL_Y_OFFSET)

        self.stat: Label = Label(text=str(stat),
                                 font=Statistics.STAT_FONT,
                                 size=Statistics.STAT_SIZE,
                                 antialias=True,
                                 color=GREEN,
                                 opacity=OPAQUE,
                                 x=x + self.icon_rect.width + Statistics.STAT_X_OFFSET,
                                 y=y + self.label.rect.height + Statistics.STAT_Y_OFFSET)
        
    def update(self, stat: int) -> None:
        self.label.update()
        self.stat.text = str(stat)
        self.stat.update()
    
    def draw(self, display: pygame.Surface) -> None:
        display.blit(self.icon, self.icon_rect)
        self.label.draw(display)
        self.stat.draw(display)

class Score(Statistics):
    COIN_IMG: str = os.path.join(paths.SPRITES, "coin.png")
    COIN_HEIGHT: int = scale_to_resolution(33)

    SCORE_X: int = scale_to_resolution(24)
    SCORE_Y: int = scale_to_resolution(24)

    def __init__(self, score: int = 0) -> None:
        super().__init__(icon=Score.COIN_IMG,
                         icon_height=Score.COIN_HEIGHT,
                         label="score",
                         stat=score,
                         x=Score.SCORE_X, y=Score.SCORE_Y)
        
class Health(Statistics):
    HEART_IMG: str = os.path.join(paths.SPRITES, "heart.png")
    HEART_HEIGHT: int = scale_to_resolution(30)

    HEALTH_X: int = scale_to_resolution(24)
    HEALTH_Y: int = scale_to_resolution(71)

    def __init__(self, health: int) -> None:
        super().__init__(icon=Health.HEART_IMG,
                         icon_height=Health.HEART_HEIGHT,
                         label="health",
                         stat=health,
                         x=Health.HEALTH_X, y=Health.HEALTH_Y)
