__author__ = 'mwech'
import pygame
from pygame.constants import DOUBLEBUF, OPENGL, QUIT
from OpenGL.GLUT import *
from OpenGL.GLU import *
from experiments.strategy.ConcreteObject import ConcreteObject
from experiments.strategy.ObjectValues import ObjectValues
from OpenGL.GL import *


class Event():
    def controllEvents(self):
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
                        referenz = ObjectValues()
                        referenz.speedPlanet-=0.3
                        referenz.speedMond-=0.2
                    #Rotation schneller --> Pfeiltaste rechts
                    if event.key == pygame.K_RIGHT:
                        referenz = ObjectValues()
                        referenz.speedPlanet+=0.3
                        referenz.speedMond+=0.2
                    #Rotationsstop --> Pfeiltaste unten
                    if event.key == pygame.K_DOWN:
                        referenz = ObjectValues()
                        #a = int(referenz.manometer[1])
                        del referenz.manometer[:]
                        referenz.manometer.extend("2")
                        referenz.speedPlanet=0
                        referenz.speedMond=0
