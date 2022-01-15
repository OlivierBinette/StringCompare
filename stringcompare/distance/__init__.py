try:  # C++ imports
    from stringcompare.distance._comparator import Comparator, StringComparator
    from stringcompare.distance._levenshtein import Levenshtein
    from stringcompare.distance._lcs import LCSDistance
    from stringcompare.distance._dameraulevenshtein import DamerauLevenshtein
    from stringcompare.distance._jaro import Jaro
    from stringcompare.distance._jarowinkler import JaroWinkler
except:
    import warnings
    warnings.warn(
        "Could not load C++ shared library. Using pure Python implementation instead.")
    from .comparator import Comparator, StringComparator
    from .levenhstein import Levenshtein
    from .dameraulevenshtein import DamerauLevenshtein
    from .jaro import Jaro
    from .jarowinkler import JaroWinkler
    from .lcs import LCSDistance
