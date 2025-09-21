from stringcompare.distance import *
from stringcompare.preprocessing import *

from importlib.metadata import version

__version__ = version("py-stringcompare")

__all__ = ["__version__"] + distance.__all__ + preprocessing.__all__
