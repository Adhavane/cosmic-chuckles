#!/usr/bin/env python3

"""health.py: Health class."""

import pygame

from settings import Settings
settings = Settings()

from caption import Caption, CaptionList

class Health:
    def __init__(self, health: int) -> None:
        self.heart = pygame.image.load(settings.HEART_IMG).convert_alpha()
        
        scale = settings.HEART_HEIGHT / self.heart.get_height()
        self.heart = pygame.transform.scale(self.heart, (int(self.heart.get_width() * scale), int(self.heart.get_height() * scale)))

        self.heart_rect = self.heart.get_rect()
        self.heart_rect.x = settings.HEART_X
        self.heart_rect.y = settings.HEART_Y

        health_left = Caption(" <", settings.HEALTH_FONT, settings.HEALTH_SIZE,
                              True, settings.WHITE,
                              self.heart_rect.x + self.heart_rect.width,
                              settings.HEALTH_Y)
        health_counter = Caption(str(health), settings.HEALTH_FONT, settings.HEALTH_SIZE,
                                 True, settings.GREEN,
                                 health_left.rect.x + health_left.rect.width,
                                 settings.HEALTH_Y)
        health_right = Caption(">", settings.HEALTH_FONT, settings.HEALTH_SIZE,
                               True, settings.WHITE,
                               health_counter.rect.x + health_counter.rect.width,
                               settings.HEALTH_Y)
        
        self.health = CaptionList([health_left, health_counter, health_right])

    def update(self, health: int) -> None:
        self.health[1].text = str(health)
        self.health.update()

    def draw(self, screen: pygame.Surface) -> None:
        screen.blit(self.heart, self.heart_rect)
        self.health.draw(screen)
