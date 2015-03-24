#!/usr/bin/python2.4
from __future__ import with_statement

#import openGL
from OpenGL import *
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import string
import sys
from PIL import Image

window_x=800
window_y=600

eyex = 0
eyey = 0
eyez = 5

lookx = 0 #152100000000
looky = 0
lookz = 0
light = 0

name = 'Sun Earth & Moon Animation'

def LoadTextures():
    global textures, quadratic
    image = Image.open("House.png")
	
    ix = image.size[0]
    iy = image.size[1]
    image = image.convert("RGBA").tostring("raw", "RGBA")
	
    # Create Texture
    textures = glGenTextures(3)
    glBindTexture(GL_TEXTURE_2D, int(textures[0]))   # 2d texture (x and y size)
	
    glPixelStorei(GL_UNPACK_ALIGNMENT,1)
    glTexImage2D(GL_TEXTURE_2D, 0, 3, ix, iy, 0, GL_RGBA, GL_UNSIGNED_BYTE, image)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
    glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_DECAL)
    			# Create Texture Coords (NEW) 
            


def InitGL():
    global quadratic
    LoadTextures()

    glEnable(GL_TEXTURE_2D)
    glClearColor(0.0, 0.0, 0.0, 0.0)	# This Will Clear The Background Color To Black
    glClearDepth(1.0)					# Enables Clearing Of The Depth Buffer
    glDepthFunc(GL_LESS)				# The Type Of Depth Test To Do
    glEnable(GL_DEPTH_TEST)				# Enables Depth Testing
    glShadeModel(GL_SMOOTH)

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(130,1., .1,100)
    glMatrixMode(GL_MODELVIEW)

    glLightfv(GL_LIGHT0, GL_AMBIENT, (0.5, 0.5, 0.5, 1.0))		# Setup The Ambient Light 
    glLightfv(GL_LIGHT0, GL_DIFFUSE, (1.0, 1.0, 1.0, 1.0))		# Setup The Diffuse Light 
    glLightfv(GL_LIGHT0, GL_POSITION, (0.0, 0.0, 2.0, 1.0))	# Position The Light 
    glEnable(GL_LIGHT0)					# Enable Light One 
    
def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH)
    glutInitWindowSize(window_x, window_y)
    glutCreateWindow(b"Sun Earth & Moon Animation")

    'init openGL'
    glutDisplayFunc(display)
    
    glutIdleFunc(display)

    InitGL()
    
    glutMainLoop()

def material(red, green, blue, alpha, spec, shiny):
    ambient_diffuse = [red, green, blue, alpha]
    specular = [spec, spec, spec, spec]
    shininess = [shiny]
    emission = [0, 0, 0, 1]

    glMaterialfv(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE, ambient_diffuse)
    glMaterialfv(GL_FRONT_AND_BACK, GL_SPECULAR, specular)
    glMaterialfv(GL_FRONT_AND_BACK, GL_SHININESS, shininess)
    glMaterialfv(GL_FRONT_AND_BACK, GL_EMISSION, emission)


def display():
    global textures, quadratic, light
    
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    quadratic = gluNewQuadric()
    gluQuadricNormals(quadratic, GLU_SMOOTH)		# Create Smooth Normals (NEW) 
    gluQuadricTexture(quadratic, GL_TRUE)
    gluLookAt(0, 0, -15, 0, 0, 0, 0, 1, 0);

    glBindTexture(GL_TEXTURE_2D, int(textures[0]))
    glEnable(GL_LIGHTING)
    gluSphere(quadratic, 5, 32, 32)
    
    glutSwapBuffers()

if __name__ == "__main__": main()        


