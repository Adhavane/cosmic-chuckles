#!/usr/bin/env python

"""enemy.py: Enemy class and subclasses."""

import pygame
from abc import ABC, abstractmethod

from settings import *
settings = Settings()

class Enemy(ABC, pygame.sprite.Sprite):
    pass
