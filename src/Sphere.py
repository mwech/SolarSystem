import time
import pygame
from pygame.constants import DOUBLEBUF, OPENGL

__author__ = 'mwech'
from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
import sys
from PIL import Image


class Sphere(object):
    __speedPlanet = 1.5
    __speedMond = 1
    __speedSonne = 0
    __zaehler = 0

    def __init__(self):
        self.display()

    def LoadTextures(self, name):

        image = Image.open(name)
        ix = image.size[0]
        iy = image.size[1]
        image = image.convert("RGBA").tostring("raw", "RGBA")
        # Create Texture
        if name == "sun.jpg":
            global texturesSun
            texturesSun = glGenTextures(3)
            glBindTexture(GL_TEXTURE_2D, int(texturesSun[1]))   # 2d texture (x and y size)
        if name == "planet.png":
            global texturesPlanet
            texturesPlanet = glGenTextures(3)
            glBindTexture(GL_TEXTURE_2D, int(texturesPlanet[1]))   # 2d texture (x and y size)
        if name == "moon.jpg":
            global texturesMoon
            texturesMoon = glGenTextures(3)
            glBindTexture(GL_TEXTURE_2D, int(texturesMoon[1]))   # 2d texture (x and y size)

        glPixelStorei(GL_UNPACK_ALIGNMENT,1)
        glTexImage2D(GL_TEXTURE_2D, 0, 3, ix, iy, 0, GL_RGBA, GL_UNSIGNED_BYTE, image)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
        glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_DECAL)

    def depth(self):
        glShadeModel(GL_SMOOTH)
        glEnable(GL_CULL_FACE)
        glDepthFunc(GL_LESS)
        glEnable(GL_DEPTH_TEST)
        glEnable(GL_TEXTURE_2D)

    def light(self):
        lightZeroPosition = [10., 4., 10., 1.]
        lightZeroColor = [0.8, 1.0, 0.8, 1.0]  # green tinged
        glLightfv(GL_LIGHT0, GL_POSITION, lightZeroPosition)
        glLightfv(GL_LIGHT0, GL_DIFFUSE, lightZeroColor)
        glLightf(GL_LIGHT0, GL_CONSTANT_ATTENUATION, 0.1)
        glLightf(GL_LIGHT0, GL_LINEAR_ATTENUATION, 0.05)
        glEnable(GL_LIGHTING)
        glEnable(GL_LIGHT0)

    def idle(self):
        glutPostRedisplay()

    def sphereMaterial(self, mat):
        if(mat == 1):
            color = [1.0, 1., 0.0, 1.]
            glMaterialfv(GL_FRONT, GL_DIFFUSE, color)
        if(mat == 2):
            color = [0.0, 1., 0.0, 1.]
            glMaterialfv(GL_FRONT, GL_DIFFUSE, color)
        if(mat == 3):
            color = [0.5, 0.5, 1, 1.]
            glMaterialfv(GL_FRONT, GL_DIFFUSE, color)

    def rotate(self, art):
        if art == "Sonne":
            glTranslate(1, 0, 1)
            glRotate(Sphere.__speedSonne*Sphere.__zaehler, 0, 1, 0)
            glTranslate(-1, 0, -1)
        if art == "Mond":
            glTranslate(1, 0, 1)
            glRotate(Sphere.__speedMond*Sphere.__zaehler, 0, 1, 0)
            glTranslate(-1, 0, -1)
        if art == "Planet":
            glTranslate(1, 0, 1)
            glRotate(Sphere.__speedPlanet*Sphere.__zaehler, 0, 1, 0)
            glTranslate(-1, 0, -1)

    def drawSphere(self, x, y, z, mat, size, art, textur):
        if(mat == 1):
            self.sphereMaterial(1)
        if(mat == 2):
            self.sphereMaterial(2)
        if(mat == 3):
            self.sphereMaterial(3)

        glPushMatrix()
        self.rotate(art)
        position = (x,y,z)
        try:
            glTranslatef(*position)
            quadratic = gluNewQuadric()
            if textur == 1:
                gluQuadricTexture(quadratic, GL_TRUE)
                glBindTexture(GL_TEXTURE_2D, int(texturesSun[1]))
            if textur == 2:
                gluQuadricTexture(quadratic, GL_TRUE)
                glBindTexture(GL_TEXTURE_2D, int(texturesPlanet[1]))
            if textur == 3:
                gluQuadricTexture(quadratic, GL_TRUE)
                glBindTexture(GL_TEXTURE_2D, int(texturesMoon[1]))
            gluSphere(quadratic, size, 20, 20)
        finally:
            if(art=="Sonne"):
                glPopMatrix()
            if(art=="Mond"):
                glPopMatrix()
                glPopMatrix()

    def perspective(self, liste):
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(120., 1., 1., 50.)
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        gluLookAt(liste[0], liste[1], liste[2],
                  liste[3], liste[4], liste[5],
                  liste[6], liste[7], liste[8])

    def display(self):
        pygame.init()
        display = (800, 600)
        pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
        liste = [0, 0, 10,
                 0, 0, 0,
                 0, 1, 0]
        self.perspective(liste)
        self.LoadTextures("sun.jpg")
        self.LoadTextures("planet.png")
        self.LoadTextures("moon.jpg")
        self.depth()
        #self.sphereMaterial()
        self.light()
        while True:
            Sphere.__zaehler+=1
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                if event.type == pygame.KEYDOWN:
                    #Rotation langsamer --> Pfeiltaste links
                    if event.key == pygame.K_LEFT:
                        Sphere.__speedPlanet-=0.3
                        Sphere.__speedMond-=0.2
                    #Rotation schneller --> Pfeiltaste rechts
                    if event.key == pygame.K_RIGHT:
                        Sphere.__speedPlanet+=0.3
                        Sphere.__speedMond+=0.2
                    #Rotationsstop --> Pfeiltaste unten
                    if event.key == pygame.K_DOWN:
                        Sphere.__speedPlanet=0
                        Sphere.__speedMond=0
                    #Überkopfsicht --> Taste w
                    if event.key == pygame.K_w:
                        liste = [0, -5, 10,
                                 0, 0, 0,
                                 0, 1, 0]
                        self.perspective(liste)
                    #Froschperspektive --> Taste s
                    if event.key == pygame.K_s:
                        liste = [0, 8, 10,
                                 0, 0, 0,
                                 0, 1, 0]
                        self.perspective(liste)

                    if event.key == pygame.K_j:
                        glDisable(GL_TEXTURE_2D)

                if event.type == pygame.MOUSEBUTTONDOWN:

                    if event.button == 4:
                        glTranslatef(0, 0, 0.0)
                    if event.button == 5:
                         glTranslatef(0, -0, 0.0)
                    #Licht aus --> Maus links
                    if event.button == 1:
                        glDisable(GL_TEXTURE_2D)
                    #Licht an --> Maus rechts
                    if event.button == 3:
                        glEnable(GL_TEXTURE_2D)

            glClearColor(0., 0., 0., 1.)
            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

            self.drawSphere(0,0,0,1,1,"Sonne",1)

            self.drawSphere(-3,0,-1,2,1,"Planet",2)

            self.drawSphere(-3,1,-2,3,0.5,"Mond",3)

            self.drawSphere(4,0,-2,2,1,"Planet",2)

            self.drawSphere(4.5,3,-2,3, 0.5,"Mond",3)

            pygame.display.flip()
            pygame.time.wait(10)
        return
Sphere()

"Push Sonne Pop"
"Push Planet Push Mond Pop Pop"