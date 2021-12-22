#!/usr/bin/env python

import random
import pygame
import random
import time
from constant import *

#defines new enemy with health
class enemyShip(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image_orig = pygame.transform.scale(enemy_img, (50, 38))
        self.image_orig.set_colorkey(BLACK)
        self.image = self.image_orig.copy()
        self.rect = self.image.get_rect()
        self.radius = 20
        self.rect.centerx = WIDTH / 2
        self.rect.top = 20
        self.speedx = 5
        self.speedy = 3
        self.last_shot = pygame.time.get_ticks()
        self.shoot_delay = 250
        #self.last_update = pygame.time.get_ticks()

    def update(self):
        if (self.rect.right > WIDTH - 10):
            self.speedx = -5
            self.speedy = 3
        elif (self.rect.left < 10):
            self.speedx = 5
            self.speedy = -3
        if (self.rect.right > WIDTH / 2 and self.speedx == 5):
            self.speedy = 3
        elif (self.rect.left < WIDTH / 2 and self.speedx == -5):
            self.speedy = -3
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_SPACE]:
            self.shoot()

    def shoot(self):
        ##print('shoot')
        now = pygame.time.get_ticks()
        if now - self.last_shot > self.shoot_delay:
            self.last_shot = now
            bullet = Bullet(self.rect.centerx, self.rect.top)
            all_sprites.add(bullet)
            #bullets.add(bullet)
            #shooting_sound.play()
        """
        bullet = Bullet(self.rect.centerx, self.rect.top)
        all_sprites.add(bullet)
        bullets.add(bullet)"""
        

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        ##print('init bull')
        pygame.sprite.Sprite.__init__(self)
        self.image = ebullet_img
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        ## place the bullet according to the current position of the player
        self.rect.top = y 
        self.rect.centerx = x
        self.speedy = 10

    def update(self):
        ##print('updated bullet')
        """should spawn right in front of the player"""
        self.rect.y += self.speedy
        ## kill the sprite after it moves over the top border
        if self.rect.top > HEIGHT:
            self.kill()

        ## now we need a way to shoot
        ## lets bind it to "spacebar".
        ## adding an event for it in Game loop


       


    
