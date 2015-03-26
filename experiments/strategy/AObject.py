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
        self._util_verhalten.light()
        self._util_verhalten.depth()
        self._util_verhalten.perspective(1)
        self._util_verhalten.loadTexture("hallo")


    @abc.abstractmethod
    def perform_design(self):
        """

        :return: /
        """
        self._design_verhalten.sun(4,0,-2,2,1,"Planet",2)
        self._design_verhalten.planet(4,0,-2,2,1,"Planet",2)
        self._design_verhalten.mond(4,0,-2,2,1,"Planet",2)