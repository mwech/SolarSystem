from experiments.strategy.DesignVerhalten import DesignVerhalten
from experiments.strategy.ObjectValues import ObjectValues
from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
__author__ = 'mwech'

class Design(DesignVerhalten):
    """
    Design
    :param DesignVerhalten: reference of the DesignVerhalten class
    """

    def drawSphere(self, x, y, z, mat, size, art, textur, number):
        referenz = ObjectValues()

        if(mat == 1):
            color = [1.0, 1., 0.0, 1.]
            glMaterialfv(GL_FRONT, GL_DIFFUSE, color)
        if(mat == 2):
            color = [0.0, 1., 0.0, 1.]
            glMaterialfv(GL_FRONT, GL_DIFFUSE, color)
        if(mat == 3):
            color = [0.5, 0.5, 1, 1.]
            glMaterialfv(GL_FRONT, GL_DIFFUSE, color)

        glPushMatrix()
        self.rotate(art, number, referenz)
        position = (x,y,z)
        try:
            glTranslatef(*position)
            quadratic = gluNewQuadric()

            if textur == 1:
                gluQuadricTexture(quadratic, GL_TRUE)
                glBindTexture(GL_TEXTURE_2D, int(referenz.texturesSun[1]))
            if textur == 2:
                gluQuadricTexture(quadratic, GL_TRUE)
                glBindTexture(GL_TEXTURE_2D, int(referenz.texturesPlanet[1]))
            if textur == 3:
                gluQuadricTexture(quadratic, GL_TRUE)
                glBindTexture(GL_TEXTURE_2D, int(referenz.texturesMoon[1]))

            gluSphere(quadratic, size, 20, 20)
        finally:
            if(art=="Sonne"):
                glPopMatrix()
            if(art=="Mond"):
                glPopMatrix()
                glPopMatrix()



    def rotate(self, art, number, referenz):
        if art == "Sonne":
            glRotate(referenz.speedSonne*number, 0, 1, 0)
            glTranslate(1, 0, 1)
        if art == "Planet":
            glRotate(referenz.speedPlanet*number, 0, 1, 0)
            glTranslate(1, 0, 1)
        if art == "Mond":
            glRotate(referenz.speedMond*number, 0, 1, 0)
            glTranslate(1, 0, 1)
