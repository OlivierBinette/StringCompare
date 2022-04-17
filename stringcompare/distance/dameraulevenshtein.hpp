#pragma once

#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include <vector>

#include "comparator.hpp"

namespace py = pybind11;
using namespace std;

template<class T>
using Mat = vector<vector<T>>;

class DamerauLevenshtein: public StringComparator {
public:

  bool normalize;
  bool similarity;
  int dmat_size;
  Mat<int> dmat;

  DamerauLevenshtein(bool normalize=true, bool similarity=false, int dmat_size=100){
    this->normalize = normalize;
    this->similarity = similarity;
    this->dmat_size = dmat_size;

    dmat = Mat<int>(3, vector<int>(dmat_size));
  }

  int dameraulevenshtein(const string &s, const string &t) {
    int m = s.size();
    int n = t.size();

    for (int i = 0; i < dmat_size; i++) {
      dmat[0][i] = i;
    }

    int cost;
    for (int j = 1; j <= n; j++) {
      dmat[(j-1) % 3][0] = j-1;
      dmat[j % 3][0] = j;
      for (int i = 1; i <= m; i++) {
        cost = 0;
        if (s[i-1] != t[j-1]) {
          cost = 1;
        }
        dmat[j % 3][i] = min({dmat[j % 3][i-1] + 1, dmat[(j-1) % 3][i] +
                                 1, dmat[(j-1) % 3][i-1] + cost});
        if ((i > 1) & (j > 1) & (s[i-1] == t[j-2]) & (s[i-2] == t[j-1])) {
            dmat[j % 3][i] = std::min({dmat[j % 3][i], dmat[(j-2) % 3][i-2] + 1});
        }
      }
    }

    return dmat[n % 3][m];
  }

  double compare(const string &s, const string &t) {
    int len = s.size() + t.size();
    if (len == 0) {
      return similarity;
    }

    size_t m = max(s.size(), t.size()) + 1;
    dmat[0].reserve(m);
    dmat[1].reserve(m);
    dmat[2].reserve(m);

    double dist = dameraulevenshtein(s, t);

    if (similarity) {
      double sim = (len - dist) / 2.0;
      if (normalize) {
        sim = sim / (len - sim);
      }
      return sim;
    } else {
      if (normalize) {
        dist = 2 * dist / (len + dist);
      }
      return dist;
    }
  }
};
