#!/usr/bin/env python3
from setuptools import setup, find_packages
from pybind11.setup_helpers import build_ext, intree_extensions

if __name__ == "__main__":
    ext_modules = intree_extensions(["stringcompare/distance/_distance.cpp"])

    setup(ext_modules=ext_modules,
          name="stringcompare",
          version="0.0.1.post",
          author="Olivier Binette",
          author_email="olivier.binette@gmail.com",
          description="Efficient string comparison functions.",
          license="GPL 3",
          license_files="LICENSE",
          keywords=["record-linkage", "string-distance",
                    "edit-distance", "levenshtein", "string-matching"],
          url="https://github.com/OlivierBinette/StringCompare",
          include_package_data=True,
          packages=find_packages(),
          install_requires=["numpy",
                            "scipy",
                            "pandas",
                            "igraph",
                            "sklearn",
                            "pybind11"],
          cmdclass={"build_ext": build_ext})
