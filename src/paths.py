#!/usr/bin/env python3

"""paths.py: Paths to files."""

import os

SRC: str = os.path.dirname(__file__)

SHADERS: str = os.path.join(SRC, "shaders")

ASSETS: str = os.path.join(os.path.dirname(SRC), "assets")
IMAGES: str = os.path.join(ASSETS, "images")
SPRITES: str = os.path.join(ASSETS, "sprites")
FONTS: str = os.path.join(ASSETS, "fonts")
