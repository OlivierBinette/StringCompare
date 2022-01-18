#!/usr/bin/env python3
from setuptools import setup
import warnings
from glob import glob
from pybind11.setup_helpers import build_ext, intree_extensions

if __name__ == "__main__":
    ext_modules = intree_extensions(["stringcompare/distance/_distance.cpp"])

    setup(ext_modules=ext_modules,
          name="stringcompare",
          author="Olivier Binette",
          author_email="olivier.binette@gmail.com",
          install_requires=["numpy",
                            "scipy",
                            "pandas",
                            "igraph",
                            "sklearn",
                            "pybind11"],
          cmdclass={"build_ext": build_ext})
