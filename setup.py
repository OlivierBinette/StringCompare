#!/usr/bin/env python3
from setuptools import setup
import warnings

if __name__ == "__main__":
    try:
        from pybind11.setup_helpers import build_ext, intree_extensions
        ext_modules = intree_extensions(
            ["stringcompare/comparator/_levenshtein.cpp",
             "stringcompare/comparator/_comparator.cpp",
             "stringcompare/comparator/_lcs.cpp",
             "stringcompare/comparator/_dameraulevenshtein.cpp",
             "stringcompare/comparator/_jaro.cpp",
             "stringcompare/comparator/_jarowinkler.cpp"])
        setup(ext_modules=ext_modules, cmdclass={"build_ext": build_ext})
    except:
        warnings.warn(
            "Could not build package using C++ source. Trying again in pure Python.")
        setup()
