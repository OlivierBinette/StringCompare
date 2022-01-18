#pragma once

#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include <vector>

#include "comparator.hpp"

namespace py = pybind11;
using namespace std;

template<class T>
using Mat = vector<vector<T>>;

class LCSDistance: public StringComparator {
public:

  bool normalize;
  bool similarity;
  int dmat_size;
  bool check_bounds;
  Mat<int> dmat;

  LCSDistance(bool normalize=true, bool similarity=false, int dmat_size=100, bool check_bounds=true){
    this->normalize = normalize;
    this->similarity = similarity;
    this->dmat_size = dmat_size;
    this->check_bounds = check_bounds;

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
    if (check_bounds) {
      auto m = max(s.size(), t.size()) + 1;
      dmat[0].reserve(m);
      dmat[1].reserve(m);
    }

    double len = s.size() + t.size();
    if (len == 0) {
      return similarity;
    }

    double dist = len - 2.0 * lcs(s, t);
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

