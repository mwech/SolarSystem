__author__ = 'mwech'
import abc

class DesignVerhalten():
    """
    DesignVerhalten
    :param:nothing
    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def designe(self):
        """

        :return: is empty
        """
        return