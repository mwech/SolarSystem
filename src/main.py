from src.ConcreteObject import ConcreteObject
from src.SplashScreen import SplashScreen
from src.Event import Event
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
        display = (800, 600)
        screen = pygame.display.get_surface()
        pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

        concrete = ConcreteObject()
        liste = [0, 0, 10,
                 0, 0, 0,
                 0, 1, 0]
        concrete.perform_util(liste)
        instEvent = Event()
        instEvent.controllEvents()

main()