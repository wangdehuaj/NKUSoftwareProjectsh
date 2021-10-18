#!/usr/bin/env python

import unittest
from enemyShip_class import enemyShip
from space_shooter import Player

# Test cases for Explosion class
class TestExplosion(unittest.TestCase):

    def setUp(self):
        test_enemyShip = enemyShip()
        self.test_explosion = Explosion(test_enemyShip.rect.center, 'enemy')

    def test_update(self):
        self.test_explosion.update()
        self.assertEqual(self.test_explosion.frame, 1)
    print("\nFinish get_name test\n")

if __name__ == '__main__':
    unittest.main()
