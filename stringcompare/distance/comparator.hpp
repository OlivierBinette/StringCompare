#pragma once

#include <pybind11/pybind11.h>
#include <pybind11/numpy.h>
#include <pybind11/stl.h>
#include <vector>

namespace py = pybind11;
using namespace std;

template<class dtype>
class Comparator {
    public:
    virtual double compare(const dtype &s, const dtype &t) = 0;

    double operator()(const dtype &s, const dtype &t) {
        return compare(s, t);
    }

    py::array_t<double> elementwise(const vector<dtype> &l1, const vector<dtype> &l2) {

        if (l1.size() != l2.size()) {
            std::length_error("Lists should be of the same size.");
        }

        py::array_t<double> result(l1.size());
        auto res = result.mutable_unchecked<1>();
        for (long int i = 0; i < l1.size(); i++) {
            res(i) = this->compare(l1[i], l2[i]);
        }

        return result;
    }

    py::array_t<double> pairwise(const vector<dtype> &l1, const vector<dtype> &l2){
        py::array_t<double> result({l1.size(), l2.size()});
        auto res = result.mutable_unchecked<2>();
        for (size_t i = 0; i < l1.size(); i++) {
            for (size_t j = 0; j < l2.size(); j++) {
                res(i,j) = this->compare(l1[i], l2[j]);
            }
        }

        return result;
    }

};

class StringComparator: public Comparator<string> {};

class NumericComparator: public Comparator<double> {};


template<class T>
void declare_comparator(py::module &m, string name, char* classdoc="", char* comparedoc="", char* ewdoc="", char* pwdoc="") {
    py::class_<T>(m, name.c_str(), classdoc)
        .def("__call__", &T::operator())
        .def("compare", &T::compare, comparedoc)
        .def("elementwise", &T::elementwise, ewdoc)
        .def("pairwise", &T::pairwise, pwdoc);
}

