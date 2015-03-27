__author__ = 'mwech'
import abc

class AObject(object):
    __metaclass__ = abc.ABCMeta

    def __init__(self):
        pass

    @abc.abstractmethod
    def set_util_verhalten(self, uv):
        """

        :param uv: utilverhalten
        :return: /
        """
        self._util_verhalten = uv

    @abc.abstractmethod
    def set_design_verhalten(self, dv):
        """

        :param dv:designverhalten
        :return: /
        """
        self._design_verhalten = dv

    @abc.abstractmethod
    def perform_util(self):
        """

        :return: /
        """
        liste = [0, 0, 10,
                 0, 0, 0,
                 0, 1, 0]
        self._util_verhalten.light()
        self._util_verhalten.depth()
        self._util_verhalten.perspective(liste)
        self._util_verhalten.loadTexture("sun.jpg")
        self._util_verhalten.loadTexture("planet.png")
        self._util_verhalten.loadTexture("moon.jpg")


    @abc.abstractmethod
    def perform_design(self, number):
        """

        :return: /
        """
        self._design_verhalten.sun(0,0,0,1,1,"Sonne",1,number)
        self._design_verhalten.planet(-3,0,-1,2,1,"Planet",2,number)
        self._design_verhalten.mond(-3,1,-2,3,0.2,"Mond",3,number)
        self._design_verhalten.planet(4,0,-2,2,1,"Planet",2,number)
        self._design_verhalten.mond(4.5,3,-2,3, 0.2,"Mond",3,number)
