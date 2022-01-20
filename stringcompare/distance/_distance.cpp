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

PYBIND11_MODULE(_distance, m) {

    m.attr("__name__") = "stringcompare.distance._distance";

    declare_comparator<Comparator<py::object>>(m, "Comparator", 
R""""(
Abstract base class for pybind11 comparator objects.

Provides the :func:`~stringcompare.Comparator.compare` function for comparison of two elements, the :func:`~stringcompare.Comparator.elementwise` function for elementwise comparison between two lists, and the :func:`~stringcompare.Comparator.pairwise` function for pairwise comparison between elements of two lists.

Parameters for the comparison functions (e.g. to return a distance or similarity, whether or not to normalize, weights, etc) should be provided to the constructor.

All subclass implementations of these functions are in C++ for efficiency.

.. seealso:: :class:`StringComparator` :class:`NumericComparator`
)"""",
R"""(
Comparison between two elements.

:param s: object to compare from
:param t: object to compare to
:return: numeric value of the comparison
)""");
    declare_comparator<StringComparator>(m, "StringComparator");
    declare_comparator<NumericComparator>(m, "NumericComparator");

    py::class_<Levenshtein, StringComparator>(m, "Levenshtein")
      .def(py::init<bool, bool, int, bool>(), py::arg("normalize")=true, py::arg("similarity")=false, py::arg("dmat_size")=100, py::arg("check_bounds")=true)
      .def("compare", &Levenshtein::compare);

    py::class_<DamerauLevenshtein, StringComparator>(m, "DamerauLevenshtein")
      .def(py::init<bool, bool, int, bool>(), py::arg("normalize")=true, py::arg("similarity")=false, py::arg("dmat_size")=100, py::arg("check_bounds")=true)
      .def("compare", &DamerauLevenshtein::compare);

    py::class_<Jaro, StringComparator>(m, "Jaro")
      .def(py::init<bool>(), py::arg("similarity")=false)
      .def("compare", &Jaro::compare);
  
    py::class_<JaroWinkler, StringComparator>(m, "JaroWinkler")
      .def(py::init<bool>(), py::arg("similarity")=false)
      .def("compare", &JaroWinkler::compare);

    py::class_<LCSDistance, StringComparator>(m, "LCSDistance")
      .def(py::init<bool, bool, int, bool>(), py::arg("normalize")=true, py::arg("similarity")=false, py::arg("dmat_size")=100, py::arg("check_bounds")=true)
      .def("compare", &LCSDistance::compare);

}