from src.AObject import AObject
from src.Design import Design
from src.Util import Util

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

        util_instanz = Util()
        self._util_verhalten = util_instanz

        design_instanz = Design()
        self._design_verhalten = design_instanz
