#!/usr/bin/env python3

"""particle.py: Particle class and subclasses."""

import os
import random
from typing import List, Tuple

import src.paths as paths
from src.utils import scale_to_resolution

from src.prefabs.projectile import Projectile

class Particle(Projectile):
    IMG: str = os.path.join(paths.SPRITES, "particle.png")
   
    HEIGHT_MIN: int = scale_to_resolution(1)
    HEIGHT_MAX: int = scale_to_resolution(5)
    
    ANGLE_MIN: int = 0
    ANGLE_MAX: int = 360

    DAMAGE_MIN: int = 0
    DAMAGE_MAX: int = 0

    SPEED_MIN: int = 1
    SPEED_MAX: int = 5

    LIFETIME_MIN: int = 1
    LIFETIME_MAX: int = 30

    def __init__(self, colors: Tuple[List[Tuple[int, int, int]], List[int]], x: int, y: int) -> None:
        color = random.choices(colors[0], weights=colors[1], k=1)[0]
        height = random.randint(Particle.HEIGHT_MIN, Particle.HEIGHT_MAX)
        angle = random.randint(Particle.ANGLE_MIN, Particle.ANGLE_MAX)
        damage = random.randint(Particle.DAMAGE_MIN, Particle.DAMAGE_MAX)
        speed = random.randint(Particle.SPEED_MIN, Particle.SPEED_MAX)
        lifetime = random.randint(Particle.LIFETIME_MIN, Particle.LIFETIME_MAX)

        super().__init__(Particle.IMG,
                         x, y, height,
                         angle, damage, speed, lifetime)

        self.image.fill(color)

    def destroy(self) -> None:
        super().destroy()
        self.kill()
