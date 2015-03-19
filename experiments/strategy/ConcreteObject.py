from experiments.strategy.AObject import AObject
from experiments.strategy.Design import Design
from experiments.strategy.Rotation import Rotation

__author__ = 'mwech'
'''
IMPORTS
'''


class ConcreteObject(AObject):
    """
    ConcreteObject
    :param Duck: Reference to the class AObject
    """
    def __init__(self):
        """

        :return: nothing
        """
        AObject.__init__(self)

        rotation_instanz = Rotation()
        self._rotation_verhalten = rotation_instanz
        design_instanz = Design()
        self._design_verhalten = design_instanz
