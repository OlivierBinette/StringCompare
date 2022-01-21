 
[![Python package](https://github.com/OlivierBinette/StringCompare/actions/workflows/python-package-conda.yml/badge.svg)](https://github.com/OlivierBinette/StringCompare/actions/workflows/python-package-conda.yml) 
[![codecov](https://codecov.io/gh/OlivierBinette/StringCompare/branch/main/graph/badge.svg?token=F8ASD5R051)](https://codecov.io/gh/OlivierBinette/StringCompare)
[![CodeFactor](https://www.codefactor.io/repository/github/olivierbinette/stringcompare/badge)](https://www.codefactor.io/repository/github/olivierbinette/stringcompare)
[![Lifecycle Maturing](https://img.shields.io/badge/lifecycle-maturing-blue.svg)](https://lifecycle.r-lib.org/articles/stages.html)
[![Release version](https://img.shields.io/github/v/release/olivierbinette/stringcompare)](https://github.com/OlivierBinette/StringCompare/releases) 
[![Sponsors](https://img.shields.io/github/sponsors/OlivierBinette)](https://github.com/sponsors/OlivierBinette) 


# ⚡ **StringCompare**: Efficient String Comparison Functions

**StringCompare** is a Python package for efficient string similarity computation and approximate string matching. It is inspired by the excellent [*comparator*](https://github.com/ngmarchant/comparator) and [*stringdist*](https://github.com/markvanderloo/stringdist) R packages, as well as from the [*py_stringmatching*](https://github.com/anhaidgroup/py_stringmatching), [*jellyfish*](https://github.com/jamesturk/jellyfish), and [*textdistance*](https://github.com/life4/textdistance) Python packages.

The key feature of **StringCompare** is a focus on speed and extensibility through its [*pybind11* ](https://github.com/pybind/pybind11) C++ implementation. **StringCompare** is faster than other Python libraries (see benchmark below) and much more memory efficient when dealing with long strings.

The [complete API documentation](https://olivierbinette.github.io/StringCompare/source/stringcompare.html) is available on the project website [olivierbinette.github.io/StringCompare](https://olivierbinette.github.io/StringCompare).

## Installation

Install the latest release version from github using the following command:

    pip install setuptools wheel pybind11
    pip install git+https://github.com/OlivierBinette/StringCompare.git@release

## Project Roadmap

**StringCompare** currently implements [edit distances](https://en.wikipedia.org/wiki/Edit_distance) and similarity functions, such as the Levenshtein, Damerau-Levenshtein, Jaro, and Jaro-Winkler distances. This is *stage 1* of the following development roadmap: 

| Stage  | Goals | Status|
| :-------------: | ------------- | :-------------: |
| 1  | pybind11 framework and edit-based distances (Levenshtein, Damerau-Levenshtein, Jaro, and Jaro-Winkler) | ✔️ |
| 2  | Token-based and hybrid distances (tf-idf similarity, LSH, Monge-Elkan, ...)  | ... |
| 3  | Vocabulary optimizations and metric trees | ...  |
| 4  | Embeddings and string distance learning | ...  |



## Examples

Comparison algorithms are instanciated as `Comparator` object, which provides the `compare()` method (equivalent to `__call__()`) for string comparison.


```python
from stringcompare import Levenshtein, Jaro, JaroWinkler, DamerauLevenshtein, LCSDistance

lev = Levenshtein(normalize=True, similarity=False)

lev("Olivier", "Oliver") # same as lev.compare("Olivier", "Oliver")
```




    0.14285714285714285



Comparator objects also provide the `elementwise()` function for elementwise comparison between lists


```python
lev.elementwise(["Olivier", "Olivier"], ["Oliver", "Olivia"])
```




    array([0.14285714, 0.26666667])



and the `pairwise()` function for pairwise comparisons.


```python
lev.pairwise(["Olivier", "Oliver"], ["Olivier", "Olivia"])
```




    array([[0.        , 0.26666667],
           [0.14285714, 0.28571429]])



## Benchmark

Comparison of the Jaro-Winkler implementation speed for different Python packages:

**StringCompare**


```python
from stringcompare import JaroWinkler
cmp = JaroWinkler()
%timeit cmp.compare("Olivier Binette", "Oilvier Benet")
```

    361 ns ± 0.916 ns per loop (mean ± std. dev. of 7 runs, 1000000 loops each)


**jellyfish**


```python
from jellyfish import jaro_winkler
%timeit jaro_winkler("Olivier Binette", "Oilvier Benet")
```

    1.53 µs ± 20.6 ns per loop (mean ± std. dev. of 7 runs, 1000000 loops each)


**py_stringmatching**


```python
from py_stringmatching import JaroWinkler
jw = JaroWinkler()
%timeit jw.get_sim_score("Olivier Binette", "Oilvier Benet")
```

    3.22 µs ± 142 ns per loop (mean ± std. dev. of 7 runs, 100000 loops each)


**textdistance**


```python
from textdistance import jaro_winkler
%timeit jaro_winkler("Olivier Binette", "Oilvier Benet")
```

    3.42 µs ± 38.4 ns per loop (mean ± std. dev. of 7 runs, 100000 loops each)


## Known Bugs

- *pybind11* has compatibility issues with gcc 11 (e.g. on Ubuntu 21.10). If running Linux and `gcc --version` is 11, then use the following commands to configure your environment before installing:

        sudo apt-get install gcc-9 g++-9
        export CC=gcc-9 && export CXX=g++-9

Please report installation issues [here](https://github.com/OlivierBinette/StringCompare/issues).

## Contribute

**StringCompare** is currently in early development stage and contributions are welcome! See the [contributing](https://stringcompare.readthedocs.io/en/latest/CONTRIBUTING.html) page for more information.
