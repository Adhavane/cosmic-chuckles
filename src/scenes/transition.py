#!/usr/bin/env python3

"""transition.py: TransitionState class."""

from __future__ import annotations

import pygame
from typing import Tuple
import random
import math

from src.settings import Settings
settings = Settings()

from src.scenes.state import State
from src.game import Game

class TransitionState(State):
    def __init__(self, game: Game, execution_time: int) -> None:
        super().__init__(game)

        self.execution_time: int = execution_time

        self.grid_size = 128  # Size of the grid
        self.square_size = math.ceil(settings.SCREEN_WIDTH / self.grid_size)  # Size of each square
        
        self.colors = []  # List to store random colors for each square
        # Generate random colors for each square
        for _ in range(self.grid_size):
            row_colors = []
            for _ in range(self.grid_size):
                color = [255, 255, 255, 0]
                row_colors.append(color)
            self.colors.append(row_colors)
        
        self.squares = []  # List to store the squares
        for y in range(self.grid_size):
            for x in range(self.grid_size):
                square = pygame.Surface((self.square_size, self.square_size))
                square.fill(self.colors[y][x])
                square.set_alpha(self.colors[y][x][3])
                square_rect = square.get_rect()
                square_rect.x = x * self.square_size
                square_rect.y = y * self.square_size
                self.squares.append((square, square_rect))

        self.fill_rate = round(self.grid_size * self.grid_size / self.execution_time)

    def events(self, _: pygame.event.Event) -> None:
        return super().events(_)
    
    def update(self) -> None:
        super().update()

        # Fill the grid with random squares
        filled = self.fill_rate
        while filled > 0:
            # Choose a random square
            y = random.randint(0, self.grid_size - 1)
            x = random.randint(0, self.grid_size - 1)
            # If the square is already filled, skip it
            if self.colors[y][x][3] == 255:
                continue

            # Set the alpha to 255
            self.colors[y][x][3] = 255
            # Update the square
            self.squares[y * self.grid_size + x][0].fill(self.colors[y][x])
            self.squares[y * self.grid_size + x][0].set_alpha(self.colors[y][x][3])

            filled -= 1

    def draw(self) -> None:
        super().draw()

        # Draw the squares
        for square in self.squares:
            self.game.display.blit(square[0], square[1])
        