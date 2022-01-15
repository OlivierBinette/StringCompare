#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include <vector>

#include "_comparator.cpp"

namespace py = pybind11;
using namespace std;

template<class T>
using Mat = vector<vector<T>>;

class LCSDistance: public StringComparator {
public:

  bool normalize;
  bool similarity;
  int dmat_size;
  Mat<int> dmat;

  LCSDistance(bool normalize=true, bool similarity=false, int dmat_size=100){
    this->normalize = normalize;
    this->similarity = similarity;
    this->dmat_size = dmat_size;

    dmat = Mat<int>(2, vector<int>(dmat_size));
  }

  int lcs(const string &s, const string &t) {
    int m = s.size();
    int n = t.size();

    for (int i = 0; i < dmat_size; i++) {
      dmat[0][i] = 0;
    }

    for (int j = 1; j <= n; j++) {
      dmat[(j-1) % 2][0] = 0;
      dmat[j % 2][1] = 0;
      for (int i = 1; i <= m; i++) {
        if (s[i-1] != t[j-1]){
          dmat[j % 2][i] = std::max({dmat[(j-1) % 2][i], dmat[j % 2][i-1]});
        } else {
            dmat[j % 2][i] = dmat[(j-1) % 2][i-1] + 1;
        }
        
      }
    }

    return dmat[n % 2][m];
  }

  double compare(const string &s, const string &t) {
    double dist = s.size() + t.size() - 2.0 * lcs(s, t);

    if (similarity) {
      double sim = (s.size() + t.size() - dist) / 2.0;
      if (normalize) {
        sim = sim / (s.size() + t.size() - sim);
      }
      return sim;
    } else {
      if (normalize) {
        dist = 2 * dist / (s.size() + t.size() + dist);
      }
      return dist;
    }
  }
  
};


PYBIND11_MODULE(_lcs,m) {

  m.doc() = "";
  m.attr("__name__") = "stringcompare.distance._lcs";

  py::class_<LCSDistance, StringComparator>(m, "LCSDistance")
        .def(py::init<bool, bool, int>(), py::arg("normalize")=true, py::arg("similarity")=false, py::arg("dmat_size")=100)
        .def("compare", &LCSDistance::compare);
}
