#!/usr/bin/env python3

"""scene_manager.py: SceneManager class."""

from __future__ import annotations

import pygame
from typing import List, Optional

from src.settings import Settings
settings = Settings()

from src.scenes.state import State

# Use a LIFO stack to manage scenes.
# The first scene in the queue is the current scene.
class SceneManager:
    def __init__(self, game: Game) -> None:
        self.game: Game = game

        self.scene_stack: List[State] = []

    def is_empty(self) -> bool:
        return not self.scene_stack
    
    def push(self, scene: State) -> None:
        self.scene_stack.append(scene)

    def pop(self) -> Optional[State]:
        if not self.is_empty():
            return self.scene_stack.pop()
        return None
    
from src.game import Game
