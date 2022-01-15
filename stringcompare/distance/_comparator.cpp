#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include <vector>

namespace py = pybind11;
using namespace std;

template<class T>
using Mat = vector<vector<T>>;

template <class dtype>
class Comparator {
    public:
    virtual double compare(const dtype &s, const dtype &t) = 0;

    vector<double> elementwise(const vector<dtype> &l1, const vector<dtype> &l2) {
        if (l1.size() != l2.size()) {
            std::length_error("Lists should be of the same size.");
        }

        vector<double> res(l1.size());
        for (size_t i = 0; i < l1.size(); i++) {
            res[i] = this->compare(l1[i], l2[i]);
        }

        return res;
    }

    Mat<double> pairwise(const vector<dtype> &l1, const vector<dtype> &l2){
        Mat<double> res(l1.size(), vector<double>(l2.size()));
        for (size_t i = 0; i < l1.size(); i++) {
            for (size_t j = 0; j < l2.size(); j++) {
                res[i][j] = this->compare(l1[i], l2[j]);
            }
        }

        return res;
    }

};

class StringComparator: public Comparator<string> {};

class NumericComparator: public Comparator<double> {};

template<class T>
void declare_comparator(py::module &m, string name) {
    py::class_<T>(m, name.c_str())
        .def("compare", &T::compare)
        .def("elementwise", &T::elementwise)
        .def("pairwise", &T::pairwise);
}

PYBIND11_MODULE(_comparator, m) {

    m.doc() = "";
    m.attr("__name__") = "stringcompare.distance._comparator";

    declare_comparator<Comparator<py::object>>(m, "Comparator");
    declare_comparator<StringComparator>(m, "StringComparator");
    declare_comparator<NumericComparator>(m, "NumericComparator");
}
