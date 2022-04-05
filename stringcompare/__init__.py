from .distance import *
from .preprocessing import *

import pkg_resources

__version__ = pkg_resources.require("stringcompare")[0].version

__all__ = ["__version__"] + distance.__all__ + preprocessing.__all__
