#!/usr/bin/env python3

"""game_over.py: GameOverState class."""

import pygame

from settings import Settings
settings = Settings()

from state import State
from caption import Caption

class GameOverState(State):
    def __init__(self, game, score: int) -> None:
        super().__init__(game)

        self.score = score

        self.score_caption = Caption("SCORE", settings.SCORE_FONT, settings.SCORE_SIZE,
                                     True, settings.WHITE,
                                     settings.WIDTH / 2,
                                     settings.HEIGHT / 2 + settings.SCORE_SIZE)
        self.score_counter = Caption(str(score), settings.SCORE_FONT, settings.SCORE_SIZE,
                                     True, settings.GREEN,
                                     settings.WIDTH / 2,
                                     settings.HEIGHT / 2 + settings.SCORE_SIZE * 2)

    def update(self) -> None:
        pass

    def draw(self) -> None:
        self.score_caption.draw(self.game.screen)
        self.score_counter.draw(self.game.screen)
    