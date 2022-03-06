import pygame
from constant import *
from space_shooter import *
from enemyShip_class import enemyShip
from bullet_class import Bullet


# This opens the input file to get the direction/speed the enemy bullet will travel.
with open("kyle_test_input.txt","r") as input_file:
    tests = input_file.readlines()

# whitespace deletion
tests = [x.strip() for x in tests]

# open the output file for the test and test the bullets direction
with open("kyle_test_output.txt", "w+") as output:
        for test in tests:
            x = WIDTH / 2
            position = HEIGHT / 4
            direction = int(test)
            result = Bullet(x, position, direction)

            #position = 3 * HEIGHT / 4
            #result = Bullet(x, position, direction)

            if direction > 0 and position == HEIGHT / 4:
                output.write("Tested: " + str(test) + " for enemy to player\n")
                update = True
                continue
            elif direction < 0 and position == HEIGHT / 4:
                output.write("Tested: " + str(test) + " for enemy shooting away\n")
                update = False
                continue
            elif direction > 0 and position == 3 * HEIGHT / 4:
                output.write("Tested: " + str(test) + " for player shooting away\n")
                update = False
                continue
            elif direction < 0 and position == 3 * HEIGHT / 4:
                output.write("Tested: " + str(test) + " for player shooting to enemy\n")
                update = True
                continue
            elif direction == 0:
                output.write("Tested: " + str(test) + " cannot happen\n")
                update = False
                continue
            else:
                output.write("Tested: " + str(test) + " THIS SHOULD NEVER HAPPEN\n")
                update = False
                continue

            output.write("\nShooter\tDirection\tUpdate\n\n")    
            if direction > 0 and updates == True:
                output.write("EnemyShip\t" + str(test) + "\tYES\n")
                continue
            elif direction < 0 and updates == True:
                output.write("Player\t" + str(test) + "\tYES\n")
                continue
            elif position == HEIGHT / 4:
                output.write("EnemyShip\t" + str(test) + "\tNO\n")
                continue
            elif position == 3 * HEIGHT / 4:
                output.write("Player\t" + str(test) + "\tNO\n")
                continue
            else:
                output.write("NO! THIS SHOULDNT HAPPEN\n")
                continue

            
            
