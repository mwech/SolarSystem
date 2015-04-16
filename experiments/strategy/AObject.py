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
    def perform_util(self, liste):
        """

        :return: /
        """
        self._util_verhalten.depth()
        self._util_verhalten.light()
        self._util_verhalten.perspective(liste)
        self._util_verhalten.loadTexture("texturen/sun.jpg")
        self._util_verhalten.loadTexture("texturen/planet.png")
        self._util_verhalten.loadTexture("texturen/moon.jpg")
        self._util_verhalten.loadTexture("texturen/world2.png")


    @abc.abstractmethod
    def perform_design(self, number, speedPlanet, speedMond):
        """

        :return: /
        """
        #x, y, z, mat, size, art, textur, number, speed
        self._design_verhalten.drawSphere(0, 0, 0, 1, 1, "Sonne", 1, number, 0)

        self._design_verhalten.drawSphere(-6, 0, -2, 2, 0.6, "Planet", 2, number, speedPlanet)
        self._design_verhalten.drawSphere(-3, 0, -2, 3, 0.2, "Mond", 3, number, speedMond)

        self._design_verhalten.drawSphere(5, 0, -8, 4, 0.6, "Planet", 4, number, speedPlanet)
        self._design_verhalten.drawSphere(1, 0, -1, 3, 0.2, "Mond", 3, number, speedMond)
