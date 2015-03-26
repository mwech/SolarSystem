__author__ = 'mwech'
import abc

class DesignVerhalten():
    """
    DesignVerhalten
    :param:nothing
    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def sun(self, x, y, z, mat, size, art, textur):
        """

        :return: is empty
        """
        return

    @abc.abstractmethod
    def planet(self, x, y, z, mat, size, art, textur):
        """

        :return: is empty
        """
        return

    @abc.abstractmethod
    def mond(self, x, y, z, mat, size, art, textur):
        """

        :return: is empty
        """
        return