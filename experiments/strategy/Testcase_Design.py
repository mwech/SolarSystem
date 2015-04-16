__author__ = 'arif'

import unittest
from Design import Design

class MyTestCase(unittest.TestCase):

    def setUp(self):
        pass

    def test_drawSphere_false_input(self):
        x = 5
        y = 'text1'
        z = 'tex2t'
        mat = 4
        art = 5
        textur = "Planet"
        number = 1
        speed = 3
        self.assertRaises(TypeError, x, y, z, mat, art, textur, number, speed)

    def test_drawSphere2_false_input(self):
        x = 'text1'
        y = 2
        z = -2
        mat = 'text2'
        art = 'text3'
        textur = 3
        number = 'text1'
        speed = 'text1'
        self.assertRaises(TypeError, x, y, z, mat, art, textur, number, speed)

    def test_drawSphere3_false_input(self):
        x = 0
        y = 0
        z = 0
        mat = 0
        art = 0
        textur = 0
        number = 0
        speed = 0
        self.assertRaises(TypeError, x, y, z, mat, art, textur, number, speed)

    def test_drawSphere4_false_input(self):
        x = True
        y = True
        z = True
        mat = False
        art = False
        textur = True
        number = False
        speed = True
        self.assertRaises(TypeError, x, y, z, mat, art, textur, number, speed)

    def test_rotate_false_input(self):
        art = 2
        number = 3
        speed = 4
        self.assertRaises(TypeError, art, number, speed)

    def test_rotate2_false_input(self):
        art = "Mond"
        number = "test"
        speed = 4
        self.assertRaises(TypeError, art, number, speed)

    def test_rotate3_false_input(self):
        art = 0
        number = 0
        speed = 0
        self.assertRaises(TypeError, art, number, speed)

    def test_rotate4_false_input(self):
        art = -5
        number = -10
        speed = -50
        self.assertRaises(TypeError, art, number, speed)

    def test_rotate5_false_input(self):
        art = True
        number = True
        speed = False
        self.assertRaises(TypeError, art, number, speed)

    def test_rotate6_false_input(self):
        art = -5
        number = -10
        speed = False
        self.assertRaises(TypeError, art, number, speed)


if __name__ == '__main__':
    unittest.main()


