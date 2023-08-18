#!/usr/bin/env python3

"""fps.py: FPS class."""

import os
from typing import Tuple

import src.paths as paths
from src.constants import WHITE, SEMI_TRANSLUCENT
from src.utils import scale_to_resolution

from src.ui.label import Label

class FPS(Label):
    X: int = scale_to_resolution(613)
    Y: int = scale_to_resolution(488)
    Y_PADDING: int = -6
    FONT: str = os.path.join(paths.FONTS, "Pixel Gosub.otf")
    SIZE: int = scale_to_resolution(13.5)
    COLOR: Tuple[int, int, int] = WHITE
    OPACITY: int = SEMI_TRANSLUCENT

    def __init__(self, fps: float = 0) -> None:
        super().__init__(text=f"FPS {fps:5.2f}",
                         font=FPS.FONT,
                         size=FPS.SIZE,
                         antialias=True,
                         color=FPS.COLOR,
                         opacity=FPS.OPACITY,
                         x=FPS.X,
                         y=FPS.Y + FPS.Y_PADDING)

    def update(self, fps: float) -> None:
        self.text = f"FPS {fps:5.2f}"
        super().update()
