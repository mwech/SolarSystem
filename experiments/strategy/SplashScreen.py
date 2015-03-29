__author__ = 'mwech'
import pygame
from pygame.constants import DOUBLEBUF, OPENGL

class SplashScreen():
    def initSplashScreen(self):
        """SPLASHSCREEN INIT """
        screen = pygame.display.set_mode([800, 600])  # Setting the size of the screen
        image = pygame.image.load("texturen/Splashscreen_v1.jpg").convert()  # Splashscreen
        logoimage = screen.blit(image, (0, 0))
        pygame.display.flip()
        pygame.time.delay(3500)