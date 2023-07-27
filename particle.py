#!/usr/bin/env python

"""particle.py: Particle class and subclasses."""

import random
from typing import Tuple

from settings import *
settings = Settings()

from projectile import Projectile

class Particle(Projectile):
    def __init__(self, color: Tuple[int, int, int], x: int, y: int) -> None:
        angle_min = 0
        angle_max = 360
        speed_min = 1
        speed_max = 3
        damage_min = 0
        damage_max = 0
        lifetime_min = 10
        lifetime_max = 20

        angle = random.randint(angle_min, angle_max)
        speed = random.randint(speed_min, speed_max)
        damage = random.randint(damage_min, damage_max)
        lifetime = random.randint(lifetime_min, lifetime_max)

        super().__init__(settings.PARTICLE_IMG, x, y, angle, speed, damage, lifetime)

        self.image.fill(color)
