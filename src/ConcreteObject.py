from AObject import AObject
from Design import Design
from Util import Util

__author__ = 'mwech'

"""
@author: Maximilian Wech
@version: 2015 03 27
@description: Klasse, die Design- und Util Verhalten zuweist
"""

class ConcreteObject(AObject):
    """
    ConcreteObject: Verwendung der abstrakten Klasse AObject
    """
    def __init__(self):
        """
        Konstruktor, in dem die Verhalten zugewiesen werden
        """
        AObject.__init__(self)

        util_instanz = Util() #Instanz-Erstellung
        self._util_verhalten = util_instanz #Zuweisung des Verhaltens für das Util

        design_instanz = Design() #Instanz-Erstellung
        self._design_verhalten = design_instanz #Zuweisung des Verhaltens für das Design
