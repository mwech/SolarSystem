from ConcreteObject import ConcreteObject
from SplashScreen import SplashScreen
from Event import Event
from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
import pygame
from pygame.constants import DOUBLEBUF, OPENGL, QUIT

__author__ = 'mwech'
"""
@author: Maximilian Wech
@version: 2015 03 28
@description: Main
"""

class main():
    """
    main class
    """

    def __init__(self):
        """
        Konstruktor
        """
        self.display()

    def display(self):

        #Starten des SpashScreens
        instSplash = SplashScreen()
        instSplash.initSplashScreen()

        """ PYGAME INIT """
        pygame.init()
        display = (1080, 720)
        screen = pygame.display.get_surface()
        pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

        concrete = ConcreteObject()
        liste = [0, 0, 10,
                 0, 0, 0,
                 0, 1, 0]
        #Aufruf der Basic Methoden (Licht,etc.)
        concrete.perform_util(liste)
        #Auf Events prüfen
        instEvent = Event()
        instEvent.controllEvents()

main()