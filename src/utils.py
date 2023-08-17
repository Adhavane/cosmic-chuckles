#!/usr/bin/env python3

"""utils.py: Utility functions."""

from constants import LAST_TIME, DELTA_TIME, SCALE_FACTOR

import time
from typing import List, Tuple
from PIL import Image, ImageDraw

def get_delta_time() -> float:
    """Returns the time between two frames."""
    global LAST_TIME
    global DELTA_TIME
    current_time: float = time.time()
    DELTA_TIME = current_time - LAST_TIME
    LAST_TIME = current_time
    return DELTA_TIME

def scale_to_resolution(size: int) -> int:
    """Scales a size to the current resolution."""
    global SCALE_FACTOR
    return round(size * SCALE_FACTOR)

def extract_color_palette(image: str) -> Tuple[List[Tuple[int, int, int]], List[int]]:
    """Extracts color palettes from an image."""
    img: Image.Image = Image.open(image)
    colors: List[Tuple[int, int, int]] = img.getcolors(maxcolors=256)
    palette: List[Tuple[int, int, int]] = [color for (_, color) in colors]
    weights: List[int] = [count for (count, _) in colors]
    return palette, weights
