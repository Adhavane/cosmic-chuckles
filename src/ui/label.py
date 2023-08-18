#!/usr/bin/env python3

"""label.py: Label class and subclasses."""

import pygame
from typing import Tuple

class Label(pygame.sprite.Sprite):
    def __init__(self,
                 text: str,
                 font: str | None,
                 size: int,
                 antialias: bool,
                 color: Tuple[int, int, int],
                 opacity: int,
                 x: int, y: int) -> None:
        super().__init__()

        self.text: str = text
        self.size: int = size
        self.font: pygame.font.Font = pygame.font.Font(font, self.size)
        
        self.antialias: bool = antialias
        self.color: Tuple[int, int, int] = color
        self.opacity: int = opacity

        self.text_render: pygame.Surface = self.font.render(self.text, self.antialias, self.color)
        self.text_render.set_alpha(self.opacity)
        self.rect: pygame.Rect = self.text_render.get_rect()
        
        self.x: int = x
        self.y: int = y

    def update(self) -> None:
        self.text_render = self.font.render(self.text, self.antialias, self.color)
        self.text_render.set_alpha(self.opacity)
        self.rect = self.text_render.get_rect()

    def draw(self, display: pygame.Surface) -> None:
        display.blit(self.text_render, (self.x, self.y))
