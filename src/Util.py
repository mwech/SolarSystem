from src.UtilVerhalten import UtilVerhalten
from src.ObjectValues import ObjectValues
from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
from PIL import Image
import imghdr

__author__ = 'mwech'

"""
@author: Maximilian Wech, Arif Balkan
@version: 2015 03 28
@description: Verwenden der abstrakten Klasse; Führt Basic Methoden (wie zB Erstellung von Licht, Texturen,etc.) durch
"""

class Util(UtilVerhalten):
    """
    Util: Verwenden der abstrakten Klasse; Führt Basic Methoden (wie zB Erstellung von Licht, Texturen,etc.) durch
    :param UtilVerhalten: reference of theUtilVerhalten class
    """
    def light(self):
        """
        Setzen des Lichtes
        :return: /
        """
        lightZeroPosition = [0., 0., -6., 1] #Position des Lichtes
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

    def validTexture(self, name):
        """
        Überprüfen des Fileformats der Textur
        :return: /
        """
        try:
            image_type = imghdr.what(name)
            if image_type:
                return True
        except (FileNotFoundError, AttributeError, ValueError) as e:
            return False


    def depth(self):
        """
        Setzen einiger notwendiger Eigenschaften
        :return: /
        """
        glShadeModel(GL_SMOOTH)
        glEnable(GL_CULL_FACE)
        glDepthFunc(GL_LESS)
        glEnable(GL_DEPTH_TEST)


    def perspective(self, liste):
        """
        Setzen der Perspektive
        :param liste: Werte, die für den gluLookAt Befehl zum Setzen der Perspektive notwendig sind
        :return: /
        """
        if liste: #Wenn die liste nicht Leer ist
            if len(liste)==9: #Liste braucht 9 Elemente
                glMatrixMode(GL_PROJECTION)
                glLoadIdentity()
                gluPerspective(80, 1080 / 720, 0.01, 120)
                glMatrixMode(GL_MODELVIEW)
                glLoadIdentity()
                #Zuweisen der Perspektive anhand des Parameters
                gluLookAt(liste[0], liste[1], liste[2],
                  liste[3], liste[4], liste[5],
                  liste[6], liste[7], liste[8])
            else:
                raise ValueError("Liste hat nicht die richtige Größe")
        else:
            raise ValueError("Perspektiven-Liste darf nicht leer sein")

    def loadTexture(self, name):
        """
        Erstellt Texturen und stellt diese bereit
        :return: /
        """
        if name == "sun.jpg" or name == "moon.jpg" or name == "planet.png" or name == "world2.png" or name =="mars.jpg":
            image = Image.open(name) #Öffnen der Textur
            #Größe bestimmen
            ix = image.size[0]
            iy = image.size[1]
            image = image.convert("RGBA").tostring("raw", "RGBA")
            referenz = ObjectValues()
            # Create Texture
            if name == "sun.jpg":
                #Auslagern der Textur in die Klasse ObjectValues
                referenz.texturesSun.extend(glGenTextures(3))
                glBindTexture(GL_TEXTURE_2D, int(referenz.texturesSun[1]))
            if name == "planet.png":
                #Auslagern der Textur in die Klasse ObjectValues
                referenz.texturesPlanet.extend(glGenTextures(3))
                glBindTexture(GL_TEXTURE_2D, int(referenz.texturesPlanet[1]))
            if name == "moon.jpg":
                #Auslagern der Textur in die Klasse ObjectValues
                referenz.texturesMoon.extend(glGenTextures(3))
                glBindTexture(GL_TEXTURE_2D, int(referenz.texturesMoon[1]))
            if name == "world2.png":
                #Auslagern der Textur in die Klasse ObjectValues
                referenz.texturesWorld.extend(glGenTextures(3))
                glBindTexture(GL_TEXTURE_2D, int(referenz.texturesWorld[1]))
            if name == "mars.jpg":
                #Auslagern der Textur in die Klasse ObjectValues
                referenz.texturesMars.extend(glGenTextures(3))
                glBindTexture(GL_TEXTURE_2D, int(referenz.texturesMars[1]))

            glPixelStorei(GL_UNPACK_ALIGNMENT,1)
            glTexImage2D(GL_TEXTURE_2D, 0, 3, ix, iy, 0, GL_RGBA, GL_UNSIGNED_BYTE, image)
            glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP)
            glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP)
            glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
            glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
            glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
            glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
            glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_DECAL)
            glEnable(GL_TEXTURE_2D)
        else:
            raise Error("Angegebene Textur nicht erlaubt")
