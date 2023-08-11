#!/usr/bin/env python3

"""scene_manager.py: SceneManager class."""

from __future__ import annotations

import pygame
from typing import List, Optional

from src.settings import Settings
settings = Settings()

from src.scenes.state import State

# Use a FIFO queue to manage the scenes.
# The first scene in the queue is the current scene.
class SceneManager:
    def __init__(self, game: Game) -> None:
        self.game: Game = game

        self.scene_queue: List[State] = []

    def is_empty(self) -> bool:
        return not self.scene_queue
    
    def enqueue(self, scene: State) -> None:
        self.scene_queue.append(scene)

    def dequeue(self) -> Optional[State]:
        if not self.is_empty():
            return self.scene_queue.pop(0)
        return None

from src.game import Game
