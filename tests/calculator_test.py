"""Testing the Calculator"""
# pylint: disable=redefined-outer-name,unused-argument,missing-function-docstring

import pytest
from calc.calculator import Calculator
from calc.history.calculations import Calculations


@pytest.fixture
def clear_history_fixture():
    """define a function that will run each time you pass it to a test, it is called a fixture"""
    # pylint: disable=redefined-outer-name
    Calculations.clear_history()


# You have to add the fixture function as a parameter to the test that you want to use it with
def test_calculator_add_static(clear_history_fixture):
    """testing that our calculator has a static method for addition"""
    # pylint: disable=unused-argument,redefined-outer-name
    assert Calculator.add_numbers(1.0, 2.0, 3.0) == 6.0


def test_calculator_subtract_static(clear_history_fixture):
    """Testing the subtract method of the calc"""
    # pylint: disable=unused-argument,redefined-outer-name
    assert Calculator.subtract_numbers(1.0, 2.0) == -3.0


def test_calculator_multiply_static(clear_history_fixture):
    """Testing the subtract method of the calc"""
    # pylint: disable=unused-argument,redefined-outer-name
    assert Calculator.multiply_numbers(1.0, 2.0) == 2.0


def test_calculator_divide_static(clear_history_fixture):
    """Testing the divide method of the calculator"""
    # pylint: disable=unused-argument,redefined-outer-name
    assert Calculator.divide_numbers(12.0, 2.0) == 6.0
    assert Calculator.divide_numbers(12.0, 0.0) is None
