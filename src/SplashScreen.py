__author__ = 'arif'
import pygame
from pygame.constants import DOUBLEBUF, OPENGL

"""
@author: Arif Balkan
@version: 2015 03 28
@description: Laden des Spashscreens und Anzeigen im pygame window
"""

class SplashScreen():
    """
    SplashScreen: Laden des Spashscreens und Anzeigen im pygame window
    """
    def initSplashScreen(self):
        """
        Konstruktor
        """
        """SPLASHSCREEN INIT """
        screen = pygame.display.set_mode([1080,720])  # Setting the size of the screen
        image = pygame.image.load("texturen/Splashscreen_v2.jpg").convert()  # Splashscreen
        logoimage = screen.blit(image, (0, 0))
        pygame.display.flip()
        pygame.time.delay(3500)