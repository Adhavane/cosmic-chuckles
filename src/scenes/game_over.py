#!/usr/bin/env python3

"""game_over.py: GameOverState class."""

import pygame

from src.settings import Settings
settings = Settings()

from src.scenes.state import State
from src.ui.label import Label

class GameOverState(State):
    def __init__(self, game, score: int) -> None:
        super().__init__(game)

        self.gameover: pygame.Surface = pygame.image.load(settings.GAMEOVER_IMG).convert_alpha()

        scale: float = settings.GAMEOVER_HEIGHT / self.gameover.get_height()
        width: int = int(self.gameover.get_width() * scale)
        height: int = int(self.gameover.get_height() * scale)
        self.gameover = pygame.transform.scale(self.gameover, (width, height))

        self.gameover_rect: pygame.Rect = self.gameover.get_rect()
        self.gameover_rect.x = int(settings.SCREEN_WIDTH / 2 - self.gameover_rect.width / 2)
        self.gameover_rect.y = settings.GAMEOVER_Y

        self.score: Label = Label(str(score), settings.SCORE_FONT, settings.SCORE_SIZE,
                                      True, settings.WHITE,
                                      0, 0)
        self.score.rect.x = int(settings.SCREEN_WIDTH / 2 - self.score.rect.width / 2)
        self.score.rect.y = settings.GAMEOVER_CAPTION_Y

        self.press: Label = Label("PRESS ENTER TO PLAY AGAIN", settings.SCORE_FONT, settings.SCORE_SIZE,
                                        True, settings.WHITE,
                                        0, 0)
        self.press.rect.x = int(settings.SCREEN_WIDTH / 2 - self.press.rect.width / 2)
        self.press.rect.y = settings.GAMEOVER_PRESS_Y

    def events(self, event: pygame.event.Event) -> None:
        from src.scenes.play import PlayState

        super().events(event)

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                self.game.change_state(PlayState(self.game))

    def update(self) -> None:
        super().update()

    def draw(self) -> None:
        super().draw()

        self.game.display.blit(self.gameover, self.gameover_rect)
        self.score.draw(self.game.display)
        self.press.draw(self.game.display)
