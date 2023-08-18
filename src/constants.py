#!/usr/bin/env python3

"""settings.py: Settings for the game."""

import time

class Timer:
    LAST_TIME = time.time()
    DELTA_TIME = 0

TIMER = Timer()

# Screen settings for format 4:3
SCALE_FACTOR = 2
SCREEN_WIDTH = 690 * SCALE_FACTOR
SCREEN_HEIGHT = 512 * SCALE_FACTOR

FPS = 60

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0 , 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

OPAQUE = 255
SEMI_OPAQUE = 192
TRANSLUCENT = 128
SEMI_TRANSLUCENT = 64
TRANSPARENT = 0
