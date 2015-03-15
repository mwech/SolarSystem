import time
import pygame
from pygame.constants import DOUBLEBUF, OPENGL

__author__ = 'mwech'
from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
import sys

class Sphere(object):
    __speed = 0.4
    __starttime = time.time()

    def __init__(self):
        self.display()

    def depth(self):
        glShadeModel(GL_SMOOTH)
        glEnable(GL_CULL_FACE)
        glDepthFunc(GL_LESS)
        glEnable(GL_DEPTH_TEST)

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

    def drawSphere(self, x, y, z, zahl, mat):
        #Sphere.__speed=0.3
        if(mat == 1):
            self.sphereMaterial(1)
        if(mat == 2):
            self.sphereMaterial(2)
        if(mat == 3):
            self.sphereMaterial(3)
        if(zahl == 1):
            self.rotation(1)
        if(zahl == 2):
            self.rotation(2)
        position = (x,y,z)
        glPushMatrix()
        try:
            glTranslatef(*position)
            glRotatef(360,1,0,0)
            sphere = gluNewQuadric()
            # gluQuadricDrawStyle(sphere,GLU_LINE);
            gluSphere(sphere, 1, 20, 20)
        finally:
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


    def rotation(self, zahl):
        angle = Sphere.__speed
        #print(angle)
        if(zahl == 1):
            glTranslate(1, 0, 1);
            glRotate(angle, 0, 1, 0)
            glTranslate(-1, 0, -1);
        return angle

    def display(self):
        pygame.init()
        display = (800, 600)
        pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
        liste = [0, 0, 10,
                 0, 0, 0,
                 0, 1, 0]
        self.perspective(liste)
        self.depth()
        #self.sphereMaterial()
        self.light()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                if event.type == pygame.KEYDOWN:
                    #Rotation langsamer --> Pfeiltaste links
                    if event.key == pygame.K_LEFT:
                        Sphere.__speed-=0.2
                    #Rotation schneller --> Pfeiltaste rechts
                    if event.key == pygame.K_RIGHT:
                        Sphere.__speed+=0.2
                    #Rotationsstop --> Pfeiltaste unten
                    if event.key == pygame.K_DOWN:
                        Sphere.__speed=0
                    #Überkopfsicht --> Taste w
                    if event.key == pygame.K_w:
                        liste = [0, -5, 10,
                                 0, 0, 0,
                                 0, 1, 0]
                        self.perspective(liste)
                    #Froschperspektive --> Taste s
                    if event.key == pygame.K_s:
                        liste = [0, 5, 10,
                                 0, 0, 0,
                                 0, 1, 0]
                        self.perspective(liste)

                if event.type == pygame.MOUSEBUTTONDOWN:

                    if event.button == 4:
                        glTranslatef(0, 0, 0.0)
                    if event.button == 5:
                         glTranslatef(0, -0, 0.0)
                    #Licht aus --> Maus links
                    if event.button == 1:
                        glDisable(GL_LIGHTING)
                        glDisable(GL_LIGHT0)
                    #Licht an --> Maus rechts
                    if event.button == 3:
                        glEnable(GL_LIGHTING)
                        glEnable(GL_LIGHT0)

            glClearColor(0., 0., 0., 1.)
            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
            self.drawSphere(0,0,0,2,1)
            self.drawSphere(0,0,-2,1,2)
            self.drawSphere(3,0,-2,1,2)
            self.drawSphere(0,0,-4,1,3)
            self.drawSphere(3,0,-4,1,3)
            pygame.display.flip()
            pygame.time.wait(10)
        return

Sphere()

