from experiments.strategy.ConcreteObject import ConcreteObject
from experiments.strategy.ObjectValues import ObjectValues
from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
import pygame
from pygame.constants import DOUBLEBUF, OPENGL

__author__ = 'mwech'


class main():
    """
    main class
    """

    def __init__(self):
        """

        :return: nothing
        """
        """SPLASHSCREEN INIT """
        screen = pygame.display.set_mode([1280, 720])  # Setting the size of the screen
        image = pygame.image.load("texturen/Splashscreen_v1.jpg").convert()  # Splashscreen
        logoimage = screen.blit(image, (0, 0))
        pygame.display.flip()
        pygame.time.delay(3500)

        """ PYGAME INIT """
        pygame.init()
        display = (800, 600)
        screen = pygame.display.get_surface()
        pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

        concrete = ConcreteObject()
        concrete.perform_util()
        referenz = ObjectValues()
        zaehler = 0
        while True:
            zaehler += 1
            glClearColor(0., 0., 0., 1.)
            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
            concrete.perform_design(zaehler)

            pygame.display.flip()
            pygame.time.wait(10)

        """
            1. SplashScreen ->Pygame
            2. perspective(liste)
            3. depth()
            4. light()
            5. LoadTexture(name)
            6. while()
            7.      for()
            8.          Maus, Tastatur --> Pygame
            9.      clear
            10.     drawSphere(self, x, y, z, mat, size, art, textur) --> sphereMaterial(), rotate()
            11.     pygame close
            """

        """
            Util: SplashScreen(), depth(), perspective(liste), light(), LoadTexture(name)
            Event:
            Sphere: sonne(x,y,z,mat,size,art,textur), planet(x,y,z,mat,size,art,textur), mond(x,y,z,mat,size,art,textur) rotieren und material
        """


main()