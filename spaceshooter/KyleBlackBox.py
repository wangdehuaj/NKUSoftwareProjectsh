# This is my attempt at black box testing

import pygame
from constant import *
from space_shooter import *
import enemyShip from enemyShip_class
import Bullet from bullet_class

# This opens the input file to get the direction/speed the enemy bullet will travel.
with open("spaceshooter/kyle_test_input.txt","r") as input_file:
    test = input_file.readlines()

# Remove white space characters
tests = [x.strip() for x in tests]

# open the output file for the test and test the bullets direction
with open("spaceshooter/kyle_test_output.txt", "w+") as output:
        for test in tests:  
            enemyResult = Bullet(enemyShip.rect.centerx, enemyShip.rect.bottom + 10, int(test))
            ShooterResult = Bullet(Player.rect.centerx, player.rect.top, int(test))
            position = Bullet.rect.bottom 

            # This gets the bullets direction toward the player
            if direction > 0 and position == enemyShip.rect.bottom:
                all_sprites.add(result)
                bullets.add(result)
                updates = true
                output.write("Tested: " + str(test) + " in Bullet and is headed towards player from enemy\n")
                continue
            # This gets the bullets heading the wrong way, away from the player    
            elif direction < 0 and position == player.rect.top:
                all_sprites.add(result)
                bullets.add(result)
                updates = true    
                output.write("Tested: " + str(test) + " in Bullet and is headed away from player to enemy\n")
                continue
            #This gets the bullets that dont move at all. They shouldn't be created or updated.   
            elif direction == 0:
                updates = false
                output.write("Tested: 0, and didnt create. Cant update in 0 direction\n")
                continue
            elif direction < 0 and position == enemyShip.rect.bottom:
                updates = false
                output.write("Tested: " + str(test) + " from enemy ship. cannot shoot backwards\n")
                continue
            elif direction > 0 and position == player.rect.top:
                updates = false
                output.write("Tested: " + str(test) + " from player ship. Cannot shoot backwards\n")
                continue
            else:
                output.write("Tested: " + str(test) + " and this should never happen\n")
                continue

            output.write("\nShooter\tDirection\tUpdate\n\n")    
            if direction > 0 and updates == true:
                output.write("EnemyShip\t" + str(test) + "\tYES\n")
                continue
            elif direction < 0 and updates == true:
                output.write("Player\t" + str(test) + "\tYES\n")
                continue
            elif position == enemyShip.rect.bottom:
                output.write("EnemyShip\t" + str(test) + "\tNO\n")
                continue
            elif position == player.rect.top:
                output.write("Player\t" + str(test) + "\tNO\n")
                continue
            else:
                output.write("NO! THIS SHOULDNT HAPPEN\n")
                continue
    
            
print("Done Testing")
                
