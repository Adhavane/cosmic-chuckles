#!/usr/bin/env python

"""score.py: Score class."""

import pygame

from settings import *
settings = Settings()

from caption import Caption, CaptionList

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
