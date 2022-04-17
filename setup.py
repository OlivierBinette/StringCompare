#!/usr/bin/env python3
from setuptools import setup, find_packages
from pybind11.setup_helpers import build_ext, intree_extensions

if __name__ == "__main__":
    ext_modules = intree_extensions(["stringcompare/distance/_distance.cpp", "stringcompare/preprocessing/_preprocessing.cpp"])

    setup(
        ext_modules=ext_modules,
        name="stringcompare",
        version="0.1.0",
        author="Olivier Binette",
        author_email="olivier.binette@gmail.com",
        description="Efficient string comparison functions.",
        #license="",
        #license_files="",
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
        install_requires=["numpy", "pybind11"],
        cmdclass={"build_ext": build_ext},
    )
