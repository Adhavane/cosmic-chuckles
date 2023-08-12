#!/usr/bin/env python3

"""button.py: Button class and subclasses."""

from __future__ import annotations

import pygame
from abc import ABC, abstractmethod
from typing import Callable, Dict, Tuple

from src.settings import Settings
settings = Settings()

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
    def __init__(self, game: Game) -> None:
        from src.scenes.play import PlayState
        from src.scenes.transition import TransitionState

        game.scene_manager.push(PlayState(game))
        game.scene_manager.push(TransitionState(game, settings.TRANSITION_TIME))

        super().__init__(settings.PLAY_IMGS,
                         round(settings.SCREEN_WIDTH / 2),
                         settings.PLAY_Y,
                         settings.PLAY_HEIGHT,
                         settings.PLAY_OPACITY,
                         game.next_state)

class ButtonQuit(Button):
    def __init__(self, game: Game) -> None:
        super().__init__(settings.QUIT_IMGS,
                         round(settings.SCREEN_WIDTH / 2),
                         settings.QUIT_Y,
                         settings.QUIT_HEIGHT,
                         settings.QUIT_OPACITY,
                         game.quit)
        
from src.game import Game
