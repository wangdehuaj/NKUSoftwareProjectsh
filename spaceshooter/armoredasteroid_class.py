#!/usr/bin/env python

import random
import pygame
from mob_class import Mob
from constant import GREEN

class ArmoredAsteroid(Mob):
    def __init__(self):
        Mob.__init__(self)

        colorImage = pygame.Surface(self.image_orig.get_size()).convert_alpha()
        colorImage.fill(GREEN)
        self.image_orig.blit(colorImage, (0,0), special_flags = pygame.BLEND_RGBA_MULT)
        self.image = self.image_orig.copy()

        self.speedy = random.randrange(3, 8)