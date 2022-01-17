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

    declare_comparator<Comparator<py::object>>(m, "Comparator");
    declare_comparator<StringComparator>(m, "StringComparator");
    declare_comparator<NumericComparator>(m, "NumericComparator");

    py::class_<Levenshtein, StringComparator>(m, "Levenshtein")
      .def(py::init<bool, bool, int>(), py::arg("normalize")=true, py::arg("similarity")=false, py::arg("dmat_size")=100)
      .def("compare", &Levenshtein::compare);

    py::class_<DamerauLevenshtein, StringComparator>(m, "DamerauLevenshtein")
      .def(py::init<bool, bool, int>(), py::arg("normalize")=true, py::arg("similarity")=false, py::arg("dmat_size")=100)
      .def("compare", &DamerauLevenshtein::compare);

    py::class_<Jaro, StringComparator>(m, "Jaro")
      .def(py::init<bool>(), py::arg("similarity")=false)
      .def("compare", &Jaro::compare);
  
    py::class_<JaroWinkler, StringComparator>(m, "JaroWinkler")
      .def(py::init<bool>(), py::arg("similarity")=false)
      .def("compare", &JaroWinkler::compare);

    py::class_<LCSDistance, StringComparator>(m, "LCSDistance")
      .def(py::init<bool, bool, int>(), py::arg("normalize")=true, py::arg("similarity")=false, py::arg("dmat_size")=100)
      .def("compare", &LCSDistance::compare);

}