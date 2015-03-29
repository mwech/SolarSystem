__author__ = 'mwech'
import abc

"""
@author: Maximilian Wech
@version: 2015 03 28
@description: Abstrakte Klasse DesignVerhalten, welche definiert, wie die Methode zum Erstellen der Sonne,Planeten,Monde
              aufgebaut ist
"""

class DesignVerhalten():
    """
    DesignVerhalten: Abstrakte Klasse DesignVerhalten, welche definiert, wie die Methode zum Erstellen der Sonne,Planeten,Monde
    aufgebaut ist
    """
    __metaclass__ = abc.ABCMeta #Abstrakte Klasse

    @abc.abstractmethod
    def drawSphere(self, x, y, z, mat, size, art, textur, number, speed):
        """
        Erstellen und zuweisen einiger notwendiger Eigenschaften (Größe, Farbe,etc.) für die Sonne/Planeten/Monde
        :param x: Die x-Koordinate der Anfangsposition
        :param y: Die y-Koordinate der Anfangsposition
        :param z: Die y-Koordinate der Anfangsposition
        :param mat: Zahl, des zu verwendenden Materials
        :param size: Der Radius der Kugel
        :param art: Beschreibt, ob es sich um eine Sonne, Planet, oder Mond handelt
        :param textur: Beschreibt, welche Texture verwendet werden soll
        :param number: Zaehler der bei jedem mal aufrufen erhöht wird
        :param speed: die Geschwindigkeit, mit der rotiert werden soll
        :return: /
        """
        return

