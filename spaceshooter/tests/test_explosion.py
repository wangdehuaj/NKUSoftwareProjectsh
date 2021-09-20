#!/usr/bin/env python

import unittest
from explosion_class import Explosion
from space_shooter import Player

# Test cases for Explosion class
class TestExplosion(unittest.TestCase):

    def setUp(self):
        test_player = Player()
        self.test_explosion = Explosion(test_player.rect.center, 'lg')

    def test_update(self):
        self.test_explosion.update()
        self.assertEqual(self.test_explosion.frame, 1)
