#!/usr/bin/env python3

"""particle.py: Particle class and subclasses."""

import random
from typing import List, Tuple

from constants import Settings
settings = Settings()

from src.prefabs.projectile import Projectile

class Particle(Projectile):
    def __init__(self, colors: Tuple[List[Tuple[int, int, int]], List[int]], x: int, y: int) -> None:
        color = random.choices(colors[0], weights=colors[1], k=1)[0]
        height = random.randint(settings.PARTICLE_HEIGHT_MIN, settings.PARTICLE_HEIGHT_MAX)
        angle = random.randint(settings.PARTICLE_ANGLE_MIN, settings.PARTICLE_ANGLE_MAX)
        damage = random.randint(settings.PARTICLE_DAMAGE_MIN, settings.PARTICLE_DAMAGE_MAX)
        speed = random.randint(settings.PARTICLE_SPEED_MIN, settings.PARTICLE_SPEED_MAX)
        lifetime = random.randint(settings.PARTICLE_LIFETIME_MIN, settings.PARTICLE_LIFETIME_MAX)

        super().__init__(settings.PARTICLE_IMG,
                         x, y, height,
                         angle, damage, speed, lifetime)

        self.image.fill(color)

    def destroy(self) -> None:
        super().destroy()
        self.kill()
