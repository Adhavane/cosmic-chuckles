#!/usr/bin/env python3

"""transition.py: TransitionState class."""

from __future__ import annotations

import pygame
from typing import Callable, Tuple
import random
import math

from src.settings import Settings
settings = Settings()

from src.scenes.state import State
from src.game import Game

class TransitionState(State):
    def __init__(self, game: Game, script: Callable,
                 execution_time: int) -> None:
        super().__init__(game)

        self.execution_time: int = execution_time

        self.grid_size = 32  # Size of the grid
        self.square_size = math.ceil(settings.SCREEN_WIDTH / self.grid_size)  # Size of each square
        
        self.colors = []  # List to store random colors for each square
        for _ in range(self.grid_size):
            row_colors = []
            for _ in range(self.grid_size):
                row_colors.append(settings.BLACK)
            self.colors.append(row_colors)

        self.squares = []  # List to store the squares
        self.squares_unfilled = []  # List to store the unfilled squares
        for y in range(self.grid_size):
            for x in range(self.grid_size):
                square = pygame.Surface((self.square_size, self.square_size))
                square.fill(self.colors[y][x])
                square.set_alpha(self.colors[y][x][3])
                square_rect = square.get_rect()
                square_rect.x = x * self.square_size
                square_rect.y = y * self.square_size
                self.squares.append((square, square_rect))
                self.squares_unfilled.append((square, square_rect))
        
        self.script = script
        self.fill_rate = round(self.grid_size * self.grid_size / self.execution_time * settings.FPS)

    def events(self, _: pygame.event.Event) -> None:
        return super().events(_)
    
    def update(self) -> None:
        super().update()

        self.script()

    def fade_in(self) -> None:
        self.fade(255)

    def fade_out(self) -> None:
        self.fade(0)

    def fade(self, opacity: int) -> None:
        # Fill the grid with random squares
        for _ in range(self.fill_rate):
            if len(self.squares_unfilled) > 0:
                square = self.squares_unfilled.pop(random.randrange(len(self.squares_unfilled)))
                y_index = square[1].y // self.square_size
                x_index = square[1].x // self.square_size
                self.colors[y_index][x_index][3] = opacity
                square[0].fill(self.colors[y_index][x_index])
                square[0].set_alpha(self.colors[y_index][x_index][3])

        # Check if the grid is filled
        if self.check_done():
            self.game.next_state()

    def check_done(self) -> bool:
        for y in range(self.grid_size):
            for x in range(self.grid_size):
                if self.colors[y][x][3] == 0:
                    return False
        return True

    def draw(self) -> None:
        super().draw()

        # Draw the squares
        for square in self.squares:
            if square[0].get_alpha() > 0:
                self.game.display.blit(square[0], square[1])
