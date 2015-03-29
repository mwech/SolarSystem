__author__ = 'mwech'
import pygame
from pygame.constants import DOUBLEBUF, OPENGL, QUIT
from OpenGL.GLUT import *
from OpenGL.GLU import *
from ConcreteObject import ConcreteObject
from ObjectValues import ObjectValues
from OpenGL.GL import *


class Event():
    __speedMond = 1.5
    __speedPlanet = 0.5
    __hilfe = 0
    __zaehler = 0
    __zahl = 0


    def controllEvents(self):
        #zaehler = 0
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    quit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                #------------------------------------------------------------------------#
                    #Linke Maustaste: Deaktivieren von Texturen / Aktivieren von Licht
                    if event.button == 1:
                        glDisable(GL_TEXTURE_2D)

                    #Rechte Maustaste: Aktivieren von Texturen / Deaktivieren von Licht
                    if event.button == 3:
                        glEnable(GL_TEXTURE_2D)
                #------------------------------------------------------------------------#
                if event.type == pygame.KEYDOWN:
                #------------------------------------------------------------------------#
                    #Q- Froschperspektive
                    if event.key == pygame.K_q:
                        liste = [0, -5, 10,
                                 0, 0, 0,
                                 0, 1, 0]
                        concrete = ConcreteObject()
                        concrete.perform_util(liste)

                    #W- Vogelperspektive
                    if event.key == pygame.K_w:
                        liste = [0, 8, 10,
                                 0, 0, 0,
                                 0, 1, 0]
                        concrete = ConcreteObject()
                        concrete.perform_util(liste)

                    #E- Normalperspektive
                    if event.key == pygame.K_e:
                        liste = [0, 0, 10,
                                 0, 0, 0,
                                 0, 1, 0]
                        concrete = ConcreteObject()
                        concrete.perform_util(liste)
                    #------------------------------------------------------------------------#

                    if event.key == pygame.K_LEFT:
                        if Event.__hilfe == 1:
                            Event.__hilfe = 0
                            Event.__zahl = -2
                        else:
                            Event.__zaehler-=2
                            Event.__zahl-=1
                    #Rotation schneller --> Pfeiltaste rechts
                    if event.key == pygame.K_RIGHT:
                        if Event.__hilfe == 1:
                            Event.__hilfe = 0
                            Event.__zahl = 0
                        else:
                            Event.__zaehler+=2
                            Event.__zahl +=1

                    #Rotationsstop --> Pfeiltaste unten
                    if event.key == pygame.K_DOWN:
                        Event.__hilfe = 1
            if Event.__hilfe!=1:
                Event.__zaehler += 1 + Event.__zahl
            glClearColor(0., 0., 0., 1.)
            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
            concrete = ConcreteObject()
            concrete.perform_design(Event.__zaehler, Event.__speedPlanet, Event.__speedMond)

            pygame.display.flip()
            pygame.time.wait(10)
        return
