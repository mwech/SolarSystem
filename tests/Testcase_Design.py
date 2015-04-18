
import unittest
from src.Design import Design

"""
@author: Arif Balkan, Maximilian Wech
@version: 2015 04 18
@description: Testen der Design Klasse
"""

class Design_Testcases(unittest.TestCase):

    def setUp(self):
        global design
        design = Design()

    @unittest.expectedFailure
    def test_drawSphere_radius_less_than_0(self):
        design.drawSphere(0,0,0,1,-2,"Sonne",1,2,0)

    @unittest.expectedFailure
    def test_drawSphere_radius_greater_than_15(self):
        design.drawSphere(0,0,0,1,17,"Sonne",1,2,0)

    @unittest.expectedFailure
    def test_drawSphere_material_less_than_1(self):
        design.drawSphere(0,0,0,-2,-2,"Sonne",1,2,0)

    @unittest.expectedFailure
    def test_drawSphere_material_greater_than_3(self):
        design.drawSphere(0,0,0,4,1,"Sonne",1,2,0)

    @unittest.expectedFailure
    def test_drawSphere_texture_less_than_1(self):
        design.drawSphere(0,0,0,2,-2,"Sonne",0,2,0)

    @unittest.expectedFailure
    def test_drawSphere_texture_greater_than_4(self):
        design.drawSphere(0,0,0,2,1,"Sonne",5,2,0)

    @unittest.expectedFailure
    def test_drawSphere_art_not_accepted(self):
        design.drawSphere(0,0,0,2,1,"Asteroide",4,2,0)

    @unittest.expectedFailure
    def test_drawSphere_art_not_accepted2(self):
        design.drawSphere(0,0,0,2,1,"Galaxie",4,2,0)

    @unittest.expectedFailure
    def test_drawSphere_art_not_accepted3(self):
        design.drawSphere(0,0,0,2,1,"Stern",4,2,0)

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

