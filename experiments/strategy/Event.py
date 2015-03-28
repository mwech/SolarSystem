__author__ = 'mwech'
import pygame
from pygame.constants import DOUBLEBUF, OPENGL, QUIT
from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *


class Event():
    def controllEvents(self):
        for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    quit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        glDisable(GL_TEXTURE_2D)

                    #Licht an --> Maus rechts
                    if event.button == 3:
                        glEnable(GL_TEXTURE_2D)