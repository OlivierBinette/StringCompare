.. role:: raw-html-m2r(raw)
   :format: html



.. image:: https://github.com/OlivierBinette/StringCompare/actions/workflows/python-package-conda.yml/badge.svg
   :target: https://github.com/OlivierBinette/StringCompare/actions/workflows/python-package-conda.yml
   :alt: Python package
 

.. image:: https://codecov.io/gh/OlivierBinette/StringCompare/branch/main/graph/badge.svg?token=F8ASD5R051
   :target: https://codecov.io/gh/OlivierBinette/StringCompare
   :alt: codecov


.. image:: https://www.codefactor.io/repository/github/olivierbinette/stringcompare/badge
   :target: https://www.codefactor.io/repository/github/olivierbinette/stringcompare
   :alt: CodeFactor


.. image:: https://img.shields.io/badge/lifecycle-maturing-blue.svg
   :target: https://lifecycle.r-lib.org/articles/stages.html
   :alt: Lifecycle Maturing


.. image:: https://img.shields.io/github/v/release/olivierbinette/stringcompare
   :target: https://github.com/OlivierBinette/StringCompare/releases
   :alt: Release version
 

.. image:: https://img.shields.io/github/sponsors/OlivierBinette
   :target: https://github.com/sponsors/OlivierBinette
   :alt: Sponsors
 

⚡ **StringCompare**\ : Efficient String Comparison Functions
===============================================================

**StringCompare** is a Python package for efficient string similarity computation and approximate string matching. It is inspired by the excellent `\ *comparator* <https://github.com/ngmarchant/comparator>`_ and `\ *stringdist* <https://github.com/markvanderloo/stringdist>`_ R packages, and from the equally excellent `\ *py_stringmatching* <https://github.com/anhaidgroup/py_stringmatching>`_\ , `\ *jellyfish* <https://github.com/jamesturk/jellyfish>`_\ , and `\ *textdistance* <https://github.com/life4/textdistance>`_ Python packages.

The key feature of **StringCompare** is a focus on speed, extensibility and maintainability through its `\ *pybind11*  <https://github.com/pybind/pybind11>`_ C++ implementation. **StringCompare** is faster than most other Python libraries (see benchmark below) and much more memory efficient when dealing with long strings.

The `complete API documentation <https://olivierbinette.github.io/StringCompare/source/stringcompare.html>`_ is available on the project website `olivierbinette.github.io/StringCompare <https://olivierbinette.github.io/StringCompare>`_.

Installation
------------

Install the released version from github using the following commands:

.. code-block:: bash

       pip install git+https://github.com/OlivierBinette/StringCompare.git@release

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
     - ✔️
   * - 2
     - Token-based and hybrid distances (tf-idf similarity, LSH, Monge-Elkan, ...)
     - ...
   * - 3
     - Vocabulary optimizations and metric trees
     - ...
   * - 4
     - Embeddings and string distance learning
     - ...


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

Comparison of the Damerau-Levenshtein implementation speed for different Python packages, when comparing the strings "Olivier Binette" and "Oilvier Benet":

.. code-block:: python

   from timeit import timeit
   from tabulate import tabulate

   # Comparison functions
   from stringcompare import DamerauLevenshtein
   cmp = DamerauLevenshtein()
   from jellyfish import damerau_levenshtein_distance
   from textdistance import damerau_levenshtein

   functions = {
       "StringCompare": cmp.compare,
       "jellyfish": damerau_levenshtein_distance,
       "textdistance": damerau_levenshtein,
   }

   table = [
       [name, timeit(lambda: fun("Olivier Binette", "Oilvier Benet"), number=1000000) * 1000]
       for name, fun in functions.items()
   ]
   print(tabulate(table, headers=["Package", "avg runtime (ns)"]))

.. code-block::

   Package          avg runtime (ns)
   -------------  ------------------
   StringCompare             697.834
   jellyfish                 974.363
   textdistance             3982.73



Performance notes
^^^^^^^^^^^^^^^^^

The use of pybind11 comes with a small performance overhead. We could be faster if we directly interfaced with CPython.

However, the use of pybind11 allows the library to be easily extensible and maintainable. The C++ implementation has little to worry about Python, excepted for the use of a pybind11 numpy wrapper in some places. Pybind11 takes care of the details of exposing the C++ API to Python.

Known Bugs
----------

*pybind11* has compatibility issues with gcc 11 (e.g. on Ubuntu 21.10). If running Linux and ``gcc --version`` is 11, then use the following commands to configure your environment before (re)installing:

.. code-block:: bash

           sudo apt install g++-9 gcc-9
           export CC=gcc-9 CXX=g++-9

If this is unsuccessful, you might want to use **StringCompare** within a `Docker <https://www.docker.com/>`_ container. I recommend using the python:3.7.9 base image. For example, after installing docker, you can launch an interactive bash session and install **StringCompare** as follows:

.. code-block:: bash

           sudo docker run -it python:3.7.9 bash
           pip install git+https://github.com/OlivierBinette/StringCompare.git
           python
           >>> import stringcompare

Please report installation issues `here <https://github.com/OlivierBinette/StringCompare/issues>`_.

Contribute
----------

**StringCompare** is currently in early development stage and contributions are welcome! See the `contributing <https://olivierbinette.github.io/StringCompare/contributing.html>`_ page for more information. 

Acknowledgements
----------------

This project is made possible by the support of the `Natural Sciences and Engineering Research Council of Canada (NSERC) <www.nserc-crsng.gc.ca>`_ and by the support of a `G-Research <https://www.gresearch.co.uk/>`_ grant.

:raw-html-m2r:`<a href="https://www.gresearch.co.uk/"><img src="https://res-1.cloudinary.com/crunchbase-production/image/upload/c_lpad,h_256,w_256,f_auto,q_auto:eco/gtqacyz2dx8jqicpnmqr" height=100 style="margin:20px"></a>`\ :raw-html-m2r:`<a href="https://www.nserc-crsng.gc.ca"><img src="https://umanitoba.ca/faculties/engineering/media/NSERC_Logo.png" height=100 style="margin:20px"></a>`

I would also like to thank the support of my individual `Github sponsors <https://github.com/sponsors/olivierbinette>`_.
