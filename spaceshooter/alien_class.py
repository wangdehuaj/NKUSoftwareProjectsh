import pygame
import random

from os import path
from constant import *


alien_img =  pygame.image.load(path.join(img_dir, 'alienShip_1.png')).convert()

## changed / added Alien
class Alien(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image_orig = pygame.transform.scale(alien_img, (60, 45))
        self.image_orig.set_colorkey(BLACK)
        self.image = self.image_orig.copy()
        self.rect = self.image.get_rect()
        self.radius = 10
        self.rect.centerx = 0
        self.rect.top = 20 

        ## randomize the movements a little more 
        self.speedx = random.randrange(5, 10)
        
        self.last_update = pygame.time.get_ticks()  ## time when the rotation has to happen
        
    def update(self):
        self.rect.x += self.speedx
        ## now what if the mob element goes out of the screen

## exit
        if (self.rect.right > WIDTH + 20):
            self.rect.x = 0
