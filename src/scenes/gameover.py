#!/usr/bin/env python3

"""game_over.py: GameOverState class."""

import pygame

from src.settings import Settings
settings = Settings()

from src.scenes.state import State
from src.gui.caption import Caption

class GameOverState(State):
    def __init__(self, game, score: int) -> None:
        super().__init__(game)

        self.score = score

        self.score_caption = Caption("SCORE", settings.SCORE_FONT, settings.SCORE_SIZE,
                                     True, settings.WHITE,
                                     int(settings.SCREEN_WIDTH / 2),
                                     int(settings.SCREEN_HEIGHT / 2 + settings.SCORE_SIZE))
        self.score_counter = Caption(str(score), settings.SCORE_FONT, settings.SCORE_SIZE,
                                     True, settings.GREEN,
                                     int(settings.SCREEN_WIDTH / 2),
                                     int(settings.SCREEN_HEIGHT / 2 + settings.SCORE_SIZE * 2))

    def update(self) -> None:
        pass

    def draw(self) -> None:
        self.score_caption.draw(self.game.screen)
        self.score_counter.draw(self.game.screen)
    