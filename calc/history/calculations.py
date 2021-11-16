"""Calculation history Class"""


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
