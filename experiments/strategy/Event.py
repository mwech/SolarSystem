__author__ = 'mwech'
import pygame
from pygame.constants import DOUBLEBUF, OPENGL, QUIT
from OpenGL.GLUT import *
from OpenGL.GLU import *
from experiments.strategy.ConcreteObject import ConcreteObject
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

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        liste = [0, -5, 10,
                                 0, 0, 0,
                                 0, 1, 0]
                        concrete = ConcreteObject()
                        concrete.perform_util(liste)

                    if event.key == pygame.K_w:
                        liste = [0, 8, 10,
                                 0, 0, 0,
                                 0, 1, 0]
                        concrete = ConcreteObject()
                        concrete.perform_util(liste)

                    if event.key == pygame.K_e:
                        liste = [0, 0, 10,
                                 0, 0, 0,
                                 0, 1, 0]
                        concrete = ConcreteObject()
                        concrete.perform_util(liste)
