#pragma once

#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include <vector>

#include "comparator.hpp"

namespace py = pybind11;
using namespace std;

template<class T>
using Mat = vector<vector<T>>;

class Levenshtein: public StringComparator {
public:

  bool normalize;
  bool similarity;
  int dmat_size;
  Mat<int> dmat;

  Levenshtein(bool normalize=true, bool similarity=false, int dmat_size=100){
    this->normalize = normalize;
    this->similarity = similarity;
    this->dmat_size = dmat_size;

    this->dmat = Mat<int>(2, vector<int>(dmat_size));
  }

  int levenshtein(const string &s, const string &t) {
    int m = s.size();
    int n = t.size();

    for (int i = 0; i < dmat_size; i++) {
      dmat[0][i] = i;
    }

    int cost;
    for (int j = 1; j <= n; j++) {
      dmat[(j-1) % 2][0] = j-1;
      dmat[j % 2][1] = j;
      for (int i = 1; i <= m; i++) {
        cost = 0;
        if (s[i-1] != t[j-1]){
          cost = 1;
        }
        dmat[j % 2][i] = min({dmat[j % 2][i-1] + 1, dmat[(j-1) % 2][i] +
                                 1, dmat[(j-1) % 2][i-1] + cost});
      }
    }

    return dmat[n % 2][m];
  }

  double compare(const string &s, const string &t) {
    double dist = levenshtein(s, t);

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
