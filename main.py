#!/usr/bin/env python

"""main.py: Main file for the game."""

import ctypes
ctypes.windll.user32.SetProcessDPIAware()

from game import Game

def main() -> None:
    game = Game()
    game.run()

if __name__ == "__main__":
    main()
