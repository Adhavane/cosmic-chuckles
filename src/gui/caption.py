#!/usr/bin/env python3

"""caption.py: Caption class and subclasses."""

import pygame
from typing import List, Tuple
from abc import ABC, abstractmethod

from src.settings import Settings
settings = Settings()

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
    def __init__(self, captions: List[Caption]) -> None:
        super().__init__(captions)

    # def __add__(self, captions: List[Caption]) -> List[Caption]:
    #     for caption in captions:
    #         super().append(caption)
    #     return self
    
    # def __sub__(self, captions: List[Caption]) -> List[Caption]:
    #     for caption in captions:
    #         super().remove(caption)
    #     return self

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
