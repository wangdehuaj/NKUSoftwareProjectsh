#!/usr/bin/env python

import unittest
from armoredasteroid_class import ArmoredAsteroid
from constant import BLACK

# Test cases for Explosion class
class TestArmoredAsteroid(unittest.TestCase):

    def setUp(self):
        self.test_armoredasteroid = ArmoredAsteroid()

    def test_color(self):
        self.assertEqual(self.test_armoredasteroid.image.get_colorkey, BLACK)