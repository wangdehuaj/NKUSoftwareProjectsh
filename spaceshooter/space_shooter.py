
from explosion_class import Explosion
from mob_class import Mob
from enemyShip_class import enemyShip
from alien_class import Alien
from bullet_class import Bullet
from pow_class import Pow
from armoredasteroid_class import ArmoredAsteroid
from missile_class import *

# ## assets folder
# img_dir = path.join(path.dirname(__file__), 'assets')
# sound_folder = path.join(path.dirname(__file__), 'sounds')

# font_name = pygame.font.match_font('arial')

###############################
## to placed in "__init__.py" later
## initialize pygame and create window
pygame.init()
pygame.mixer.init()  ## For sound
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Shooter")
clock = pygame.time.Clock()     ## For syncing the FPS
###############################


global player_hide_timer 
player_hide_timer = pygame.time.get_ticks()
global player_lives
player_lives = 3



def main_menu():
    global screen

    menu_song = pygame.mixer.music.load(path.join(sound_folder, "menu.ogg"))
    pygame.mixer.music.play(-1)

    title = pygame.image.load(path.join(img_dir, "main.png")).convert()
    title = pygame.transform.scale(title, (WIDTH, HEIGHT), screen)

    screen.blit(title, (0, 0))
    pygame.display.update()

    while True:
        ev = pygame.event.poll()
        if ev.type == pygame.KEYDOWN:
            if ev.key == pygame.K_RETURN:
                break
            elif ev.key == pygame.K_q:
                pygame.quit()
                quit()
        elif ev.type == pygame.QUIT:
            pygame.quit()
            quit()
        else:
            text_file = open("high_scores.txt", "w+")
            whole_thing = text_file.read()
            draw_text(screen, "High_score :" + whole_thing , 50, WIDTH/2, (HEIGHT/2) + 100 )
            text_file.close()
            
            draw_text(screen, "Press [ENTER] To Begin", 30, WIDTH/2, HEIGHT/2)
            draw_text(screen, "or [Q] To Quit", 30, WIDTH/2, (HEIGHT/2)+40)
            pygame.display.update()

    #pygame.mixer.music.stop()
    ready = pygame.mixer.Sound(path.join(sound_folder, 'getready.ogg'))
    ready.play()
    screen.fill(BLACK)
    draw_text(screen, "GET READY!", 40, WIDTH/2, HEIGHT/4)
    draw_text(screen, "Instructions: ", 30, WIDTH/2, HEIGHT/2)    
    draw_text(screen, "Use the arrow keys to move, ", 20, WIDTH/2, (HEIGHT/2)+30)
    draw_text(screen, "press [SPACE] to fire, ", 20, WIDTH/2, (HEIGHT/2)+55)
    draw_text(screen, "press [p] to pause, ", 20, WIDTH/2, (HEIGHT/2)+80)
    draw_text(screen, "press [ENTER] to resume, ", 20, WIDTH/2, (HEIGHT/2)+105)
    draw_text(screen, "press [esc] to leave the game, ", 20, WIDTH/2, (HEIGHT/2)+130)
    draw_text(screen, "press [m] to mute/unmute ", 20, WIDTH/2, (HEIGHT/2)+155)
    
    pygame.display.update()


def draw_text(surf, text, size, x, y):
    ## selecting a cross platform font to display the score
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, WHITE)       ## True denotes the font to be anti-aliased
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)


def draw_shield_bar(surf, x, y, pct):
    # if pct < 0:
    #     pct = 0
    pct = max(pct, 0) 
    ## moving them to top
    # BAR_LENGTH = 100
    # BAR_HEIGHT = 10
    fill = (pct / 100) * BAR_LENGTH
    outline_rect = pygame.Rect(x, y, BAR_LENGTH, BAR_HEIGHT)
    fill_rect = pygame.Rect(x, y, fill, BAR_HEIGHT)
    pygame.draw.rect(surf, GREEN, fill_rect)
    pygame.draw.rect(surf, WHITE, outline_rect, 2)

def draw_lives(surf, x, y, lives, img):
    for i in range(lives):
        img_rect= img.get_rect()
        img_rect.x = x + 30 * i
        img_rect.y = y
        surf.blit(img, img_rect)

def draw_bulletstatus(surf, x, y, bulletstatus, img):
    for i in range(bulletstatus):
        img_rect= img.get_rect()
        img_rect.x = x + 30 * i
        img_rect.y = y
        surf.blit(img, img_rect)
        
def draw_missiletatus(surf, x, y, missilestatus, img):
    for i in range(missilestatus):
        img_rect= img.get_rect()
        img_rect.x = x + 30 * i
        img_rect.y = y
        surf.blit(img, img_rect)

## changed/added alien
def newalien():
    alien = Alien()
    all_sprites.add(alien)
    mobs.add(alien)

def newmob(health): #Evan
    if health != 100:
        mob_element = Mob()
        all_sprites.add(mob_element)
        mobs.add(mob_element)
        return 1
    else:
        for i in range(2):
            mob_element = Mob()
            all_sprites.add(mob_element)
            mobs.add(mob_element)
        return 2


def newArmoredAsteroid(): #Evan
    aa_element = ArmoredAsteroid()
    all_sprites.add(aa_element)
    aas.add(aa_element)

def newEnemy():
    enemy = enemyShip()
    all_sprites.add(enemy)
    mobs.add(enemy)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        ## scale the player img down
        self.image = pygame.transform.scale(player_img, (50, 38))
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.radius = 20
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGHT - 10
        self.speedx = 0
        self.speedy = 0
        self.shield = 100
        self.direction = -10
        self.bulletstatus = 0
        self.missilestatus = 0
        self.shoot_delay = 250
        self.last_shot = pygame.time.get_ticks()
        self.hidden = False
        self.power = 1
        self.power_timer = pygame.time.get_ticks()

    def reset(self):
        self.__init__()

    def update(self):
        ## time out for powerups
        if self.power >=2 and pygame.time.get_ticks() - self.power_time > POWERUP_TIME:
            self.power -= 1
            self.power_time = pygame.time.get_ticks()

        ## unhide
        

        self.speedx = 0
        self.speedy = 0## makes the player static in the screen by default. 
        # then we have to check whether there is an event hanlding being done for the arrow keys being 
        ## pressed 

        ## will give back a list of the keys which happen to be pressed down at that moment
        keystate = pygame.key.get_pressed()     
        if keystate[pygame.K_LEFT]:
            self.speedx = -5
        if keystate[pygame.K_RIGHT]:
            self.speedx = 5
        if keystate[pygame.K_UP]:
            self.speedy = -5
        if keystate[pygame.K_DOWN]:
            self.speedy = 5

        #Fire weapons by holding spacebar
        if keystate[pygame.K_SPACE] and self.hidden == False:
            self.shoot()

        ## check for the borders at the left and right
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.bottom < 38:
            self.rect.bottom = 38
        if self.rect.top > HEIGHT-38:
            self.rect.top = HEIGHT-38
            
        self.rect.x += self.speedx
        self.rect.y += self.speedy

    def shoot(self):
        ## to tell the bullet where to spawn
        now = pygame.time.get_ticks()
        if now - self.last_shot > self.shoot_delay:
            self.last_shot = now
            if self.power == 1:
                self.bulletstatus = 1
                self.missilestatus = 0
                bullet = Bullet(self.rect.centerx, self.rect.top, self.direction)
                all_sprites.add(bullet)
                weapons.add(bullet)
                shooting_sound.play()

            if self.power == 2:
                self.bulletstatus = 2
                self.missilestatus = 0
                weaponslot1 = Bullet(self.rect.left, self.rect.centery, self.direction)
                weaponslot2 = Bullet(self.rect.right, self.rect.centery, self.direction)
                all_sprites.add(weaponslot1)
                all_sprites.add(weaponslot2)
                weapons.add(weaponslot1)
                weapons.add(weaponslot2)
                shooting_sound.play()

            if self.power == 3:
                self.bulletstatus = 3
                self.missilestatus = 0
                weaponslot1 = Bullet(self.rect.left, self.rect.centery, self.direction) # bullet shoots from left of ship
                weaponslot2 = Bullet(self.rect.right, self.rect.centery, self.direction)# bullet shoots from right of ship
                weaponslot3 = Bullet(self.rect.centerx, self.rect.top, self.direction) # bullet shoots from center of ship
                all_sprites.add(weaponslot1)
                all_sprites.add(weaponslot2)
                all_sprites.add(weaponslot3)
                weapons.add(weaponslot1)
                weapons.add(weaponslot2)
                weapons.add(weaponslot3)
                shooting_sound.play()

            if self.power == 4:
                self.missilestatus = 1
                weaponslot1 = Bullet(self.rect.left, self.rect.centery, self.direction) # Bullet shoots from left of ship
                weaponslot2 = Bullet(self.rect.right, self.rect.centery, self.direction)# Bullet shoots from right of ship
                weaponslot3 = Missile(self.rect.centerx, self.rect.top) # Missile shoots from center of ship
                all_sprites.add(weaponslot1)
                all_sprites.add(weaponslot2)
                all_sprites.add(weaponslot3)
                weapons.add(weaponslot1)
                weapons.add(weaponslot2)
                weapons.add(weaponslot3)
                shooting_sound.play()
                missile_sound.play()

            if self.power >= 5:
                self.missilestatus = 3
                weaponslot1 = Missile(self.rect.left, self.rect.centery) # Missile shoots from left of ship
                weaponslot2 = Missile(self.rect.right, self.rect.centery)# Missile shoots from right of ship
                weaponslot3 = Missile(self.rect.centerx, self.rect.top) # Missile shoots from center of ship
                all_sprites.add(weaponslot1)
                all_sprites.add(weaponslot2)
                all_sprites.add(weaponslot3)
                weapons.add(weaponslot1)
                weapons.add(weaponslot2)
                weapons.add(weaponslot3)
                missile_sound.play()

    def powerup(self):
        self.power += 1
        self.power_time = pygame.time.get_ticks()
        

    def hide(self):
        global player_hide_timer
        player_hide_timer = pygame.time.get_ticks()
        self.kill()


def check_player(player_status, death_time):
    if player_status and death_time > 1000:
        global player
        player = Player()
        player.rect.centerx = WIDTH / 2
        player.rect.bottom = HEIGHT - 30
        all_sprites.add(player)
        return 0
    else:
        # print('death timer insufficeient')
        return 1

###################################################
## Load all game images

background = pygame.image.load(path.join(img_dir, 'starfield.png')).convert()
background_rect = background.get_rect()
## ^^ draw this rect first

player_img = pygame.image.load(path.join(img_dir, 'playerShip1_orange.png')).convert()
bullet_img = pygame.image.load(path.join(img_dir, 'laserRed16.png')).convert()
player_mini_img = pygame.transform.scale(player_img, (25, 19))
player_mini_img.set_colorkey(BLACK)
bullet_mini_img = pygame.transform.scale(bullet_img, (10, 19))
bullet_mini_img.set_colorkey(BLACK)
missile_mini_img = pygame.transform.scale(missile_img, (12, 19))
missile_mini_img.set_colorkey(BLACK)

###################################################


###################################################
### Load all game sounds
shooting_sound = pygame.mixer.Sound(path.join(sound_folder, 'pew.wav'))
missile_sound = pygame.mixer.Sound(path.join(sound_folder, 'rocket.ogg'))
expl_sounds = []
for sound in ['expl3.wav', 'expl6.wav']:
    expl_sounds.append(pygame.mixer.Sound(path.join(sound_folder, sound)))
## main background music
#pygame.mixer.music.load(path.join(sound_folder, 'tgfcoder-FrozenJam-SeamlessLoop.ogg'))
pygame.mixer.music.set_volume(0.2)      ## simmered the sound down a little

player_die_sound = pygame.mixer.Sound(path.join(sound_folder, 'rumble1.ogg'))
###################################################

## TODO: make the game music loop over again and again. play(loops=-1) is not working
# Error :
# TypeError: play() takes no keyword arguments
#pygame.mixer.music.play()

#############################
## Game loop
running = True
menu_display = True
pause = False
mute = False

player = Player()

while running:
    if menu_display:
        main_menu()
        pygame.time.wait(3000)

        #Stop menu music
        pygame.mixer.music.stop()
        #Play the gameplay music
        pygame.mixer.music.load(path.join(sound_folder, 'tgfcoder-FrozenJam-SeamlessLoop.ogg'))
        pygame.mixer.music.play(-1)     ## makes the gameplay sound in an endless loop

        menu_display = False

        ## group all the sprites together for ease of update
        all_sprites.add(player)
        eShip = enemyShip()

    ## changed how many spawn
        ## spawn a group of mob
        mobs = pygame.sprite.Group()
        aas = pygame.sprite.Group()
        for i in range(random.randint(5,9)):
            newmob(player.shield)
            
        for i in range(random.randint(1,3)):
            newArmoredAsteroid()

        newEnemy()
        

        ## group for bullets
        weapons = pygame.sprite.Group()
        powerups = pygame.sprite.Group()

        #### Score board variable
        score = 0

        

        

    #1 Process input/events
    clock.tick(FPS)     ## will make the loop run at the same speed all the time
    for event in pygame.event.get(): # gets all the events which have occured till now and keeps tab of them.
        ## listening for the the X button at the top
        if event.type == pygame.QUIT:
            running = False

        ## Press ESC to exit game
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
        # ## event for shooting the bullets
        # elif event.type == pygame.KEYDOWN:
        #     if event.key == pygame.K_SPACE:
        #         player.shoot()      ## we have to define the shoot()  function
            elif event.key == pygame.K_p:
               pause = True
            elif event.key == pygame.K_m:
                mute = not mute
    #2 Update
    if pause == False:
        all_sprites.update()

    if mute == True:
        pygame.mixer.pause()
        pygame.mixer.music.pause()
    else:
        pygame.mixer.unpause()
        pygame.mixer.music.unpause()


    check_player(not player.alive(), pygame.time.get_ticks() - player_hide_timer)

    ## check if a bullet hit a mob
    ## now we have a group of bullets and a group of mob
    hits = pygame.sprite.groupcollide(mobs, weapons, True, True) #Evan
    aa_hits = pygame.sprite.groupcollide(aas, weapons, False, True) #Evan
    ## now as we delete the mob element when we hit one with a bullet, we need to respawn them again
    ## as there will be no mob_elements left out
    for hit in hits:
        ## give different scores for hitting big and small metoers
        #Changed how things are scored
        radius = hit.radius
        if radius < 10:
            gotScore = 50
        elif radius == 10:
            gotScore = 500
        elif radius < 15:
            gotScore = 40
        elif radius < 30:
            gotScore = 30
        elif radius < 50:
            gotScore = 20
        elif radius < 55:
            gotScore = 10
        else:
            gotScore = 5
        score += gotScore
        random.choice(expl_sounds).play()
        # m = Mob()
        # all_sprites.add(m)
        # mobs.add(m)
        expl = Explosion(hit.rect.center, 'lg')
        all_sprites.add(expl)
        if random.random() > 0.9:
            pow = Pow(hit.rect.center)
            all_sprites.add(pow)
            powerups.add(pow)
        newmob(player.shield)        ## spawn a new mob

        ##Added alien
        if (score % 1000 == 0):
            newalien()
                


    ## ^^ the above loop will create the amount of mob objects which were killed spawn again
    #########################
   

    ## check if the player collides with the mob
    hits = pygame.sprite.spritecollide(player, mobs, True, pygame.sprite.collide_circle) ## gives back a list, True makes the mob element disappear

    if player.alive():
        for hit in hits:
            player.shield -= hit.radius * 2
            expl = Explosion(hit.rect.center, 'sm')
            all_sprites.add(expl)
            newmob(player.shield)
            if player.shield <= 0: 
                player_die_sound.play()
                death_explosion = Explosion(player.rect.center, 'lg')
                all_sprites.add(death_explosion)
                # running = False     ## GAME OVER 3:D
                #player.hide()
                player_lives -= 1
                player.shield = 100

    ## check if the player collides with the armored asteroid
    hits = pygame.sprite.spritecollide(player, aas, True, pygame.sprite.collide_circle) ## gives back a list, True makes the mob element disappear
    if player.alive():
        for hit in hits:
            player.shield -= hit.radius * 2
            expl = Explosion(hit.rect.center, 'sm')
            all_sprites.add(expl)
            newArmoredAsteroid()
            if player.shield <= 0: 
                player_die_sound.play()
                death_explosion = Explosion(player.rect.center, 'lg')
                all_sprites.add(death_explosion)
                # running = False     ## GAME OVER 3:D
                player.hide()
                player_lives -= 1
                player.shield = 100    

    ## if the player hit a power up
    hits = pygame.sprite.spritecollide(player, powerups, True)
    for hit in hits:
        if hit.type == 'shield':
            player.shield += random.randrange(10, 30)
            if player.shield >= 100:
                player.shield = 100
        if hit.type == 'gun':
            player.powerup()

    ## if player died and the explosion has finished, end game
    if player_lives <= 0 and not death_explosion.alive():
        running = False

        ## write high score
        # with ("high_scores.txt", "r") as f:
        #     data = f.read()

        #     if data == '':
        #         data = 0
        #     data1 = int(data)
        #     f.close()
        #     if(data1 < score):
        #         with open("high_scores.txt", "w") as f:       
        #             f.write(str(score))
        #     f.close()
            
        # menu_display = True
        # pygame.display.update()

    #3 Draw/render
    screen.fill(BLACK)
     ## draw the stargaze.png image
    screen.blit(background, background_rect)

    all_sprites.draw(screen)
    draw_text(screen, str(score), 18, WIDTH / 2, 10)     ## 10px down from the screen
    draw_shield_bar(screen, 5, 5, player.shield)

    # Draw lives
    draw_lives(screen, WIDTH - 100, 5, player_lives, player_mini_img)
    draw_bulletstatus(screen, WIDTH - 90, 35, player.bulletstatus, bullet_mini_img)
    draw_missiletatus(screen, WIDTH - 40, 35, player.missilestatus, missile_mini_img)

    ## Done after drawing everything to the screen
    pygame.display.flip()

    ## Replay function
    if running == False:
        while True:
            ev = pygame.event.poll()
            if ev.type == pygame.KEYDOWN:
                if ev.key == pygame.K_RETURN:
                    all_sprites.empty()
                    player.reset()
                    player_lives = 3
                    running = True
                    menu_display = True
                    break
                elif ev.key == pygame.K_q:
                    pygame.quit()
                    break
            elif ev.type == pygame.QUIT:
                 pygame.quit()
                 break
            else:
                 draw_text(screen, "Press [ENTER] to Replay", 30, WIDTH/2, HEIGHT/2)
                 draw_text(screen, "or [Q] to Quit", 30, WIDTH/2, (HEIGHT/2)+40)
                 pygame.display.update()
    ## Pause code
    if pause == True:
        while True:
            pygame.mixer.music.pause()
            ev = pygame.event.poll()
            if ev.type == pygame.KEYDOWN:
                if ev.key == pygame.K_RETURN:
                    pause = False
                    pygame.mixer.music.unpause()
                    break
                elif ev.key == pygame.K_ESCAPE:
                    running = False
                    pygame.quit()
                    
            else:
                draw_text(screen, "Game Paused...", 30, WIDTH/2, HEIGHT/2)
                draw_text(screen, "Press [ENTER] to resume game", 30, WIDTH/2, (HEIGHT/2)+40)
                draw_text(screen, "or [ESC] to exit game", 30, WIDTH/2, (HEIGHT/2)+80)
                pygame.display.update()
pygame.quit()
