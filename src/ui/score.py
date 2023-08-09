#!/usr/bin/env python3

"""score.py: Score class."""

import pygame

from src.settings import Settings
settings = Settings()

from src.ui.statistics import Statistics

class Score(Statistics):
    def __init__(self, score: int) -> None:
        super().__init__(settings.COIN_IMG,
                         "score", score,
                         settings.SCORE_X, settings.SCORE_Y)
