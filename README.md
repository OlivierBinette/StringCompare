## 

[![Python package](https://github.com/OlivierBinette/StringCompare/actions/workflows/python-package-conda.yml/badge.svg)](https://github.com/OlivierBinette/StringCompare/actions/workflows/python-package-conda.yml) 
![![Lifecycle Maturing](https://lifecycle.r-lib.org/articles/figures/lifecycle-maturing.svg)](https://lifecycle.r-lib.org/articles/stages.html)

# :zap: **StringCompare**: Efficient String Comparison Functions

**StringCompare** is a Python package for efficient string similarity computation and approximate string matching. It is inspired by Neil Marchant's excellent [*comparator*](https://github.com/ngmarchant/comparator) R package, as well as from the [*py_stringmatching*](https://github.com/anhaidgroup/py_stringmatching), [*jellyfish*](https://github.com/jamesturk/jellyfish), and [*textdistance*](https://github.com/life4/textdistance) Python packages.

The key feature of **StringCompare** is a focus on speed through its [*pybind11* ](https://github.com/pybind/pybind11) C++ implementation. **StringCompare** is faster than other libraries (see benchmark below) and much more memory efficient when dealing with long strings.

## Installation

Install from github using the following command:

    pip install git+https://github.com/OlivierBinette/StringCompare.git

## User Guide

Comparison algorithms are instanciated as `Comparator` object, which provides the `compare()` method for string comparison, the `elementwise()` method for elementwise comparison of lists of strings, and the `pairwise()` method for pairwise comparisons between lists.


```python
from stringcompare import Levenshtein, Jaro, JaroWinkler, DamerauLevenshtein, LCSDistance

cmp = Levenshtein(normalize=True, similarity=False)
cmp.compare("Olivier", "Oliver")
```




    0.14285714285714285




```python
cmp.elementwise(["Olivier", "Olivier"], ["Oliver", "Olivia"])
```




    array([0.14285714, 0.26666667])




```python
cmp.pairwise(["Olivier", "Oliver"], ["Olivier", "Olivia"])
```




    array([[0.        , 0.26666667],
           [0.14285714, 0.28571429]])



## Project Roadmap

**StringCompare** currently implements [edit distances](https://en.wikipedia.org/wiki/Edit_distance) and similarity functions, such as the Levenshtein, Damerau-Levenshtein, Jaro, and Jaro-Winkler distances. This is *stage 1* of the following development roadmap: 

| Stage  | Goals | Status|
| :-------------: | ------------- | :-------------: |
| 1  | pybind11 framework and edit-based distances (Levenshtein, Damerau-Levenshtein, Jaro, and Jaro-Winkler) | ![Stable](https://lifecycle.r-lib.org/articles/figures/lifecycle-stable.svg)  |
| 2  | Token-based and hybrid distances (tf-idf similarity, LSH, Monge-Elkan, ...)  |   |
| 3  | Vocabulary optimizations and metric trees |   |
| 3  | Embeddings and string distance learning |   |



## Benchmark

**StringCompare**


```python
from stringcompare import JaroWinkler
cmp = JaroWinkler()
%timeit cmp.compare("Olivier Binette", "Oilvier Benet")
```

    385 ns ± 13.8 ns per loop (mean ± std. dev. of 7 runs, 1000000 loops each)


**jellyfish**


```python
from jellyfish import jaro_winkler
%timeit jaro_winkler("Olivier Binette", "Oilvier Benet")
```

    966 ns ± 35.2 ns per loop (mean ± std. dev. of 7 runs, 1000000 loops each)


**py_stringmatching**


```python
from py_stringmatching import JaroWinkler
jw = JaroWinkler()
%timeit jw.get_sim_score("Olivier Binette", "Oilvier Benet")
```

    3.37 µs ± 68.3 ns per loop (mean ± std. dev. of 7 runs, 100000 loops each)


**textdistance**


```python
from textdistance import jaro_winkler
%timeit jaro_winkler("Olivier Binette", "Oilvier Benet")
```

    3.46 µs ± 43.8 ns per loop (mean ± std. dev. of 7 runs, 100000 loops each)


## Known Bugs

- *pybind11* has compatibility issues with gcc 11 (e.g. on Ubuntu 21.10). If running Linux and `gcc --version` is 11, then use the following commands to configure your environment before installing:

        sudo apt-get install gcc-9 g++-9
        export CC=gcc-9 && export CXX=g++-9

Please report installation issues [here](https://github.com/OlivierBinette/StringCompare/issues).

## Contribute

**StringCompare** is currently in early development stage and contributions are welcome!
