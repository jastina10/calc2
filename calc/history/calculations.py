"""Calculation history Class"""
from calc.calculations.addition import Addition
from calc.calculations.division import Division
from calc.calculations.multiplication import Multiplication
from calc.calculations.subtraction import Subtraction


class Calculations:
    """Calculation history Class"""
    history = []

    # pylint: disable=too-few-public-methods
    @staticmethod
    def clear_history():
        """Calculation history Class"""
        Calculations.history.clear()
        return True

    @staticmethod
    def count_history():
        """Calculation history Class"""
        return len(Calculations.history)

    @staticmethod
    def get_last_calculation():
        """Calculation history Class"""
        return Calculations.history[-1]

    @staticmethod
    def get_first_calculation():
        """Calculation history Class"""
        return Calculations.history[-1]

    @staticmethod
    def get_calculation(num):
        """ get a specific calculation from history"""
        return Calculations.history[num]

    @staticmethod
    def add_calculation(calculation):
        """ get a specific calculation from history"""
        return Calculations.history.append(calculation)


    @staticmethod
    def add_calculation(inserted_calculation):
        """append calculation from history"""
        return Calculations.history.append(inserted_calculation)

    @staticmethod
    def addition_calculation(values):  # pass list of values
        """add Addition to history by creating addition calculation object using factory method"""
        Calculations.add_calculation(Addition.create(values))
        return Calculations.history[-1]  # return the result of the addition from the history

    @staticmethod
    def multiplication_calculation(values):
        """add Multiplication to history by creating addition calculation object using factory method"""
        Calculations.add_calculation(Multiplication.create(values))
        return Calculations.history[-1]

    @staticmethod
    def subtraction_calculation(values):
        """add Subtraction to history by creating addition calculation object using factory method"""
        Calculations.add_calculation(Subtraction.create(values))
        return Calculations.history[-1]

    @staticmethod
    def division_calculation(values):
        """add Division to history by creating addition calculation object using factory method"""
        Calculations.add_calculation(Division.create(values))
        return Calculations.history[-1]