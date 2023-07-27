#!/usr/bin/env python3

"""score.py: Score class."""

import pygame

from settings import *
settings = Settings()

from caption import Caption, CaptionList

class Score(CaptionList):
    def __init__(self) -> None:
        score_left = Caption("SCORE<", settings.SCORE_FONT, settings.SCORE_SIZE,
                             True, settings.WHITE,
                             settings.SCORE_X, settings.SCORE_Y)
        score_counter = Caption("0", settings.SCORE_FONT, settings.SCORE_SIZE,
                                True, settings.GREEN,
                                settings.SCORE_X + score_left.rect.width,
                                settings.SCORE_Y)
        score_right = Caption(">", settings.SCORE_FONT, settings.SCORE_SIZE,
                              True, settings.WHITE,
                              settings.SCORE_X + score_left.rect.width + score_counter.rect.width,
                              settings.SCORE_Y)
        self.append(score_left)
        self.append(score_counter)
        self.append(score_right)

    def update(self, score: int) -> None:
        self[1].text = str(score)
        super().update()

    def draw(self, screen: pygame.Surface) -> None:
        super().draw(screen)
