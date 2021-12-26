#!/usr/bin/env python

import unittest
from enemyShip_class import enemyShip
from space_shooter import newEnemy

# Test cases for Explosion class
class TestEnemyShip(unittest.TestCase):

    def setUp(self):
        self.enemyShip = newEnemy()
        self.test_explosion = Explosion(test_enemyShip.rect.center, 'enemy')

    def tearDown(self):
        self.test_explosion.update()
        self.assertEqual(self.test_explosion.frame, 1)
    
    def test_update(self):
        newPosition = self.rect.x + self.speedx
        self.assertEqual(calc.add(self.rect.x, self.speedx), newPosition)


if __name__ == '__main__':
    unittest.main()
