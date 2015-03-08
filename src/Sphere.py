import time
import pygame
from pygame.constants import DOUBLEBUF, OPENGL

__author__ = 'mwech'
from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
import sys

class Sphere(object):
    __speed = 1

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


    def sphereMaterial(self):
        color = [1.0, 1., 0.0, 1.]
        glMaterialfv(GL_FRONT, GL_DIFFUSE, color)


    def drawSphere(self, x, y, z):
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


    def perspective(self):
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(120., 1., 1., 50.)
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        gluLookAt(0, 0, 10,
                  0, 0, 0,
                  0, 1, 0)


    def rotation(self):
        angle = Sphere.__speed
       #print(angle)
        glTranslate(0, -2, 3);
        glRotate(angle, 0, 1, 0)
        glTranslate(0, 2, -3);
        return angle


    def display(self):
        pygame.init()
        display = (800, 600)
        pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
        self.perspective()
        self.depth()
        self.sphereMaterial()
        self.light()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        Sphere.__speed-=1
                        #self.rotation(3)
                    if event.key == pygame.K_RIGHT:
                        Sphere.__speed+=1
                    if event.key == pygame.K_DOWN:
                        Sphere.__speed=0

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 4:
                        glTranslatef(0, 0, 0.0)
                    if event.button == 5:
                         glTranslatef(0, -0, 0.0)

                    if event.button == 1:
                        glDisable(GL_LIGHTING)
                        glDisable(GL_LIGHT0)
                    if event.button == 3:
                        glEnable(GL_LIGHTING)
                        glEnable(GL_LIGHT0)

            glClearColor(0., 0., 0., 1.)
            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
            self.drawSphere(3,0,1)
            self.drawSphere(1,1,2)
            self.rotation()
            pygame.display.flip()
            pygame.time.wait(10)
        return

Sphere()

