from UtilVerhalten import UtilVerhalten
from ObjectValues import ObjectValues
from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
from PIL import Image
from math import pi
import imghdr

__author__ = 'mwech, balkan'
class Util(UtilVerhalten):
    """
    Util
    :param UtilVerhalten: reference of theUtilVerhalten class
    """
    def light(self):
        """

        :return: nothing
        """
        lightZeroPosition = [0., 0., -6., 1]
        lightZeroColor = [0.8, 1.0, 0.8, 1.0]  # green tinged
        glLightfv(GL_LIGHT0, GL_POSITION, lightZeroPosition)
        glLightfv(GL_LIGHT0, GL_DIFFUSE, lightZeroColor)
        glLightf(GL_LIGHT0, GL_CONSTANT_ATTENUATION, 0.2)
        glLightf(GL_LIGHT0, GL_LINEAR_ATTENUATION, 0.1)
        glTexGeni(GL_S, GL_TEXTURE_GEN_MODE, GL_SPHERE_MAP)
        glTexGeni(GL_T, GL_TEXTURE_GEN_MODE, GL_SPHERE_MAP)
        glEnable(GL_TEXTURE_GEN_S)
        glEnable(GL_TEXTURE_GEN_T)
        glEnable(GL_LIGHTING)
        glEnable(GL_LIGHT0)


    def depth(self):
        """

        :return: nothing
        """
        glShadeModel(GL_SMOOTH)
        glEnable(GL_CULL_FACE)
        glDepthFunc(GL_LESS)
        glEnable(GL_DEPTH_TEST)


    def perspective(self, liste):
        """

        :return: nothing
        """
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(80, 1080 / 720, 0.01, 120)
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        gluLookAt(liste[0], liste[1], liste[2],
                  liste[3], liste[4], liste[5],
                  liste[6], liste[7], liste[8])

    def validTexture(self, name):
        try:
            image_type = imghdr.what(name)
            if image_type:
                return True
        except (FileNotFoundError, AttributeError, ValueError) as e:
            return False

    def loadTexture(self, name):
        """

        :return: nothing
        """
        image = Image.open(name)
        ix = image.size[0]
        iy = image.size[1]
        image = image.convert("RGBA").tostring("raw", "RGBA")
        referenz = ObjectValues()
        # Create Texture
        if name == "texturen/sun.jpg":
            referenz.texturesSun.extend(glGenTextures(3))
            glBindTexture(GL_TEXTURE_2D, int(referenz.texturesSun[1]))   # 2d texture (x and y size)
        if name == "texturen/planet.png":
            referenz.texturesPlanet.extend(glGenTextures(3))
            glBindTexture(GL_TEXTURE_2D, int(referenz.texturesPlanet[1]))   # 2d texture (x and y size)
        if name == "texturen/moon.jpg":
            referenz.texturesMoon.extend(glGenTextures(3))
            glBindTexture(GL_TEXTURE_2D, int(referenz.texturesMoon[1]))   # 2d texture (x and y size)
        if name == "texturen/world2.png":
            referenz.texturPlanet2.extend(glGenTextures(3))
            glBindTexture(GL_TEXTURE_2D, int(referenz.texturPlanet2[1]))   # 2d texture (x and y size)

        #glPixelStorei(GL_UNPACK_ALIGNMENT,1)
        glTexImage2D(GL_TEXTURE_2D, 0, 3, ix, iy, 0, GL_RGBA, GL_UNSIGNED_BYTE, image)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
        glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_DECAL)
        glEnable(GL_TEXTURE_2D)