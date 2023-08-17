#!/usr/bin/env python3

"""main.py: Main file for the game."""

__author__ = "Adhavane Moudougannane"
__contact__ = "adhavane.moudougannane[at]etu[dot]utc[dot]fr"
__copyright__ = "Copyright 2023, Amoudou"
__credits__ = ["Adhavane Moudougannane"]
__date__ = "2023/07/23"
__email__ = "adhavane.moudougannane[at]etu[dot]utc[dot]fr"
__maintainer__ = "Adhavane Moudougannane"
__status__ = "Prototype"

import ctypes
ctypes.windll.user32.SetProcessDPIAware()

from src.game import Game

def main() -> None:
    game: Game = Game()
    game.run()

if __name__ == "__main__":
    import cProfile
    cProfile.run("print(main())", sort="cumtime")
    # main()
