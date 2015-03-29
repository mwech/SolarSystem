from src.ConcreteObject import ConcreteObject
from src.SplashScreen import SplashScreen
from src.Event import Event
from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
import pygame
from pygame.constants import DOUBLEBUF, OPENGL, QUIT

__author__ = 'mwech'


class main():
    """
    main class
    """

    def __init__(self):
        """

        :return: nothing
        """
        self.display()

    def display(self):

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