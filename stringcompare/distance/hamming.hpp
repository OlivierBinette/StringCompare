#pragma once

#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include <vector>

#include "comparator.hpp"

namespace py = pybind11;
using namespace std;

class Hamming: public StringComparator {
public:

  bool normalize;
  bool similarity;

  Hamming(bool normalize=true, bool similarity=false){
    this->normalize = normalize;
    this->similarity = similarity;
  }

  int hamming(const string &s, const string &t) {
    int m = s.size();
    int n = t.size();
    int min_length = min(m, n);

    int distance = 0;
    for (int i = 0; i < min_length; i++) {
      distance += (s[i] != t[i]);
    }
    distance += max(m, n) - min_length;
    
    return distance;
  }

  double compare(const string &s, const string &t) {
    double len = max(s.size(), t.size());

    if (len == 0) {
      return similarity;
    }

    double result = hamming(s, t);

    if (similarity) {
      result = len - result;
    }
    if (normalize) {
        result = result / len;
    }

    return result;
  }
  
};
