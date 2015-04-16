from DesignVerhalten import DesignVerhalten
from ObjectValues import ObjectValues
from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
__author__ = 'mwech'

class Design(DesignVerhalten):
    """
    Design
    :param DesignVerhalten: reference of the DesignVerhalten class
    """

    def drawSphere(self, x, y, z, mat, size, art, textur, number, speed):

        if isinstance(x, int) and isinstance(y, int) and isinstance(z, int) and isinstance(mat, int) and isinstance(size, float) or isinstance(size, int) \
                and isinstance(art, str) and isinstance(textur, int) and isinstance(number, int) and isinstance(speed, int) and size > 0:
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
            if(mat == 4):
                color = [0.0, 1., 1.0, 1.]
                glMaterialfv(GL_FRONT, GL_DIFFUSE, color)

            glPushMatrix()
            self.rotate(art, number, speed)
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
                if textur == 4:
                    gluQuadricTexture(quadratic, GL_TRUE)
                    glBindTexture(GL_TEXTURE_2D, int(referenz.texturPlanet2[1]))

                gluSphere(quadratic, size, 20, 20)
            finally:
                if(art=="Sonne"):
                    glPopMatrix()
                if(art=="Mond"):
                    glPopMatrix()
                    glPopMatrix()
        else:
            raise TypeError('Only String,Integer and Float allowed')



    def rotate(self, art, number, speed):
        if isinstance(art, str) and isinstance(number, int) and isinstance(number, float) or isinstance(number, int):
            referenz = ObjectValues()
            if isinstance(art, str):
                if art == "Sonne":
                    glRotate(0, 0, 1, 0)
                    glTranslate(1, 0, 1)
                if art == "Planet":
                    glRotate(speed*number, 0, 1, 0)
                    glTranslate(1, 0, 1)
                if art == "Mond":
                    glRotate(speed*number, 0, 1, 0)
                    glTranslate(1, 0, 1)

                    #print(referenz.speed)
        else:
            raise TypeError('Only String,Integer and Float allowed')

