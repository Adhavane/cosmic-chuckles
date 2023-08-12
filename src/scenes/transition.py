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

        self.start_time: int = pygame.time.get_ticks()
        self.end_time: int = self.start_time + execution_time

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
        
    def events(self, _: pygame.event.Event) -> None:
        return super().events(_)
    
    def update(self) -> None:
        super().update()

        # Update the colors of the squares
        for y in range(self.grid_size):
            for x in range(self.grid_size):
                if self.colors[y][x][3] != 255:
                    self.colors[y][x][3] = random.choice([0, 255])
                    print("Updated color")

    def draw(self) -> None:
        super().draw()

        for y in range(self.grid_size):
            for x in range(self.grid_size):
                color = tuple(self.colors[y][x])
                x_pos = x * self.square_size
                y_pos = y * self.square_size
                pygame.draw.rect(self.game.display, color, (x_pos, y_pos, self.square_size, self.square_size))
