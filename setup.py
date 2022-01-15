#!/usr/bin/env python3
from setuptools import setup
import warnings

if __name__ == "__main__":
    try:
        from pybind11.setup_helpers import build_ext, intree_extensions
        from pybind11.setup_helpers import Pybind11Extension

        ext_modules = intree_extensions(
            ["stringcompare/distance/_comparator.cpp",
             "stringcompare/distance/_levenshtein.cpp",
             "stringcompare/distance/_lcs.cpp",
             "stringcompare/distance/_dameraulevenshtein.cpp",
             "stringcompare/distance/_jaro.cpp",
             "stringcompare/distance/_jarowinkler.cpp"])
        setup(ext_modules=ext_modules, cmdclass={"build_ext": build_ext})
    except:
        warnings.warn(
            "Could not build package using C++ source. Trying again with pure Python.")
        setup()
