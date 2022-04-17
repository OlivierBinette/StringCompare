#include <pybind11/pybind11.h>
#include <pybind11/numpy.h>
#include <pybind11/stl.h>
#include <vector>

#include "comparator.hpp"
#include "levenshtein.hpp"
#include "dameraulevenshtein.hpp"
#include "jaro.hpp"
#include "jarowinkler.hpp"
#include "lcs.hpp"
#include "characterdifference.hpp"
#include "hamming.hpp"

PYBIND11_MODULE(_distance, m) {

    m.attr("__name__") = "stringcompare.distance._distance";

    declare_comparator<Comparator<py::object>>(m, "Comparator", 
R""""(
Abstract base class for pybind11 comparator objects.

Provides the :func:`~stringcompare.Comparator.compare` function for comparison of two elements, the :func:`~stringcompare.Comparator.elementwise` function for elementwise comparison between two lists, and the :func:`~stringcompare.Comparator.pairwise` function for pairwise comparison between elements of two lists.

Parameters for the comparison functions (e.g. to return a distance or similarity, whether or not to normalize, weights, etc) should be provided to the constructor.

The current class structure, implemented in C++, is as follows::

  Comparator
  ─┬────────
   ├─► compare()
   │
   ├─► elementwise()
   │
   ├─► pairwise()
   │
   │StringComparator
   └─┬──────────────
     │
     │ Levenshtein
     ├────────────
     │
     │ DamerauLevenshtein
     ├───────────────────
     │
     │ LCSDistance
     ├────────────
     │
     │ Jaro
     ├─────
     │
     │ JaroWinkler
     └────────────
     │
     │ CharacterDifference
     └────────────────────
     │
     │ Hamming
     └────────

.. seealso:: :class:`StringComparator` :class:`NumericComparator`
)"""",
R"""(
Comparison between two elements.

:param arg0: Object to compare from.
:param arg1: Object to compare to.
:return: Numeric value of the comparison.
)""",
R"""(
Elementwise comparison between two lists.

:param arg0: List of objects to compare from.
:param arg1: List of objects to compare to.
:return: Numpy array containing comparison values.

.. note:: The two lists :code:`arg0` and :code:`arg1` should be of the same length.
)""",
R"""(
Pairwise comparison between two lists.

:param arg0: List of objects to compare from.
:param arg1: List of objects to compare to.
:return: 2x2 numpy array containing comparison values, where each row corresponds to an element of :code:`arg0` and each column corresponds to an element of :code:`arg1`.
)""");
    declare_comparator<StringComparator>(m, "StringComparator");
    declare_comparator<NumericComparator>(m, "NumericComparator");

    py::class_<Levenshtein, StringComparator>(m, "Levenshtein",
    R"""(
    Levenshtein distance

    This is defined as the "minimum number of single-character edits (insertions, deletions or substitutions) required to change one word into the other" (see `Wikipedia page <https://en.wikipedia.org/wiki/Levenshtein_distance>`_). The distance may be normalized or returned as a similarity score instead.

    :param normalize: Whether or not to normalize the result to be between 0 and 1. Defaults to True.
    :param similarity: Whether or not to return a similarity score (higher for more similar strings) or a distance score (closer to zero for more similar strings). Defaults to False.
    :param dmat_size: Initial ength of the internal string buffer. Defaults to 100.
    
    :Examples:
    >>> from stringcompare import Levenshtein
    >>> lev = Levenshtein()
    >>> lev("Olivier", "Oilvier") # Same as lev.compare("Olivier", "Oilvier")
    0.25

    >>> lev = Levenshtein(normalize=False)
    >>> lev("Olivier", "Oilvier")
    2.0

    >>> lev = Levenshtein(normalize=False, similarity=True)
    >>> lev("Olivier", "Oilvier")
    6.0

    >>> lev.elementwise(["a", "ab"], ["b", "ba"])
    array([0.5, 1.])

    >>> lev.pairwise(["a", "ab"], ["b", "ba"])
    array([[0.5, 1. ],
           [1. , 1. ]])
    )"""
    )
      .def(py::init<bool, bool, int>(), py::arg("normalize")=true, py::arg("similarity")=false, py::arg("dmat_size")=100)
      .def("compare", &Levenshtein::compare);

    py::class_<DamerauLevenshtein, StringComparator>(m, "DamerauLevenshtein",
    R"""(
    Damerau-Levenshtein distance

    This is the minimum number of insertions, deletions, substitutions or transpositions required to change one word into the other. The distance may be normalized or returned as a similarity score instead.

    :param normalize: Whether or not to normalize the result to be between 0 and 1. Defaults to True.
    :param similarity: Whether or not to return a similarity score (higher for more similar strings) or a distance score (closer to zero for more similar strings). Defaults to False.
    :param dmat_size: Initial length of the internal string buffer.
    )""")
      .def(py::init<bool, bool, int>(), py::arg("normalize")=true, py::arg("similarity")=false, py::arg("dmat_size")=100)
      .def("compare", &DamerauLevenshtein::compare);

    py::class_<Jaro, StringComparator>(m, "Jaro",
    R"""(
    Jaro distance

    :param similarity: Whether or not to return a similarity score (higher for more similar strings) or a distance score (closer to zero for more similar strings). Defaults to False.
    )"""
    )
      .def(py::init<bool>(), py::arg("similarity")=false)
      .def("compare", &Jaro::compare);
  
    py::class_<JaroWinkler, StringComparator>(m, "JaroWinkler",
    R"""(
    Jaro-Winkler distance

    :param similarity: Whether or not to return a similarity score (higher for more similar strings) or a distance score (closer to zero for more similar strings). Defaults to False.
    )"""
    )
      .def(py::init<bool>(), py::arg("similarity")=false)
      .def("compare", &JaroWinkler::compare);

    py::class_<LCSDistance, StringComparator>(m, "LCSDistance",
    R"""(
    Longest common subsequence (LCS) distance

    This is the minimum number of insertions or deletions required to change one word into the other. The distance may be normalized or returned as a similarity score instead.

    :param normalize: Whether or not to normalize the result to be between 0 and 1. Defaults to True.
    :param similarity: Whether or not to return a similarity score (higher for more similar strings) or a distance score (closer to zero for more similar strings). Defaults to False.
    :param dmat_size: Initial length of the internal string buffer.
    )"""
    )
      .def(py::init<bool, bool, int>(), py::arg("normalize")=true, py::arg("similarity")=false, py::arg("dmat_size")=100)
      .def("compare", &LCSDistance::compare);

    py::class_<CharacterDifference, StringComparator>(m, "CharacterDifference",
    R"""(
    Character difference between two strings.

    This is the number of characters differing between two strings. The distance may be normalized or returned as a similarity score instead.

    :param normalize: Whether or not to normalize the result to be between 0 and 1. Defaults to True.
    :param similarity: Whether or not to return a similarity score (higher for more similar strings) or a distance score (closer to zero for more similar strings). Defaults to False.
    )"""
    )
      .def(py::init<bool, bool>(), py::arg("normalize")=true, py::arg("similarity")=false)
      .def("compare", &CharacterDifference::compare);
    
    py::class_<Hamming, StringComparator>(m, "Hamming",
    R"""(
    Hamming distance between two strings.

    This is the number of differences between corresponding characters in the strings.

    :param normalize: Whether or not to normalize the result to be between 0 and 1. Defaults to True.
    :param similarity: Whether or not to return a similarity score (higher for more similar strings) or a distance score (closer to zero for more similar strings). Defaults to False.
    )"""
    )
      .def(py::init<bool, bool>(), py::arg("normalize")=true, py::arg("similarity")=false)
      .def("compare", &Hamming::compare);
}
