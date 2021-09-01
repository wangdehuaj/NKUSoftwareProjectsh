import unittest

# This is the class we want to test. So, we need to import it
import spaceShooter as MissileClass


class Testing(unittest.TestCase):
    def test_string(self):
        powerup_images['tri_missile'] = tri_missile.png
        missile_string = 'tri_missile'
        self.assertEqual(powerup_images, missile_string)

    def test_boolean(self):
        powerup_images = True
        missile_string = True
        self.assertEqual(powerup_images, missile_string)


    # if the don't match it will fail the test case
    if powerup_images == missile_string:
        self.assertEqual(self.powerup_images, missile_string)

    print("\nFinish get_name test\n")

if __name__ == '__main__':
    unittest.main()
