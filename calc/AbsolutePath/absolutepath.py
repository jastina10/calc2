"""absolute path of a csv file for pylint"""
from pathlib import Path

def absolutepath(filepath):
    """returns the absolute path"""
    relativepath = Path(filepath)
    return relativepath.absolute()
