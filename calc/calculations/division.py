"""Division Class"""
from calc.calculations.calculation import Calculation


class Division(Calculation):
    """division calculation object"""

    def get_result(self):
        """get the division results"""
        try:
            return self.values[0] / self.values[1]
        except ZeroDivisionError as error:
            return print(error)
