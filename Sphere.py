import time

__author__ = 'mwech'
from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
import sys

def depth():
    glShadeModel(GL_SMOOTH)
    glEnable(GL_CULL_FACE)
    glEnable(GL_DEPTH_TEST)

def light():
    glEnable(GL_LIGHTING)
    lightZeroPosition = [10., 4., 10., 1.]
    lightZeroColor = [0.8, 1.0, 0.8, 1.0]  # green tinged
    glLightfv(GL_LIGHT0, GL_POSITION, lightZeroPosition)
    glLightfv(GL_LIGHT0, GL_DIFFUSE, lightZeroColor)
    glLightf(GL_LIGHT0, GL_CONSTANT_ATTENUATION, 0.1)
    glLightf(GL_LIGHT0, GL_LINEAR_ATTENUATION, 0.05)
    glEnable(GL_LIGHT0)

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(800, 800)
    glutCreateWindow(b"Scene")

    depth()
    light()

    glutDisplayFunc(display)

    glutMainLoop()
    return

def sphereMaterial():
    color = [1.0, 0., 0., 1.]
    glMaterialfv(GL_FRONT, GL_DIFFUSE, color)

def drawSphere():
    position = (0,0,0)
    glPushMatrix()
    try:
        glTranslatef(*position)
        glutSolidSphere(2, 40, 40)
    finally:
        glPopMatrix()

def perspective():
    glMatrixMode(GL_PROJECTION)
    gluPerspective(40., 1., 1., 40.)
    glMatrixMode(GL_MODELVIEW)
    gluLookAt(0, 0, 10,
              0, 0, 0,
              0, 1, 0)
    #glPushMatrix()

def rotation():
    starttime = time.time()
    angle = (((time.time()-starttime)%10)/10)* 360
    glRotate( angle, 0,1,0)
    return angle

def display():

    glClearColor(0., 0., 0., 1.)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    glPushMatrix()
    sphereMaterial()
    rotation()
    drawSphere()
    glPopMatrix()

    glutSwapBuffers()

    perspective()
    return

if __name__ == '__main__': main()
