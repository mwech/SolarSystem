from experiments.strategy.ConcreteObject import ConcreteObject

__author__ = 'mwech'

class main():
    """
    main class
    """
    def __init__(self):
        """

        :return: nothing
        """
        if __name__ == "__main__":

            concrete = ConcreteObject()
            concrete.perform_util()
            concrete.perform_design()

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