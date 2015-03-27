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
    def sun(self, x, y, z, mat, size, art, textur):
        """

        :return: nothing
        """
        """
        MATERIALS
        """
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

        """
        ROTATION
        """
        glTranslate(1, 0, 1)
        glRotate(referenz.speedSonne*referenz.zaehler, 0, 1, 0)
        glTranslate(-1, 0, -1)

        position = (x,y,z)
        try:
            glTranslatef(*position)
            quadratic = gluNewQuadric()
            #print(referenz.texturesSun)
            gluQuadricTexture(quadratic, GL_TRUE)
            glBindTexture(GL_TEXTURE_2D, int(referenz.texturesSun[1]))

            gluSphere(quadratic, size, 20, 20)
        finally:
            glPopMatrix()


    def planet(self, x, y, z, mat, size, art, textur):
        """

        :return: nothing
        """
        """
        MATERIALS
        """
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
        glTranslate(1, 0, 1)
        glRotate(referenz.speedPlanet*referenz.zaehler, 0, 1, 0)
        glTranslate(-1, 0, -1)
        position = (x,y,z)

        glTranslatef(*position)
        quadratic = gluNewQuadric()

        gluQuadricTexture(quadratic, GL_TRUE)
        glBindTexture(GL_TEXTURE_2D, int(referenz.texturesPlanet[1]))

        gluSphere(quadratic, size, 20, 20)



    def mond(self, x, y, z, mat, size, art, textur):
        """

        :return: nothing
        """
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
        glTranslate(1, 0, 1)
        glRotate(referenz.speedMond*referenz.zaehler, 0, 1, 0)
        glTranslate(-1, 0, -1)
        position = (x,y,z)
        try:
            glTranslatef(*position)
            quadratic = gluNewQuadric()

            gluQuadricTexture(quadratic, GL_TRUE)
            glBindTexture(GL_TEXTURE_2D, int(referenz.texturesMoon[1]))

            gluSphere(quadratic, size, 20, 20)
        finally:
            glPopMatrix()
            glPopMatrix()