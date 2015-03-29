__author__ = 'arif'

import unittest
from src.Util import Util

"""
@author: Arif Balkan
@version: 2015 03 29
@description: Testen der Util Klasse
"""

class MyTestCase(unittest.TestCase):

    def setUp(self):
        global ut
        ut = Util()

    def testValidFilename(self):
       actual = ut.validTexture("../src/texturen/moon.jpg")
       expected = True
       self.assertEquals(actual, expected)

    def testValidFilename2(self):
       actual = ut.validTexture("../src/texturen/world2.png")
       expected = True
       self.assertEquals(actual, expected)

    def testValidFilename3(self):
       actual = ut.validTexture("../src/texturen/world2.gif")
       expected = False
       self.assertEquals(actual, expected)

    def testValidFilename4(self):
       actual = ut.validTexture("../src/Splashscreen_v1.jpg")
       expected = False
       self.assertEquals(actual, expected)

    def testValidFilename5(self):
       actual = ut.validTexture(0)
       expected = False
       self.assertEquals(actual, expected)

    def testValidFilename6(self):
       actual = ut.validTexture(0.58)
       expected = False
       self.assertEquals(actual, expected)

    def testValidFilename7(self):
       actual = ut.validTexture('world2')
       expected = False
       self.assertEquals(actual, expected)

    def testValidFilename8(self):
       actual = ut.validTexture(-5)
       expected = False
       self.assertEquals(actual, expected)

    def tearDown(self):
        ut = None

if __name__ == '__main__':
    unittest.main()
