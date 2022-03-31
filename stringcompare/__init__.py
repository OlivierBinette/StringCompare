from .distance import *

import pkg_resources

__version__ = pkg_resources.require("stringcompare")[0].version

__all__ = distance.__all__ + ["__version__"]
