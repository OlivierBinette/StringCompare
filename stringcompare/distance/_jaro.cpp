#include <pybind11/pybind11.h>
#include <vector>

#include "_comparator.cpp"

namespace py = pybind11;
using namespace std;

class Jaro: public StringComparator {
public:

  bool similarity;

  Jaro(bool similarity=false){
    this->similarity = similarity;
  }

  static double jaro(const string &s, const string &t) {
    int window = max(1.0, floor(max(s.size(), t.size()) / 2.0) - 1);

    double m = 0;
    vector<bool> found_s = vector<bool>(s.size(), false);
    vector<bool> found_t = vector<bool>(t.size(), false);

    size_t j0, j1;
    for (size_t i = 0; i < s.size(); i++) {
        for (size_t j = 0; j < t.size(); j++) {
            if (!found_t[j] && (s[i] == t[j]) && (abs(int(i)-int(j)) < window)) {
                m += 1;
                found_s[i] = true;
                found_t[j] = true;
                break;
            }
        }
    }

    if (m == 0) {
        return 0.0;
    }

    double transpositions = 0;
    int j = 0;
    for (size_t i = 0; i < s.size(); i++) {
        if (found_s[i]) {
            while (!found_t[j]) {
                j += 1;
            }
            if (s[i] != t[j]) {
                transpositions += 1;
            }
            j += 1;
        }
    }
    
    return (m/s.size() + m/t.size() + (m-transpositions/2.0)/m) / 3.0;
  }

  double compare(const string &s, const string &t) {
      if (this->similarity == true) {
          return jaro(s, t);
      } else { 
          return 1.0 - jaro(s, t);
      } 
  }
  
};


PYBIND11_MODULE(_jaro,m) {

  m.doc() = "";
  m.attr("__name__") = "stringcompare.distance._jaro";

  py::class_<Jaro, StringComparator>(m, "Jaro")
        .def(py::init<bool>(), py::arg("similarity")=false)
        .def("compare", &Jaro::compare);

}
