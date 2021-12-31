#!/usr/bin/env python

import random
import pygame
import random
import time
from constant import *
from bullet_class import Bullet

#defines new enemy with health
class enemyShip(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image_orig = pygame.transform.scale(enemy_img, (50, 38))
        self.image_orig.set_colorkey(BLACK)
        self.image = self.image_orig.copy()
        self.rect = self.image.get_rect()
        self.radius = 20
        self.direction = 10
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
            ebullet = Bullet(self.rect.centerx, self.rect.top, self.direction)
            all_sprites.add(ebullet)
            bullets.add(ebullet)
            #shooting_sound.play()
        
    
