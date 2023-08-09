#!/usr/bin/env python3

"""statistics.py: Statistics class."""

import pygame
from abc import ABC, abstractmethod

from src.settings import Settings
settings = Settings()

from src.ui.label import Label

class Statistics(ABC):
    def __init__(self, icon: str, icon_height: int,
                 label: str, stat: int, x: int, y: int) -> None:
        self.icon: pygame.Surface = pygame.image.load(icon).convert_alpha()

        scale: float = icon_height / self.icon.get_height()
        width: int = round(self.icon.get_width() * scale)
        self.icon = pygame.transform.scale(self.icon, (width, icon_height))

        self.icon_rect: pygame.Rect = self.icon.get_rect()
        self.icon_rect.x = x
        self.icon_rect.y = y

        self.label: Label = Label(label, settings.STATISTICS_LABEL_FONT, settings.STATISTICS_LABEL_SIZE,
                                  True, settings.WHITE, settings.OPAQUE,
                                  x + self.icon_rect.width + settings.STATISTICS_LABEL_X_OFFSET,
                                  y + settings.STATISTICS_LABEL_Y_OFFSET)
        
        self.stat: Label = Label(f"<{stat}>", settings.STATISTICS_STAT_FONT, settings.STATISTICS_STAT_SIZE,
                                 True, settings.GREEN, settings.OPAQUE,
                                 x + self.icon_rect.width + settings.STATISTICS_STAT_X_OFFSET,
                                 y + self.label.rect.height + settings.STATISTICS_STAT_Y_OFFSET)
        
    def update(self, stat: int) -> None:
        self.label.update()
        self.stat.text = str(stat)
        self.stat.update()
    
    def draw(self, display: pygame.Surface) -> None:
        display.blit(self.icon, self.icon_rect)
        self.label.draw(display)
        self.stat.draw(display)

class Score(Statistics):
    def __init__(self, score: int = 0) -> None:
        super().__init__(settings.COIN_IMG, settings.COIN_HEIGHT,
                         "score", score,
                         settings.SCORE_X, settings.SCORE_Y)
        
class Health(Statistics):
    def __init__(self, health: int) -> None:
        super().__init__(settings.HEART_IMG, settings.HEART_HEIGHT,
                         "health", health,
                         settings.HEALTH_X, settings.HEALTH_Y)
