import time
import pygame
from pygame.constants import DOUBLEBUF, OPENGL

__author__ = 'mwech'
from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
import sys


def depth():
    glShadeModel(GL_SMOOTH)
    glEnable(GL_CULL_FACE)
    glDepthFunc(GL_LESS)
    glEnable(GL_DEPTH_TEST)


def light():
    lightZeroPosition = [10., 4., 10., 1.]
    lightZeroColor = [0.8, 1.0, 0.8, 1.0]  # green tinged
    glLightfv(GL_LIGHT0, GL_POSITION, lightZeroPosition)
    glLightfv(GL_LIGHT0, GL_DIFFUSE, lightZeroColor)
    glLightf(GL_LIGHT0, GL_CONSTANT_ATTENUATION, 0.1)
    glLightf(GL_LIGHT0, GL_LINEAR_ATTENUATION, 0.05)
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)


def main():
    '''
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(800, 800)
    glutCreateWindow(b"Scene")
    glutDisplayFunc(display)
    glutIdleFunc(display)
    glutMainLoop()
    return
    '''

def idle():
    glutPostRedisplay()


def sphereMaterial():
    color = [1.0, 1., 0.0, 1.]
    glMaterialfv(GL_FRONT, GL_DIFFUSE, color)


def drawSphere(par):
    position = (3, 0.5, 2.5)
    glTranslate(par,0,0)
    glPushMatrix()
    try:
        sphere = gluNewQuadric()
        #gluQuadricDrawStyle(sphere,GLU_LINE);
        gluSphere(sphere,1,20,20)

    finally:
        glPopMatrix()


def drawSphere2():
    glPushMatrix()
    try:
        sphere = gluNewQuadric()
        #gluQuadricDrawStyle(sphere,GLU_LINE);
        gluSphere(sphere,1,20,20)

    finally:
        glPopMatrix()


def perspective():
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(120., 1., 1., 50.)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluLookAt(0, 0, 10,
              0, 0, 0,
              0, 1, 0)
    # glPushMatrix()


starttime = time.time()


def rotation(period=10):
    """Do rotation of the scene at given rate"""
    # print(starttime)
    angle = 1
    print(angle)
    glTranslate(0, -2, 3);
    glRotate(angle, 0, 1, 0)
    glTranslate(0, 2, -3);
    return angle


def display(clear=1, swap=1):
    pygame.init()
    display = (800,600)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
    perspective()
    depth()
    # glPushMatrix()
    sphereMaterial()

    #rotation()

    #drawSphere2()

    #glPopMatrix()
    '''
    if swap:
        glutSwapBuffers()
    '''
    while True:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 4:
                    glTranslatef(0, 0, 1.0)

                if event.button == 5:
                    glTranslatef(0, 0, -1.0)
        light()
        glClearColor(0., 0., 0., 1.)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        #glTranslate(0,0,)
        drawSphere(0)
        rotation()
        #drawSphere2()
        pygame.display.flip()
        pygame.time.wait(10)
    return


if __name__ == '__main__': display()
