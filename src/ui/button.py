#!/usr/bin/env python3

"""button.py: Button class and subclasses."""

from __future__ import annotations

import os
import pygame
from abc import ABC, abstractmethod
from typing import Callable, Dict, Tuple

import src.paths as paths
from src.constants import SCREEN_WIDTH
from src.utils import scale_to_resolution

class Button(ABC, pygame.sprite.Sprite):
    def __init__(self,
                 images: Dict[str, str],
                 x: int, y: int,
                 height: int,
                 opacity: Dict[str, int],
                 event: Callable,
                 *event_args: Tuple,
                 **event_kwargs: Dict) -> None:
        super().__init__()

        self.images: Dict[str, str] = images
        
        self.x: int = x
        self.y: int = y
        self.height: int = height
        
        self.opacity: Dict[str, int] = opacity
        
        self.state: str = "unselected"
        self.change_state(self.state)

        self.event: Callable = event
        self.event_args: Tuple = event_args
        self.event_kwargs: Dict = event_kwargs

    def mouse_over(self) -> bool:
        mouse_pos: Tuple[int, int] = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_pos):
            return True
        return False
    
    def mouse_click(self) -> bool:
        mouse_click: Tuple[bool, bool, bool] = pygame.mouse.get_pressed()
        if mouse_click[0] and self.mouse_over():
            return True
        return False
    
    def change_state(self, state: str) -> None:
        self.state = state
        self.image: pygame.Surface = pygame.image.load(self.images[self.state]).convert_alpha()

        self.rect: pygame.Rect = self.image.get_rect()
        scale: float = self.height / self.rect.height
        width: int = round(self.rect.width * scale)
        height: int = round(self.rect.height * scale)
        self.image = pygame.transform.scale(self.image, (width, height))

        self.rect = self.image.get_rect()
        self.rect.x = round(self.x - self.rect.width / 2)
        self.rect.y = self.y

        self.image.set_alpha(self.opacity[self.state])
    
    def update(self) -> None:
        if self.state == "selected" and pygame.key.get_pressed()[pygame.K_RETURN]:
            self.event(*self.event_args, **self.event_kwargs)

    def draw(self, display) -> None:
        display.blit(self.image, self.rect)

class ButtonPlay(Button):
    IMGS: Dict[str, str] = {"selected": f"{os.path.join(paths.SPRITES, 'play_selected.png')}",
                            "unselected": f"{os.path.join(paths.SPRITES, 'play_unselected.png')}"}
    Y: int = scale_to_resolution(326)
    HEIGHT: int = scale_to_resolution(36)
    OPACITY: Dict[str, int] = {"selected": 255,
                               "unselected": 64}
    
    def __init__(self, game: Game) -> None:
        from src.scenes.play import PlayState
        from src.scenes.transition import TransitionState

        game.scene_manager.push(PlayState(game))

        super().__init__(ButtonPlay.IMGS,
                         round(SCREEN_WIDTH / 2),
                         ButtonPlay.Y,
                         ButtonPlay.HEIGHT,
                         ButtonPlay.OPACITY,
                         game.next_state)

class ButtonQuit(Button):
    IMGS: Dict[str, str] = {"selected": f"{os.path.join(paths.SPRITES, 'quit_selected.png')}",
                            "unselected": f"{os.path.join(paths.SPRITES, 'quit_unselected.png')}"}
    Y: int = scale_to_resolution(380)
    HEIGHT: int = scale_to_resolution(36)
    OPACITY: Dict[str, int] = {"selected": 255,
                               "unselected": 64}
    
    def __init__(self, game: Game) -> None:
        super().__init__(ButtonQuit.IMGS,
                         round(SCREEN_WIDTH / 2),
                         ButtonQuit.Y,
                         ButtonQuit.HEIGHT,
                         ButtonQuit.OPACITY,
                         game.quit)
        
from src.game import Game
