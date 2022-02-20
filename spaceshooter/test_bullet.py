#!/usr/bin/env python

import unittest
from bullet_class import Bullet
from space_shooter import *
from enemyShip_class import *


# Test cases for Explosion class
class Bullet(unittest.TestCase):

    def test_bullet(self):
        self.assertEqual(player.bulletstatus, 1)

    def test_direction(self):
        self.assertEqual(player.direction, -10)
        self.assertEqual(eShip.direction, 10)
        
    def test_playerUpdate(self):
        position = player.rect.y
        movement = position - 10
        player.rect.y += player.direction
        self.assertEqual(player.rect.y, movement)

    def test_enemyUpdate(self):
        position = eShip.rect.y
        movement = position + 10
        eShip.rect.y += eShip.direction
        self.assertEqual(eShip.rect.y, movement)
        

if __name__ == '__main__':
    unittest.main()
