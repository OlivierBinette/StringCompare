

.. image:: https://github.com/OlivierBinette/StringCompare/actions/workflows/python-package-conda.yml/badge.svg
   :target: https://github.com/OlivierBinette/StringCompare/actions/workflows/python-package-conda.yml
   :alt: Python package
 

.. image:: https://codecov.io/gh/OlivierBinette/StringCompare/branch/main/graph/badge.svg?token=F8ASD5R051
   :target: https://codecov.io/gh/OlivierBinette/StringCompare
   :alt: codecov


.. image:: https://img.shields.io/badge/License-GPLv3-blue.svg
   :target: https://www.gnu.org/licenses/gpl-3.0
   :alt: License: GPL v3


.. image:: https://img.shields.io/badge/lifecycle-maturing-blue.svg
   :target: https://lifecycle.r-lib.org/articles/stages.html
   :alt: Lifecycle Maturing


⚡ **StringCompare**\ : Efficient String Comparison Functions
===============================================================

**StringCompare** is a Python package for efficient string similarity computation and approximate string matching. It is inspired by the excellent `\ *comparator* <https://github.com/ngmarchant/comparator>`_ and `\ *stringdist* <https://github.com/markvanderloo/stringdist>`_ R packages, as well as from the `\ *py_stringmatching* <https://github.com/anhaidgroup/py_stringmatching>`_\ , `\ *jellyfish* <https://github.com/jamesturk/jellyfish>`_\ , and `\ *textdistance* <https://github.com/life4/textdistance>`_ Python packages.

The key feature of **StringCompare** is a focus on speed and extensibility through its `\ *pybind11*  <https://github.com/pybind/pybind11>`_ C++ implementation. **StringCompare** is faster than other Python libraries (see benchmark below) and much more memory efficient when dealing with long strings.

Installation
------------

Install from github using the following command:

.. code-block::

   pip install setuptools wheel pybind11
   pip install git+https://github.com/OlivierBinette/StringCompare.git


Project Roadmap
---------------

**StringCompare** currently implements `edit distances <https://en.wikipedia.org/wiki/Edit_distance>`_ and similarity functions, such as the Levenshtein, Damerau-Levenshtein, Jaro, and Jaro-Winkler distances. This is *stage 1* of the following development roadmap: 

.. list-table::
   :header-rows: 1

   * - Stage
     - Goals
     - Status
   * - 1
     - pybind11 framework and edit-based distances (Levenshtein, Damerau-Levenshtein, Jaro, and Jaro-Winkler)
     - 
     .. image:: https://lifecycle.r-lib.org/articles/figures/lifecycle-stable.svg
        :target: https://lifecycle.r-lib.org/articles/figures/lifecycle-stable.svg
        :alt: Stable
     
   * - 2
     - Token-based and hybrid distances (tf-idf similarity, LSH, Monge-Elkan, ...)
     - 
   * - 3
     - Vocabulary optimizations and metric trees
     - 
   * - 4
     - Embeddings and string distance learning


Examples
--------

Comparison algorithms are instanciated as ``Comparator`` object, which provides the ``compare()`` method (equivalent to ``__call__()``\ ) for string comparison.

.. code-block:: python

   from stringcompare import Levenshtein, Jaro, JaroWinkler, DamerauLevenshtein, LCSDistance

   lev = Levenshtein(normalize=True, similarity=False)

   lev("Olivier", "Oliver") # same as lev.compare("Olivier", "Oliver")

.. code-block::

   0.14285714285714285




Comparator objects also provide the ``elementwise()`` function for elementwise comparison between lists

.. code-block:: python

   lev.elementwise(["Olivier", "Olivier"], ["Oliver", "Olivia"])

.. code-block::

   array([0.14285714, 0.26666667])




and the ``pairwise()`` function for pairwise comparisons.

.. code-block:: python

   lev.pairwise(["Olivier", "Oliver"], ["Olivier", "Olivia"])

.. code-block::

   array([[0.        , 0.26666667],
          [0.14285714, 0.28571429]])




Benchmark
---------

Comparison of the Jaro-Winkler implementation speed for different Python packages:

**StringCompare**

.. code-block:: python

   from stringcompare import JaroWinkler
   cmp = JaroWinkler()
   %timeit cmp.compare("Olivier Binette", "Oilvier Benet")

.. code-block::

   361 ns ± 0.916 ns per loop (mean ± std. dev. of 7 runs, 1000000 loops each)



**jellyfish**

.. code-block:: python

   from jellyfish import jaro_winkler
   %timeit jaro_winkler("Olivier Binette", "Oilvier Benet")

.. code-block::

   1.53 µs ± 20.6 ns per loop (mean ± std. dev. of 7 runs, 1000000 loops each)



**py_stringmatching**

.. code-block:: python

   from py_stringmatching import JaroWinkler
   jw = JaroWinkler()
   %timeit jw.get_sim_score("Olivier Binette", "Oilvier Benet")

.. code-block::

   3.22 µs ± 142 ns per loop (mean ± std. dev. of 7 runs, 100000 loops each)



**textdistance**

.. code-block:: python

   from textdistance import jaro_winkler
   %timeit jaro_winkler("Olivier Binette", "Oilvier Benet")

.. code-block::

   3.42 µs ± 38.4 ns per loop (mean ± std. dev. of 7 runs, 100000 loops each)



Known Bugs
----------


* 
  *pybind11* has compatibility issues with gcc 11 (e.g. on Ubuntu 21.10). If running Linux and ``gcc --version`` is 11, then use the following commands to configure your environment before installing:

  .. code-block::

       sudo apt-get install gcc-9 g++-9
       export CC=gcc-9 && export CXX=g++-9

Please report installation issues `here <https://github.com/OlivierBinette/StringCompare/issues>`_.

Contribute
----------

**StringCompare** is currently in early development stage and contributions are welcome!
