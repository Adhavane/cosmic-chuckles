#!/usr/bin/env python3

"""health.py: Health class."""

import pygame

from src.settings import Settings
settings = Settings()

from src.ui.label import Label, LabelList

class Health:
    def __init__(self, health: int) -> None:
        self.heart: pygame.Surface = pygame.image.load(settings.HEART_IMG).convert_alpha()
        
        scale: float = settings.HEART_HEIGHT / self.heart.get_height()
        width: int = int(self.heart.get_width() * scale)
        height: int = int(self.heart.get_height() * scale)
        self.heart = pygame.transform.scale(self.heart, (width, height))

        self.heart_rect: pygame.Rect = self.heart.get_rect()
        self.heart_rect.x = int(settings.SCREEN_WIDTH / 2 - self.heart_rect.width / 2)
        self.heart_rect.y = settings.HEART_Y

        health_left: Label = Label(" <", settings.HEALTH_FONT, settings.HEALTH_SIZE,
                                       True, settings.WHITE,
                                       self.heart_rect.x + self.heart_rect.width,
                                       settings.HEALTH_Y)
        health_counter: Label = Label(str(health), settings.HEALTH_FONT, settings.HEALTH_SIZE,
                                          True, settings.GREEN,
                                          health_left.rect.x + health_left.rect.width,
                                          settings.HEALTH_Y)
        health_right: Label = Label(">", settings.HEALTH_FONT, settings.HEALTH_SIZE,
                                        True, settings.WHITE,
                                        health_counter.rect.x + health_counter.rect.width,
                                        settings.HEALTH_Y)
        
        self.health: LabelList = LabelList([health_left, health_counter, health_right])

    def update(self, health: int) -> None:
        self.health[1].text = str(health)
        self.health.update()

    def draw(self, screen: pygame.Surface) -> None:
        screen.blit(self.heart, self.heart_rect)
        self.health.draw(screen)
