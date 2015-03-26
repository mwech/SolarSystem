from experiments.strategy.UtilVerhalten import UtilVerhalten

__author__ = 'mwech'
class Util(UtilVerhalten):
    """
    Util
    :param UtilVerhalten: reference of theUtilVerhalten class
    """
    def light(self):
        """

        :return: nothing
        """
        print("light!")

    def depth(self):
        """

        :return: nothing
        """
        print("depth!")

    def perspective(self, liste):
        """

        :return: nothing
        """
        print("perspective!")

    def loadTexture(self, name):
        """

        :return: nothing
        """
        print("loadTexture!" + name)
