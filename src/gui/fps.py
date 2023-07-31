#!/usr/bin/env python3

"""fps.py: FPS class."""

import pygame

from src.settings import Settings
settings = Settings()

from src.gui.caption import Caption, CaptionList

class FPS(CaptionList):
    def __init__(self) -> None:
        fps_left = Caption("<", settings.FPS_FONT, settings.FPS_SIZE,
                           True, settings.WHITE,
                           settings.FPS_X, settings.FPS_Y)
        fps_counter = Caption("0", settings.FPS_FONT, settings.FPS_SIZE,
                              True, settings.GREEN,
                              settings.FPS_X + fps_left.rect.width,
                              settings.FPS_Y)
        fps_right = Caption(">", settings.FPS_FONT, settings.FPS_SIZE,
                            True, settings.WHITE,
                            settings.FPS_X + fps_left.rect.width + fps_counter.rect.width,
                            settings.FPS_Y)
        self.append(fps_left)
        self.append(fps_counter)
        self.append(fps_right)

    def update(self, fps: int) -> None:
        self[1].text = str(fps)
        super().update()

    def draw(self, screen: pygame.Surface) -> None:
        super().draw(screen)
