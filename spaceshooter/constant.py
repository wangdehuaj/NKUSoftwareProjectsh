#!/usr/bin/env python

from os import path
import pygame

## assets folder
img_dir = path.join(path.dirname(__file__), 'assets')
sound_folder = path.join(path.dirname(__file__), 'sounds')

font_name = pygame.font.match_font('arial')

###############################
## to be placed in "constant.py" later
WIDTH = 480
HEIGHT = 600
FPS = 60
POWERUP_TIME = 5000
BAR_LENGTH = 100
BAR_HEIGHT = 10

# Define Colors 
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
###############################

###################################################
## Load all meteor explosion images
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Shooter")
print('Loading meteor images')
meteor_images = []
meteor_list = [
    'meteorBrown_big1.png',
    'meteorBrown_big2.png',
    'meteorBrown_med1.png',
    'meteorBrown_med3.png',
    'meteorBrown_small1.png',
    'meteorBrown_small2.png',
    'meteorBrown_tiny1.png'
]
missile_img = pygame.image.load(path.join(img_dir, 'missile.png')).convert_alpha()
enemy_img = pygame.image.load(path.join(img_dir, 'enemyShip_black.png')).convert()
bullet_img = pygame.image.load(path.join(img_dir, 'laserRed16.png')).convert()
ebullet_img = pygame.image.load(path.join(img_dir, 'laserYellow1.png')).convert()
all_sprites = pygame.sprite.Group()
bullets = pygame.sprite.Group()

for image in meteor_list:
    meteor_images.append(pygame.image.load(path.join(img_dir, image)).convert())
    
