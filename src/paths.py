#!/usr/bin/env python3

"""paths.py: Paths to files."""

import os

ASSETS: str = os.path.join(os.path.dirname(__file__), "assets")
IMAGES: str = os.path.join(ASSETS, "images")
SPRITES: str = os.path.join(IMAGES, "sprites")
FONTS: str = os.path.join(ASSETS, "fonts")
SHADERS: str = os.path.join(ASSETS, "shaders")