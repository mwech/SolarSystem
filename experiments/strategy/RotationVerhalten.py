__author__ = 'mwech'

import abc

class RotationVerhalten():
    """
    RotationVerhalten
    :param:nothing
    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def rotieren(self):
        """

        :return: is empty
        """
        return