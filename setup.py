#!/usr/bin/env python3
from setuptools import setup, find_packages
from pybind11.setup_helpers import build_ext, Pybind11Extension

if __name__ == "__main__":
    ext_modules = [
        Pybind11Extension(
            "stringcompare.distance._distance", 
            ["stringcompare/distance/_distance.cpp"], 
            cxx_std=11
        )
    ]

    setup(
        ext_modules=ext_modules,
        name="py-stringcompare",
        version="0.2.1",
        author="Olivier Binette",
        author_email="olivier.binette@gmail.com",
        description="Efficient string comparison functions.",
        readme = "README.md",
        keywords=[
            "record-linkage",
            "string-distance",
            "edit-distance",
            "levenshtein",
            "string-matching",
        ],
        url="https://github.com/OlivierBinette/StringCompare",
        include_package_data=True,
        packages=find_packages(),
        python_requires=">=3.8",
        install_requires=[
            "numpy>=1,<3", 
            "pybind11>=2.4,<4"
        ],
        cmdclass={"build_ext": build_ext},
    )
