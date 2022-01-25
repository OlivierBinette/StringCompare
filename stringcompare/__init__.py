from .distance import (
    Levenshtein,
    DamerauLevenshtein,
    LCSDistance,
    Jaro,
    JaroWinkler,
    Comparator,
    StringComparator,
)

import pkg_resources

__version__ = pkg_resources.require("stringcompare")[0].version

__all__ = [
    "Levenshtein",
    "DamerauLevenshtein",
    "LCSDistance",
    "Jaro",
    "JaroWinkler",
    "Comparator",
    "StringComparator",
    "__version__",
]
