#pragma once

#include <pybind11/pybind11.h>
#include <vector>

#include "comparator.hpp"

namespace py = pybind11;
using namespace std;

class Jaro: public StringComparator {
public:

  bool similarity;

  Jaro(bool similarity=false){
    this->similarity = similarity;
  }

  static double jaro(const string &s, const string &t) {
    auto ssize = s.size();
    auto tsize = t.size();
    if (ssize + tsize == 0) {
        return 1.0;
    }
    int window = max(1.0, floor(max(ssize, tsize) / 2.0) - 1);

    double m = 0;
    vector<bool> found_s = vector<bool>(ssize, false);
    vector<bool> found_t = vector<bool>(tsize, false);

    for (size_t i = 0; i < ssize; i++) {
        for (size_t j = 0; j < tsize; j++) {
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
    for (size_t i = 0; i < ssize; i++) {
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
    
    return (m/ssize + m/tsize + (m-transpositions/2.0)/m) / 3.0;
  }

  double compare(const string &s, const string &t) {
      if (this->similarity == true) {
          return jaro(s, t);
      } else { 
          return 1.0 - jaro(s, t);
      } 
  }
  
};
