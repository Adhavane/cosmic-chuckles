#!/usr/bin/env python3

"""fps.py: FPS class."""

from src.settings import Settings
settings = Settings()

from src.ui.label import Label

class FPS(Label):
    def __init__(self, fps: float = 0) -> None:
        super().__init__(f"FPS {fps:5.2f}", settings.FPS_FONT, settings.FPS_SIZE,
                         True, settings.FPS_COLOR, settings.FPS_OPACITY,
                         settings.FPS_X, settings.FPS_Y + settings.FPS_Y_PADDING)

    def update(self, fps: float) -> None:
        self.text = f"FPS {fps:5.2f}"
        super().update()
