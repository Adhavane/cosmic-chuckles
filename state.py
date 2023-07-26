#!/usr/bin/env python

"""state.py: State class."""

from abc import ABC, abstractmethod

class State(ABC):
    def __init__(self, game) -> None:
        self.game = game
