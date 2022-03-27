import pygame
from BulletHandler import *


# This opens the input file to get the direction/speed the enemy bullet will travel.
with open("kyle_test_input.txt","r") as input_file:
        tests = input_file.readlines()

# whitespace deletion
tests = [x.strip() for x in tests]
print("Input\t\tPlayer Ship\tEnemy Ship\n")

# open the output file for the test and test the bullets direction
for test in tests:
        direction = int(test)
        BulletHandler(direction)



            

            
            
