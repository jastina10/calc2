"""Main function to initiate the calculator_test.py file"""

from time import sleep
import pytest


print('main.py will pytest for calculator_test.py file')
sleep(3)


def main():
    """Runs the pytest program"""
    print('Running pytest ...')
    retcode = pytest.main(['--pylint', 'tests/calculator_test.py'])
    print(retcode)
    print("Test complete")


if __name__ == '__main__':
    main()
