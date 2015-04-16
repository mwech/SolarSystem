from src.DesignVerhalten import DesignVerhalten
from src.ObjectValues import ObjectValues
from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
__author__ = 'mwech'

"""
@author: Maximilian Wech, Arif Balkan
@version: 2015 03 28
@description: Verwenden der abstrakten Klasse; Erstellung/Initialsierung der Sonne/Planeten/Monde und Erstellung der
              Rotation dieser
"""
class Design(DesignVerhalten):
    """
    Design: Verwenden der abstrakten Klasse; Erstellung/Initialsierung der Sonne/Planeten/Monde und Erstellung der
    Rotation dieser
    :param DesignVerhalten: reference of the DesignVerhalten class
    """

    def drawSphere(self, x, y, z, mat, size, art, textur, number, speed):
        """
        Erstellen und zuweisen einiger notwendiger Eigenschaften (Größe, Farbe,etc.) für die Sonne/Planeten/Monde
        :param x: Die x-Koordinate der Anfangsposition
        :param y: Die y-Koordinate der Anfangsposition
        :param z: Die y-Koordinate der Anfangsposition
        :param mat: Zahl, des zu verwendenden Materials
        :param size: Der Radius der Kugel
        :param art: Beschreibt, ob es sich um eine Sonne, Planet, oder Mond handelt
        :param textur: Beschreibt, welche Texture verwendet werden soll
        :param number: Zaehler der bei jedem mal aufrufen erhöht wird
        :param speed: die Geschwindigkeit, mit der rotiert werden soll
        :return: /
        """
        if isinstance(x, int) and isinstance(y, int) and isinstance(z, int) and isinstance(mat, int) and isinstance(size, float) or isinstance(size, int) \
                and isinstance(art, str) and isinstance(textur, int) and isinstance(number, int) and isinstance(speed, int) and size > 0:
            referenz = ObjectValues()

            if(mat == 1): #Wenn mat 1, dann Farbe gelb zuweisen -> Sonne
                color = [1.0, 1., 0.0, 1.]
                glMaterialfv(GL_FRONT, GL_DIFFUSE, color)
            if(mat == 2): #Wenn mat 2, dann Farbe grün zuweisen -> Planeten
                color = [0.0, 1., 0.0, 1.]
                glMaterialfv(GL_FRONT, GL_DIFFUSE, color)
            if(mat == 3): #Wenn mat 3, dann Farbe blau zuweisen -> Monde
                color = [0.5, 0.5, 1, 1.]
                glMaterialfv(GL_FRONT, GL_DIFFUSE, color)

            glPushMatrix() #Definieren der Push Matrix
            self.rotate(art, number, speed) #Vor dem zeichnen muss die Rotation initialisiert werden
            position = (x,y,z) #Koordinaten der Position
            try:
                glTranslatef(*position) #Zuweisen der Position
                quadratic = gluNewQuadric()

                if textur == 1: #Wenn textur 1, dann Sonnentextur zuweisen
                    gluQuadricTexture(quadratic, GL_TRUE)
                    glBindTexture(GL_TEXTURE_2D, int(referenz.texturesSun[1]))
                if textur == 2: #Wenn textur 2, dann Planetentextur zuweisen
                    gluQuadricTexture(quadratic, GL_TRUE)
                    glBindTexture(GL_TEXTURE_2D, int(referenz.texturesPlanet[1]))
                if textur == 3: #Wenn textur 3, dann Mondtextur zuweisen
                    gluQuadricTexture(quadratic, GL_TRUE)
                    glBindTexture(GL_TEXTURE_2D, int(referenz.texturesMoon[1]))
                if textur == 4: #Wenn textur 4, dann 2. Planettextur zuweisen
                    gluQuadricTexture(quadratic, GL_TRUE)
                    glBindTexture(GL_TEXTURE_2D, int(referenz.texturesWorld[1]))

                gluSphere(quadratic, size, 20, 20) #Zeichnen der Kugel
            finally:
                if(art=="Sonne"): #Pop Matrix für die Sonne
                    glPopMatrix()
                if(art=="Mond"):
                    #Bei Monden muss zweimal PopMatrix verwendet werden, da bei Planeten keine zugewiesen wird
                    #->Monde drehen sich um Planeten
                    glPopMatrix()
                    glPopMatrix()
        else:
            raise TypeError('Only String,Integer and Float allowed')

    def rotate(self, art, number, speed):
        """
        Methode, die Objekte rotiert
        :param art: Beschreibt, ob es sich um Sonne/Planeten/Monde handelt
        :param number: Zaehler der bei jedem mal aufrufen erhöht wird
        :param speed: die Geschwindigkeit, mit der rotiert werden soll
        :return: /
        """
        if isinstance(art, str) and isinstance(number, int) and isinstance(number, float) or isinstance(number, int):
            if art == "Sonne": #Sonne wird nicht gedreht
                glRotate(0, 0, 1, 0)
                glTranslate(1, 0, 1)
            if art == "Planet":
                glRotate(speed*number, 0, 1, 0) #Allgemeiner Speed von Planeten * Zaehler
                glTranslate(1, 0, 1)
            if art == "Mond":
                glRotate(speed*number, 0, 1, 0) #Allgemeiner Speed von Monden * Zaehler
                glTranslate(1, 0, 1)
        else:
            raise TypeError('Only String,Integer and Float allowed')
