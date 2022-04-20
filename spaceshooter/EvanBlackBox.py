#!/usr/bin/env python

import pygame

from mob_class import Mob

#-------- This is the method I wanted to test, but trying to import it just launches the game..... so I brought it here for proof of concept.
all_sprites = pygame.sprite.Group()
mobs = pygame.sprite.Group()

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

#----------- Start black box testing
with open("spaceshooter/evan_test_input.txt", "r") as input_file:
    tests = input_file.readlines()

# you may also want to remove whitespace characters like `\n` at the end of each line
tests = [x.strip() for x in tests]

with open("spaceshooter/evan_test_output.txt", "w+") as output:
    for test in tests:
        result = newmob(int(test))

        if test == '100' and result == 2:
            output.write("Tested: " + str(test).ljust(4) + " in newmob(). " "Result: " + str(result).ljust(4) + " -Passed" + "\n")
            continue
        elif test != '100' and result == 2:
            output.write("Tested: " + str(test).ljust(4) + " in newmob(). " "Result: " + str(result).ljust(4) + " -Failed" + "\n")
            continue

        if test != '100' and result == 1:
            output.write("Tested: " + str(test).ljust(4) + " in newmob(). " "Result: " + str(result).ljust(4) + " -Passed" + "\n")
            continue
        elif test == '100' and result == 1:
            output.write("Tested: " + str(test).ljust(4) + " in newmob(). " "Result: " + str(result).ljust(4) + " -Failed" + "\n")
            continue

print("Done Testing")