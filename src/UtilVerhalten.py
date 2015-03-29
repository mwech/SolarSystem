__author__ = 'mwech'

import abc

class UtilVerhalten():
    """
    UtilVerhalten
    :param:nothing
    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def light(self):
        """

        :return: is empty
        """
        return

    @abc.abstractmethod
    def depth(self):
        """

        :return: is empty
        """
        return

    @abc.abstractmethod
    def perspective(self, liste):
        """

        :return: is empty
        """
        return

    @abc.abstractmethod
    def loadTexture(self, name):
        """

        :return: is empty
        """
        return