__author__ = 'arif'

import time

from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
import sys

class Sphere(object):
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

    def main(self):
        glutInit(sys.argv)
        glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
        glutInitWindowSize(800, 800)
        glutCreateWindow(b"Scene")
        glutDisplayFunc(self.display())
        glutIdleFunc(self.display())
        glutMainLoop()
        return

    def idle(self):
        glutPostRedisplay()

    def sphereMaterial(self):
        color = [1.0, 1., 0.0, 1.]
        glMaterialfv(GL_FRONT, GL_DIFFUSE, color)

    def drawSphere(self):
        position = (0,-1,0)
        glPushMatrix()
        try:
            glTranslatef(*position)
            glRotatef(360, 1,0 , 0)
            glutSolidSphere(0.5, 40, 40)
        finally:
            glPopMatrix()

    def drawSphere2(self):
        position = (2,0.5,2)
        glPushMatrix()
        try:
            glTranslatef(*position)
            glRotatef(360, 1,0 , 0)
            glutSolidSphere(0.5, 40, 40)
        finally:
            glPopMatrix()

    def perspective(self):
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(120., 1., 1., 40.)
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        gluLookAt(0, 0, 10,
                  0, 0, 0,
                  0, 1, 0)
        #glPushMatrix()

    starttime = time.time()

    def rotation(self):
        period = 10
        starttime = 1
        """Do rotation of the scene at given rate"""
        #print(starttime)
        angle = (((time.time()-starttime)%period)/period)* 360
        print(angle)
        glTranslate(0, -2, 4);
        glRotate( angle, 0,1,0)
        glTranslate(0, 2, -4);
        return angle


    def display(self):
        clear, swap = 1
        if clear:
            glClearColor(0., 0., 0., 1.)
            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        test.perspective()
        test.light()
        test.depth()
        #glPushMatrix()
        test.sphereMaterial()
        test.rotation()
        test.drawSphere()
        test.drawSphere2()
        #glPopMatrix()
        if swap:
            glutSwapBuffers()


        return

test = Sphere()