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

        scale: float = settings.GAMEOVER_IMG_HEIGHT / self.gameover.get_height()
        width: int = round(self.gameover.get_width() * scale)
        height: int = round(self.gameover.get_height() * scale)
        self.gameover = pygame.transform.scale(self.gameover, (width, height))

        self.gameover_rect: pygame.Rect = self.gameover.get_rect()
        self.gameover_rect.x = round(settings.SCREEN_WIDTH / 2 - self.gameover_rect.width / 2)
        self.gameover_rect.y = settings.GAMEOVER_IMG_Y

        self.score: Label = Label(str(score), settings.GAMEOVER_SCORE_FONT, settings.GAMEOVER_SCORE_SIZE,
                                  True, settings.GREEN, settings.OPAQUE, 0, 0)
        self.score.x = round(settings.SCREEN_WIDTH / 2 - self.score.rect.width / 2)
        self.score.y = settings.GAMEOVER_SCORE_Y + settings.GAMEOVER_SCORE_Y_PADDING

        self.press: Label = Label("PRESS ENTER TO PLAY AGAIN", settings.GAMEOVER_PRESS_FONT, settings.GAMEOVER_PRESS_SIZE,
                                  True, settings.WHITE, settings.OPAQUE, 0, 0)
        self.press.x = round(settings.SCREEN_WIDTH / 2 - self.press.rect.width / 2)
        self.press.y = settings.GAMEOVER_PRESS_Y

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
