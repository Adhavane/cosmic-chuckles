#!/usr/bin/env python3

"""button.py: Button class and subclasses."""

import pygame
from abc import ABC, abstractmethod
from typing import Callable, Dict

from src.settings import Settings
settings = Settings()

from src.scenes.play import PlayState

class Game:
    pass

class Button(ABC, pygame.sprite.Sprite):
    def __init__(self,
                 images: Dict[str, str],
                 x: int, y: int,
                 height: int,
                 opacity: Dict[str, int],
                 event: Callable[[], None],
                 *event_args,
                 **event_kwargs) -> None:
        super().__init__()

        self.images = images
        
        self.x = x
        self.y = y
        self.height = height
        
        self.opacity = opacity
        
        self.state = "unselected"
        self.change_state(self.state)

        self.event = event
        self.event_args = event_args
        self.event_kwargs = event_kwargs

    def mouse_over(self) -> bool:
        mouse_pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_pos):
            return True
        return False
    
    def mouse_click(self) -> bool:
        mouse_click = pygame.mouse.get_pressed()
        if mouse_click[0] and self.mouse_over():
            return True
        return False
    
    def change_state(self, state: str) -> None:
        self.state = state
        self.image = pygame.image.load(self.images[self.state]).convert_alpha()

        self.rect = self.image.get_rect()
        scale = self.height / self.rect.height
        self.image = pygame.transform.scale(self.image, (int(self.rect.width * scale), int(self.rect.height * scale)))

        self.rect = self.image.get_rect()
        self.rect.x = self.x - self.rect.width / 2
        self.rect.y = self.y

        self.image.set_alpha(self.opacity[self.state])
    
    def update(self) -> None:
        if self.state == "selected" and pygame.key.get_pressed()[pygame.K_RETURN]:
            self.event(*self.event_args, **self.event_kwargs)

    def draw(self, screen) -> None:
        screen.blit(self.image, self.rect)

class ButtonPlay(Button):
    def __init__(self, game: Game) -> None:
        super().__init__(settings.PLAY_IMGS,
                         settings.WIDTH / 2, settings.PLAY_Y,
                         settings.PLAY_HEIGHT,
                         settings.PLAY_OPACITY,
                         game.change_state, PlayState(game))

class ButtonQuit(Button):
    def __init__(self, game: Game) -> None:
        super().__init__(settings.QUIT_IMGS,
                         settings.WIDTH / 2, settings.QUIT_Y,
                         settings.QUIT_HEIGHT,
                         settings.QUIT_OPACITY,
                         game.quit)
