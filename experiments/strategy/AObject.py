__author__ = 'mwech'
import abc
class AObject(object):
    __metaclass__ = abc.ABCMeta

    def __init__(self):
        pass

    @abc.abstractmethod
    def set_rotation_verhalten(self, rv):
        """

        :param rv: rotationverhalten
        :return: /
        """
        self._rotation_verhalten = rv

    @abc.abstractmethod
    def set_design_verhalten(self, dv):
        """

        :param dv:designverhalten
        :return: /
        """
        self._design_verhalten = dv

    @abc.abstractmethod
    def perform_rotation(self):
        """

        :return: /
        """
        self._rotation_verhalten.rotieren()

    @abc.abstractmethod
    def perform_design(self):
        """

        :return: /
        """
        self._design_verhalten.designe()