import pygame
from constant import *
from space_shooter import *
from enemyShip_class import enemyShip
from bullet_class import Bullet

class BulletHandler(pygame.sprite.Sprite):
    def __init__(self, direction):
        if (direction == 0):
            print("0\t\tNo\t\tNo\n")
        elif (direction > 0):
            print(str(direction) + "\t\tNo\t\tYes\n")
        elif (direction < 0):
            print(str(direction) + "\t\tYes\t\tNo\n")
        
    
