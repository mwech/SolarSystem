__author__ = 'mwech'

import abc

"""
@author: Maximilian Wech
@version: 2015 03 28
@description: Abstrakte Klasse UtilVerhalten, welche definiert, wie Basic Methoden (zB Erstellen von Licht,
              Texturen,etc.) aufgebaut sind
"""

class UtilVerhalten():
    """
    UtilVerhalten: Abstrakte Klasse UtilVerhalten, welche definiert, wie Basic Methoden (zB Erstellen von Licht,
                Texturen,etc.) aufgebaut sind
    :param:nothing
    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def light(self):
        """
        Setzen des Lichtes
        :return: /
        """
        return

    @abc.abstractmethod
    def depth(self):
        """
        Setzen einiger notwendiger Eigenschaften
        :return: /
        """
        return

    @abc.abstractmethod
    def perspective(self, liste):
        """
        Setzen der Perspektive
        :param liste: Werte, die für den gluLookAt Befehl zum Setzen der Perspektive notwendig sind
        :return: /
        """
        return

    @abc.abstractmethod
    def loadTexture(self, name):
        """
        Erstellt Texturen und stellt diese bereit
        :param name: Der Name der Textur
        :return: /
        """
        return