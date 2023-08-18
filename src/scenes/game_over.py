#!/usr/bin/env python3

"""game_over.py: GameOverState class."""

import os
import pygame

import src.paths as paths
from src.constants import \
    SCREEN_WIDTH, GREEN, WHITE, OPAQUE
from src.utils import scale_to_resolution

from src.scenes.state import Scene
from src.ui.label import Label

class GameOverState(Scene):
    IMG: str = os.path.join(paths.SPRITES, "game_over.png")
    IMG_HEIGHT: int = scale_to_resolution(220)
    IMG_Y: int = scale_to_resolution(71)

    SCORE_FONT: str = os.path.join(paths.FONTS, "Pixel Gosub.otf")
    SCORE_SIZE = scale_to_resolution(43.21)
    SCORE_Y = scale_to_resolution(339)
    SCORE_Y_PADDING = scale_to_resolution(-18)

    PRESS_FONT: str = os.path.join(paths.FONTS, "Pixel Gosub.otf")
    PRESS_SIZE = scale_to_resolution(14.4)
    PRESS_Y = scale_to_resolution(466)

    def __init__(self, game, score: int) -> None:
        super().__init__(game)

        self.gameover: pygame.Surface = pygame.image.load(GameOverState.IMG).convert_alpha()

        scale: float = GameOverState.IMG_HEIGHT / self.gameover.get_height()
        width: int = round(self.gameover.get_width() * scale)
        height: int = round(self.gameover.get_height() * scale)
        self.gameover = pygame.transform.scale(self.gameover, (width, height))

        self.gameover_rect: pygame.Rect = self.gameover.get_rect()
        self.gameover_rect.x = round(SCREEN_WIDTH / 2 - self.gameover_rect.width / 2)
        self.gameover_rect.y = GameOverState.IMG_Y

        self.score: Label = Label(text=str(score),
                                  font=GameOverState.SCORE_FONT,
                                  size=GameOverState.SCORE_SIZE,
                                  antialias=True,
                                  color=GREEN,
                                  opacity=OPAQUE,
                                  x=0, y=0)
        self.score.x = round(SCREEN_WIDTH / 2 - self.score.rect.width / 2)
        self.score.y = GameOverState.SCORE_Y + GameOverState.SCORE_Y_PADDING

        self.press: Label = Label(text="PRESS ENTER TO PLAY AGAIN",
                                  font=GameOverState.PRESS_FONT,
                                  size=GameOverState.PRESS_SIZE,
                                  antialias=True,
                                  color=WHITE,
                                  opacity=OPAQUE,
                                  x=0, y=0)
        self.press.x = round(SCREEN_WIDTH / 2 - self.press.rect.width / 2)
        self.press.y = GameOverState.PRESS_Y

    def events(self, event: pygame.event.Event) -> None:
        from src.scenes.play import PlayState

        super().events(event)

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                self.game.scene_manager.push(PlayState(self.game))
                self.game.next_state()

    def update(self) -> None:
        super().update()

    def draw(self) -> None:
        super().draw()

        self.game.display.blit(self.gameover, self.gameover_rect)
        self.score.draw(self.game.display)
        self.press.draw(self.game.display)
