__author__ = 'mwech'
import abc
"""
@author: Maximilian Wech
@version: 2015 03 29
@description: Abstrakte Klasse, welche die abstrakten Methoden zum Setzen der Verhalten, sowie die Inhalte der
              Ausführung der perform Methoden enthält.
"""

class AObject(object):
    """
    AObject: Abstrakte Klasse, welche die abstrakten Methoden zum Setzen der Verhalten, sowie die Inhalte der
             Ausführung der perform Methoden enthält.
    """

    __metaclass__ = abc.ABCMeta   #Abstrakte Klasse

    def __init__(self):
        """
        Konstruktor
        """
        pass

    @abc.abstractmethod
    def set_util_verhalten(self, uv):
        """
        Sets the utilverhalten
        :param uv: utilverhalten
        :return: /
        """
        self._util_verhalten = uv

    @abc.abstractmethod
    def set_design_verhalten(self, dv):
        """
        Sets the designverhalten
        :param dv:designverhalten
        :return: /
        """
        self._design_verhalten = dv

    @abc.abstractmethod
    def perform_util(self, liste):
        """
        Mit dieser Methode, werden die Basic Funktionen zum Setzen von Licht, Texturierung,etc. aufgerufen
        :param liste: Werte, die für den gluLookAt Befehl zum Setzen der Perspektive notwendig sind
        :return: /
        """
        self._util_verhalten.depth()
        self._util_verhalten.light() #Methode zum Licht setzen aufrufen
        self._util_verhalten.perspective(liste) #Methode zum Perspektive setzen aufrufen
        self._util_verhalten.loadTexture("sun.jpg") #Methode für die Texturierung (der Sonne) aufrufen
        self._util_verhalten.loadTexture("planet.png") #Methode für die Texturierung (der Planeten) aufrufen
        self._util_verhalten.loadTexture("moon.jpg") #Methode für die Texturierung (der Monde) aufrufen


    @abc.abstractmethod
    def perform_design(self, number, speedPlanet, speedMond):
        """
        Aufrufen der Methode zum Erstellen der Sonne/Planeten/Monde
        :param number: Zaehler der bei jedem mal aufrufen erhöht wird
        :param speedPlanet: Die Geschwindigkeit der Planeten
        :param speedMond: Die Geschwindigkeiten der Monde
        :return: /
        """
        self._design_verhalten.drawSphere(0,0,0,1,2,"Sonne",1,number,0) #Zeichnen der Sonne

        self._design_verhalten.drawSphere(-6,0,-2,2,0.6,"Planet",2,number, speedPlanet) #Zeichnen des Planets
        self._design_verhalten.drawSphere(-3,0,-2,3,0.3,"Mond",3,number, speedMond) #Zeichnen des dazugehörigen Monds

        self._design_verhalten.drawSphere(5,0,-2,2,0.6,"Planet",2,number, speedPlanet) #Zeichnen des Planets
        self._design_verhalten.drawSphere(1,0,-1,3, 0.3,"Mond",3,number, speedMond) #Zeichnen des dazugehörigen Monds
